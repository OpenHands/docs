# OpenHands SDK Documentation Guidelines

These instructions are ONLY for modifying the documentation associated with the agent SDK which mainly lives under the
sdk folder.

## Repository Structure

Applicable files when modifying the agent SDK documentation:

```
docs/
├── .openhands/microagents/sdk-guidelines.md     # Guidelines for changing SDK documentation (this file)
├── .github/
│   ├── scripts/
│   │   └── sync_code_blocks.py # Code synchronization script
│   └── workflows/              # CI/CD workflows
├── sdk/                        # Agent SDK documentation
│   ├── guides/                 # SDK tutorials and guides
│   └── arch/                   # Architecture documentation
└── docs.json                   # Mintlify navigation configuration
```

## Agent SDK Documentation System Overview

The documentation follows a synchronized approach where code examples are automatically kept in sync with actual 
example files in the agent-sdk repository.

## Automatic Code Synchronization

### How It Works

The sync system ensures documentation code blocks match the actual source files:

1. **Trigger**: GitHub Actions workflow runs on:
   - Pull requests to docs repository
   - Manual workflow dispatch
   - Scheduled intervals

2. **Scan**: Python script (`docs/.github/scripts/sync_code_blocks.py`) scans all MDX files

3. **Extract**: Finds code blocks with file references using regex:
   - Pattern: ```python icon="python" expandable examples/path/to/file.py

4. **Compare**: Reads actual file from agent-sdk repository and compares content

5. **Update**: If differences found, updates the code block in the MDX file

6. **Commit**: Creates a commit with updated documentation

### Sync Script Details

**Location**: `docs/.github/scripts/sync_code_blocks.py`

**Key Functions:**
- `find_mdx_files()` - Recursively finds all .mdx files
- `extract_code_blocks()` - Uses regex to find synced code blocks
- `read_source_file()` - Reads content from agent-sdk repository
- `normalize_content()` - Normalizes whitespace for comparison
- `update_doc_file()` - Updates MDX files with current source content

**Pattern Matching:**
```python
pattern = r'```python[^\n]*\s+(examples/[^\s]+\.py)\n(.*?)```'
```
- Captures file path: `examples/01_standalone_sdk/02_custom_tools.py`
- Captures code content between opening and closing ```

## MDX Documentation Format

### Standard Structure

Documentation is deployed with Mintlify from GitHub. The files follow this pattern 
(see `docs/sdk/guides/custom-tools.mdx` and `docs/sdk/arch/tool-system.mdx` as reference):

1. **Frontmatter** - YAML metadata with title and description
2. **Introduction** - Brief overview of the feature
3. **Example Section** with:
   - `<Note>` component linking to GitHub source
   - Main code block with special syntax for auto-sync
   - Bash code block showing how to run the example
4. **Detailed Explanations** - Breaking down key concepts with inline code highlights
5. **Next Steps** - Links to related documentation

### Code Block Syntax

#### Python Code Blocks (Auto-Synced)
```python icon="python" expandable examples/01_standalone_sdk/02_custom_tools.py
<code content here - will be automatically synced>
```

**Key attributes:**
- `icon="python"` - Displays Python icon in the UI
- `expandable` - Makes the code block collapsible
- `examples/01_standalone_sdk/02_custom_tools.py` - File path relative to agent-sdk root
  - This path is used by the sync script to locate the source file
  - Path must match the actual file location in agent-sdk repository

You should make sure your code block follows the same format for the auto-sync between actual code and example to work.

#### Bash Code Blocks (Manual)
```bash Running the Example
export LLM_API_KEY="your-api-key"
cd agent-sdk
uv run python examples/01_standalone_sdk/02_custom_tools.py
```

**Note:** The title "Running the Example" appears as a label in the rendered documentation.

#### Inline Code Highlights
Use `highlight={line_numbers}` to emphasize specific lines:

```python highlight={3-4}
mcp_config = {
    "mcpServers": {
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "repomix": {"command": "npx", "args": ["-y", "repomix@1.4.2", "--mcp"]},
    }
}
```

### Note Component
Links to the GitHub source file:

```mdx
<Note>
This example is available on GitHub: [examples/01_standalone_sdk/02_custom_tools.py](https://github.com/OpenHands/software-agent-sdk/blob/main/examples/01_standalone_sdk/02_custom_tools.py)
</Note>
```

## Writing New Documentation

### Step-by-Step Guide

1. **Create Example File** in `agent-sdk/examples/`
   ```python
   # agent-sdk/examples/01_standalone_sdk/XX_new_feature.py
   import os
   from openhands.sdk import LLM, Agent
   # ... your example code
   ```

2. **Create MDX File** in `docs/sdk/guides/`
   ```mdx
   ---
   title: New Feature Guide
   description: How to use the new feature
   ---

   ## Basic Example

   <Note>
   This example is available on GitHub: [examples/01_standalone_sdk/XX_new_feature.py](...)
   </Note>

   ```python icon="python" expandable examples/01_standalone_sdk/XX_new_feature.py
   import os
   from openhands.sdk import LLM, Agent
   # ... copy initial code here
   ```

   ```bash Running the Example
   export LLM_API_KEY="your-api-key"
   cd agent-sdk
   uv run python examples/01_standalone_sdk/XX_new_feature.py
   ```

   ### Key Concept
   Explain the feature with code highlights...
   ```

3. **Sync Will Handle Updates**
   - Initial code can be copied manually or left minimal
   - Sync workflow will automatically update to match actual file
   - Subsequent changes to example file auto-propagate to docs

### Best Practices

1. **File Paths**: Always use relative paths from agent-sdk root
   - ✅ `examples/01_standalone_sdk/02_custom_tools.py`
   - ❌ `agent-sdk/examples/...` or absolute paths

2. **Code Organization**: Keep example files focused and self-contained
   - Include all necessary imports
   - Add comments explaining key concepts
   - Make examples runnable with minimal setup

3. **Documentation Flow**:
   - Start with complete working example
   - Break down into sections with highlights
   - Explain concepts with inline code snippets
   - Link to related documentation

4. **Consistency**: Follow existing patterns
   - Use same icon/expandable syntax
   - Include "Running the Example" bash block
   - Structure sections similarly to other guides

5. **Testing**: Before committing documentation
   - Ensure example file runs successfully
   - Verify file paths are correct
   - Check that code blocks render properly
   - Test all links work

## Common Patterns

### Multi-File Examples
When an example spans multiple files, you can include multiple synced code blocks:

```mdx
```python icon="python" expandable examples/01_standalone_sdk/main.py
# main file content
```

```python icon="python" expandable examples/01_standalone_sdk/helper.py
# helper file content
```
```

### Partial Code Examples
For showing specific patterns without full sync, use regular code blocks:

```mdx
```python
# This won't be auto-synced
def example_pattern():
    pass
```
```

### Configuration Examples
For YAML, JSON, or other config files, use appropriate language tags:

```yaml
name: Example Workflow
on: [push]
```

## Mintlify Documentation

You can check https://www.mintlify.com/docs for documentation on what our doc site supports.

## CI/CD Workflows

### Code Synchronization Workflow
- **File**: `.github/workflows/sync-docs-code-blocks.yml`
- **Triggers**: Push to any branch, daily at 2 AM UTC, manual dispatch
- **Purpose**: Keeps code blocks in sync with agent-sdk examples
- **Actions**: Checks out both repositories, runs sync script, commits changes if needed

### OpenAPI Sync Workflow
- **File**: `.github/workflows/sync-agent-sdk-openapi.yml`
- **Purpose**: Syncs OpenAPI specifications for API documentation

## Notes

- For agent-sdk examples, ensure the file path in code blocks is correct
- For short agent-sdk examples, you don't need `expandable` in example file
- When you add new pages that need to refer to agent-sdk example script, you should create an empty block with correct block name (refer to the python example script correctly), then run `python .github/scripts/sync_code_blocks.py` to sync it
