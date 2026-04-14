#!/usr/bin/env python3
"""
Sync use-case automation cards to the automation examples page.

Each use-case page under ``openhands/usage/use-cases/`` is the **source of
truth**.  If a page's YAML frontmatter contains an ``automation:`` block, the
script copies that content into the "Use Case Automations" section of
``openhands/usage/automations/examples.mdx``.

The generated section lives between marker comments in examples.mdx:
  {/* BEGIN:use-case-automations */}  …  {/* END:use-case-automations */}

Usage:
  python .github/scripts/sync_use_case_automations.py          # write mode
  python .github/scripts/sync_use_case_automations.py --check  # CI check

Exit codes:
  0 — examples page is in sync (or was updated in write mode)
  1 — examples page is out of sync (check mode)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
EXAMPLES_PAGE = REPO_ROOT / "openhands" / "usage" / "automations" / "examples.mdx"
USE_CASES_DIR = REPO_ROOT / "openhands" / "usage" / "use-cases"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)


# ── Frontmatter parsing ──────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
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


# ── Generator ─────────────────────────────────────────────────────────


def generate_examples_section(use_cases: list[tuple[str, dict]]) -> str:
    """Generate the ``use-case-automations`` block for *examples.mdx*.

    Each card links to the "Automate This" section of the corresponding
    use-case page, where the full prompt and instructions live.
    """
    parts: list[str] = []

    parts.append(
        "## Use Case Automations\n"
        "\n"
        "Each use case has a ready-to-use automation prompt. "
        "Click a card to see the full instructions.\n"
        "\n"
        "<CardGroup cols={2}>"
    )

    for slug, auto in use_cases:
        parts.append(
            f'  <Card\n'
            f'    title="{auto["card_title"]}"\n'
            f'    icon="{auto["icon"]}"\n'
            f'    href="/openhands/usage/use-cases/{slug}#automate-this"\n'
            f'  >\n'
            f'    {auto["card_description"]}\n'
            f'  </Card>'
        )

    parts.append("</CardGroup>")

    return "\n".join(parts)


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

    original = EXAMPLES_PAGE.read_text()
    generated = generate_examples_section(use_cases)
    updated = replace_marker_section(original, "use-case-automations", generated)

    if updated == original:
        print("✅  Automation examples page is in sync.")
        return 0

    if args.check:
        print(
            "❌  openhands/usage/automations/examples.mdx is out of sync "
            "with use-case frontmatter.\n"
            "\n"
            "Run:  python .github/scripts/sync_use_case_automations.py\n"
            "Then commit the updated file."
        )
        return 1

    EXAMPLES_PAGE.write_text(updated)
    print(f"✅  Updated {EXAMPLES_PAGE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
