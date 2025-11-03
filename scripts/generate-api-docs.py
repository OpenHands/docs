#!/usr/bin/env python3
"""
API Documentation Generation Script

This script generates API reference documentation from the OpenHands software-agent-sdk
repository using Sphinx with markdown output for Mintlify integration.

Requirements:
- sphinx
- sphinx-markdown-builder
- myst-parser

Usage:
    python scripts/generate-api-docs.py [--clean] [--verbose]
"""

import argparse
import json
import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional


class APIDocGenerator:
    """Generates API documentation from the software-agent-sdk repository."""
    
    def __init__(self, docs_root: Path, verbose: bool = False):
        self.docs_root = docs_root
        self.scripts_dir = docs_root / "scripts"
        self.sphinx_dir = self.scripts_dir / "sphinx"
        self.sdk_repo_dir = docs_root / "agent-sdk"
        self.api_docs_output = docs_root / "sdk" / "api-reference"
        self.verbose = verbose
        
        # Setup logging
        level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def run_command(self, cmd: List[str], cwd: Optional[Path] = None, check: bool = True) -> subprocess.CompletedProcess:
        """Run a shell command with error handling."""
        cwd = cwd or self.docs_root
        self.logger.debug(f"Running command: {' '.join(cmd)} in {cwd}")
        
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd,
                capture_output=True,
                text=True,
                check=check
            )
            
            if self.verbose and result.stdout:
                self.logger.debug(f"STDOUT: {result.stdout}")
            if result.stderr:
                self.logger.warning(f"STDERR: {result.stderr}")
                
            return result
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {' '.join(cmd)}")
            self.logger.error(f"Exit code: {e.returncode}")
            self.logger.error(f"STDOUT: {e.stdout}")
            self.logger.error(f"STDERR: {e.stderr}")
            raise
    
    def clone_or_update_sdk_repo(self) -> None:
        """Clone or update the software-agent-sdk repository."""
        sdk_repo_url = "https://github.com/OpenHands/software-agent-sdk.git"
        
        if self.sdk_repo_dir.exists():
            self.logger.info("Updating existing agent-sdk repository...")
            self.run_command(["git", "fetch", "origin"], cwd=self.sdk_repo_dir)
            self.run_command(["git", "reset", "--hard", "origin/main"], cwd=self.sdk_repo_dir)
        else:
            self.logger.info("Cloning agent-sdk repository...")
            self.run_command(["git", "clone", sdk_repo_url, str(self.sdk_repo_dir)])
    
    def check_dependencies(self) -> None:
        """Check if required Python packages are installed."""
        required_packages = ["sphinx", "sphinx_markdown_builder", "myst_parser"]
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package.replace("-", "_"))
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            self.logger.error(f"Missing required packages: {', '.join(missing_packages)}")
            self.logger.error("Install them with: pip install sphinx sphinx-markdown-builder myst-parser")
            sys.exit(1)
    
    def setup_sphinx_directories(self) -> None:
        """Create necessary Sphinx directories."""
        self.sphinx_dir.mkdir(parents=True, exist_ok=True)
        (self.sphinx_dir / "source").mkdir(exist_ok=True)
        (self.sphinx_dir / "build").mkdir(exist_ok=True)
    
    def generate_rst_files(self) -> None:
        """Generate RST files for Sphinx autodoc."""
        source_dir = self.sphinx_dir / "source"
        
        # Find Python packages in the SDK
        # Point directly to the sdk directory since that's where the actual modules are
        openhands_sdk_dir = self.sdk_repo_dir / "openhands-sdk" / "openhands" / "sdk"
        if not openhands_sdk_dir.exists():
            self.logger.error(f"SDK directory not found: {openhands_sdk_dir}")
            sys.exit(1)
        
        # Generate module documentation
        self.logger.info("Generating RST files with sphinx-apidoc...")
        self.run_command([
            "sphinx-apidoc",
            "-f",  # Force overwrite
            "-e",  # Put each module on separate page
            "-M",  # Put module documentation before submodule documentation
            "-o", str(source_dir),
            str(openhands_sdk_dir),
            "--separate"
        ])
    
    def run_sphinx_build(self) -> None:
        """Run Sphinx build to generate markdown files."""
        self.logger.info("Building documentation with Sphinx...")
        
        build_dir = self.sphinx_dir / "build" / "markdown"
        source_dir = self.sphinx_dir / "source"
        
        self.run_command([
            "sphinx-build",
            "-b", "markdown",
            "-E",  # Don't use saved environment
            str(source_dir),
            str(build_dir)
        ])
        
        return build_dir
    
    def organize_output_docs(self, build_dir: Path) -> None:
        """Organize and clean up the generated markdown files."""
        self.logger.info("Organizing output documentation...")
        
        # Remove existing API docs
        if self.api_docs_output.exists():
            shutil.rmtree(self.api_docs_output)
        
        self.api_docs_output.mkdir(parents=True, exist_ok=True)
        
        # Copy and organize markdown files
        if build_dir.exists():
            for md_file in build_dir.glob("*.md"):
                if md_file.name not in ["index.md"]:  # Skip main index
                    # Clean up the markdown content for Mintlify
                    self.clean_markdown_file(md_file, self.api_docs_output / md_file.name)
        
        # Create a main index file
        self.create_api_index()
    
    def clean_markdown_file(self, input_file: Path, output_file: Path) -> None:
        """Clean up Sphinx-generated markdown for Mintlify compatibility."""
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove Sphinx-specific syntax that might not work well with Mintlify
        # Add frontmatter for Mintlify
        module_name = input_file.stem
        
        # Fix title formatting - keep it as code-like instead of title case
        if module_name.startswith("openhands"):
            title = module_name  # Keep the full module path
        else:
            title = f"openhands.{module_name}"  # Add the openhands prefix if missing
        
        frontmatter = f"""---
title: {title}
description: API reference for {title}
---

"""
        
        # Clean up content
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Skip certain Sphinx directives that don't translate well
            if line.strip().startswith(':orphan:'):
                continue
            if line.strip().startswith('.. currentmodule::'):
                continue
            
            cleaned_lines.append(line)
        
        cleaned_content = frontmatter + '\n'.join(cleaned_lines)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
    
    def create_api_index(self) -> None:
        """Create the main API reference index file."""
        index_content = """---
title: API Reference
description: Complete API reference for the OpenHands SDK
---

# API Reference

This section contains the complete API reference documentation for the OpenHands SDK, automatically generated from the source code.

## Modules

"""
        
        # List all generated markdown files
        for md_file in sorted(self.api_docs_output.glob("*.md")):
            if md_file.name != "index.md":
                module_name = md_file.stem
                title = module_name.replace("openhands.", "").replace("_", " ").title()
                index_content += f"- [{title}](./{md_file.name})\n"
        
        index_file = self.api_docs_output / "index.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
    
    def generate_mint_config_snippet(self) -> Dict:
        """Generate a mint.json configuration snippet for the API docs."""
        api_pages = []
        
        # Add index page
        api_pages.append("sdk/api-reference/index")
        
        # Add all module pages
        for md_file in sorted(self.api_docs_output.glob("*.md")):
            if md_file.name != "index.md":
                page_path = f"sdk/api-reference/{md_file.stem}"
                api_pages.append(page_path)
        
        config_snippet = {
            "group": "API Reference",
            "pages": api_pages
        }
        
        return config_snippet
    
    def save_mint_config_snippet(self, config: Dict) -> None:
        """Save the mint.json configuration snippet to a file."""
        config_file = self.scripts_dir / "mint-config-snippet.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        
        self.logger.info(f"Mint.json configuration snippet saved to {config_file}")
    
    def setup_sphinx_structure(self) -> None:
        """Ensure Sphinx directories and configuration files exist."""
        source_dir = self.sphinx_dir / "source"
        source_dir.mkdir(parents=True, exist_ok=True)
        
        # Ensure conf.py exists
        conf_py = source_dir / "conf.py"
        if not conf_py.exists():
            conf_content = '''# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenHands SDK'
copyright = '2024, OpenHands'
author = 'OpenHands'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Autosummary settings
autosummary_generate = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# MyST settings
myst_enable_extensions = [
    "deflist",
    "tasklist",
    "colon_fence",
]

# Markdown builder settings
markdown_http_base = "https://github.com/OpenHands/software-agent-sdk"
markdown_uri_doc_suffix = ".md"

# Custom settings for cleaner markdown output
suppress_warnings = ['myst.header']

# Add the SDK source path to Python path
import sys
import os
sys.path.insert(0, os.path.abspath('../../../agent-sdk/openhands-sdk'))
sys.path.insert(0, os.path.abspath('../../../agent-sdk/openhands-sdk/openhands'))
'''
            conf_py.write_text(conf_content)
        
        # Ensure index.rst exists
        index_rst = source_dir / "index.rst"
        if not index_rst.exists():
            index_content = '''OpenHands SDK API Reference
============================

Welcome to the OpenHands SDK API reference documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
'''
            index_rst.write_text(index_content)

    def clean_build_artifacts(self) -> None:
        """Clean up build artifacts but keep generated docs."""
        self.logger.info("Cleaning build artifacts...")
        
        build_dir = self.sphinx_dir / "build"
        if build_dir.exists():
            shutil.rmtree(build_dir)
        
        source_dir = self.sphinx_dir / "source"
        if source_dir.exists():
            # Keep conf.py and index.rst, remove generated files
            for file in source_dir.glob("*.rst"):
                if file.name not in ["index.rst", "conf.py"]:
                    file.unlink()
            # Also remove any Python cache files
            for file in source_dir.glob("*.py"):
                if file.name not in ["conf.py"]:
                    file.unlink()
    
    def generate(self, clean: bool = False) -> None:
        """Main method to generate API documentation."""
        try:
            self.logger.info("Starting API documentation generation...")
            
            # Clean previous build if requested
            if clean:
                self.logger.info("Cleaning previous build...")
                self.clean_build_artifacts()
                if self.api_docs_output.exists():
                    shutil.rmtree(self.api_docs_output)
            
            # Check dependencies
            self.check_dependencies()
            
            # Set up Sphinx structure
            self.setup_sphinx_structure()
            
            # Clone or update SDK repository
            self.clone_or_update_sdk_repo()
            
            # Setup Sphinx directories
            self.setup_sphinx_directories()
            
            # Generate RST files
            self.generate_rst_files()
            
            # Run Sphinx build
            build_dir = self.run_sphinx_build()
            
            # Organize output documentation
            self.organize_output_docs(build_dir)
            
            # Generate mint.json configuration
            mint_config = self.generate_mint_config_snippet()
            self.save_mint_config_snippet(mint_config)
            
            # Clean up build artifacts
            self.clean_build_artifacts()
            
            self.logger.info("API documentation generation completed successfully!")
            self.logger.info(f"Generated documentation available in: {self.api_docs_output}")
            
        except Exception as e:
            self.logger.error(f"Documentation generation failed: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate API documentation from software-agent-sdk")
    parser.add_argument("--clean", action="store_true", help="Clean previous build artifacts")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Determine docs root directory
    script_path = Path(__file__).resolve()
    docs_root = script_path.parent.parent
    
    # Generate documentation
    generator = APIDocGenerator(docs_root, verbose=args.verbose)
    generator.generate(clean=args.clean)


if __name__ == "__main__":
    main()