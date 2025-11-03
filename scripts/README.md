# API Documentation Generation Pipeline

This directory contains the automated pipeline for generating API reference documentation from the [OpenHands software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) repository.

## Overview

The pipeline uses Sphinx with the `sphinx-markdown-builder` extension to generate clean Markdown files from Python docstrings, which are then integrated into the Mintlify documentation site.

## Files Structure

```
scripts/
├── README.md                    # This file
├── generate-api-docs.py         # Main generation script
├── mint-config-snippet.json     # Generated Mintlify config snippet
└── sphinx/
    └── source/
        ├── conf.py              # Sphinx configuration
        └── index.rst            # Main documentation index
```

## Prerequisites

### Required Python Packages

Install the required dependencies:

```bash
pip install sphinx sphinx-markdown-builder myst-parser
```

### System Requirements

- Python 3.8+
- Git (for cloning the SDK repository)
- Internet connection (for cloning/updating the SDK repo)

## Usage

### Basic Usage

Generate API documentation with default settings:

```bash
cd docs
python scripts/generate-api-docs.py
```

### Advanced Usage

```bash
# Clean previous build and regenerate everything
python scripts/generate-api-docs.py --clean

# Enable verbose output for debugging
python scripts/generate-api-docs.py --verbose

# Combine options
python scripts/generate-api-docs.py --clean --verbose
```

### Command Line Options

- `--clean`: Remove all previous build artifacts and generated documentation before starting
- `--verbose`, `-v`: Enable detailed logging output for debugging

## How It Works

The generation pipeline follows these steps:

1. **Dependency Check**: Verifies that required Python packages are installed
2. **Repository Management**: Clones or updates the `software-agent-sdk` repository
3. **Sphinx Setup**: Creates necessary Sphinx directories and configuration
4. **RST Generation**: Uses `sphinx-apidoc` to generate RST files from Python source
5. **Markdown Build**: Runs Sphinx with the markdown builder to generate clean Markdown
6. **Content Organization**: Processes and organizes the generated Markdown files
7. **Mintlify Integration**: Creates configuration snippets for easy integration
8. **Cleanup**: Removes build artifacts while preserving generated documentation

## Output

The script generates the following:

### Generated Documentation

- **`api-reference/`**: Directory containing all generated API documentation
  - `index.md`: Main API reference index page
  - `openhands.*.md`: Individual module documentation files

### Configuration Files

- **`scripts/mint-config-snippet.json`**: Ready-to-use configuration snippet for `docs.json`

## Integration with Mintlify

### Automatic Integration

The generated `mint-config-snippet.json` contains the navigation structure for the API reference:

```json
{
  "group": "API Reference",
  "pages": [
    "api-reference/index",
    "api-reference/openhands.agent",
    "api-reference/openhands.conversation",
    ...
  ]
}
```

### Manual Integration

To integrate the API reference into your `docs.json`:

1. Run the generation script
2. Copy the contents of `scripts/mint-config-snippet.json`
3. Add it to the appropriate section in your `docs.json` navigation

Example integration in `docs.json`:

```json
{
  "navigation": {
    "tabs": [
      {
        "tab": "SDK",
        "pages": [
          "sdk/index",
          "sdk/getting-started",
          {
            "group": "Guides",
            "pages": ["..."]
          },
          {
            "group": "API Reference",
            "pages": [
              "api-reference/index",
              "api-reference/openhands.agent",
              "api-reference/openhands.conversation"
            ]
          }
        ]
      }
    ]
  }
}
```

## Customization

### Sphinx Configuration

Modify `scripts/sphinx/source/conf.py` to customize:

- **Extensions**: Add or remove Sphinx extensions
- **Autodoc Options**: Control what gets documented
- **Napoleon Settings**: Configure docstring parsing
- **Markdown Output**: Adjust markdown generation settings

### Content Processing

The script includes content processing functions that can be customized:

- `clean_markdown_file()`: Modify how individual files are processed
- `create_api_index()`: Customize the main index page
- `organize_output_docs()`: Change how files are organized

### Module Selection

To document specific modules only, modify the `generate_rst_files()` method in the script to include/exclude specific paths.

## Troubleshooting

### Common Issues

1. **Missing Dependencies**
   ```
   Error: Missing required packages: sphinx, sphinx_markdown_builder, myst_parser
   ```
   **Solution**: Install the required packages with pip

2. **SDK Repository Not Found**
   ```
   Error: openhands-sdk directory not found
   ```
   **Solution**: Ensure the SDK repository is properly cloned and contains the expected structure

3. **Permission Errors**
   ```
   Error: Permission denied when writing files
   ```
   **Solution**: Check file permissions and ensure the script has write access to the docs directory

### Debug Mode

Use the `--verbose` flag to get detailed logging:

```bash
python scripts/generate-api-docs.py --verbose
```

This will show:
- Command execution details
- File processing steps
- Sphinx build output
- Error stack traces

### Manual Cleanup

If the script fails partway through, you can manually clean up:

```bash
# Remove build artifacts
rm -rf scripts/sphinx/build/
rm -rf scripts/sphinx/source/openhands*.rst

# Remove generated docs (if needed)
rm -rf api-reference/

# Remove cloned repository (if needed)
rm -rf agent-sdk/
```

## Automation

### CI/CD Integration

The script is designed to be idempotent and safe for CI/CD environments:

```yaml
# Example GitHub Actions step
- name: Generate API Documentation
  run: |
    cd docs
    pip install sphinx sphinx-markdown-builder myst-parser
    python scripts/generate-api-docs.py --clean
```

### Scheduled Updates

You can set up scheduled updates to keep the API documentation current:

```yaml
# Example cron job
name: Update API Docs
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  workflow_dispatch:

jobs:
  update-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install sphinx sphinx-markdown-builder myst-parser
      - name: Generate documentation
        run: |
          cd docs
          python scripts/generate-api-docs.py --clean
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add api-reference/
          git diff --staged --quiet || git commit -m "Update API documentation"
          git push
```

## Contributing

When modifying the generation pipeline:

1. Test changes locally with `--verbose` flag
2. Verify generated Markdown renders correctly in Mintlify
3. Check that all module documentation is complete
4. Update this README if adding new features or changing behavior

## Support

For issues with the documentation generation pipeline:

1. Check the troubleshooting section above
2. Run with `--verbose` to get detailed error information
3. Open an issue in the OpenHands/docs repository with the full error output