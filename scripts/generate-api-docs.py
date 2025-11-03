#!/usr/bin/env python3
"""
Simple API documentation generator for OpenHands SDK.

This script generates clean, parser-friendly markdown documentation
by extracting docstrings and presenting them in a simple format.
"""

import os
import re
import json
import shutil
import logging
import subprocess
from pathlib import Path
from typing import Dict, List, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimpleAPIDocGenerator:
    def __init__(self, docs_dir: Path):
        self.docs_dir = docs_dir
        self.agent_sdk_dir = docs_dir / "agent-sdk"
        self.output_dir = docs_dir / "sdk" / "api-reference"
        self.sphinx_dir = docs_dir / "scripts" / "sphinx"
        
    def run(self):
        """Main execution method."""
        logger.info("Starting simple API documentation generation...")
        
        # Step 1: Setup agent-sdk repository
        self.setup_agent_sdk()
        
        # Step 2: Install the SDK
        self.install_sdk()
        
        # Step 3: Generate documentation using Sphinx
        self.generate_sphinx_docs()
        
        # Step 4: Clean and simplify the generated markdown
        self.clean_generated_docs()
        
        # Step 5: Update navigation
        self.update_navigation()
        
        logger.info("API documentation generation completed successfully!")
        
    def setup_agent_sdk(self):
        """Clone or update the agent-sdk repository."""
        if self.agent_sdk_dir.exists():
            logger.info("Updating existing agent-sdk repository...")
            self.run_command(["git", "fetch", "origin"], cwd=self.agent_sdk_dir)
            self.run_command(["git", "reset", "--hard", "origin/main"], cwd=self.agent_sdk_dir)
        else:
            logger.info("Cloning agent-sdk repository...")
            self.run_command([
                "git", "clone", 
                "https://github.com/OpenHands/software-agent-sdk.git",
                str(self.agent_sdk_dir)
            ])
            
    def install_sdk(self):
        """Install the SDK package."""
        logger.info("Installing openhands-sdk package...")
        sdk_path = self.agent_sdk_dir / "openhands-sdk"
        self.run_command([
            "python", "-m", "pip", "install", "-e", str(sdk_path)
        ])
        
    def generate_sphinx_docs(self):
        """Generate documentation using Sphinx."""
        logger.info("Generating documentation with Sphinx...")
        
        # Create Sphinx configuration
        self.create_sphinx_config()
        
        # Generate RST files
        self.create_rst_files()
        
        # Build documentation
        self.build_sphinx_docs()
        
    def create_sphinx_config(self):
        """Create a simple Sphinx configuration."""
        sphinx_source = self.sphinx_dir / "source"
        sphinx_source.mkdir(parents=True, exist_ok=True)
        
        conf_py = sphinx_source / "conf.py"
        conf_py.write_text('''
import os
import sys
sys.path.insert(0, os.path.abspath('../../../agent-sdk/openhands-sdk'))

project = 'OpenHands SDK'
copyright = '2024, OpenHands'
author = 'OpenHands'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_markdown_builder',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'special-members': '__init__',
}

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

html_theme = 'sphinx_rtd_theme'
''')
        
    def create_rst_files(self):
        """Create RST files for the main SDK modules."""
        sphinx_source = self.sphinx_dir / "source"
        
        # Main index file
        index_rst = sphinx_source / "index.rst"
        index_rst.write_text('''
OpenHands SDK API Reference
===========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   openhands.sdk

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
''')
        
        # Main SDK module
        sdk_rst = sphinx_source / "openhands.sdk.rst"
        sdk_rst.write_text('''
openhands.sdk package
=====================

.. automodule:: openhands.sdk
   :members:
   :undoc-members:
   :show-inheritance:

Submodules
----------

.. toctree::
   :maxdepth: 1

   openhands.sdk.agent
   openhands.sdk.conversation
   openhands.sdk.event
   openhands.sdk.llm
   openhands.sdk.tool
   openhands.sdk.workspace
   openhands.sdk.security
   openhands.sdk.utils
''')
        
        # Generate RST files for each major module
        modules = [
            'agent', 'conversation', 'event', 'llm', 
            'tool', 'workspace', 'security', 'utils'
        ]
        
        for module in modules:
            module_rst = sphinx_source / f"openhands.sdk.{module}.rst"
            module_rst.write_text(f'''
openhands.sdk.{module} module
{'=' * (len(f'openhands.sdk.{module} module'))}

.. automodule:: openhands.sdk.{module}
   :members:
   :undoc-members:
   :show-inheritance:
''')
            
    def build_sphinx_docs(self):
        """Build the Sphinx documentation."""
        build_dir = self.sphinx_dir / "build"
        source_dir = self.sphinx_dir / "source"
        
        # Clean previous build
        if build_dir.exists():
            shutil.rmtree(build_dir)
            
        # Build markdown documentation
        self.run_command([
            "sphinx-build", "-b", "markdown", 
            str(source_dir), str(build_dir)
        ])
        
    def clean_generated_docs(self):
        """Clean and simplify the generated markdown files."""
        logger.info("Cleaning generated documentation...")
        
        build_dir = self.sphinx_dir / "build"
        
        # Remove old output directory
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Process each markdown file
        for md_file in build_dir.glob("*.md"):
            if md_file.name == "index.md":
                continue
                
            logger.info(f"Processing {md_file.name}")
            content = md_file.read_text()
            
            # Clean the content
            cleaned_content = self.clean_markdown_content(content, md_file.name)
            
            # Write to output directory with .mdx extension
            output_filename = md_file.name.replace('.md', '.mdx')
            output_file = self.output_dir / output_filename
            output_file.write_text(cleaned_content)
            
    def clean_markdown_content(self, content: str, filename: str) -> str:
        """Clean markdown content to be parser-friendly."""
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Skip empty lines and sphinx-specific content
            if not line.strip():
                cleaned_lines.append(line)
                continue
                
            # Clean headers - remove complex signatures, keep just names
            if line.startswith('#'):
                line = self.clean_header(line)
                
            # Remove problematic patterns
            line = self.remove_problematic_patterns(line)
            
            cleaned_lines.append(line)
            
        # Add frontmatter
        module_name = filename.replace('.md', '')
        frontmatter = f'''---
title: {module_name}
description: API reference for {module_name}
---

'''
        
        return frontmatter + '\n'.join(cleaned_lines)
        
    def clean_header(self, line: str) -> str:
        """Clean header lines to contain only class/method names."""
        # Extract just the class or method name from complex signatures
        
        # Pattern for class headers: "### class ClassName(...)"
        class_match = re.match(r'^(#+)\s*class\s+([^(]+)', line)
        if class_match:
            level, class_name = class_match.groups()
            # Clean up the class name
            class_name = class_name.strip().split('.')[-1]  # Get just the class name
            return f"{level} {class_name}"
            
        # Pattern for method headers: "#### method_name(...)"
        method_match = re.match(r'^(#+)\s*([^(]+)\(', line)
        if method_match:
            level, method_name = method_match.groups()
            # Clean up the method name
            method_name = method_name.strip().split('.')[-1]  # Get just the method name
            # Remove any decorators or prefixes
            method_name = re.sub(r'^(static|class|abstract|property)\s+', '', method_name)
            return f"{level} {method_name}"
            
        # Pattern for property headers: "#### property property_name"
        prop_match = re.match(r'^(#+)\s*property\s+([^:]+)', line)
        if prop_match:
            level, prop_name = prop_match.groups()
            prop_name = prop_name.strip()
            return f"{level} {prop_name}"
            
        # For other headers, just clean up basic formatting
        line = re.sub(r'\*([^*]+)\*', r'\1', line)  # Remove emphasis
        return line
        
    def remove_problematic_patterns(self, line: str) -> str:
        """Remove patterns that cause parsing issues."""
        # Remove all emphasis and bold formatting
        line = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)  # Remove bold
        line = re.sub(r'\*([^*]+)\*', r'\1', line)      # Remove emphasis
        
        # Fix HTML-like tags
        line = line.replace('<', '`<').replace('>', '>`')
        
        # Remove escaped characters that cause issues
        line = line.replace('\\*', '*')
        line = line.replace('\\', '')
        
        # Fix dictionary/object literals that cause parsing issues
        # Pattern: = {'key': 'value', 'key2': 'value2'} or = {}
        if ' = {' in line and '}' in line:
            # Replace with a simple description
            line = re.sub(r' = \{[^}]*\}', ' = (configuration object)', line)
        
        # Fix JSON-like patterns that cause parsing issues
        # Pattern: { "type": "function", "name": …, "description": …, "parameters": … }
        if line.strip().startswith('{') and line.strip().endswith('}'):
            # Replace with a simple description
            line = '(JSON configuration object)'
        
        # Fix ClassVar patterns
        line = re.sub(r'ClassVar\[([^\]]+)\]', r'ClassVar[\1]', line)
        
        # Fix template string patterns like ${variable}
        line = re.sub(r'\$\{[^}]+\}', '(variable)', line)
        
        return line
        
    def update_navigation(self):
        """Update the navigation configuration."""
        logger.info("Updating navigation configuration...")
        
        # Generate navigation entries for all API files
        api_files = list(self.output_dir.glob("*.mdx"))
        nav_entries = []
        
        for api_file in sorted(api_files):
            module_name = api_file.stem
            nav_entries.append(f'"sdk/api-reference/{module_name}"')
            
        # Create navigation snippet
        nav_config = {
            "navigation": [
                {
                    "group": "API Reference",
                    "pages": [entry.strip('"') for entry in nav_entries]
                }
            ]
        }
        
        # Save navigation snippet
        nav_file = self.docs_dir / "scripts" / "mint-config-snippet.json"
        nav_file.write_text(json.dumps(nav_config, indent=2))
        
        logger.info(f"Generated navigation for {len(nav_entries)} API reference files")
        
    def run_command(self, cmd: List[str], cwd: Path = None):
        """Run a shell command with error handling."""
        try:
            result = subprocess.run(
                cmd, 
                cwd=cwd or self.docs_dir,
                capture_output=True, 
                text=True, 
                check=True
            )
            if result.stdout:
                logger.debug(f"STDOUT: {result.stdout}")
            if result.stderr:
                logger.warning(f"STDERR: {result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {' '.join(cmd)}")
            logger.error(f"Exit code: {e.returncode}")
            logger.error(f"STDOUT: {e.stdout}")
            logger.error(f"STDERR: {e.stderr}")
            raise


def main():
    """Main entry point."""
    docs_dir = Path(__file__).parent.parent
    generator = SimpleAPIDocGenerator(docs_dir)
    generator.run()


if __name__ == "__main__":
    main()