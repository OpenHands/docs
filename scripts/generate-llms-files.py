#!/usr/bin/env python3

"""Generate custom `llms.txt` + `llms-full.txt` for the OpenHands docs site.

Why this exists
--------------
Mintlify automatically generates and hosts `/llms.txt` and `/llms-full.txt` for
Mintlify-backed documentation sites.

For OpenHands, we want those files to provide **V1-only** context to LLMs while we
still keep some legacy V0 pages available for humans. In particular, we want to
exclude:

- The legacy docs subtree under `openhands/usage/v0/`
- Any page whose filename starts with `V0*`

Mintlify supports overriding the auto-generated files by committing `llms.txt`
(and/or `llms-full.txt`) to the repository root.

References:
- Mintlify docs: https://www.mintlify.com/docs/ai/llmstxt
- llms.txt proposal: https://llmstxt.org/

How to use
----------
Run from the repository root (this repo's `docs/` directory):

    ./scripts/generate-llms-files.py

This will rewrite `./llms.txt` and `./llms-full.txt`.

Design notes
------------
- We only parse `title` and `description` from MDX frontmatter.
- We intentionally group OpenHands pages into sections that clearly distinguish:
  - OpenHands CLI
  - OpenHands Web App Server (incl. "Local GUI")
  - OpenHands Cloud
  - OpenHands Software Agent SDK

"""


from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://docs.openhands.dev"

EXCLUDED_DIRS = {".git", ".github", ".agents", "tests", "openapi", "logo"}


@dataclass(frozen=True)
class DocPage:
    rel_path: Path
    route: str
    title: str
    description: str | None
    body: str


_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def _strip_quotes(val: str) -> str:
    val = val.strip()
    if (val.startswith('"') and val.endswith('"')) or (
        val.startswith("'") and val.endswith("'")
    ):
        return val[1:-1]
    return val


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}, text

    fm_text = m.group(1)
    body = text[m.end() :]

    fm: dict[str, str] = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip()
        if not k:
            continue
        fm[k] = _strip_quotes(v)

    return fm, body


def rel_to_route(rel_path: Path) -> str:
    p = rel_path.as_posix()
    if p.endswith(".mdx"):
        p = p[: -len(".mdx")]

    if p.endswith("/index"):
        p = p[: -len("/index")]

    return "/" + p.lstrip("/")


def is_v0_page(rel_path: Path) -> bool:
    s = rel_path.as_posix()
    if "/openhands/usage/v0/" in s:
        return True
    if rel_path.name.startswith("V0"):
        return True
    return False


def iter_doc_pages() -> list[DocPage]:
    pages: list[DocPage] = []

    for mdx_path in sorted(ROOT.rglob("*.mdx")):
        rel_path = mdx_path.relative_to(ROOT)

        if any(part in EXCLUDED_DIRS for part in rel_path.parts):
            continue
        if is_v0_page(rel_path):
            continue

        raw = mdx_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(raw)

        title = fm.get("title")
        if not title:
            continue

        description = fm.get("description")
        route = rel_to_route(rel_path)

        pages.append(
            DocPage(
                rel_path=rel_path,
                route=route,
                title=title,
                description=description,
                body=body.strip(),
            )
        )

    return pages


LLMS_SECTION_ORDER = [
    "OpenHands Software Agent SDK",
    "OpenHands CLI",
    "OpenHands Web App Server",
    "OpenHands Cloud",
    "OpenHands Overview",
    "Other",
]


def section_name(page: DocPage) -> str:
    """Map a page to an `llms.txt` section.

    This is deliberately opinionated. The goal is to make it obvious to an LLM
    what content is about:

    - the OpenHands CLI
    - the OpenHands Web App + server (what the nav historically called "Local GUI")
    - OpenHands Cloud
    - the OpenHands Software Agent SDK

    """

    route = page.route

    if route.startswith("/sdk"):
        return "OpenHands Software Agent SDK"

    if route.startswith("/openhands/usage/cli"):
        return "OpenHands CLI"

    if route.startswith("/openhands/usage/cloud"):
        return "OpenHands Cloud"

    if route.startswith("/openhands/usage"):
        return "OpenHands Web App Server"

    if route.startswith("/overview"):
        return "OpenHands Overview"

    return "Other"


def _section_sort_key(section: str) -> tuple[int, str]:
    """Stable ordering for llms sections, with a sane fallback."""

    try:
        return (LLMS_SECTION_ORDER.index(section), "")
    except ValueError:
        return (len(LLMS_SECTION_ORDER), section.lower())


def build_llms_txt(pages: list[DocPage]) -> str:
    """Generate `llms.txt`.

    The format follows the llms.txt proposal:
    - One H1
    - A short blockquote summary
    - Optional non-heading text
    - H2 sections containing bullet lists of links

    """

    grouped: dict[str, list[DocPage]] = {}
    for page in pages:
        grouped.setdefault(section_name(page), []).append(page)

    for section_pages in grouped.values():
        section_pages.sort(key=lambda p: (p.title.lower(), p.route))

    lines: list[str] = [
        "# OpenHands Docs",
        "",
        "> LLM-friendly index of OpenHands documentation (V1). Legacy V0 docs pages are intentionally excluded.",
        "",
        "The sections below intentionally separate OpenHands product documentation (Web App Server / Cloud / CLI)",
        "from the OpenHands Software Agent SDK.",
        "",
    ]

    for section in sorted(grouped.keys(), key=_section_sort_key):
        lines.append(f"## {section}")
        lines.append("")

        for page in grouped[section]:
            url = f"{BASE_URL}{page.route}.md"
            line = f"- [{page.title}]({url})"
            if page.description:
                line += f": {page.description}"
            lines.append(line)

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_llms_full_txt(pages: list[DocPage]) -> str:
    """Generate `llms-full.txt`.

    This is meant to be copy/pasteable context for AI tools.

    Unlike `llms.txt`, there is no strict spec for `llms-full.txt`, but we keep a
    single H1, then use H2/H3 headings to make the document navigable.

    """

    grouped: dict[str, list[DocPage]] = {}
    for page in pages:
        grouped.setdefault(section_name(page), []).append(page)

    for section_pages in grouped.values():
        section_pages.sort(key=lambda p: p.route)

    lines: list[str] = [
        "# OpenHands Docs",
        "",
        "> Consolidated documentation context for LLMs (V1-only). Legacy V0 docs pages are intentionally excluded.",
        "",
    ]

    for section in sorted(grouped.keys(), key=_section_sort_key):
        lines.append(f"## {section}")
        lines.append("")

        for page in grouped[section]:
            lines.append(f"### {page.title}")
            lines.append(f"Source: {BASE_URL}{page.route}.md")
            lines.append("")
            if page.body:
                lines.append(page.body)
                lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    pages = iter_doc_pages()

    llms_txt = build_llms_txt(pages)
    llms_full = build_llms_full_txt(pages)

    (ROOT / "llms.txt").write_text(llms_txt, encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(llms_full, encoding="utf-8")


if __name__ == "__main__":
    main()
