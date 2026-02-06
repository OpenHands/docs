#!/usr/bin/env python3
"""
API documentation generator for OpenHands SDK using Sphinx JSON builder.

Uses ``sphinx-build -b json`` to produce structured HTML, then parses it
into clean, Mintlify-compatible MDX files.  This approach replaces the
former markdown builder + regex-cleanup pipeline with a more reliable
HTML-tree-based conversion.
"""

from __future__ import annotations

import json
import logging
import re
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Optional

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ── Minimal HTML DOM ─────────────────────────────────────────────────────

VOID_TAGS = frozenset(
    {
        "area", "base", "br", "col", "embed", "hr", "img",
        "input", "link", "meta", "source", "track", "wbr",
    }
)


class El:
    """Lightweight DOM node."""

    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag: str, attrs: dict[str, str]):
        self.tag = tag
        self.attrs = attrs
        self.children: list["El | str"] = []

    @property
    def classes(self) -> list[str]:
        return self.attrs.get("class", "").split()

    @property
    def id(self) -> str:
        return self.attrs.get("id", "")

    def text(self) -> str:
        parts: list[str] = []
        for c in self.children:
            parts.append(c if isinstance(c, str) else c.text())
        return "".join(parts)

    def find(self, tag: str | None = None, *, cls: str | None = None) -> "El | None":
        for r in self._iter(tag, cls):
            return r
        return None

    def find_all(
        self, tag: str | None = None, *, cls: str | None = None
    ) -> list["El"]:
        return list(self._iter(tag, cls))

    def direct(self, tag: str | None = None) -> list["El"]:
        return [
            c
            for c in self.children
            if isinstance(c, El) and (tag is None or c.tag == tag)
        ]

    def _iter(self, tag: str | None, cls: str | None):
        for c in self.children:
            if not isinstance(c, El):
                continue
            ok = True
            if tag and c.tag != tag:
                ok = False
            if cls and cls not in c.classes:
                ok = False
            if ok:
                yield c
            yield from c._iter(tag, cls)

    def __repr__(self) -> str:
        return f"<{self.tag} class={' '.join(self.classes)!r}>"


class _TreeBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = El("root", {})
        self._stack: list[El] = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        el = El(tag, {k: (v or "") for k, v in attrs})
        self._stack[-1].children.append(el)
        if tag not in VOID_TAGS:
            self._stack.append(el)

    def handle_endtag(self, tag: str) -> None:
        for i in range(len(self._stack) - 1, 0, -1):
            if self._stack[i].tag == tag:
                del self._stack[i:]
                return

    def handle_data(self, data: str) -> None:
        self._stack[-1].children.append(data)


def _parse(html: str) -> El:
    b = _TreeBuilder()
    b.feed(html)
    return b.root


# ── Sphinx HTML → MDX converter ─────────────────────────────────────────


class _Converter:
    """Walk Sphinx autodoc HTML and emit Mintlify-compatible MDX."""

    CLASS_MODULE: dict[str, str] = {
        "Agent": "agent", "AgentBase": "agent", "AgentContext": "agent",
        "BaseConversation": "conversation", "Conversation": "conversation",
        "LocalConversation": "conversation", "RemoteConversation": "conversation",
        "ConversationState": "conversation", "ConversationStats": "conversation",
        "ConversationExecutionStatus": "conversation",
        "ConversationVisualizerBase": "conversation",
        "DefaultConversationVisualizer": "conversation",
        "EventLog": "conversation", "EventsListBase": "conversation",
        "SecretRegistry": "conversation", "StuckDetector": "conversation",
        "Event": "event", "LLMConvertibleEvent": "event",
        "MessageEvent": "event", "ActionEvent": "event",
        "ObservationEvent": "event", "ObservationBaseEvent": "event",
        "AgentErrorEvent": "event", "PauseEvent": "event",
        "SystemPromptEvent": "event", "TokenEvent": "event",
        "UserRejectObservation": "event",
        "Condensation": "event", "CondensationRequest": "event",
        "CondensationSummaryEvent": "event",
        "ConversationStateUpdateEvent": "event",
        "LLMCompletionLogEvent": "event",
        "LLM": "llm", "LLMRegistry": "llm", "LLMResponse": "llm",
        "Message": "llm", "ImageContent": "llm", "TextContent": "llm",
        "ThinkingBlock": "llm", "RedactedThinkingBlock": "llm",
        "Metrics": "llm", "MetricsSnapshot": "llm",
        "RegistryEvent": "llm", "RouterLLM": "llm",
        "ReasoningItemModel": "llm", "MessageToolCall": "llm",
        "SecurityRisk": "security", "SecurityManager": "security",
        "Tool": "tool", "ToolDefinition": "tool", "ToolAnnotations": "tool",
        "Action": "tool", "Observation": "tool",
        "ToolExecutor": "tool", "ExecutableTool": "tool",
        "FinishTool": "tool", "ThinkTool": "tool",
        "Workspace": "workspace", "BaseWorkspace": "workspace",
        "LocalWorkspace": "workspace", "RemoteWorkspace": "workspace",
        "CommandResult": "workspace", "FileOperationResult": "workspace",
    }

    def __init__(self, module: str) -> None:
        self.module = module
        self.module_short = module.split(".")[-1]
        self._out: list[str] = []

    # ── public API ───────────────────────────────────────────────────

    def convert(self, html_body: str) -> str:
        root = _parse(html_body)
        self._out = []
        self._walk_root(root)
        body = "\n".join(self._out)
        return (
            f"---\n"
            f"title: {self.module}\n"
            f"description: API reference for {self.module} module\n"
            f"---\n\n{body}\n"
        )

    # ── root walker ──────────────────────────────────────────────────

    def _emit(self, line: str = "") -> None:
        self._out.append(line)

    def _walk_root(self, root: El) -> None:
        for child in root.children:
            if isinstance(child, str):
                t = child.strip()
                if t:
                    self._emit(t)
                continue
            if child.tag in ("section", "div"):
                self._walk_root(child)
            elif child.tag == "dl":
                self._handle_dl(child, level=3)
            elif child.tag == "p":
                t = self._inline(child).strip()
                if t:
                    self._emit(t)
                    self._emit()

    def _handle_dl(self, dl: El, level: int) -> None:
        css = dl.classes
        if "class" in css and "py" in css:
            self._handle_class(dl, level)
        elif "function" in css and "py" in css:
            self._handle_function(dl, level)

    # ── classes ───────────────────────────────────────────────────────

    def _handle_class(self, dl: El, level: int) -> None:
        dts = dl.direct("dt")
        dds = dl.direct("dd")
        if not dts:
            return
        dt = dts[0]
        name = self._sig_name(dt)
        self._emit(f"\n{'#' * level} class {name}")
        self._emit()
        if not dds:
            return
        dd = dds[0]

        bases_line = ""
        desc: list[str] = []
        example_lines: list[str] = []
        properties: list[dict[str, Any]] = []
        methods: list[list[str]] = []
        nested_classes: list[El] = []

        for child in dd.children:
            if not isinstance(child, El):
                continue
            if child.tag == "p":
                txt = self._inline(child).strip()
                if txt.startswith("Bases:"):
                    bases_line = txt
                elif txt:
                    desc.append(txt)
            elif child.tag == "div" and "admonition" in child.classes:
                title_el = child.find("p", cls="admonition-title")
                title_text = title_el.text().strip() if title_el else ""
                if title_text.lower() == "example":
                    example_lines = self._extract_example(child)
                else:
                    # NOTE / other admonitions go into methods bucket
                    methods.append(self._format_admonition(child, level + 1))
            elif child.tag == "dl" and "py" in child.classes:
                if "class" in child.classes:
                    nested_classes.append(child)
                else:
                    self._classify_member(child, level + 1, properties, methods)

        # Emit bases
        if bases_line:
            self._emit(bases_line)
            self._emit()
        # Emit description
        for p in desc:
            self._emit(p)
            self._emit()
        # Emit example
        if example_lines:
            self._emit(f"{'#' * (level + 1)} Example")
            self._emit()
            for ln in example_lines:
                self._emit(ln)
            self._emit()
        # Emit properties
        if properties:
            self._emit()
            self._emit(f"{'#' * (level + 1)} Properties")
            self._emit()
            for prop in properties:
                self._emit(prop["header"])
                for d in prop.get("desc", []):
                    self._emit(f"  {d}")
        # Emit methods
        if methods:
            self._emit()
            self._emit(f"{'#' * (level + 1)} Methods")
            self._emit()
            for m_lines in methods:
                for ln in m_lines:
                    self._emit(ln)
        # Nested classes
        for nc in nested_classes:
            self._emit()
            self._handle_class(nc, level)

    def _classify_member(
        self,
        dl: El,
        level: int,
        properties: list[dict[str, Any]],
        methods: list[list[str]],
    ) -> None:
        css = dl.classes
        dt = dl.find("dt")
        dd = dl.find("dd")
        if not dt:
            return

        is_prop = "property" in css
        is_attr = "attribute" in css

        if is_prop or (is_attr and self._has_type_annotation(dt)):
            prop = self._extract_property(dt, dd)
            if prop:
                properties.append(prop)
        else:
            m = self._extract_method_or_attr(dt, dd, level)
            if m:
                methods.append(m)

    def _has_type_annotation(self, dt: El) -> bool:
        for em in dt.find_all("em", cls="property"):
            t = em.text()
            if ":" in t and "class" not in t:
                return True
        full = dt.text()
        name = self._sig_name(dt)
        after = full.split(name, 1)[-1] if name in full else full
        if re.match(r"\s*:\s*\S", after):
            return True
        return False

    def _extract_property(self, dt: El, dd: El | None) -> dict[str, Any] | None:
        name = self._sig_name(dt)
        if not name:
            return None
        type_str = self._extract_type(dt)
        value_str = self._extract_value(dt)
        if type_str:
            header = f"- `{name}`: {type_str}"
        elif value_str:
            header = f"- `{name}`: {value_str}"
        else:
            header = f"- `{name}`"
        desc: list[str] = []
        if dd:
            for child in dd.children:
                if isinstance(child, El) and child.tag == "p":
                    t = self._inline(child).strip()
                    if t:
                        desc.append(t)
                elif isinstance(child, El) and child.tag == "dl":
                    desc.extend(self._format_field_list(child))
        return {"header": header, "desc": desc}

    def _extract_method_or_attr(
        self, dt: El, dd: El | None, level: int
    ) -> list[str] | None:
        name = self._sig_name(dt)
        if not name:
            return None
        lines: list[str] = []
        has_paren = bool(dt.find("span", cls="sig-paren"))
        prefix = self._method_prefix(dt)
        value = self._extract_value(dt)
        if has_paren:
            hdr = f"{'#' * level} "
            if prefix:
                hdr += f"{prefix} "
            hdr += f"{name}()"
            lines.append(hdr)
        elif value:
            lines.append(f"{'#' * level} {name} = {value}")
        else:
            lines.append(f"{'#' * level} {name}")
        lines.append("")
        if dd:
            lines.extend(self._format_body(dd))
        return lines

    # ── module-level functions ────────────────────────────────────────

    def _handle_function(self, dl: El, level: int) -> None:
        dts = dl.direct("dt")
        dds = dl.direct("dd")
        if not dts:
            return
        dt = dts[0]
        dd = dds[0] if dds else None
        name = self._sig_name(dt)
        self._emit(f"\n{'#' * level} {name}()")
        self._emit()
        if dd:
            for ln in self._format_body(dd):
                self._emit(ln)

    # ── body / field-list formatting ─────────────────────────────────

    def _format_body(self, dd: El) -> list[str]:
        lines: list[str] = []
        for child in dd.children:
            if not isinstance(child, El):
                continue
            if child.tag == "p":
                t = self._inline(child).strip()
                if t:
                    lines.append(t)
            elif child.tag == "dl":
                lines.extend(self._format_field_list(child))
            elif child.tag in ("ul", "ol"):
                lines.extend(self._format_list(child))
            elif child.tag == "div" and "admonition" in child.classes:
                lines.extend(self._format_admonition(child, 4))
            elif child.tag == "blockquote":
                lines.extend(self._format_blockquote(child))
            elif child.tag == "div" and child.find("pre"):
                pre = child.find("pre")
                if pre:
                    code = pre.text().strip()
                    lines.append("```python")
                    lines.append(code)
                    lines.append("```")
            elif child.tag == "pre":
                code = child.text().strip()
                lines.append("```python")
                lines.append(code)
                lines.append("```")
        if lines:
            lines.append("")
        return lines

    def _format_field_list(self, dl: El) -> list[str]:
        lines: list[str] = []
        dts = dl.direct("dt")
        dds = dl.direct("dd")
        for dt, dd in zip(dts, dds):
            label = dt.text().strip().rstrip(":")
            if label in (
                "Parameters", "Params", "Parameter", "Keyword Arguments"
            ):
                lines.append("* Parameters:")
                ul = dd.find("ul")
                if ul:
                    for li in ul.direct("li"):
                        t = self._format_param(li)
                        lines.append(f"  * {t}")
                else:
                    for p in dd.direct("p"):
                        t = self._format_param(p)
                        if t:
                            lines.append(f"  {t}")
            elif label == "Returns":
                lines.append("* Returns:")
                t = self._inline(dd).strip()
                if t:
                    lines.append(f"  {t}")
            elif label == "Return type":
                lines.append("* Return type:")
                t = self._inline(dd).strip()
                if t:
                    lines.append(f"  {t}")
            elif label in ("Raises", "Raise"):
                lines.append("* Raises:")
                ul = dd.find("ul")
                if ul:
                    for li in ul.direct("li"):
                        t = self._inline(li).strip()
                        lines.append(f"  {t}")
                else:
                    t = self._inline(dd).strip()
                    if t:
                        lines.append(f"  {t}")
            elif label == "Type":
                lines.append("* Type:")
                t = self._inline(dd).strip()
                if t:
                    lines.append(f"  {t}")
            else:
                lines.append(f"* {label}:")
                t = self._inline(dd).strip()
                if t:
                    lines.append(f"  {t}")
        return lines

    def _format_param(self, el: El) -> str:
        """Format a parameter list item, converting <strong> names to backticks."""
        text = self._inline(el).strip()
        # Pattern: "name – description" or "name (type) – description"
        m = re.match(r"^(\w+)\s*(\([^)]*\))?\s*[–\-]\s*(.+)$", text, re.DOTALL)
        if m:
            name = m.group(1)
            desc = m.group(3).strip()
            return f"`{name}` – {desc}"
        return text

    def _format_list(self, ul: El) -> list[str]:
        lines: list[str] = []
        ordered = ul.tag == "ol"
        start = int(ul.attrs.get("start", "1"))
        for i, li in enumerate(ul.direct("li"), start):
            t = self._inline(li).strip()
            nested: list[str] = []
            for child in li.children:
                if isinstance(child, El) and child.tag in ("ul", "ol"):
                    nested.extend(self._format_list(child))
            if ordered:
                lines.append(f"{i}. {t}")
            else:
                lines.append(f"- {t}")
            for nl in nested:
                lines.append(f"  {nl}")
        return lines

    def _format_blockquote(self, bq: El) -> list[str]:
        lines: list[str] = []
        for child in bq.children:
            if isinstance(child, El) and child.tag == "p":
                t = self._inline(child).strip()
                if t:
                    lines.append(f"  {t}")
            elif isinstance(child, El) and child.tag in ("ul", "ol"):
                for ln in self._format_list(child):
                    lines.append(f"  {ln}")
        return lines

    def _format_admonition(self, div: El, level: int) -> list[str]:
        lines: list[str] = []
        title_el = div.find("p", cls="admonition-title")
        title = title_el.text().strip() if title_el else ""
        if title:
            lines.append(f"{'#' * level} {title}")
        for child in div.children:
            if (
                isinstance(child, El)
                and child.tag == "p"
                and "admonition-title" not in child.classes
            ):
                t = self._inline(child).strip()
                if t:
                    lines.append(t)
        lines.append("")
        return lines

    # ── example extraction ───────────────────────────────────────────

    def _extract_example(self, div: El) -> list[str]:
        lines: list[str] = []
        for child in div.children:
            if not isinstance(child, El):
                continue
            if "admonition-title" in child.classes:
                continue
            if child.tag == "div" and child.find("pre"):
                pre = child.find("pre")
                if pre:
                    code = pre.text().strip()
                    lines.append("```pycon")
                    lines.append(code)
                    lines.append("```")
            elif child.tag == "pre":
                code = child.text().strip()
                lines.append("```pycon")
                lines.append(code)
                lines.append("```")
            elif child.tag == "p":
                t = self._inline(child).strip()
                if t:
                    lines.append(t)
        return lines

    # ── inline text conversion ───────────────────────────────────────

    def _inline(self, el: El) -> str:
        parts: list[str] = []
        for c in el.children:
            if isinstance(c, str):
                parts.append(self._clean_text(c))
            elif c.tag == "a":
                link_text = c.text().strip()
                href = c.attrs.get("href", "")
                parts.append(self._resolve_ref(link_text, href))
            elif c.tag == "code":
                parts.append(f"`{c.text()}`")
            elif c.tag in ("em", "i"):
                if "property" in c.classes:
                    txt = c.text().strip()
                    if txt == "class":
                        continue
                    parts.append(txt)
                else:
                    parts.append(c.text())
            elif c.tag in ("strong", "b"):
                parts.append(c.text())
            elif c.tag == "br":
                parts.append("\n")
            elif c.tag == "cite":
                parts.append(f"`{c.text()}`")
            elif c.tag == "pre":
                # inline code block – shouldn't happen normally
                parts.append(f"`{c.text()}`")
            elif c.tag == "dl":
                field_lines = self._format_field_list(c)
                if field_lines:
                    parts.append("\n".join(field_lines))
            elif c.tag in ("ul", "ol"):
                list_lines = self._format_list(c)
                if list_lines:
                    parts.append("\n".join(list_lines))
            else:
                parts.append(self._inline(c))
        return "".join(parts)

    def _clean_text(self, t: str) -> str:
        if "{" in t and "}" in t:
            t = re.sub(r"\{[^}]*\}", "(configuration object)", t)
        t = re.sub(r"\$\{[^}]+\}", "(variable)", t)
        # Escape HTML-like tags so MDX doesn't treat them as JSX components
        # e.g. <secret-hidden> → `<secret-hidden>`
        t = re.sub(r"<(/?[a-zA-Z][a-zA-Z0-9_-]*)>", r"`<\1>`", t)
        return t

    def _resolve_ref(self, text: str, href: str) -> str:
        if not href or href.startswith("http"):
            if href:
                return f"[{text}]({href})"
            return text
        class_name = text.strip()
        target_module = self.CLASS_MODULE.get(class_name)
        if target_module == self.module_short:
            anchor = f"class-{class_name.lower()}"
            return f"[{class_name}](#{anchor})"
        return class_name

    # ── extraction helpers ───────────────────────────────────────────

    def _sig_name(self, dt: El) -> str:
        el = dt.find("span", cls="sig-name") or dt.find("span", cls="descname")
        if el:
            return el.text().strip()
        eid = dt.id
        return eid.split(".")[-1] if eid else dt.text().strip().split("(")[0].strip()

    def _method_prefix(self, dt: El) -> str:
        for em in dt.find_all("em", cls="property"):
            t = em.text().strip()
            for keyword in (
                "abstractmethod classmethod",
                "abstract classmethod",
                "classmethod abstractmethod",
                "abstractmethod",
                "classmethod",
                "staticmethod",
                "static",
                "final",
            ):
                if keyword in t:
                    return keyword
        return ""

    def _extract_type(self, dt: El) -> str:
        # Strategy: collect everything after the name that forms the type
        # annotation.  In Sphinx HTML, the type info may span multiple
        # sibling elements (em for ":", a for the type name, spans, etc.)
        name = self._sig_name(dt)
        full = dt.text()
        if name and name in full:
            after = full.split(name, 1)[1]
            # Match ": <type>" possibly followed by "= <value>"
            m = re.match(r"\s*:\s*(.+?)(?:\s*=.*)?$", after)
            if m:
                raw_type = m.group(1).strip()
                # Now rebuild the type with proper link resolution by
                # finding all elements after the sig-name in the dt.
                type_parts = self._collect_type_parts(dt, name)
                if type_parts:
                    return type_parts
                return self._clean_text(raw_type)
        return ""

    def _collect_type_parts(self, dt: El, sig_name: str) -> str:
        """Collect type annotation parts from dt, resolving links."""
        # Find the position after sig-name and ":"
        found_name = False
        found_colon = False
        parts: list[str] = []
        for c in dt.children:
            if not found_name:
                if isinstance(c, El):
                    txt = c.text().strip()
                    if sig_name in txt:
                        found_name = True
                continue
            if not found_colon:
                if isinstance(c, El) and "property" in c.classes:
                    txt = c.text().strip()
                    if ":" in txt:
                        found_colon = True
                        # Grab any type text after the colon within this em
                        after_colon = txt.split(":", 1)[1].strip()
                        if after_colon and after_colon != "=":
                            parts.append(after_colon)
                elif isinstance(c, str) and ":" in c:
                    found_colon = True
                    after_colon = c.split(":", 1)[1].strip()
                    if after_colon:
                        parts.append(after_colon)
                continue
            # After the colon — collect type tokens
            if isinstance(c, str):
                txt = c.strip()
                if txt.startswith("="):
                    break  # Hit the value assignment
                if txt:
                    parts.append(self._clean_text(txt))
            elif isinstance(c, El):
                txt = c.text().strip()
                if txt.startswith("="):
                    break
                if c.tag == "a":
                    parts.append(self._resolve_ref(txt, c.attrs.get("href", "")))
                elif c.tag == "code":
                    parts.append(f"`{txt}`")
                else:
                    inline = self._inline(c).strip()
                    if inline and inline != "=" and not inline.startswith("="):
                        parts.append(inline)
        return " ".join(parts).strip() if parts else ""

    def _extract_value(self, dt: El) -> str:
        full = dt.text()
        m = re.search(r"=\s*(.+)$", full)
        if m:
            val = m.group(1).strip()
            if "{" in val:
                val = "(configuration object)"
            return val
        return ""


# ── Main generator ───────────────────────────────────────────────────────


class SphinxJSONDocGenerator:
    def __init__(self, docs_dir: Path) -> None:
        self.docs_dir = docs_dir
        self.agent_sdk_dir = docs_dir / "agent-sdk"
        self.output_dir = docs_dir / "sdk" / "api-reference"
        self.sphinx_dir = docs_dir / "scripts" / "sphinx"

    def run(self) -> None:
        """Main execution method."""
        logger.info("Starting API documentation generation (Sphinx JSON)...")
        self.setup_agent_sdk()
        self.fix_agent_sdk_mdx_syntax()
        self.install_sdk()
        self.generate_sphinx_docs()
        self.convert_json_to_mdx()
        self.update_navigation()
        logger.info("API documentation generation completed successfully!")

    # ── step 1: clone / update agent-sdk ─────────────────────────────

    def setup_agent_sdk(self) -> None:
        """Clone or update the agent-sdk repository."""
        if self.agent_sdk_dir.exists():
            logger.info("Updating existing agent-sdk repository...")
            self._cmd(["git", "fetch", "origin"], cwd=self.agent_sdk_dir)
            self._cmd(
                ["git", "reset", "--hard", "origin/main"], cwd=self.agent_sdk_dir
            )
        else:
            logger.info("Cloning agent-sdk repository...")
            self._cmd(
                [
                    "git", "clone",
                    "https://github.com/OpenHands/software-agent-sdk.git",
                    str(self.agent_sdk_dir),
                ]
            )

    # ── step 2: fix MDX syntax in agent-sdk files ────────────────────

    def fix_agent_sdk_mdx_syntax(self) -> None:
        """Fix MDX syntax issues in agent-sdk files to prevent Mintlify parsing errors."""
        logger.info("Fixing MDX syntax issues in agent-sdk files...")
        agents_md = self.agent_sdk_dir / "AGENTS.md"
        if agents_md.exists():
            content = agents_md.read_text()
            content = re.sub(r"<([^<>]*@[^<>]*)>", r"&lt;\1&gt;", content)
            agents_md.write_text(content)
        readme_md = self.agent_sdk_dir / "README.md"
        if readme_md.exists():
            content = readme_md.read_text()
            content = re.sub(
                r"<!--\s*(.*?)\s*-->", r"{/* \1 */}", content, flags=re.DOTALL
            )
            content = re.sub(
                r"<(img|br|hr)([^>]*?)(?<!/)>", r"<\1\2 />", content
            )
            readme_md.write_text(content)

    # ── step 3: install SDK ──────────────────────────────────────────

    def install_sdk(self) -> None:
        """Install the SDK package."""
        logger.info("Installing openhands-sdk package...")
        sdk_path = self.agent_sdk_dir / "openhands-sdk"
        self._cmd(["python", "-m", "pip", "install", "-e", str(sdk_path)])

    # ── step 4: generate Sphinx docs (JSON builder) ──────────────────

    def generate_sphinx_docs(self) -> None:
        """Generate documentation using Sphinx JSON builder."""
        logger.info("Generating documentation with Sphinx (JSON builder)...")
        self._create_sphinx_config()
        self._create_rst_files()
        self._build_sphinx_docs()

    def _create_sphinx_config(self) -> None:
        src = self.sphinx_dir / "source"
        src.mkdir(parents=True, exist_ok=True)
        (src / "conf.py").write_text(
            "import os, sys\n"
            "sys.path.insert(0, os.path.abspath("
            "'../../../agent-sdk/openhands-sdk'))\n"
            "\n"
            "project = 'OpenHands SDK'\n"
            "copyright = '2024, OpenHands'\n"
            "author = 'OpenHands'\n"
            "\n"
            "extensions = [\n"
            "    'sphinx.ext.autodoc',\n"
            "    'sphinx.ext.napoleon',\n"
            "]\n"
            "\n"
            "autodoc_default_options = {\n"
            "    'members': True,\n"
            "    'undoc-members': True,\n"
            "    'show-inheritance': True,\n"
            "    'special-members': '__init__',\n"
            "}\n"
            "\n"
            "napoleon_google_docstring = True\n"
            "napoleon_numpy_docstring = True\n"
            "napoleon_include_init_with_doc = False\n"
            "napoleon_include_private_with_doc = False\n"
        )

    def _create_rst_files(self) -> None:
        src = self.sphinx_dir / "source"
        (src / "index.rst").write_text(
            "OpenHands SDK API Reference\n"
            "===========================\n"
            "\n"
            ".. toctree::\n"
            "   :maxdepth: 2\n"
            "   :caption: Contents:\n"
            "\n"
            "   openhands.sdk\n"
        )
        modules = [
            "agent", "conversation", "event", "llm",
            "tool", "workspace", "security", "utils",
        ]
        toctree = "\n".join(f"   openhands.sdk.{m}" for m in modules)
        (src / "openhands.sdk.rst").write_text(
            "openhands.sdk package\n"
            "=====================\n"
            "\n"
            ".. automodule:: openhands.sdk\n"
            "   :members:\n"
            "   :undoc-members:\n"
            "   :show-inheritance:\n"
            "\n"
            "Submodules\n"
            "----------\n"
            "\n"
            ".. toctree::\n"
            "   :maxdepth: 1\n"
            "\n"
            f"{toctree}\n"
        )
        for mod in modules:
            title = f"openhands.sdk.{mod} module"
            (src / f"openhands.sdk.{mod}.rst").write_text(
                f"{title}\n{'=' * len(title)}\n\n"
                f".. automodule:: openhands.sdk.{mod}\n"
                f"   :members:\n"
                f"   :undoc-members:\n"
                f"   :show-inheritance:\n"
            )

    def _build_sphinx_docs(self) -> None:
        build = self.sphinx_dir / "build"
        src = self.sphinx_dir / "source"
        if build.exists():
            shutil.rmtree(build)
        self._cmd(["sphinx-build", "-b", "json", str(src), str(build)])

    # ── step 5: convert JSON → MDX ──────────────────────────────────

    def convert_json_to_mdx(self) -> None:
        """Parse Sphinx JSON output and produce MDX files."""
        logger.info("Converting Sphinx JSON to MDX...")
        build = self.sphinx_dir / "build"
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        for fjson in sorted(build.glob("openhands.sdk.*.fjson")):
            stem = fjson.stem
            if stem == "openhands.sdk":
                logger.info(f"Skipping {fjson.name} (top-level duplicate)")
                continue
            logger.info(f"Processing {fjson.name}")
            data = json.loads(fjson.read_text())
            html_body = data.get("body", "")
            converter = _Converter(stem)
            mdx = converter.convert(html_body)
            out = self.output_dir / f"{stem}.mdx"
            out.write_text(mdx)

    # ── step 6: update navigation ────────────────────────────────────

    def update_navigation(self) -> None:
        """Update the navigation configuration."""
        logger.info("Updating navigation configuration...")
        api_files = sorted(self.output_dir.glob("*.mdx"))
        nav_entries = [f"sdk/api-reference/{f.stem}" for f in api_files]
        snippet = {
            "navigation": [{"group": "API Reference", "pages": nav_entries}]
        }
        (self.docs_dir / "scripts" / "mint-config-snippet.json").write_text(
            json.dumps(snippet, indent=2)
        )
        self._update_docs_json(nav_entries)
        logger.info(
            f"Generated navigation for {len(nav_entries)} API reference files"
        )

    def _update_docs_json(self, nav_entries: list[str]) -> None:
        docs_json = self.docs_dir / "docs.json"
        if not docs_json.exists():
            logger.warning("docs.json not found, skipping main navigation update")
            return
        try:
            cfg = json.loads(docs_json.read_text())
            updated = False
            for tab in cfg.get("navigation", {}).get("tabs", []):
                if tab.get("tab") == "SDK":
                    for page in tab.get("pages", []):
                        if (
                            isinstance(page, dict)
                            and page.get("group") == "API Reference"
                        ):
                            page["pages"] = nav_entries
                            updated = True
                            break
                    if updated:
                        break
            if updated:
                docs_json.write_text(json.dumps(cfg, indent=2))
                logger.info("Updated API Reference navigation in docs.json")
            else:
                logger.warning(
                    "Could not find API Reference section in docs.json to update"
                )
        except Exception as e:
            logger.error(f"Error updating docs.json: {e}")

    # ── utility ──────────────────────────────────────────────────────

    def _cmd(self, cmd: list[str], cwd: Path | None = None) -> None:
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd or self.docs_dir,
                capture_output=True,
                text=True,
                check=True,
            )
            if result.stdout:
                logger.debug(f"STDOUT: {result.stdout}")
            if result.stderr:
                logger.warning(f"STDERR: {result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {' '.join(cmd)}")
            logger.error(f"Exit code: {e.returncode}")
            logger.error(f"STDOUT: {e.stdout}")
            logger.error(f"STDERR: {e.stderr}")
            raise


def main() -> None:
    """Main entry point."""
    docs_dir = Path(__file__).parent.parent
    SphinxJSONDocGenerator(docs_dir).run()


if __name__ == "__main__":
    main()
