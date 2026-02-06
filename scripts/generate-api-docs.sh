#!/bin/bash

# API Documentation Generation Script
#
# Generates .mdx API reference files using griffe (mkdocstrings).

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$DOCS_ROOT"

if [ ! -f "scripts/generate-api-docs.py" ]; then
    echo "Error: Python script not found at scripts/generate-api-docs.py"
    exit 1
fi

echo "Checking dependencies..."
python3 -c "import griffe" 2>/dev/null || {
    echo "Error: griffe not installed."
    echo "Please install it with: pip install griffe"
    exit 1
}

echo "Generating API documentation..."
python3 scripts/generate-api-docs.py

echo ""
echo "Done! Generated files are in: sdk/api-reference/"
