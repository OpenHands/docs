#!/usr/bin/env python3
"""
Sync use-case automation cards across documentation pages.

Reads ``_data/use-case-automations.yaml`` (the single source of truth) and
regenerates the marked sections in:

* ``openhands/usage/automations/examples.mdx``  — card grid + Tabs per use case
* ``openhands/usage/use-cases/<slug>.mdx``       — "Automate This" section

The script replaces content between marker comments:
  {/* BEGIN:<marker> ... */}  …  {/* END:<marker> */}

Exit codes:
  0 — all files are in sync (or were updated with --write)
  1 — files are out of sync (CI check mode)
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = REPO_ROOT / "_data" / "use-case-automations.yaml"
EXAMPLES_PAGE = REPO_ROOT / "openhands" / "usage" / "automations" / "examples.mdx"
USE_CASES_DIR = REPO_ROOT / "openhands" / "usage" / "use-cases"

BEGIN_RE = re.compile(
    r"\{/\*\s*BEGIN:([\w-]+)\s*(?:—[^*]*)?\*/\}"
)
END_RE = re.compile(
    r"\{/\*\s*END:([\w-]+)\s*\*/\}"
)


def load_data() -> list[dict]:
    with open(DATA_FILE) as f:
        return yaml.safe_load(f)["use_cases"]


# ── Generators ────────────────────────────────────────────────────────

def _indent(text: str, n: int = 4) -> str:
    return textwrap.indent(text, " " * n)


def _prompt_block(prompt: str, indent: int = 4) -> str:
    """Wrap a prompt string in a fenced code block, indented."""
    lines = prompt.rstrip("\n").split("\n")
    block = "```\n" + "\n".join(lines) + "\n```"
    return _indent(block, indent)


def generate_examples_section(use_cases: list[dict]) -> str:
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

    # Cards
    for uc in use_cases:
        parts.append(
            f'  <Card\n'
            f'    title="{uc["title"]}"\n'
            f'    icon="{uc["icon"]}"\n'
            f'    href="/openhands/usage/use-cases/{uc["slug"]}"\n'
            f'  >\n'
            f'    {uc["card_description"]}\n'
            f'  </Card>'
        )

    parts.append("</CardGroup>")

    # Tabs per use case
    for uc in use_cases:
        parts.append(f'\n### {uc["title"]}')
        parts.append("")
        parts.append("<Tabs>")
        parts.append('  <Tab title="Prompt">')
        parts.append(_prompt_block(uc["automation_prompt"]))
        parts.append("  </Tab>")
        parts.append(f'  <Tab title="{uc["alt_tab_title"]}">')
        parts.append(f'    {uc["alt_tab_body"]}')
        parts.append("  </Tab>")
        parts.append("</Tabs>")

    return "\n".join(parts)


def generate_automate_this(uc: dict) -> str:
    """Generate the ``automate-this`` block for a single use-case page."""
    prompt = uc["automation_prompt"].rstrip("\n")
    return (
        f"## Automate This\n"
        f"\n"
        f'{uc["use_case_intro"]}\n'
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

def replace_marker_section(
    content: str, marker: str, new_body: str
) -> str:
    """Replace everything between BEGIN:<marker> and END:<marker>."""
    begin_pattern = re.compile(
        rf"\{{/\*\s*BEGIN:{re.escape(marker)}\s*(?:—[^*]*)?\*/\}}"
    )
    end_pattern = re.compile(
        rf"\{{/\*\s*END:{re.escape(marker)}\s*\*/\}}"
    )

    begin_match = begin_pattern.search(content)
    end_match = end_pattern.search(content)

    if not begin_match or not end_match:
        return content  # markers not found — skip

    begin_tag = begin_match.group(0)
    end_tag = end_match.group(0)

    before = content[: begin_match.start()]
    after = content[end_match.end() :]

    return f"{before}{begin_tag}\n\n{new_body}\n\n{end_tag}{after}"


# ── Main ──────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync use-case automation cards from YAML data to MDX pages."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode: exit 1 if files are out of sync (for CI).",
    )
    args = parser.parse_args()

    use_cases = load_data()
    diffs: list[str] = []

    # 1. Update examples.mdx
    original = EXAMPLES_PAGE.read_text()
    generated = generate_examples_section(use_cases)
    updated = replace_marker_section(original, "use-case-automations", generated)

    if updated != original:
        diffs.append(str(EXAMPLES_PAGE.relative_to(REPO_ROOT)))
        if not args.check:
            EXAMPLES_PAGE.write_text(updated)
            print(f"  ✏️  Updated {EXAMPLES_PAGE.relative_to(REPO_ROOT)}")

    # 2. Update individual use-case pages
    for uc in use_cases:
        page = USE_CASES_DIR / f'{uc["slug"]}.mdx'
        if not page.exists():
            print(f"  ⚠️  Use-case page not found: {page.relative_to(REPO_ROOT)}")
            diffs.append(str(page.relative_to(REPO_ROOT)) + " (missing)")
            continue

        original = page.read_text()
        generated = generate_automate_this(uc)
        updated = replace_marker_section(original, "automate-this", generated)

        if updated != original:
            diffs.append(str(page.relative_to(REPO_ROOT)))
            if not args.check:
                page.write_text(updated)
                print(f"  ✏️  Updated {page.relative_to(REPO_ROOT)}")

    # 3. Check for use-case pages without automation entries
    existing_slugs = {uc["slug"] for uc in use_cases}
    for page in sorted(USE_CASES_DIR.glob("*.mdx")):
        if page.name == "overview.mdx":
            continue
        slug = page.stem
        if slug not in existing_slugs:
            content = page.read_text()
            if BEGIN_RE.search(content):
                # Has markers but no YAML entry — stale
                print(
                    f"  ⚠️  {page.relative_to(REPO_ROOT)} has automation markers "
                    f"but no entry in {DATA_FILE.relative_to(REPO_ROOT)}"
                )

    if diffs:
        if args.check:
            print("\n❌  Files are out of sync with "
                  f"{DATA_FILE.relative_to(REPO_ROOT)}:")
            for d in diffs:
                print(f"     - {d}")
            print(
                "\nRun:  python .github/scripts/sync_use_case_automations.py\n"
                "Then commit the updated files."
            )
            return 1
        else:
            print(f"\n✅  Updated {len(diffs)} file(s).")
    else:
        print("✅  All files are in sync.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
