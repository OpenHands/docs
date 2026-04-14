#!/usr/bin/env python3
"""
Sync use-case automation cards to the automation examples page.

Each use-case page under ``openhands/usage/use-cases/`` is the **source of
truth**.  If a page's YAML frontmatter contains an ``automation:`` block, the
script treats it as an automation-enabled use case and:

1. Generates the "Use Case Automations" card grid + Tabs section in
   ``openhands/usage/automations/examples.mdx`` (between markers).
2. Generates the "Automate This" section in the use-case page itself
   (between markers).

Marker format (JSX comments, ignored by Mintlify):
  {/* BEGIN:use-case-automations */}  …  {/* END:use-case-automations */}
  {/* BEGIN:automate-this */}          …  {/* END:automate-this */}

Usage:
  python .github/scripts/sync_use_case_automations.py          # write mode
  python .github/scripts/sync_use_case_automations.py --check  # CI check

Exit codes:
  0 — all files are in sync (or were updated in write mode)
  1 — files are out of sync (check mode)
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
EXAMPLES_PAGE = REPO_ROOT / "openhands" / "usage" / "automations" / "examples.mdx"
USE_CASES_DIR = REPO_ROOT / "openhands" / "usage" / "use-cases"

# Frontmatter delimiters
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)


# ── Frontmatter parsing ──────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from an MDX file."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def collect_use_cases() -> list[tuple[str, dict]]:
    """Return (slug, automation_dict) for every use-case with automation metadata."""
    results: list[tuple[str, dict]] = []
    for page in sorted(USE_CASES_DIR.glob("*.mdx")):
        if page.name == "overview.mdx":
            continue
        fm = parse_frontmatter(page.read_text())
        if "automation" in fm:
            results.append((page.stem, fm["automation"]))
    return results


# ── Generators ────────────────────────────────────────────────────────

def _indent(text: str, n: int = 4) -> str:
    return textwrap.indent(text, " " * n)


def _prompt_block(prompt: str, indent: int = 4) -> str:
    lines = prompt.rstrip("\n").split("\n")
    block = "```\n" + "\n".join(lines) + "\n```"
    return _indent(block, indent)


def generate_examples_section(use_cases: list[tuple[str, dict]]) -> str:
    """Generate the ``use-case-automations`` block for *examples.mdx*."""
    parts: list[str] = []

    parts.append(
        "## Use Case Automations\n"
        "\n"
        "These automations correspond to documented "
        "[use cases](/openhands/usage/use-cases/overview). "
        "Each card links to the full use case guide, the relevant plugin "
        "or SDK example, and a prompt you can copy directly.\n"
        "\n"
        "<CardGroup cols={2}>"
    )

    for slug, auto in use_cases:
        parts.append(
            f'  <Card\n'
            f'    title="{auto["card_title"]}"\n'
            f'    icon="{auto["icon"]}"\n'
            f'    href="/openhands/usage/use-cases/{slug}"\n'
            f'  >\n'
            f'    {auto["card_description"]}\n'
            f'  </Card>'
        )

    parts.append("</CardGroup>")

    for slug, auto in use_cases:
        parts.append(f'\n### {auto["card_title"]}')
        parts.append("")
        parts.append("<Tabs>")
        parts.append('  <Tab title="Prompt">')
        parts.append(_prompt_block(auto["prompt"]))
        parts.append("  </Tab>")
        parts.append(f'  <Tab title="{auto["alt_tab_title"]}">')
        parts.append(f'    {auto["alt_tab_body"]}')
        parts.append("  </Tab>")
        parts.append("</Tabs>")

    return "\n".join(parts)


def generate_automate_this(auto: dict) -> str:
    """Generate the ``automate-this`` block for a single use-case page."""
    prompt = auto["prompt"].rstrip("\n")
    return (
        f"## Automate This\n"
        f"\n"
        f'{auto["intro"]}\n'
        f"\n"
        f"```\n"
        f"{prompt}\n"
        f"```\n"
        f"\n"
        f'<Card title="More Automation Templates" icon="clock" '
        f'href="/openhands/usage/automations/examples">\n'
        f"  Browse all automation examples, including vulnerability scanning, "
        f"code review, monitoring, and more.\n"
        f"</Card>"
    )


# ── Marker replacement ───────────────────────────────────────────────

def replace_marker_section(content: str, marker: str, new_body: str) -> str:
    """Replace everything between BEGIN:<marker> and END:<marker>."""
    begin_pat = re.compile(
        rf"\{{/\*\s*BEGIN:{re.escape(marker)}\s*(?:—[^*]*)?\*/\}}"
    )
    end_pat = re.compile(
        rf"\{{/\*\s*END:{re.escape(marker)}\s*\*/\}}"
    )

    begin_m = begin_pat.search(content)
    end_m = end_pat.search(content)

    if not begin_m or not end_m:
        return content

    return (
        content[: begin_m.start()]
        + begin_m.group(0)
        + "\n\n"
        + new_body
        + "\n\n"
        + end_m.group(0)
        + content[end_m.end() :]
    )


# ── Main ──────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync use-case automation cards to the examples page."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode: exit 1 if files are out of sync (for CI).",
    )
    args = parser.parse_args()

    use_cases = collect_use_cases()
    if not use_cases:
        print("No use-case pages with automation frontmatter found.")
        return 0

    diffs: list[str] = []

    # 1. Regenerate the examples page card section
    original = EXAMPLES_PAGE.read_text()
    generated = generate_examples_section(use_cases)
    updated = replace_marker_section(original, "use-case-automations", generated)

    if updated != original:
        diffs.append(str(EXAMPLES_PAGE.relative_to(REPO_ROOT)))
        if not args.check:
            EXAMPLES_PAGE.write_text(updated)
            print(f"  ✏️  Updated {EXAMPLES_PAGE.relative_to(REPO_ROOT)}")

    # 2. Regenerate the "Automate This" section in each use-case page
    for slug, auto in use_cases:
        page = USE_CASES_DIR / f"{slug}.mdx"
        original = page.read_text()
        generated = generate_automate_this(auto)
        updated = replace_marker_section(original, "automate-this", generated)

        if updated != original:
            rel = str(page.relative_to(REPO_ROOT))
            diffs.append(rel)
            if not args.check:
                page.write_text(updated)
                print(f"  ✏️  Updated {rel}")

    if diffs:
        if args.check:
            print(
                "\n❌  The automation examples page is out of sync with "
                "use-case frontmatter:"
            )
            for d in diffs:
                print(f"     - {d}")
            print(
                "\nRun:  python .github/scripts/sync_use_case_automations.py\n"
                "Then commit the updated files."
            )
            return 1
        print(f"\n✅  Updated {len(diffs)} file(s).")
    else:
        print("✅  All files are in sync.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
