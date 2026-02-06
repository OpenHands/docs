#!/usr/bin/env python3
"""API documentation generator for OpenHands SDK.

Uses griffe (mkdocstrings) to extract API information from Python source
and generates .mdx files for the documentation site.
"""

import logging
import re
import subprocess
import sys
from pathlib import Path

import griffe

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

DOCS_DIR = Path(__file__).parent.parent
AGENT_SDK_DIR = DOCS_DIR / "agent-sdk"
SDK_SRC = AGENT_SDK_DIR / "openhands-sdk"
OUTPUT_DIR = DOCS_DIR / "sdk" / "api-reference"

MODULES = [
    "openhands.sdk.agent",
    "openhands.sdk.conversation",
    "openhands.sdk.event",
    "openhands.sdk.llm",
    "openhands.sdk.security",
    "openhands.sdk.tool",
    "openhands.sdk.utils",
    "openhands.sdk.workspace",
]


# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

def setup_agent_sdk():
    """Clone or update the agent-sdk repository."""
    if AGENT_SDK_DIR.exists():
        logger.info("Updating agent-sdk...")
        subprocess.run(
            ["git", "fetch", "origin"],
            cwd=AGENT_SDK_DIR, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "reset", "--hard", "origin/main"],
            cwd=AGENT_SDK_DIR, check=True, capture_output=True,
        )
    else:
        logger.info("Cloning agent-sdk...")
        subprocess.run(
            ["git", "clone",
             "https://github.com/OpenHands/software-agent-sdk.git",
             str(AGENT_SDK_DIR)],
            check=True, capture_output=True,
        )


def install_sdk():
    """Install the SDK package."""
    logger.info("Installing openhands-sdk...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-e", str(SDK_SRC)],
        check=True, capture_output=True,
    )


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

def _escape_mdx(content: str) -> str:
    """Escape characters that MDX would try to parse as JSX.

    Curly braces and bare <tag@attr> patterns inside prose are replaced
    so that Mintlify's MDX compiler does not choke on them.  Content
    inside fenced code blocks (``` ... ```) is left untouched.
    """
    out_lines: list[str] = []
    in_code_block = False

    for line in content.split("\n"):
        if line.startswith("```"):
            in_code_block = not in_code_block
            out_lines.append(line)
            continue

        if in_code_block:
            out_lines.append(line)
            continue

        # Escape { and } outside of inline code spans
        escaped = ""
        in_backtick = False
        for ch in line:
            if ch == "`":
                in_backtick = not in_backtick
            if not in_backtick:
                if ch == "{":
                    escaped += "\\{"
                    continue
                if ch == "}":
                    escaped += "\\}"
                    continue
            escaped += ch
        # Escape bare <word> patterns that MDX reads as HTML/JSX tags
        escaped = re.sub(r"<([a-zA-Z][a-zA-Z0-9._@:/-]*)>", r"`<\1>`", escaped)
        out_lines.append(escaped)

    return "\n".join(out_lines)


def _fmt(annotation) -> str:
    """Format a type annotation as a string."""
    if annotation is None:
        return ""
    return str(annotation)


def _has_decorator(obj, name: str) -> bool:
    """Check if a griffe object has a decorator containing *name*."""
    return any(name in str(d.value) for d in getattr(obj, "decorators", []))


def _render_docstring(docstring: griffe.Docstring | None) -> list[str]:
    """Parse a Google-style docstring into markdown lines."""
    if not docstring:
        return []

    lines: list[str] = []
    for section in docstring.parse("google"):
        kind = section.kind

        if kind == griffe.DocstringSectionKind.text:
            lines.append(section.value)
            lines.append("")

        elif kind == griffe.DocstringSectionKind.parameters:
            lines.append("**Parameters:**")
            lines.append("")
            for p in section.value:
                ann = f" *{p.annotation}*" if p.annotation else ""
                desc = f" – {p.description}" if p.description else ""
                lines.append(f"- `{p.name}`{ann}{desc}")
            lines.append("")

        elif kind == griffe.DocstringSectionKind.returns:
            lines.append("**Returns:**")
            lines.append("")
            for r in section.value:
                ann = f"*{r.annotation}* " if r.annotation else ""
                lines.append(f"- {ann}{r.description or ''}".strip())
            lines.append("")

        elif kind == griffe.DocstringSectionKind.raises:
            lines.append("**Raises:**")
            lines.append("")
            for e in section.value:
                lines.append(f"- `{e.annotation}` – {e.description}")
            lines.append("")

        elif kind == griffe.DocstringSectionKind.examples:
            lines.append("**Example:**")
            lines.append("")
            for item in section.value:
                if isinstance(item, tuple):
                    item_kind, value = item
                    if item_kind == "text":
                        lines.append(value)
                    else:
                        lines.append("```python")
                        lines.append(value)
                        lines.append("```")
            lines.append("")

    return lines


def _field_description(attr: griffe.Attribute) -> str:
    """Extract the description= keyword from a Field(...) value."""
    if attr.value is None:
        return ""
    match = re.search(r"description=['\"]([^'\"]+)['\"]", str(attr.value))
    return match.group(1) if match else ""


def _render_property_line(member) -> str:
    """Render a property or attribute as a single bullet line."""
    if isinstance(member, griffe.Function):
        type_str = f": {_fmt(member.returns)}" if member.returns else ""
        desc = ""
        if member.docstring:
            for s in member.docstring.parse("google"):
                if s.kind == griffe.DocstringSectionKind.text:
                    desc = f"\n  {s.value}"
                    break
        return f"- `{member.name}`{type_str}{desc}"

    # griffe.Attribute
    type_str = f": {_fmt(member.annotation)}" if member.annotation else ""
    desc = ""
    if member.docstring:
        desc = member.docstring.value
    else:
        desc = _field_description(member)
    if desc:
        desc = f"\n  {desc}"
    return f"- `{member.name}`{type_str}{desc}"


def _render_function(func: griffe.Function, level: int = 4) -> list[str]:
    """Render a function/method as markdown."""
    hdr = "#" * level
    lines: list[str] = []

    # Build parameter signature
    params: list[str] = []
    for p in func.parameters:
        if p.name in ("self", "cls"):
            continue
        s = p.name
        if p.annotation:
            s += f": {_fmt(p.annotation)}"
        if p.default is not None:
            s += f" = {p.default}"
        params.append(s)

    sig = ", ".join(params)
    ret = f" -> {_fmt(func.returns)}" if func.returns else ""
    abstract = "abstractmethod " if _has_decorator(func, "abstractmethod") else ""

    lines.append(f"**{abstract}{func.name}({sig}){ret}**")
    lines.append("")
    lines.extend(_render_docstring(func.docstring))
    return lines


def _render_class(cls: griffe.Class) -> list[str]:
    """Render a class as markdown."""
    lines: list[str] = []

    lines.append(f"## class {cls.name}")
    lines.append("")
    if cls.bases:
        bases = ", ".join(f"`{b}`" for b in cls.bases)
        lines.append(f"Bases: {bases}")
        lines.append("")

    lines.extend(_render_docstring(cls.docstring))

    # Collect public members
    properties: list = []
    methods: list[griffe.Function] = []

    for name, member in cls.members.items():
        if name.startswith("_") and name != "__init__":
            continue
        member = _resolve(member)
        if member is None:
            continue

        if isinstance(member, griffe.Attribute):
            properties.append(member)
        elif isinstance(member, griffe.Function):
            if _has_decorator(member, "property"):
                properties.append(member)
            else:
                methods.append(member)

    if properties:
        lines.append("### Properties")
        lines.append("")
        for prop in properties:
            lines.append(_render_property_line(prop))
        lines.append("")

    if methods:
        lines.append("### Methods")
        lines.append("")
        for method in methods:
            lines.extend(_render_function(method, level=3))

    return lines


def _resolve(member):
    """Resolve a griffe Alias to its final target."""
    if isinstance(member, griffe.Alias):
        try:
            return member.final_target
        except Exception:
            return None
    return member


# ---------------------------------------------------------------------------
# Module generation
# ---------------------------------------------------------------------------

def generate_module_mdx(module_path: str) -> str:
    """Load a module with griffe and render it as .mdx."""
    module = griffe.load(module_path, search_paths=[str(SDK_SRC)])

    lines = [
        "---",
        f"title: {module_path}",
        f"description: API reference for {module_path}",
        "---",
        "",
    ]

    for name, member in module.members.items():
        if name.startswith("_"):
            continue

        obj = _resolve(member)
        if obj is None:
            continue

        if isinstance(obj, griffe.Class):
            lines.extend(_render_class(obj))
        elif isinstance(obj, griffe.Function):
            lines.extend(_render_function(obj, level=2))

    return _escape_mdx("\n".join(lines))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    setup_agent_sdk()
    install_sdk()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for module_path in MODULES:
        logger.info(f"Generating {module_path}...")
        try:
            content = generate_module_mdx(module_path)
            output_file = OUTPUT_DIR / f"{module_path}.mdx"
            output_file.write_text(content)
        except Exception as e:
            logger.error(f"  Failed to generate {module_path}: {e}")

    logger.info("Done!")


if __name__ == "__main__":
    main()
