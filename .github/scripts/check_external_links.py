#!/usr/bin/env python3
"""
External Link Checker for Documentation

This script checks external links in documentation files (.mdx, .md) for broken URLs.
It complements Mintlify's internal link checker by validating external HTTP(S) links.

Features:
- Extracts links from Markdown/MDX files
- Checks HTTP status codes with retries
- Handles rate limiting and timeouts gracefully
- Skips known false positives (Cloudflare-protected sites)
- Provides detailed error reporting
- Supports parallel checking for faster execution

Usage:
    python .github/scripts/check_external_links.py [--verbose] [--timeout SECONDS]

Exit codes:
    0 - All links valid (or only false positives detected)
    1 - Broken links found
"""

import argparse
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests

# Skip these domains - they block automated requests (Cloudflare, bot detection)
SKIP_DOMAINS = {
    "platform.openai.com",
    "openai.com",
    "www.npmjs.com",
    "npmjs.com",
    "chat.openai.com",
    "chatgpt.com",
    "marketplace.visualstudio.com",  # VS Code Marketplace blocks automated requests
}

# Skip checking links in these files (template/example files with placeholder links)
SKIP_FILES = {
    ".agents/skills/sdk-arch-guidelines.md",
}

# Skip these specific URLs (known working but returning errors to bots)
SKIP_URLS = {
    "https://github.com/OpenHands/software-agent-sdk/tree/main/path",  # Template placeholder
}

# Skip URLs matching these patterns (placeholder/example URLs in docs)
SKIP_URL_PATTERNS = [
    r"localhost",           # localhost URLs are examples
    r"127\.0\.0\.1",        # localhost IP
    r"host\.docker\.internal",  # Docker internal host
    r"example",             # example.com, example-endpoint, etc.
    r"your-",               # your-api-key, your-endpoint, etc.
    r"\{[^}]+\}",           # URLs with {placeholders}
    r"<[^>]+>",             # URLs with <placeholders>
    r"owner/repository",    # GitHub example URLs
    r"username/repo",       # GitHub example URLs
    r"…",                   # Truncated URLs with ellipsis
    r"/v1$",                # API versioned endpoints (e.g., api.groq.com/openai/v1)
    r"/v1/",                # API versioned endpoints with path
    r"api\..+\.(com|io|ai|dev)/", # API endpoints (api.*.com, api.*.io, etc.)
    r"jira\..+\.dev",       # Internal Jira instances
]

# Request timeout in seconds
DEFAULT_TIMEOUT = 15

# Maximum retries for transient failures
MAX_RETRIES = 2

# Delay between retries (seconds)
RETRY_DELAY = 2

# Maximum concurrent requests
MAX_WORKERS = 10


@dataclass
class LinkInfo:
    """Information about a link found in documentation."""
    url: str
    file_path: str
    line_number: int
    context: str


@dataclass
class LinkResult:
    """Result of checking a link."""
    link: LinkInfo
    status: str  # 'ok', 'broken', 'skipped', 'timeout'
    status_code: Optional[int] = None
    error: Optional[str] = None


def find_doc_files(root_dir: str) -> list[Path]:
    """Find all documentation files (.mdx, .md) in the directory."""
    doc_files = []
    root_path = Path(root_dir)

    for pattern in ["**/*.mdx", "**/*.md"]:
        for file_path in root_path.glob(pattern):
            # Skip node_modules, .git, etc.
            if any(part.startswith(".") or part == "node_modules" for part in file_path.parts):
                continue
            # Skip files in SKIP_FILES
            rel_path = str(file_path.relative_to(root_path))
            if rel_path in SKIP_FILES:
                continue
            doc_files.append(file_path)

    return sorted(doc_files)


def extract_links(file_path: Path, root_dir: str) -> list[LinkInfo]:
    """Extract external HTTP(S) links from a file."""
    links = []

    # Pattern to match URLs in Markdown links [text](url) and raw URLs
    # Excludes URLs inside code blocks
    url_pattern = re.compile(r'https?://[^\s\)\]\>"\'`]+')

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
        return links

    # Track if we're inside a code block
    in_code_block = False
    lines = content.split("\n")

    for line_num, line in enumerate(lines, start=1):
        # Check for code block markers
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue

        # Skip lines inside code blocks
        if in_code_block:
            continue

        # Skip HTML comments
        if "<!--" in line and "-->" in line:
            continue

        # Find all URLs in the line
        for match in url_pattern.finditer(line):
            url = match.group(0)

            # Clean up URL (remove trailing punctuation that's not part of URL)
            url = url.rstrip(".,;:!?")

            # Skip if URL is in SKIP_URLS
            if url in SKIP_URLS:
                continue

            # Skip anchor-only links
            if "#" in url and url.index("#") == len(url.split("#")[0]):
                base_url = url.split("#")[0]
                if not base_url:
                    continue

            rel_path = str(file_path.relative_to(root_dir))
            context = line.strip()[:100] + "..." if len(line.strip()) > 100 else line.strip()

            links.append(LinkInfo(
                url=url,
                file_path=rel_path,
                line_number=line_num,
                context=context
            ))

    return links


def should_skip_url(url: str) -> bool:
    """Check if URL should be skipped (known false positives or placeholders)."""
    try:
        # Check against skip patterns (placeholder/example URLs)
        for pattern in SKIP_URL_PATTERNS:
            if re.search(pattern, url, re.IGNORECASE):
                return True

        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # Check if domain or parent domain is in skip list
        for skip_domain in SKIP_DOMAINS:
            if domain == skip_domain or domain.endswith("." + skip_domain):
                return True

        return False
    except Exception:
        return False


def check_link(link: LinkInfo, timeout: int = DEFAULT_TIMEOUT) -> LinkResult:
    """Check if a link is accessible."""
    url = link.url

    # Skip known false positive domains
    if should_skip_url(url):
        return LinkResult(link=link, status="skipped", error="Domain blocks automated requests")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }

    last_error = None
    last_status_code = None

    for attempt in range(MAX_RETRIES + 1):
        try:
            # Use HEAD request first (faster), fall back to GET if needed
            response = requests.head(url, headers=headers, timeout=timeout, allow_redirects=True)
            status_code = response.status_code

            # Some servers don't support HEAD, try GET
            if status_code == 405:
                response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True, stream=True)
                status_code = response.status_code
                response.close()

            last_status_code = status_code

            # Success
            if 200 <= status_code < 400:
                return LinkResult(link=link, status="ok", status_code=status_code)

            # Client error (4xx) - likely broken
            if 400 <= status_code < 500:
                # 403 might be bot protection, skip on retry
                if status_code == 403:
                    return LinkResult(link=link, status="skipped", status_code=status_code,
                                    error="HTTP 403 - likely bot protection")
                return LinkResult(link=link, status="broken", status_code=status_code,
                                error=f"HTTP {status_code}")

            # Server error (5xx) - might be temporary
            last_error = f"HTTP {status_code}"
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue

        except requests.exceptions.Timeout:
            last_error = "Timeout"
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue

        except requests.exceptions.SSLError as e:
            last_error = f"SSL Error: {str(e)[:50]}"
            break

        except requests.exceptions.ConnectionError as e:
            last_error = f"Connection Error: {str(e)[:50]}"
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue

        except Exception as e:
            last_error = f"Error: {str(e)[:50]}"
            break

    # All retries exhausted
    if last_error == "Timeout":
        return LinkResult(link=link, status="timeout", error=last_error)

    return LinkResult(link=link, status="broken", status_code=last_status_code, error=last_error)


def main():
    parser = argparse.ArgumentParser(description="Check external links in documentation")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all links being checked")
    parser.add_argument("--timeout", "-t", type=int, default=DEFAULT_TIMEOUT, help="Request timeout in seconds")
    parser.add_argument("--no-skip", action="store_true", help="Don't skip any domains (check everything)")
    args = parser.parse_args()

    # Find documentation root
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent.parent  # .github/scripts -> .github -> root

    if not root_dir.exists():
        print(f"Error: Root directory not found: {root_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning for documentation files in {root_dir}...")

    # Find all doc files
    doc_files = find_doc_files(str(root_dir))
    print(f"Found {len(doc_files)} documentation files")

    # Extract all external links
    print("\nExtracting external links...")
    all_links: list[LinkInfo] = []
    for file_path in doc_files:
        links = extract_links(file_path, str(root_dir))
        all_links.extend(links)

    # Deduplicate URLs while keeping first occurrence info
    seen_urls: dict[str, LinkInfo] = {}
    unique_links: list[LinkInfo] = []
    for link in all_links:
        if link.url not in seen_urls:
            seen_urls[link.url] = link
            unique_links.append(link)

    print(f"Found {len(all_links)} total links ({len(unique_links)} unique URLs)")

    if not unique_links:
        print("\nNo external links found!")
        sys.exit(0)

    # Check links in parallel
    print(f"\nChecking {len(unique_links)} unique external links...")
    results: list[LinkResult] = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        if args.no_skip:
            # Clear skip domains if --no-skip is used
            SKIP_DOMAINS.clear()

        future_to_link = {
            executor.submit(check_link, link, args.timeout): link
            for link in unique_links
        }

        for i, future in enumerate(as_completed(future_to_link), 1):
            result = future.result()
            results.append(result)

            if args.verbose or result.status in ("broken", "timeout"):
                status_icon = {
                    "ok": "✓",
                    "broken": "✗",
                    "timeout": "⏱",
                    "skipped": "⊘"
                }.get(result.status, "?")
                print(f"  [{i}/{len(unique_links)}] {status_icon} {result.link.url[:80]}")
                if result.error and result.status != "skipped":
                    print(f"       Error: {result.error}")

    # Summarize results
    broken = [r for r in results if r.status == "broken"]
    timeouts = [r for r in results if r.status == "timeout"]
    skipped = [r for r in results if r.status == "skipped"]
    ok = [r for r in results if r.status == "ok"]

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  ✓ OK: {len(ok)}")
    print(f"  ⊘ Skipped (false positives): {len(skipped)}")
    print(f"  ⏱ Timeouts: {len(timeouts)}")
    print(f"  ✗ Broken: {len(broken)}")

    # Report broken links
    if broken:
        print("\n" + "=" * 60)
        print("BROKEN LINKS")
        print("=" * 60)
        for result in broken:
            print(f"\n📄 {result.link.file_path}:{result.link.line_number}")
            print(f"   URL: {result.link.url}")
            print(f"   Error: {result.error}")
            print(f"   Context: {result.link.context}")

    # Report timeouts (might be temporary issues)
    if timeouts:
        print("\n" + "=" * 60)
        print("TIMEOUT LINKS (may be slow or temporarily unavailable)")
        print("=" * 60)
        for result in timeouts:
            print(f"\n📄 {result.link.file_path}:{result.link.line_number}")
            print(f"   URL: {result.link.url}")

    # Exit with error if broken links found
    if broken:
        print(f"\n❌ Found {len(broken)} broken link(s)!")
        sys.exit(1)
    else:
        print(f"\n✅ No broken links found!")
        if timeouts:
            print(f"   ({len(timeouts)} link(s) timed out - please verify manually)")
        sys.exit(0)


if __name__ == "__main__":
    main()
