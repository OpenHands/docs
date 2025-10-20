# Documentation Code Block Sync

This directory contains scripts for automatically syncing code blocks in documentation files with their corresponding source files from the agent-sdk repository.

## Overview

The `sync_code_blocks.py` script ensures that code examples in the documentation always match the actual source code in the agent-sdk `examples/` directory. This prevents documentation drift and ensures users always see accurate, working examples.

## How It Works

1. **Scans MDX Files**: The script recursively scans all `.mdx` files in the docs repository
2. **Finds Code Blocks**: It looks for Python code blocks with file references using the pattern:
   ```markdown
   ```python icon="python" expandable examples/01_standalone_sdk/02_custom_tools.py
   <code content>
   ```
   ```
3. **Extracts File Path**: The file path is extracted from the code block metadata (e.g., `examples/01_standalone_sdk/02_custom_tools.py`)
4. **Reads Source File**: The actual source file is read from the checked-out agent-sdk repository
5. **Compares Content**: The code block content is compared with the actual file content
6. **Updates Docs**: If there are differences, the documentation file is automatically updated

## Usage

### Via GitHub Actions

The workflow `.github/workflows/sync-docs-code-blocks.yml` automatically runs:
- **Daily at 2 AM UTC** to catch any changes
- **Manually** via workflow dispatch (allows specifying a custom agent-sdk branch/tag)

When differences are detected, the workflow:
1. Checks out the docs repository
2. Checks out the agent-sdk repository into `agent-sdk/` subdirectory
3. Runs the sync script
4. Creates a pull request with the updates

### Manual Run

To test locally:

```bash
cd docs

# Clone agent-sdk if not already present
git clone https://github.com/All-Hands-AI/agent-sdk.git agent-sdk

# Run the script
python .github/scripts/sync_code_blocks.py

# Clean up
rm -rf agent-sdk
```

## Code Block Format

For the script to detect and sync code blocks, they must follow this format:

```markdown
```python icon="python" expandable examples/01_standalone_sdk/02_custom_tools.py
<code will be synced from agent-sdk/examples/01_standalone_sdk/02_custom_tools.py>
```
```

The file reference must:
- Start with `examples/`
- End with `.py`
- Be a valid path relative to the agent-sdk repository root

Examples:
- `examples/01_standalone_sdk/02_custom_tools.py`
- `examples/02_remote_agent_server/01_convo_with_local_agent_server.py`
- `examples/03_github_workflows/01_basic_action/action.py`

## Features

- **Automatic Detection**: Finds all code blocks with file references
- **Smart Comparison**: Normalizes content (trailing whitespace, line endings) for accurate comparison
- **Batch Updates**: Can update multiple files in a single run
- **GitHub Integration**: Automatically creates PRs when changes are needed
- **Safe Operation**: Only updates files with actual differences
- **Clear Logging**: Provides detailed output about what's being processed and updated
- **Flexible Scheduling**: Daily automatic runs plus manual trigger option

## Configuration

### Workflow Configuration

Edit `.github/workflows/sync-docs-code-blocks.yml` to customize:
- Schedule timing (cron expression)
- Default agent-sdk branch
- PR title/body templates

### Script Behavior

The script:
- Expects agent-sdk to be checked out in `docs/agent-sdk/`
- Scans all `.mdx` files recursively
- Updates files in-place
- Sets GitHub Actions output for PR creation

## Troubleshooting

### "Source file not found" warnings

This means the script found a code block reference but couldn't locate the corresponding source file. This can happen if:
- The file reference doesn't match an actual file in `agent-sdk/examples/`
- The file has been moved or renamed in agent-sdk
- The agent-sdk checkout is incomplete or at the wrong ref

### No changes detected when you expect them

Check that:
1. The code block format matches the expected pattern (with full `examples/` path)
2. The file path in the code block is correct and includes `.py` extension
3. Whitespace differences are normalized (trailing spaces are ignored)
4. The agent-sdk repository is checked out at the correct branch/tag

### Script fails with path errors

Ensure:
- The script is run from the docs repository root, or
- The agent-sdk repository is checked out in `docs/agent-sdk/`

## Maintenance

- Keep the regex patterns updated if the code block format changes
- Update the workflow if the repository structure changes
- Monitor workflow runs to catch any issues early
- Review PRs to ensure changes are expected

## Related Files

- `.github/workflows/sync-docs-code-blocks.yml` - GitHub Actions workflow
- `agent-sdk/examples/` - Source files that are synced to documentation
- `sdk/guides/` - Documentation files containing code blocks
