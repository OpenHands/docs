#!/usr/bin/env python3
"""
Auto-generate the REST API endpoint tables in the API reference landing page.

Reads openapi/agent-sdk.json and regenerates the "Endpoints" section in
sdk/guides/agent-server/api-reference.mdx between the AUTO-GENERATED markers.

Usage:
    python scripts/generate-rest-api-reference.py

The script is idempotent — running it multiple times produces the same output
as long as the OpenAPI spec hasn't changed.
"""

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent.parent
OPENAPI_PATH = DOCS_ROOT / "openapi" / "agent-sdk.json"
TARGET_PATH = DOCS_ROOT / "sdk" / "guides" / "agent-server" / "api-reference.mdx"

START_MARKER = "{/* AUTO-GENERATED-ENDPOINTS-START */}"
END_MARKER = "{/* AUTO-GENERATED-ENDPOINTS-END */}"

# Base path for generated endpoint URLs (matches docs.json openapi.directory)
URL_BASE = "/sdk/guides/agent-server/api-reference"

# Ordered tag config: (tag_name, description)
# Tags not listed here will be appended alphabetically at the end.
TAG_ORDER = [
    ("Conversations", "The core API for managing agent conversations — create, run, pause, and query conversations."),
    ("Events", "Send messages and retrieve events from a conversation."),
    ("Bash", "Execute shell commands and manage bash sessions."),
    ("Files", "Upload and download files from the agent workspace."),
    ("Git", "Inspect git changes and diffs within the workspace."),
    ("Tools", "List tools available to the agent."),
    ("Skills", "Manage agent skills."),
    ("Hooks", "Manage agent hooks."),
    ("VSCode", "Access VS Code integration."),
    ("Desktop", "Access desktop integration."),
    ("Server Details", "Health checks and server information."),
]

# Tags to skip entirely
SKIP_TAGS = {"Untagged"}


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug (lowercase, hyphens)."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_openapi_spec(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def extract_endpoints(spec: dict) -> dict[str, list[dict]]:
    """Group endpoints by tag from the OpenAPI spec."""
    grouped: dict[str, list[dict]] = {}
    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            if method not in ("get", "post", "put", "delete", "patch", "head", "options"):
                continue
            tags = details.get("tags", ["Untagged"])
            tag = tags[0]
            if tag in SKIP_TAGS:
                continue
            summary = details.get("summary", "")
            description = details.get("description", "")
            grouped.setdefault(tag, []).append({
                "method": method.upper(),
                "path": path,
                "summary": summary,
                "description": description,
                "tag": tag,
            })
    return grouped


def endpoint_url(tag: str, summary: str) -> str:
    return f"{URL_BASE}/{slugify(tag)}/{slugify(summary)}"


def brief_description(endpoint: dict) -> str:
    """Return a short description for the table: prefer summary, fall back to first sentence of description."""
    if endpoint["summary"]:
        return endpoint["summary"]
    desc = endpoint["description"]
    if desc:
        return desc.split(".")[0].strip()
    return ""


def generate_tables(grouped: dict[str, list[dict]]) -> str:
    """Generate the markdown tables for all endpoint groups."""
    tag_order_map = OrderedDict((name, desc) for name, desc in TAG_ORDER)
    ordered_tags: list[tuple[str, str]] = []

    # Add tags in the preferred order
    for tag_name, tag_desc in TAG_ORDER:
        if tag_name in grouped:
            ordered_tags.append((tag_name, tag_desc))

    # Append any remaining tags not in TAG_ORDER, sorted alphabetically
    for tag_name in sorted(grouped.keys()):
        if tag_name not in tag_order_map:
            ordered_tags.append((tag_name, ""))

    lines: list[str] = []
    for tag_name, tag_desc in ordered_tags:
        endpoints = grouped[tag_name]
        lines.append(f"### {tag_name}")
        lines.append("")
        if tag_desc:
            lines.append(tag_desc)
            lines.append("")
        lines.append("| Method | Endpoint | Description |")
        lines.append("|--------|----------|-------------|")
        for ep in endpoints:
            method = f"`{ep['method']}`"
            url = endpoint_url(ep["tag"], ep["summary"])
            endpoint_link = f"[`{ep['path']}`]({url})"
            desc = brief_description(ep)
            lines.append(f"| {method} | {endpoint_link} | {desc} |")
        lines.append("")

    return "\n".join(lines)


def update_file(target: Path, generated_content: str) -> bool:
    """Replace content between markers in the target file. Returns True if changes were made."""
    content = target.read_text(encoding="utf-8")

    if START_MARKER not in content or END_MARKER not in content:
        print(f"❌ Markers not found in {target}")
        print(f"   Expected: {START_MARKER} and {END_MARKER}")
        return False

    start_idx = content.index(START_MARKER) + len(START_MARKER)
    end_idx = content.index(END_MARKER)

    new_section = f"\n\n{generated_content}\n"
    new_content = content[:start_idx] + new_section + content[end_idx:]

    if new_content == content:
        return False

    target.write_text(new_content, encoding="utf-8")
    return True


def main() -> None:
    if not OPENAPI_PATH.exists():
        print(f"❌ OpenAPI spec not found: {OPENAPI_PATH}")
        sys.exit(1)
    if not TARGET_PATH.exists():
        print(f"❌ Target file not found: {TARGET_PATH}")
        sys.exit(1)

    print(f"📖 Reading OpenAPI spec: {OPENAPI_PATH}")
    spec = load_openapi_spec(OPENAPI_PATH)

    grouped = extract_endpoints(spec)
    total = sum(len(eps) for eps in grouped.values())
    print(f"📋 Found {total} endpoints across {len(grouped)} tags")

    generated = generate_tables(grouped)

    if update_file(TARGET_PATH, generated):
        print(f"✅ Updated {TARGET_PATH}")
    else:
        print("✅ No changes needed — endpoint tables are up to date.")


if __name__ == "__main__":
    main()
