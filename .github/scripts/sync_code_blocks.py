#!/usr/bin/env python3
"""
Sync code blocks in documentation files with their corresponding source files.

This script:
1. Scans MDX files for code blocks with file references (e.g., ```python expandable examples/01_standalone_sdk/02_custom_tools.py or ```yaml expandable examples/03_github_workflows/02_pr_review/workflow.yml)
2. Extracts the file path from the code block metadata
3. Reads the actual content from the source file in agent-sdk/
4. Compares the code block content with the actual file content
5. Updates the documentation if there are differences

Supported file types:
- Python files (.py) with ```python blocks
- YAML files (.yml, .yaml) with ```yaml blocks
"""

import os
import re
import sys
from pathlib import Path


def find_mdx_files(docs_path: Path) -> list[Path]:
    """Find all MDX files in the docs directory."""
    mdx_files: list[Path] = []
    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.endswith(".mdx"):
                mdx_files.append(Path(root) / file)
    return mdx_files


def extract_code_blocks(content: str) -> list[tuple[str, str, str, int, int]]:
    """
    Extract code blocks that reference source files.

    Returns list of tuples: (language, file_reference, code_content, start_pos, end_pos)

    Pattern matches blocks like:
    ```python icon="python" expandable examples/01_standalone_sdk/02_custom_tools.py
    <code content>
    ```
    
    OR
    
    ```yaml icon="yaml" expandable examples/03_github_workflows/02_pr_review/workflow.yml
    <code content>
    ```
    """
    matches: list[tuple[str, str, str, int, int]] = []
    
    # Pattern for Python files
    # The closing ``` must be at the start of a line (after newline) OR at the very end
    # The \n? before ``` makes the trailing newline optional to handle edge cases
    # where content doesn't have a trailing newline
    python_pattern = r'```python[^\n]*\s+([^\s]+\.py)\n(.*?)\n?```(?=\n|$)'
    for match in re.finditer(python_pattern, content, re.DOTALL):
        file_ref = match.group(1)
        code_content = match.group(2)
        # Strip trailing newline from code content if present (will be re-added during update)
        code_content = code_content.rstrip('\n')
        start_pos = match.start()
        end_pos = match.end()
        matches.append(('python', file_ref, code_content, start_pos, end_pos))
    
    # Pattern for YAML files
    yaml_pattern = r'```yaml[^\n]*\s+([^\s]+\.ya?ml)\n(.*?)\n?```(?=\n|$)'
    for match in re.finditer(yaml_pattern, content, re.DOTALL):
        file_ref = match.group(1)
        code_content = match.group(2)
        # Strip trailing newline from code content if present (will be re-added during update)
        code_content = code_content.rstrip('\n')
        start_pos = match.start()
        end_pos = match.end()
        matches.append(('yaml', file_ref, code_content, start_pos, end_pos))
    
    # Sort by position to maintain order
    matches.sort(key=lambda x: x[3])
    
    return matches


def read_source_file(agent_sdk_path: Path, file_ref: str) -> str | None:
    """
    Read the actual source file content.

    Args:
        agent_sdk_path: Path to agent-sdk repository
        file_ref: File reference like "examples/01_standalone_sdk/02_custom_tools.py"
    """
    source_path = agent_sdk_path / file_ref
    if not source_path.exists():
        print(f"Warning: Source file not found: {source_path}")
        return None
    try:
        return source_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {source_path}: {e}")
        return None


def normalize_content(content: str) -> str:
    """Normalize content for comparison (remove trailing whitespace, normalize line endings)."""
    return "\n".join(line.rstrip() for line in content.splitlines())


def escape_embedded_backticks(content: str) -> str:
    """
    Escape triple backticks inside source code to prevent breaking markdown code blocks.
    
    This handles the case where Python code contains triple backticks in strings
    (e.g., in docstrings or multi-line strings with markdown examples).
    
    Strategy: Replace ``` with a zero-width space between backticks: `​`​`
    This preserves the visual appearance while preventing markdown parsing issues.
    
    Tradeoff note: Zero-width spaces (U+200B) are invisible and will be copied when
    users copy-paste code from the docs. This could cause subtle issues if users paste
    code containing these characters. However, this is acceptable because:
    1. The affected code is primarily display content (example outputs), not executable
    2. Alternative approaches (like changing source files) aren't feasible since we
       sync from an external repository (agent-sdk)
    3. Most modern editors will highlight invisible Unicode characters
    
    The function is idempotent - applying it multiple times produces the same result
    since we only replace actual triple backticks, not already-escaped sequences.
    """
    if not content:
        return content
    # Use a zero-width space (U+200B) between backticks
    # This makes ``` render correctly in the code block without closing it
    return content.replace("```", "`\u200b`\u200b`")


def resolve_paths() -> tuple[Path, Path]:
    """
    Determine docs root and agent-sdk path robustly across CI and local layouts.
    Priority for agent-sdk path:
      1) AGENT_SDK_PATH (env override)
      2) $GITHUB_WORKSPACE/agent-sdk
      3) docs_root/'agent-sdk'
      4) docs_root.parent/'agent-sdk' (legacy)
    """
    # docs repo root (script is at docs/.github/scripts/sync_code_blocks.py)
    script_file = Path(__file__).resolve()
    docs_root = script_file.parent.parent.parent

    candidates: list[Path] = []

    # 1) Explicit env override
    env_override = os.environ.get("AGENT_SDK_PATH")
    if env_override:
        candidates.append(Path(env_override).expanduser().resolve())

    # 2) Standard GitHub workspace sibling
    gh_ws = os.environ.get("GITHUB_WORKSPACE")
    if gh_ws:
        candidates.append(Path(gh_ws).resolve() / "agent-sdk")

    # 3) Sibling inside the docs repo root
    candidates.append(docs_root / "agent-sdk")

    # 4) Legacy parent-of-docs-root layout
    candidates.append(docs_root.parent / "agent-sdk")

    print(f"🔍 Scanning for MDX files in {docs_root}")
    print("🔎 Trying agent-sdk paths (in order):")
    for p in candidates:
        print(f"   - {p}")

    for p in candidates:
        if p.exists():
            print(f"📁 Using Agent SDK path: {p}")
            return docs_root, p

    # If none exist, fail with a helpful message
    print("❌ Agent SDK path not found in any of the expected locations.")
    print("   Set AGENT_SDK_PATH, or checkout the repo to one of the tried paths above.")
    sys.exit(1)


def update_doc_file(
    doc_path: Path,
    content: str,
    code_blocks: list[tuple[str, str, str, int, int]],
    agent_sdk_path: Path,
) -> bool:
    """
    Update documentation file with correct code blocks.

    Returns True if changes were made, False otherwise.
    """
    changes_made = False
    new_content = content
    offset = 0  # Track offset due to content changes

    for language, file_ref, old_code, start_pos, end_pos in code_blocks:
        actual_content = read_source_file(agent_sdk_path, file_ref)
        if actual_content is None:
            continue

        # Compare normalized versions: old doc content vs escaped actual content
        # We always compare against escaped version since that's what will be written
        old_display = normalize_content(old_code)
        new_display = normalize_content(escape_embedded_backticks(actual_content))
        
        if old_display != new_display:
            print(f"\n📝 Found difference in {doc_path.name} for {file_ref}")
            print("   Updating code block...")

            adj_start = start_pos + offset
            adj_end = end_pos + offset

            # Match opening line with the appropriate language
            opening_line_match = re.search(
                r"```" + re.escape(language) + r"[^\n]*\s+" + re.escape(file_ref),
                new_content[adj_start:adj_end],
            )
            if opening_line_match:
                opening_line = opening_line_match.group(0)
                # Escape any embedded triple backticks in the source content
                # to prevent them from closing the markdown code block
                escaped_content = escape_embedded_backticks(actual_content)
                # Preserve trailing newline behavior
                if escaped_content.endswith("\n"):
                    new_block = f"{opening_line}\n{escaped_content}```"
                else:
                    new_block = f"{opening_line}\n{escaped_content}\n```"
                old_block = new_content[adj_start:adj_end]

                new_content = new_content[:adj_start] + new_block + new_content[adj_end:]
                offset += len(new_block) - len(old_block)
                changes_made = True

    if changes_made:
        try:
            doc_path.write_text(new_content, encoding="utf-8")
            print(f"✅ Updated {doc_path}")
            return True
        except Exception as e:
            print(f"❌ Error writing {doc_path}: {e}")
            return False

    return False


def main() -> None:
    docs_root, agent_sdk_path = resolve_paths()

    # Find all MDX files
    mdx_files = find_mdx_files(docs_root)
    print(f"📄 Found {len(mdx_files)} MDX files")

    total_changes = 0
    files_changed: list[str] = []

    for mdx_file in mdx_files:
        try:
            content = mdx_file.read_text(encoding="utf-8")
            code_blocks = extract_code_blocks(content)
            if not code_blocks:
                continue

            print(f"\n📋 Processing {mdx_file.relative_to(docs_root)}")
            print(f"   Found {len(code_blocks)} code block(s) with file references")

            if update_doc_file(mdxx_file := mdx_file, content=content, code_blocks=code_blocks, agent_sdk_path=agent_sdk_path):
                total_changes += 1
                files_changed.append(str(mdxx_file.relative_to(docs_root)))
        except Exception as e:
            print(f"❌ Error processing {mdx_file}: {e}")
            continue

    print("\n" + "=" * 60)
    if total_changes > 0:
        print(f"✅ Updated {total_changes} file(s):")
        for file in files_changed:
            print(f"   - {file}")
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
                f.write("changes=true\n")
    else:
        print("✅ All code blocks are in sync!")
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
                f.write("changes=false\n")
    print("=" * 60)


if __name__ == "__main__":
    main()
