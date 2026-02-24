#!/usr/bin/env python3

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


def group_name(rel_path: Path) -> str:
    top = rel_path.parts[0]
    return {
        "overview": "Overview",
        "openhands": "OpenHands",
        "sdk": "Agent SDK",
    }.get(top, top.replace("-", " ").title())


def build_llms_txt(pages: list[DocPage]) -> str:
    grouped: dict[str, list[DocPage]] = {}
    for p in pages:
        grouped.setdefault(group_name(p.rel_path), []).append(p)

    for g in grouped:
        grouped[g] = sorted(grouped[g], key=lambda x: (x.title.lower(), x.route))

    lines: list[str] = [
        "# OpenHands Docs",
        "",
        "> LLM-friendly index of OpenHands documentation (V1). Legacy V0 docs pages are intentionally excluded.",
        "",
    ]

    for group in sorted(grouped.keys()):
        lines.append(f"## {group}")
        lines.append("")

        for p in grouped[group]:
            url = f"{BASE_URL}{p.route}.md"
            line = f"- [{p.title}]({url})"
            if p.description:
                line += f": {p.description}"
            lines.append(line)

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_llms_full_txt(pages: list[DocPage]) -> str:
    header = [
        "# OpenHands Docs",
        "",
        "> Consolidated documentation context for LLMs (V1-only). Legacy V0 docs pages are intentionally excluded.",
        "",
    ]

    chunks: list[str] = ["\n".join(header).rstrip()]

    for p in sorted(pages, key=lambda x: x.route):
        chunks.append(
            f"\n\n# {p.title}\nSource: {BASE_URL}{p.route}\n\n{p.body}\n"
        )

    return "".join(chunks).lstrip() + "\n"


def main() -> None:
    pages = iter_doc_pages()

    llms_txt = build_llms_txt(pages)
    llms_full = build_llms_full_txt(pages)

    (ROOT / "llms.txt").write_text(llms_txt, encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(llms_full, encoding="utf-8")


if __name__ == "__main__":
    main()
