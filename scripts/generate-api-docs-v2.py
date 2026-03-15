#!/usr/bin/env python3
"""
Proof-of-concept: Direct Python-to-MDX API documentation generator.

This replaces the 1268-line Sphinx-based generator with direct introspection.
Run with: uv run python scripts/generate-api-docs-v2.py

Requirements:
- software-agent-sdk installed (pip install -e ../agent-sdk/openhands-sdk)
"""

import importlib
import inspect
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, get_type_hints


# Modules to document (from openhands.sdk)
MODULES_TO_DOCUMENT = [
    "openhands.sdk.agent",
    "openhands.sdk.llm",
    "openhands.sdk.conversation",
    "openhands.sdk.tool",
    "openhands.sdk.workspace",
    "openhands.sdk.event",
    "openhands.sdk.context",
    "openhands.sdk.hooks",
    "openhands.sdk.mcp",
    "openhands.sdk.critic",
    "openhands.sdk.plugin",
    "openhands.sdk.subagent",
    "openhands.sdk.io",
    "openhands.sdk.secret",
    "openhands.sdk.security",
    "openhands.sdk.skills",
    "openhands.sdk.observability",
    "openhands.sdk.logger",
    "openhands.sdk.utils",
]


@dataclass
class ParsedDocstring:
    """Parsed Google-style docstring."""
    description: str = ""
    args: list[tuple[str, str]] = field(default_factory=list)
    returns: str = ""
    raises: list[tuple[str, str]] = field(default_factory=list)
    attributes: list[tuple[str, str]] = field(default_factory=list)
    example: str = ""
    notes: str = ""


def parse_google_docstring(docstring: str | None) -> ParsedDocstring:
    """Parse a Google-style docstring into structured sections."""
    if not docstring:
        return ParsedDocstring()
    
    result = ParsedDocstring()
    lines = docstring.split('\n')
    
    current_section = 'description'
    section_content = []
    current_item_name = None
    current_item_desc = []
    
    def flush_item():
        nonlocal current_item_name, current_item_desc
        if current_item_name:
            desc = ' '.join(current_item_desc).strip()
            if current_section == 'args':
                result.args.append((current_item_name, desc))
            elif current_section == 'attributes':
                result.attributes.append((current_item_name, desc))
            elif current_section == 'raises':
                result.raises.append((current_item_name, desc))
        current_item_name = None
        current_item_desc = []
    
    def flush_section():
        nonlocal section_content
        content = '\n'.join(section_content).strip()
        if current_section == 'description':
            result.description = content
        elif current_section == 'returns':
            result.returns = content
        elif current_section == 'example':
            result.example = content
        elif current_section == 'notes':
            result.notes = content
        section_content = []
    
    section_headers = {
        'Args:': 'args',
        'Arguments:': 'args',
        'Parameters:': 'args',
        'Attributes:': 'attributes',
        'Returns:': 'returns',
        'Raises:': 'raises',
        'Example:': 'example',
        'Examples:': 'example',
        'Note:': 'notes',
        'Notes:': 'notes',
    }
    
    for line in lines:
        stripped = line.strip()
        
        # Check for section header
        if stripped in section_headers:
            flush_item()
            flush_section()
            current_section = section_headers[stripped]
            continue
        
        # Handle items in Args/Attributes/Raises sections
        if current_section in ('args', 'attributes', 'raises'):
            # Check for new item (name: description or name -- description)
            item_match = re.match(r'^(\w+)\s*(?::|--)\s*(.*)$', stripped)
            if item_match and not stripped.startswith(' '):
                flush_item()
                current_item_name = item_match.group(1)
                current_item_desc = [item_match.group(2)] if item_match.group(2) else []
            elif current_item_name and stripped:
                # Continuation of current item
                current_item_desc.append(stripped)
            continue
        
        # Regular content
        section_content.append(line)
    
    # Flush remaining
    flush_item()
    flush_section()
    
    return result


def format_signature(sig: inspect.Signature, max_line_length: int = 80) -> str:
    """Format a signature for display, wrapping long signatures."""
    params = []
    for name, param in sig.parameters.items():
        if name == 'self':
            continue
        
        param_str = name
        if param.annotation != inspect.Parameter.empty:
            # Simplify complex annotations
            ann = format_annotation(param.annotation)
            param_str = f"{name}: {ann}"
        
        if param.default != inspect.Parameter.empty:
            default = repr(param.default)
            if len(default) > 30:
                default = "..."
            param_str = f"{param_str} = {default}"
        
        params.append(param_str)
    
    # Check return annotation
    return_ann = ""
    if sig.return_annotation != inspect.Signature.empty:
        return_ann = f" -> {format_annotation(sig.return_annotation)}"
    
    params_str = ", ".join(params)
    if len(params_str) + len(return_ann) > max_line_length:
        # Multi-line format
        params_str = ",\n    ".join(params)
        return f"(\n    {params_str}\n){return_ann}"
    
    return f"({params_str}){return_ann}"


def format_annotation(annotation: Any) -> str:
    """Format a type annotation for display."""
    if annotation is None:
        return "None"
    
    if hasattr(annotation, '__name__'):
        return annotation.__name__
    
    # Handle string annotations
    if isinstance(annotation, str):
        return annotation
    
    # Handle typing constructs
    origin = getattr(annotation, '__origin__', None)
    args = getattr(annotation, '__args__', ())
    
    if origin is not None:
        origin_name = getattr(origin, '__name__', str(origin))
        if args:
            args_str = ", ".join(format_annotation(a) for a in args)
            return f"{origin_name}[{args_str}]"
        return origin_name
    
    return str(annotation).replace('typing.', '')


def escape_mdx(text: str) -> str:
    """Escape text for MDX compatibility."""
    # Escape curly braces outside of code blocks
    # This is a simplified version - full impl would track code blocks
    text = re.sub(r'(?<!`)\{(?!`)', r'\\{', text)
    text = re.sub(r'(?<!`)\}(?!`)', r'\\}', text)
    return text


def generate_class_docs(name: str, cls: type) -> str:
    """Generate MDX documentation for a class."""
    doc = inspect.getdoc(cls) or ""
    parsed = parse_google_docstring(doc)
    
    # Get signature
    try:
        sig = inspect.signature(cls)
        sig_str = format_signature(sig)
    except (ValueError, TypeError):
        sig_str = "()"
    
    mdx = f"""
---

### {name}

```python
class {name}{sig_str}
```

{parsed.description}

"""
    
    # Attributes section
    if parsed.attributes:
        mdx += "**Attributes:**\n\n"
        for attr_name, attr_desc in parsed.attributes:
            mdx += f"- `{attr_name}`: {escape_mdx(attr_desc)}\n"
        mdx += "\n"
    
    # Example section
    if parsed.example:
        mdx += f"**Example:**\n\n{parsed.example}\n\n"
    
    # Methods
    methods = []
    for method_name, method in inspect.getmembers(cls):
        if method_name.startswith('_') and method_name != '__init__':
            continue
        if not callable(method):
            continue
        if inspect.ismethod(method) or inspect.isfunction(method):
            # Skip inherited methods from base classes like BaseModel
            if hasattr(method, '__qualname__') and cls.__name__ in method.__qualname__:
                methods.append((method_name, method))
    
    for method_name, method in methods:
        mdx += generate_method_docs(method_name, method)
    
    return mdx


def generate_method_docs(name: str, method) -> str:
    """Generate MDX documentation for a method."""
    doc = inspect.getdoc(method) or ""
    parsed = parse_google_docstring(doc)
    
    # Get signature
    try:
        sig = inspect.signature(method)
        sig_str = format_signature(sig)
    except (ValueError, TypeError):
        sig_str = "()"
    
    display_name = name if name != '__init__' else '\_\_init\_\_'
    
    mdx = f"""
#### {display_name}()

```python
def {name}{sig_str}
```

{parsed.description}

"""
    
    # Arguments
    if parsed.args:
        mdx += "**Arguments:**\n\n"
        for arg_name, arg_desc in parsed.args:
            mdx += f"- `{arg_name}`: {escape_mdx(arg_desc)}\n"
        mdx += "\n"
    
    # Returns
    if parsed.returns:
        mdx += f"**Returns:** {escape_mdx(parsed.returns)}\n\n"
    
    # Raises
    if parsed.raises:
        mdx += "**Raises:**\n\n"
        for exc_name, exc_desc in parsed.raises:
            mdx += f"- `{exc_name}`: {escape_mdx(exc_desc)}\n"
        mdx += "\n"
    
    # Example
    if parsed.example:
        mdx += f"**Example:**\n\n{parsed.example}\n\n"
    
    return mdx


def generate_function_docs(name: str, func) -> str:
    """Generate MDX documentation for a standalone function."""
    doc = inspect.getdoc(func) or ""
    parsed = parse_google_docstring(doc)
    
    try:
        sig = inspect.signature(func)
        sig_str = format_signature(sig)
    except (ValueError, TypeError):
        sig_str = "()"
    
    mdx = f"""
---

### {name}()

```python
def {name}{sig_str}
```

{parsed.description}

"""
    
    if parsed.args:
        mdx += "**Arguments:**\n\n"
        for arg_name, arg_desc in parsed.args:
            mdx += f"- `{arg_name}`: {escape_mdx(arg_desc)}\n"
        mdx += "\n"
    
    if parsed.returns:
        mdx += f"**Returns:** {escape_mdx(parsed.returns)}\n\n"
    
    if parsed.example:
        mdx += f"**Example:**\n\n{parsed.example}\n\n"
    
    return mdx


def get_public_members(module) -> list[tuple[str, Any]]:
    """Get public members of a module, respecting __all__ if defined."""
    if hasattr(module, '__all__'):
        members = []
        for name in module.__all__:
            if hasattr(module, name):
                members.append((name, getattr(module, name)))
        return members
    
    # Fallback: get non-private members
    return [
        (name, obj) for name, obj in inspect.getmembers(module)
        if not name.startswith('_')
    ]


def generate_module_docs(module_name: str) -> str:
    """Generate MDX documentation for a module."""
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Warning: Could not import {module_name}: {e}")
        return ""
    
    mdx = f"""---
title: {module_name}
description: API reference for {module_name} module
---

"""
    
    members = get_public_members(module)
    
    # Separate classes and functions
    classes = [(n, o) for n, o in members if inspect.isclass(o)]
    functions = [(n, o) for n, o in members if inspect.isfunction(o)]
    
    # Generate docs for classes first
    for name, cls in classes:
        # Skip if class is imported from another module
        if hasattr(cls, '__module__') and not cls.__module__.startswith(module_name.rsplit('.', 1)[0]):
            continue
        mdx += generate_class_docs(name, cls)
    
    # Then functions
    for name, func in functions:
        if hasattr(func, '__module__') and not func.__module__.startswith(module_name.rsplit('.', 1)[0]):
            continue
        mdx += generate_function_docs(name, func)
    
    return mdx


def main():
    """Generate API documentation for all modules."""
    # Add agent-sdk to path if needed
    agent_sdk_path = Path(__file__).parent.parent.parent / "agent-sdk" / "openhands-sdk"
    if agent_sdk_path.exists():
        sys.path.insert(0, str(agent_sdk_path))
    
    output_dir = Path(__file__).parent.parent / "sdk" / "api-reference-v2"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Generating API docs to {output_dir}")
    
    for module_name in MODULES_TO_DOCUMENT:
        print(f"  Processing {module_name}...")
        mdx_content = generate_module_docs(module_name)
        
        if mdx_content:
            output_file = output_dir / f"{module_name}.mdx"
            output_file.write_text(mdx_content)
            print(f"    -> {output_file.name}")
    
    print("\nDone! Generated docs are in sdk/api-reference-v2/")
    print("\nNote: This is a proof-of-concept. Full implementation would include:")
    print("  - Better type annotation formatting")
    print("  - Property detection")
    print("  - Cross-reference link generation")
    print("  - Navigation config updates")


if __name__ == "__main__":
    main()
