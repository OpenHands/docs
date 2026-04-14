#!/usr/bin/env python3
"""
Sync use-case automation cards to the automations overview page.

Each use-case page under ``openhands/usage/use-cases/`` is the **source of
truth** for its automation content.  If a page's YAML frontmatter contains
an ``automation:`` block, this script generates a card for it in the
automations overview page.

The generated card grid lives between marker comments:
  {/* BEGIN:use-case-automations */}  …  {/* END:use-case-automations */}

Each card links to the use-case page's ``#automate-this`` section where the
full prompt and instructions live.

Required frontmatter fields inside ``automation:``:
  - ``icon``    — Font Awesome icon name for the card
  - ``summary`` — Short description shown on the card

The page's ``title`` field is used as the card title (no duplication).

Usage:
  python .github/scripts/sync_use_case_automations.py          # write mode
  python .github/scripts/sync_use_case_automations.py --check  # CI check

Exit codes:
  0 — target page is in sync (or was updated in write mode)
  1 — target page is out of sync (check mode) or validation error
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
AUTOMATIONS_PAGE = REPO_ROOT / "openhands" / "usage" / "automations" / "overview.mdx"
USE_CASES_DIR = REPO_ROOT / "openhands" / "usage" / "use-cases"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)
REQUIRED_FIELDS = ("icon", "summary")


# ── Frontmatter parsing ──────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def collect_use_cases() -> list[tuple[str, str, dict]]:
    """Return (slug, page_title, automation_dict) for use-cases with automation metadata."""
    results: list[tuple[str, str, dict]] = []
    errors: list[str] = []

    for page in sorted(USE_CASES_DIR.glob("*.mdx")):
        if page.name == "overview.mdx":
            continue
        fm = parse_frontmatter(page.read_text())
        if "automation" not in fm:
            continue

        auto = fm["automation"]
        rel = page.relative_to(REPO_ROOT)

        for field in REQUIRED_FIELDS:
            if field not in auto:
                errors.append(f"  {rel}: missing automation.{field}")

        if "title" not in fm:
            errors.append(f"  {rel}: missing top-level title")

        if not errors or all(f"  {rel}" not in e for e in errors):
            results.append((page.stem, fm["title"], auto))

    if errors:
        print("❌  Frontmatter validation errors:", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)

    return results


# ── Generator ─────────────────────────────────────────────────────────


def generate_card_section(use_cases: list[tuple[str, str, dict]]) -> str:
    """Generate the ``use-case-automations`` card grid.

    Each card links to the use-case page's #automate-this section.
    """
    parts: list[str] = []

    parts.append(
        "Each use case has a ready-to-use automation prompt. "
        "Click a card to see the full instructions.\n"
        "\n"
        "<CardGroup cols={2}>"
    )

    for slug, title, auto in use_cases:
        parts.append(
            f'  <Card\n'
            f'    title="{title}"\n'
            f'    icon="{auto["icon"]}"\n'
            f'    href="/openhands/usage/use-cases/{slug}#automate-this"\n'
            f'  >\n'
            f'    {auto["summary"]}\n'
            f'  </Card>'
        )

    parts.append("</CardGroup>")

    return "\n".join(parts)


# ── Marker replacement ───────────────────────────────────────────────


def replace_marker_section(
    content: str, marker: str, new_body: str, filepath: Path
) -> str:
    """Replace everything between BEGIN:<marker> and END:<marker>."""
    begin_pat = re.compile(
        rf"\{{/\*\s*BEGIN:{re.escape(marker)}\s*(?:—[^*]*)?\*/\}}"
    )
    end_pat = re.compile(
        rf"\{{/\*\s*END:{re.escape(marker)}\s*\*/\}}"
    )

    begin_m = begin_pat.search(content)
    end_m = end_pat.search(content)

    if not begin_m and not end_m:
        print(
            f"❌  {filepath.relative_to(REPO_ROOT)}: "
            f"missing both BEGIN:{marker} and END:{marker} markers",
            file=sys.stderr,
        )
        sys.exit(1)
    if not begin_m:
        print(
            f"❌  {filepath.relative_to(REPO_ROOT)}: "
            f"missing BEGIN:{marker} marker",
            file=sys.stderr,
        )
        sys.exit(1)
    if not end_m:
        print(
            f"❌  {filepath.relative_to(REPO_ROOT)}: "
            f"missing END:{marker} marker",
            file=sys.stderr,
        )
        sys.exit(1)
    if begin_m.start() >= end_m.start():
        print(
            f"❌  {filepath.relative_to(REPO_ROOT)}: "
            f"BEGIN:{marker} must come before END:{marker}",
            file=sys.stderr,
        )
        sys.exit(1)

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
        description="Sync use-case automation cards to the automations page."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode: exit 1 if the page is out of sync (for CI).",
    )
    args = parser.parse_args()

    use_cases = collect_use_cases()
    if not use_cases:
        print("No use-case pages with automation frontmatter found.")
        return 0

    original = AUTOMATIONS_PAGE.read_text()
    generated = generate_card_section(use_cases)
    updated = replace_marker_section(
        original, "use-case-automations", generated, AUTOMATIONS_PAGE
    )

    if updated == original:
        print("✅  Automations page is in sync.")
        return 0

    if args.check:
        print(
            f"❌  {AUTOMATIONS_PAGE.relative_to(REPO_ROOT)} is out of sync "
            "with use-case frontmatter.\n"
            "\n"
            "Run:  python .github/scripts/sync_use_case_automations.py\n"
            "Then commit the updated file."
        )
        return 1

    AUTOMATIONS_PAGE.write_text(updated)
    print(f"✅  Updated {AUTOMATIONS_PAGE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
