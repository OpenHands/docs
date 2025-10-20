#!/usr/bin/env python3
"""
Sync code blocks in documentation files with their corresponding source files.

This script:
1. Scans MDX files for code blocks with file references (e.g., ```python expandable examples/01_standalone_sdk/02_custom_tools.py)
2. Extracts the file path from the code block metadata
3. Reads the actual content from the source file in agent-sdk/
4. Compares the code block content with the actual file content
5. Updates the documentation if there are differences
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional


def find_mdx_files(docs_path: Path) -> List[Path]:
    """Find all MDX files in the docs directory."""
    mdx_files = []
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.mdx'):
                mdx_files.append(Path(root) / file)
    return mdx_files


def extract_code_blocks(content: str) -> List[Tuple[str, str, int, int]]:
    """
    Extract code blocks that reference source files.
    
    Returns list of tuples: (file_reference, code_content, start_pos, end_pos)
    
    Pattern matches blocks like:
    ```python icon="python" expandable examples/01_standalone_sdk/02_custom_tools.py
    <code content>
    ```
    """
    # Pattern to match code blocks with file references
    # Captures the file path and the code content
    pattern = r'```python[^\n]*\s+(examples/[^\s]+\.py)\n(.*?)```'
    
    matches = []
    for match in re.finditer(pattern, content, re.DOTALL):
        file_ref = match.group(1)
        code_content = match.group(2)
        start_pos = match.start()
        end_pos = match.end()
        matches.append((file_ref, code_content, start_pos, end_pos))
    
    return matches


def read_source_file(agent_sdk_path: Path, file_ref: str) -> Optional[str]:
    """
    Read the actual source file content.
    
    Args:
        agent_sdk_path: Path to agent-sdk repository
        file_ref: File reference like "examples/01_standalone_sdk/02_custom_tools.py"
    
    Returns:
        File content or None if file not found
    """
    # file_ref is already the full path relative to agent-sdk root
    source_path = agent_sdk_path / file_ref
    
    if not source_path.exists():
        print(f"Warning: Source file not found: {source_path}")
        return None
    
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {source_path}: {e}")
        return None


def normalize_content(content: str) -> str:
    """Normalize content for comparison (remove trailing whitespace, normalize line endings)."""
    # Split into lines, strip trailing whitespace from each line, rejoin
    lines = [line.rstrip() for line in content.splitlines()]
    return '\n'.join(lines)


def update_doc_file(doc_path: Path, content: str, code_blocks: List[Tuple[str, str, int, int]], 
                   agent_sdk_path: Path) -> bool:
    """
    Update documentation file with correct code blocks.
    
    Returns True if changes were made, False otherwise.
    """
    changes_made = False
    new_content = content
    offset = 0  # Track offset due to content changes
    
    for file_ref, old_code, start_pos, end_pos in code_blocks:
        # Read actual source file
        actual_content = read_source_file(agent_sdk_path, file_ref)
        
        if actual_content is None:
            continue
        
        # Normalize both for comparison
        old_normalized = normalize_content(old_code)
        actual_normalized = normalize_content(actual_content)
        
        if old_normalized != actual_normalized:
            print(f"\n📝 Found difference in {doc_path.name} for {file_ref}")
            print(f"   Updating code block...")
            
            # Calculate adjusted positions
            adj_start = start_pos + offset
            adj_end = end_pos + offset
            
            # Extract the opening line (```python ... file_ref)
            opening_line_match = re.search(r'```python[^\n]*\s+' + re.escape(file_ref), 
                                          new_content[adj_start:adj_end])
            if opening_line_match:
                opening_line = opening_line_match.group(0)
                
                # Construct new code block (don't add extra newline if content already ends with one)
                if actual_content.endswith('\n'):
                    new_block = f"{opening_line}\n{actual_content}```"
                else:
                    new_block = f"{opening_line}\n{actual_content}\n```"
                old_block = new_content[adj_start:adj_end]
                
                # Replace in content
                new_content = new_content[:adj_start] + new_block + new_content[adj_end:]
                
                # Update offset
                offset += len(new_block) - len(old_block)
                changes_made = True
    
    if changes_made:
        try:
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated {doc_path}")
            return True
        except Exception as e:
            print(f"❌ Error writing {doc_path}: {e}")
            return False
    
    return False


def main():
    # Script is in docs/.github/scripts/
    script_dir = Path(__file__).parent.parent.parent  # docs root
    # agent-sdk is at the same level as docs, not inside docs
    agent_sdk_path = script_dir.parent / 'agent-sdk'
    
    print(f"🔍 Scanning for MDX files in {script_dir}")
    print(f"📁 Agent SDK path: {agent_sdk_path}")
    
    if not agent_sdk_path.exists():
        print(f"❌ Agent SDK path does not exist: {agent_sdk_path}")
        print(f"   Make sure agent-sdk repository is checked out at the same level as docs directory")
        sys.exit(1)
    
    # Find all MDX files
    mdx_files = find_mdx_files(script_dir)
    print(f"📄 Found {len(mdx_files)} MDX files")
    
    total_changes = 0
    files_changed = []
    
    # Process each MDX file
    for mdx_file in mdx_files:
        try:
            with open(mdx_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract code blocks
            code_blocks = extract_code_blocks(content)
            
            if not code_blocks:
                continue
            
            print(f"\n📋 Processing {mdx_file.relative_to(script_dir)}")
            print(f"   Found {len(code_blocks)} code block(s) with file references")
            
            # Update file if needed
            if update_doc_file(mdx_file, content, code_blocks, agent_sdk_path):
                total_changes += 1
                files_changed.append(str(mdx_file.relative_to(script_dir)))
        
        except Exception as e:
            print(f"❌ Error processing {mdx_file}: {e}")
            continue
    
    # Summary
    print("\n" + "="*60)
    if total_changes > 0:
        print(f"✅ Updated {total_changes} file(s):")
        for file in files_changed:
            print(f"   - {file}")
        # Set output for GitHub Actions
        if 'GITHUB_OUTPUT' in os.environ:
            with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
                f.write('changes=true\n')
    else:
        print("✅ All code blocks are in sync!")
        if 'GITHUB_OUTPUT' in os.environ:
            with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
                f.write('changes=false\n')
    print("="*60)


if __name__ == '__main__':
    main()
