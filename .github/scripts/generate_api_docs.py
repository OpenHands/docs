#!/usr/bin/env python3
"""
Generate Python API reference documentation from the software-agent-sdk.

This script extracts docstrings from Python modules and generates MDX documentation
files compatible with Mintlify.
"""

import ast
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Modules to document (from openhands.sdk)
MODULES_TO_DOCUMENT = [
    "agent",
    "conversation",
    "llm",
    "tool",
    "workspace",
    "mcp",
    "event",
    "context",
    "security",
    "io",
    "git",
]


def extract_docstring(node: ast.AST) -> Optional[str]:
    """Extract docstring from an AST node."""
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
        return ast.get_docstring(node)
    return None


def extract_function_signature(node: ast.FunctionDef) -> str:
    """Extract function signature as a string."""
    args = []
    
    # Regular arguments
    for arg in node.args.args:
        arg_str = arg.arg
        if arg.annotation:
            arg_str += f": {ast.unparse(arg.annotation)}"
        args.append(arg_str)
    
    # Return annotation
    returns = ""
    if node.returns:
        returns = f" -> {ast.unparse(node.returns)}"
    
    return f"{node.name}({', '.join(args)}){returns}"


def parse_module_file(file_path: Path) -> Dict:
    """Parse a Python file and extract documentation."""
    try:
        content = file_path.read_text()
        tree = ast.parse(content)
    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}")
        return {"module_doc": "", "classes": [], "functions": []}
    
    module_doc = ast.get_docstring(tree) or ""
    
    classes = []
    functions = []
    
    # Only process top-level nodes
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_doc = extract_docstring(node)
            methods = []
            
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_doc = extract_docstring(item)
                    methods.append({
                        "name": item.name,
                        "signature": extract_function_signature(item),
                        "docstring": method_doc or ""
                    })
            
            classes.append({
                "name": node.name,
                "docstring": class_doc or "",
                "methods": methods
            })
        
        elif isinstance(node, ast.FunctionDef):
            func_doc = extract_docstring(node)
            functions.append({
                "name": node.name,
                "signature": extract_function_signature(node),
                "docstring": func_doc or ""
            })
    
    return {
        "module_doc": module_doc,
        "classes": classes,
        "functions": functions
    }


def format_docstring(docstring: str) -> str:
    """Format a docstring for MDX output."""
    if not docstring:
        return ""
    
    # Basic formatting - could be enhanced to handle Google/NumPy style docstrings
    lines = docstring.split('\n')
    formatted = []
    
    for line in lines:
        # Convert common docstring patterns to markdown
        line = line.strip()
        if line.startswith('Args:') or line.startswith('Parameters:'):
            formatted.append('\n**Parameters:**\n')
        elif line.startswith('Returns:'):
            formatted.append('\n**Returns:**\n')
        elif line.startswith('Raises:'):
            formatted.append('\n**Raises:**\n')
        elif line.startswith('Example:') or line.startswith('Examples:'):
            formatted.append('\n**Example:**\n')
        else:
            formatted.append(line)
    
    return '\n'.join(formatted)


def generate_mdx_for_module(module_name: str, module_data: Dict, github_base: str) -> str:
    """Generate MDX content for a module."""
    title = f"{module_name.capitalize()}"
    description = f"API reference for openhands.sdk.{module_name}"
    
    content = f"""---
title: {title}
description: {description}
---

# {title}

"""
    
    if module_data.get("module_doc"):
        content += f"{format_docstring(module_data['module_doc'])}\n\n"
    
    # Add source link
    content += f"""**Source:** [`openhands/sdk/{module_name}/`]({github_base}/openhands-sdk/openhands/sdk/{module_name}/)

---

"""
    
    # Add classes
    classes = [c for c in module_data.get("classes", []) if not c["name"].startswith("_")]
    if classes:
        content += "## Classes\n\n"
        for cls in classes:
            content += f"### `{cls['name']}`\n\n"
            if cls["docstring"]:
                content += f"{format_docstring(cls['docstring'])}\n\n"
            
            # Add methods
            methods = [m for m in cls.get("methods", []) 
                      if not m["name"].startswith("_") or m["name"] == "__init__"]
            if methods:
                content += "#### Methods\n\n"
                for method in methods:
                    content += f"##### `{method['signature']}`\n\n"
                    if method["docstring"]:
                        content += f"{format_docstring(method['docstring'])}\n\n"
            
            content += "---\n\n"
    
    # Add functions
    functions = [f for f in module_data.get("functions", []) if not f["name"].startswith("_")]
    if functions:
        content += "## Functions\n\n"
        for func in functions:
            content += f"### `{func['signature']}`\n\n"
            if func["docstring"]:
                content += f"{format_docstring(func['docstring'])}\n\n"
            content += "---\n\n"
    
    return content


def generate_docs_for_all_modules(sdk_path: Path, output_dir: Path):
    """Generate documentation for all modules."""
    print(f"Generating documentation from {sdk_path}...")
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    github_base = "https://github.com/OpenHands/software-agent-sdk/tree/main"
    sdk_module_path = sdk_path / "openhands-sdk" / "openhands" / "sdk"
    
    if not sdk_module_path.exists():
        print(f"Error: SDK module path not found: {sdk_module_path}")
        sys.exit(1)
    
    # Process each module
    for module_name in MODULES_TO_DOCUMENT:
        module_dir = sdk_module_path / module_name
        
        if not module_dir.exists():
            print(f"Warning: Module directory not found: {module_dir}")
            continue
        
        print(f"Processing module: {module_name}")
        
        # Start with init file
        module_data = {"module_doc": "", "classes": [], "functions": []}
        init_file = module_dir / "__init__.py"
        
        if init_file.exists():
            module_data = parse_module_file(init_file)
        
        # Also parse other Python files in the module
        for py_file in sorted(module_dir.glob("*.py")):
            if py_file.name != "__init__.py" and not py_file.name.startswith("_"):
                print(f"  Parsing {py_file.name}")
                file_data = parse_module_file(py_file)
                module_data["classes"].extend(file_data.get("classes", []))
                module_data["functions"].extend(file_data.get("functions", []))
        
        # Generate MDX
        mdx_content = generate_mdx_for_module(module_name, module_data, github_base)
        output_file = output_dir / f"{module_name}.mdx"
        output_file.write_text(mdx_content)
        print(f"  Generated: {output_file.name}")
    
    print("Documentation generation complete")


def create_index_page(output_dir: Path):
    """Create the API reference index page."""
    content = """---
title: API Reference
description: Python API reference for the OpenHands SDK
---

# API Reference

This is the auto-generated Python API reference for the OpenHands SDK.

## Available Modules

"""
    
    # Add links to each module
    for module in MODULES_TO_DOCUMENT:
        module_title = module.replace("_", " ").title()
        content += f"- **[{module_title}](./{module})** - API reference for `openhands.sdk.{module}`\n"
    
    content += """
## Overview

The OpenHands SDK provides a Python interface for building AI agents with:

- **Agent Management**: Core agent orchestration and execution
- **Conversation Handling**: Structured dialogue and message management  
- **LLM Integration**: Support for multiple language models via LiteLLM
- **Tool System**: Extensible tool registry and execution
- **Workspace Management**: Isolated execution environments
- **MCP Support**: Model Context Protocol integration
- **Event System**: Agent lifecycle and execution events
- **Context Management**: Conversation and execution context
- **Security**: Safe code execution and sandboxing
- **I/O Handling**: Stream management and output handling
- **Git Integration**: Version control operations

For usage examples and guides, see the [SDK Documentation](/sdk/guides/quickstart).

## Source Code

The complete source code is available on GitHub: [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk)
"""
    
    index_file = output_dir / "index.mdx"
    index_file.write_text(content)
    print(f"Created overview page: {index_file}")


def update_docs_json(docs_json_path: Path):
    """Update docs.json to include API reference in navigation."""
    print("Updating docs.json navigation...")
    
    with open(docs_json_path, 'r') as f:
        docs_config = json.load(f)
    
    # Find the SDK tab
    sdk_tab = None
    for tab in docs_config.get("navigation", {}).get("tabs", []):
        if tab.get("tab") == "SDK":
            sdk_tab = tab
            break
    
    if not sdk_tab:
        print("Warning: SDK tab not found in docs.json")
        return
    
    # Check if API Reference already exists
    api_ref_exists = False
    for page in sdk_tab.get("pages", []):
        if isinstance(page, dict) and page.get("group") == "API Reference":
            api_ref_exists = True
            break
    
    if not api_ref_exists:
        # Add API Reference section
        api_ref_section = {
            "group": "API Reference",
            "pages": [
                "sdk/api/index",
                "sdk/api/agent",
                "sdk/api/conversation",
                "sdk/api/llm",
                "sdk/api/tool",
                "sdk/api/workspace",
                "sdk/api/mcp",
                "sdk/api/event",
                "sdk/api/context",
                "sdk/api/security",
                "sdk/api/io",
                "sdk/api/git",
            ]
        }
        
        # Insert after Architecture section if it exists
        pages = sdk_tab.get("pages", [])
        arch_index = None
        for i, page in enumerate(pages):
            if isinstance(page, dict) and page.get("group") == "Architecture":
                arch_index = i
                break
        
        if arch_index is not None:
            pages.insert(arch_index + 1, api_ref_section)
        else:
            # Just append at the end
            pages.append(api_ref_section)
        
        sdk_tab["pages"] = pages
        
        # Write back to docs.json
        with open(docs_json_path, 'w') as f:
            json.dump(docs_config, f, indent=2)
            f.write('\n')  # Add trailing newline
        
        print("docs.json updated successfully")
    else:
        print("API Reference already exists in docs.json")


def main():
    """Main entry point."""
    # Get paths
    script_dir = Path(__file__).parent
    docs_root = script_dir.parent.parent
    sdk_path = Path(os.environ.get("AGENT_SDK_PATH", docs_root.parent / "agent-sdk"))
    
    if not sdk_path.exists():
        print(f"Error: SDK path not found: {sdk_path}")
        print("Set AGENT_SDK_PATH environment variable to the agent-sdk repository path")
        sys.exit(1)
    
    # Output directory
    output_dir = docs_root / "sdk" / "api"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate documentation
    generate_docs_for_all_modules(sdk_path, output_dir)
    
    # Create index page
    create_index_page(output_dir)
    
    # Update docs.json
    docs_json = docs_root / "docs.json"
    update_docs_json(docs_json)
    
    print("\n✅ API documentation generation complete!")
    print(f"   Output: {output_dir}")


if __name__ == "__main__":
    main()
