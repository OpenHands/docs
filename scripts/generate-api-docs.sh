#!/bin/bash

# API Documentation Generation Script (Shell Version)
# 
# This is a simple shell wrapper around the Python script for convenience.
# For full functionality and error handling, use the Python version.

set -e

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_ROOT="$(dirname "$SCRIPT_DIR")"

# Change to docs directory
cd "$DOCS_ROOT"

# Check if Python script exists
if [ ! -f "scripts/generate-api-docs.py" ]; then
    echo "Error: Python script not found at scripts/generate-api-docs.py"
    exit 1
fi

# Check if required packages are installed
echo "Checking dependencies..."
python3 -c "import sphinx, sphinx_markdown_builder, myst_parser" 2>/dev/null || {
    echo "Error: Required packages not installed."
    echo "Please install them with: pip install sphinx sphinx-markdown-builder myst-parser"
    exit 1
}

# Parse command line arguments
CLEAN=""
VERBOSE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --clean)
            CLEAN="--clean"
            shift
            ;;
        --verbose|-v)
            VERBOSE="--verbose"
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [--clean] [--verbose]"
            echo ""
            echo "Options:"
            echo "  --clean     Clean previous build artifacts before generating"
            echo "  --verbose   Enable verbose output"
            echo "  --help      Show this help message"
            echo ""
            echo "This script generates API reference documentation from the OpenHands SDK."
            echo "Generated files will be placed in the sdk/api-reference/ directory."
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information."
            exit 1
            ;;
    esac
done

# Run the Python script
echo "Generating API documentation..."
python3 scripts/generate-api-docs.py $CLEAN $VERBOSE

echo ""
echo "✅ API documentation generation completed!"
echo "📁 Generated files are in: sdk/api-reference/"
echo "⚙️  Mint.json config snippet: scripts/mint-config-snippet.json"
echo ""
echo "Next steps:"
echo "1. Review the generated documentation in sdk/api-reference/"
echo "2. Copy the configuration from scripts/mint-config-snippet.json"
echo "3. Add it to your docs.json navigation structure"