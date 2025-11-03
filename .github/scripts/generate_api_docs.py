#!/usr/bin/env python3
"""
Generate API reference documentation from the OpenHands SDK using pydoc-markdown.

This script:
1. Uses pydoc-markdown to generate markdown from the SDK source code
2. Converts the output to Mintlify-compatible MDX format
3. Creates a single flattened sdk.mdx file containing all API documentation
4. Updates docs.json to include the API reference in navigation
"""

import json
import subprocess
import sys
from pathlib import Path


def generate_markdown_from_sdk(sdk_path: Path, output_file: Path) -> None:
    """
    Use pydoc-markdown to generate API documentation.
    
    Args:
        sdk_path: Path to the SDK source directory
        output_file: Path where the markdown will be saved
    """
    print(f"Generating API documentation from {sdk_path}...")
    
    # Run pydoc-markdown
    cmd = [
        "pydoc-markdown",
        "-I", str(sdk_path),
        "-p", "openhands.sdk",
        "--render-toc",
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            cwd=sdk_path.parent
        )
        
        markdown_content = result.stdout
        
        # Save to file
        output_file.write_text(markdown_content)
        print(f"✓ Generated {len(markdown_content)} chars of markdown")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running pydoc-markdown: {e}", file=sys.stderr)
        print(f"STDOUT: {e.stdout}", file=sys.stderr)
        print(f"STDERR: {e.stderr}", file=sys.stderr)
        sys.exit(1)


def convert_to_mdx(markdown_file: Path, mdx_file: Path, github_repo_url: str) -> None:
    """
    Convert the generated markdown to MDX format with Mintlify frontmatter.
    
    Args:
        markdown_file: Path to the input markdown file
        mdx_file: Path where the MDX file will be saved
        github_repo_url: GitHub repository URL for source links
    """
    print(f"Converting to MDX format...")
    
    markdown_content = markdown_file.read_text()
    
    # Create MDX with frontmatter
    frontmatter = """---
title: Python API Reference
description: Complete API reference for the OpenHands SDK
---

# Python API Reference

This page contains the complete API reference for the OpenHands SDK, auto-generated from the source code.

**Source:** [`openhands/sdk/`]({repo_url}/tree/main/openhands-sdk/openhands/sdk/)

---

""".format(repo_url=github_repo_url)
    
    mdx_content = frontmatter + markdown_content
    
    # Write MDX file
    mdx_file.write_text(mdx_content)
    print(f"✓ Created {mdx_file} ({len(mdx_content)} chars)")


def update_docs_json(docs_json_path: Path) -> None:
    """
    Update docs.json to include the API Reference page in navigation.
    
    Args:
        docs_json_path: Path to docs.json file
    """
    print(f"Updating {docs_json_path}...")
    
    with open(docs_json_path, 'r') as f:
        docs_config = json.load(f)
    
    # Find SDK tab in navigation.tabs
    sdk_tab = None
    tabs = docs_config.get('navigation', {}).get('tabs', [])
    for tab in tabs:
        if tab.get('tab') == 'SDK':
            sdk_tab = tab
            break
    
    if not sdk_tab:
        print("Warning: SDK tab not found in docs.json", file=sys.stderr)
        return
    
    # Check if API Reference already exists
    api_ref_entry = {
        "group": "API Reference",
        "pages": ["sdk/api/index"]
    }
    
    # Remove old API reference if exists (could be multi-file version)
    pages = sdk_tab.get('pages', [])
    filtered_pages = []
    for item in pages:
        if isinstance(item, dict) and item.get('group') == 'API Reference':
            continue
        filtered_pages.append(item)
    
    # Add the new single-file API reference
    filtered_pages.append(api_ref_entry)
    sdk_tab['pages'] = filtered_pages
    
    # Write back
    with open(docs_json_path, 'w') as f:
        json.dump(docs_config, f, indent=2)
    
    print(f"✓ Updated docs.json navigation")


def main():
    """Main entry point for the documentation generation script."""
    # Paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    # Check if agent-sdk was checked out in workflow
    # The workflow checks out to repo_root / "agent-sdk"
    agent_sdk_path = repo_root / "agent-sdk" / "openhands-sdk"
    
    if not agent_sdk_path.exists():
        print(f"Error: SDK path not found at {agent_sdk_path}", file=sys.stderr)
        sys.exit(1)
    
    # Output paths
    api_dir = repo_root / "sdk" / "api"
    api_dir.mkdir(parents=True, exist_ok=True)
    
    temp_markdown = repo_root / "temp_api.md"
    mdx_output = api_dir / "index.mdx"
    docs_json_path = repo_root / "docs.json"
    
    # GitHub repository URL
    github_repo_url = "https://github.com/OpenHands/software-agent-sdk"
    
    # Generate documentation
    print("=" * 60)
    print("Starting API documentation generation")
    print("=" * 60)
    
    generate_markdown_from_sdk(agent_sdk_path, temp_markdown)
    convert_to_mdx(temp_markdown, mdx_output, github_repo_url)
    update_docs_json(docs_json_path)
    
    # Clean up temp file
    temp_markdown.unlink()
    
    print("=" * 60)
    print("API documentation generation complete!")
    print(f"Output: {mdx_output}")
    print("=" * 60)


if __name__ == "__main__":
    main()
