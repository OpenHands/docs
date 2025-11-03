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
import re
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
    
    def install_sdk_package(self) -> None:
        """Install the openhands-sdk package so Sphinx can import modules."""
        self.logger.info("Installing openhands-sdk package...")
        try:
            # First try to install from the local cloned repo for latest changes
            sdk_package_dir = self.sdk_repo_dir / "openhands-sdk"
            if sdk_package_dir.exists():
                self.logger.info("Installing SDK from local repository...")
                self.run_command([sys.executable, "-m", "pip", "install", "-e", str(sdk_package_dir)])
            else:
                # Fallback to PyPI
                self.logger.info("Installing SDK from PyPI...")
                self.run_command([sys.executable, "-m", "pip", "install", "openhands-sdk"])
        except Exception as e:
            self.logger.warning(f"Failed to install openhands-sdk: {e}")
            self.logger.warning("Continuing without SDK installation - docstrings may be minimal")

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
        
        # Since we installed the package, we can now use the installed module path
        # instead of pointing to the source directory
        self.logger.info("Generating RST files with sphinx-apidoc for installed openhands.sdk package...")
        
        # Use the installed package location
        import openhands.sdk
        package_path = Path(openhands.sdk.__file__).parent
        
        # Generate RST files with correct module prefix
        self.run_command([
            "sphinx-apidoc",
            "-f",  # Force overwrite
            "-e",  # Put each module on separate page
            "-M",  # Put module documentation before submodule documentation
            "-o", str(source_dir),
            str(package_path),
            "--separate",
            "--module-first"
        ])
        
        # Fix the generated RST files to use the correct module names
        self._fix_rst_module_names(source_dir)
    
    def _fix_rst_module_names(self, source_dir: Path) -> None:
        """Fix RST files to use correct module names (openhands.sdk.* instead of sdk.*)."""
        self.logger.info("Fixing RST module names...")
        
        for rst_file in source_dir.glob("*.rst"):
            if rst_file.name in ["index.rst", "modules.rst"]:
                continue
                
            content = rst_file.read_text()
            
            # Replace module references - be more careful to avoid double prefixes
            content = content.replace(".. automodule:: sdk.", ".. automodule:: openhands.sdk.")
            # Fix titles and other references, but avoid double prefixes
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('sdk.') and not line.startswith('openhands.sdk.'):
                    lines[i] = line.replace('sdk.', 'openhands.sdk.', 1)
            content = '\n'.join(lines)
            
            rst_file.write_text(content)
    
    def run_sphinx_build(self) -> Path:
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
        # First, handle multiline JSON patterns that span multiple lines
        # This is a specific fix for the {"key": "value", "key2": "value2"} pattern
        json_multiline_pattern = r'(\{[^}]*"[^"]*":[^}]*,\s*\n\s*"[^"]*":[^}]*\})'
        content = re.sub(json_multiline_pattern, lambda m: '`' + m.group(1).replace('\n', ' ').strip() + '`', content, flags=re.MULTILINE)
        
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Skip certain Sphinx directives that don't translate well
            if line.strip().startswith(':orphan:'):
                continue
            if line.strip().startswith('.. currentmodule::'):
                continue
            
            # Fix problematic syntax that breaks link checkers and Mintlify
            # Handle complex type annotations with asterisks and curly braces
            if '*:' in line and '*=' in line and '{' in line and '}' in line:
                # This is likely a model_config line that's causing parsing issues
                # Simplify it by escaping or reformatting
                line = line.replace('*:', ' :').replace('*=', ' =')
                # Escape curly braces that might be interpreted as template syntax
                line = line.replace('{', '\\{').replace('}', '\\}')
            
            # Fix <factory> tags that Mintlify interprets as unclosed HTML
            if '<factory>' in line:
                line = line.replace('<factory>', '`<factory>`')
            
            # Fix other angle bracket patterns that Mintlify interprets as HTML tags
            if '<secret-hidden>' in line:
                line = line.replace('<secret-hidden>', '`<secret-hidden>`')
            
            # General fix for other potential HTML-like patterns in documentation text
            # Look for patterns like <word> or <word-word> that aren't actual HTML tags
            # Match patterns like <word> or <word-word> but not actual HTML tags like <a>, <div>, etc.
            # This regex matches angle brackets around words that contain hyphens or are not common HTML tags
            html_like_pattern = r'<([a-zA-Z][a-zA-Z0-9]*(?:-[a-zA-Z0-9]+)+)>'
            if re.search(html_like_pattern, line):
                line = re.sub(html_like_pattern, r'`<\1>`', line)
            
            # Fix complex type signatures that might cause acorn parsing issues
            # Break up very long lines with complex type annotations
            if len(line) > 500 and ('~typing.' in line or '~annotated_types.' in line):
                # This is likely a very complex class signature that might break parsers
                # We can try to make it more readable by adding line breaks, but for now
                # let's just ensure it doesn't have problematic characters
                # Replace problematic patterns that might confuse JavaScript parsers
                line = line.replace('~typing.', 'typing.')
                line = line.replace('~annotated_types.', 'annotated_types.')
                line = line.replace('~uuid.', 'uuid.')
                line = line.replace('~openhands.', 'openhands.')
            
            # Fix JSON-like patterns in documentation that confuse JavaScript parsers
            # Look for patterns like {"key": "value"} in documentation text
            if '{' in line and ':' in line and '"' in line:
                # This might be a JSON example in documentation
                # Wrap JSON-like patterns in code blocks to prevent parsing as JavaScript
                # Handle both single-line and partial JSON patterns
                json_pattern = r'(\{[^}]*"[^"]*":[^}]*)'
                if re.search(json_pattern, line):
                    line = re.sub(json_pattern, r'`\1`', line)
                
                # Also handle standalone JSON values that might be problematic
                if '"' in line and ':' in line:
                    # Pattern for "key": "value" pairs
                    kv_pattern = r'("[\w\s:]+": "[\w\s]+")'
                    line = re.sub(kv_pattern, r'`\1`', line)
            
            # Fix other problematic patterns
            # Escape asterisks that might be interpreted as emphasis when they're part of type annotations
            if line.startswith('####') and '*:' in line and not line.count('*') % 2 == 0:
                # This is a property/attribute definition with unbalanced asterisks
                line = line.replace('*:', ' :')
            
            # Fix Sphinx-generated parameter lists that cause acorn parsing errors
            # Pattern: "* **Parameters:**" creates unbalanced asterisks
            if line.strip() == '* **Parameters:**':
                line = line.replace('* **Parameters:**', '**Parameters:**')
            elif line.strip() == '* **Returns:**':
                line = line.replace('* **Returns:**', '**Returns:**')
            elif line.strip() == '* **Raises:**':
                line = line.replace('* **Raises:**', '**Raises:**')
            elif line.strip() == '* **Yields:**':
                line = line.replace('* **Yields:**', '**Yields:**')
            
            # Format long class/function signatures for better readability
            # Disabled custom formatting to rely on Sphinx's native output
            # line = self.format_long_signatures(line)
            
            cleaned_lines.append(line)
        
        cleaned_content = frontmatter + '\n'.join(cleaned_lines)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
    
    def format_long_signatures(self, line: str) -> str:
        """Format long class/function signatures for better readability."""
        # Only process lines that look like class or function signatures
        if not (line.startswith('### *class*') or line.startswith('#### ') and '(' in line and ')' in line):
            return line
        
        # If the line is not very long, don't modify it
        if len(line) < 200:
            return line
        
        # For class signatures, format them nicely
        if line.startswith('### *class*'):
            # Extract the class name and parameters
            match = re.match(r'(### \*class\* )([^(]+)\((.*)\)', line)
            if match:
                header_prefix = match.group(1)  # "### *class* "
                class_name = match.group(2).strip()  # Just the class name
                params_str = match.group(3)
                
                # Create clean title with just the class name
                result = f"{header_prefix}{class_name}\n\n"
                
                # Add parameters as formatted text if they exist
                if params_str.strip():
                    formatted_params = self.format_parameters_as_text(params_str)
                    result += f"**Parameters:**\n\n{formatted_params}\n"
                
                return result
        
        # For method signatures
        elif line.startswith('#### ') and '(' in line:
            # Extract method name and parameters
            match = re.match(r'(#### )([^(]+)\((.*)\)', line)
            if match:
                header_prefix = match.group(1)  # "#### "
                method_name = match.group(2).strip()  # Just the method name
                params_str = match.group(3)
                
                # Create clean title with just the method name
                result = f"{header_prefix}{method_name}\n\n"
                
                # Add parameters as formatted text if they exist
                if params_str.strip():
                    formatted_params = self.format_parameters_as_text(params_str)
                    result += f"**Parameters:**\n\n{formatted_params}\n"
                
                return result
        
        return line
    
    def format_parameters_as_text(self, params_str: str) -> str:
        """Format parameter list as readable text."""
        if not params_str.strip():
            return ""
        
        # Split parameters by comma, but be careful about nested types
        params = []
        current_param = ""
        bracket_depth = 0
        
        for char in params_str:
            if char in '([{':
                bracket_depth += 1
            elif char in ')]}':
                bracket_depth -= 1
            elif char == ',' and bracket_depth == 0:
                params.append(current_param.strip())
                current_param = ""
                continue
            current_param += char
        
        if current_param.strip():
            params.append(current_param.strip())
        
        # Format each parameter as a bullet point
        formatted_params = []
        for param in params:
            if param.strip():
                # Clean up the parameter for better readability
                clean_param = param.strip()
                # Wrap in code blocks for better formatting
                formatted_params.append(f"- `{clean_param}`")
        
        return "\n".join(formatted_params)
    
    def format_parameters(self, params_str: str) -> str:
        """Format parameter list for better readability (legacy method)."""
        if not params_str.strip():
            return ""
        
        # Split parameters by comma, but be careful about nested types
        params = []
        current_param = ""
        bracket_depth = 0
        
        for char in params_str:
            if char in '([{':
                bracket_depth += 1
            elif char in ')]}':
                bracket_depth -= 1
            elif char == ',' and bracket_depth == 0:
                params.append(current_param.strip())
                current_param = ""
                continue
            current_param += char
        
        if current_param.strip():
            params.append(current_param.strip())
        
        # Format each parameter with proper indentation
        formatted_params = []
        for param in params:
            if param.strip():
                # Add indentation for readability
                formatted_params.append(f"    {param.strip()}")
        
        return ",\n".join(formatted_params)
    
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
            
            # Install SDK package for proper imports
            self.install_sdk_package()
            
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