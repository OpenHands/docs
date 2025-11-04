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
        
        # Step 2: Fix MDX syntax issues in agent-sdk files
        self.fix_agent_sdk_mdx_syntax()
        
        # Step 3: Install the SDK
        self.install_sdk()
        
        # Step 4: Generate documentation using Sphinx
        self.generate_sphinx_docs()
        
        # Step 5: Clean and simplify the generated markdown
        self.clean_generated_docs()
        
        # Step 6: Update navigation
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
        
    def fix_agent_sdk_mdx_syntax(self):
        """Fix MDX syntax issues in agent-sdk files to prevent Mintlify parsing errors."""
        logger.info("Fixing MDX syntax issues in agent-sdk files...")
        
        # Fix email addresses in repo.md
        repo_md = self.agent_sdk_dir / ".openhands" / "microagents" / "repo.md"
        if repo_md.exists():
            content = repo_md.read_text()
            # Fix unescaped @ symbols in email addresses
            content = re.sub(r'<([^<>]*@[^<>]*)>', r'&lt;\1&gt;', content)
            repo_md.write_text(content)
            
        # Fix README.md
        readme_md = self.agent_sdk_dir / "README.md"
        if readme_md.exists():
            content = readme_md.read_text()
            # Convert HTML comments to JSX format
            content = re.sub(r'<!--\s*(.*?)\s*-->', r'{/* \1 */}', content, flags=re.DOTALL)
            # Fix self-closing tags
            content = re.sub(r'<(img|br|hr)([^>]*?)(?<!/)>', r'<\1\2 />', content)
            readme_md.write_text(content)
        
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
            
            # Skip the top-level openhands.sdk.md file as it duplicates content
            if md_file.name == "openhands.sdk.md":
                logger.info(f"Skipping {md_file.name} (top-level duplicate)")
                continue
                
            logger.info(f"Processing {md_file.name}")
            content = md_file.read_text()
            
            # Clean the content
            cleaned_content = self.clean_markdown_content(content, md_file.name)
            
            # Write to output directory with .mdx extension
            output_filename = md_file.name.replace('.md', '.mdx')
            output_file = self.output_dir / output_filename
            output_file.write_text(cleaned_content)
            
    def clean_multiline_dictionaries(self, content: str) -> str:
        """Clean multi-line dictionary patterns that cause parsing issues."""
        import re
        
        # Handle the specific problematic pattern that keeps appearing
        # Pattern: For example: {"Reasoning:": "bold blue",\n    "Thought:": "bold green"}
        pattern1 = r'For example: \{"[^"]*":\s*"[^"]*",\s*\n\s*"[^"]*":\s*"[^"]*"\}'
        content = re.sub(pattern1, 'For example: (configuration dictionary)', content, flags=re.DOTALL)
        
        # More general multi-line dictionary patterns
        pattern2 = r'\{"[^"]*":\s*"[^"]*",\s*\n\s*"[^"]*":\s*"[^"]*"\}'
        content = re.sub(pattern2, '(configuration dictionary)', content, flags=re.DOTALL)
        
        # Handle any remaining multi-line patterns with curly braces
        pattern3 = r'\{[^{}]*\n[^{}]*\}'
        content = re.sub(pattern3, '(configuration object)', content, flags=re.DOTALL)
        
        return content

    def fix_header_hierarchy(self, content: str) -> str:
        """Fix header hierarchy to ensure proper nesting under class headers."""
        import re
        
        lines = content.split('\n')
        result_lines = []
        in_class_section = False
        
        for line in lines:
            # Check if we're entering a class section
            if re.match(r'^### class ', line):
                in_class_section = True
                result_lines.append(line)
            # Check if we're leaving a class section (another class or module header)
            elif line.startswith('### ') and not line.startswith('### class '):
                # This is a non-class h3 header within a class section - convert to h4
                if in_class_section:
                    line = '#' + line  # Convert ### to ####
                result_lines.append(line)
            # Check if we hit another class or end of content
            elif re.match(r'^### class ', line) or line.startswith('# '):
                in_class_section = line.startswith('### class ')
                result_lines.append(line)
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)

    def reorganize_class_content(self, content: str) -> str:
        """Reorganize class content to separate properties from methods."""
        import re
        
        lines = content.split('\n')
        result_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Check if this is a class header
            if re.match(r'^### \*class\*', line):
                # Process this class
                class_lines, i = self.process_class_section(lines, i)
                result_lines.extend(class_lines)
            else:
                result_lines.append(line)
                i += 1
        
        return '\n'.join(result_lines)
    
    def process_class_section(self, lines: list[str], start_idx: int) -> tuple[list[str], int]:
        """Process a single class section, separating properties from methods."""
        import re
        
        result = []
        i = start_idx
        
        # Add the class header and description (including any ### Example sections)
        while i < len(lines):
            line = lines[i]
            # Stop when we hit the first #### (class member) or another class
            if line.startswith('####') or (line.startswith('### *class*') and i > start_idx):
                break
            # Fix Example headers to be h4 instead of h3
            if line.startswith('### ') and not line.startswith('### *class*'):
                line = '#' + line  # Convert ### to ####
            result.append(line)
            i += 1
        
        # Collect all class members
        properties = []
        methods = []
        
        while i < len(lines):
            line = lines[i]
            
            # Stop if we hit another class or module (but not ### Example sections)
            if line.startswith('### *class*'):
                break
                
            if line.startswith('####'):
                # Determine if this is a property or method
                member_lines, i = self.extract_member_section(lines, i)
                
                if self.is_property(member_lines[0]):
                    properties.extend(member_lines)
                else:
                    methods.extend(member_lines)
            else:
                i += 1
        
        # Add properties section if we have any
        if properties:
            result.append('')
            result.append('#### Properties')
            result.append('')
            
            # Convert property headers to list items
            for prop_line in properties:
                if prop_line.startswith('####'):
                    # Extract property name and type
                    prop_match = re.match(r'^####\s*([^*:]+)\s*\*?:?\s*(.*)$', prop_line)
                    if prop_match:
                        prop_name = prop_match.group(1).strip()
                        prop_type = prop_match.group(2).strip()
                        # Clean up the type annotation
                        prop_type = re.sub(r'^\*\s*', '', prop_type)  # Remove leading *
                        prop_type = re.sub(r'\s*\*$', '', prop_type)  # Remove trailing *
                        if prop_type:
                            result.append(f'- `{prop_name}`: {prop_type}')
                        else:
                            result.append(f'- `{prop_name}`')
                elif prop_line.strip() and not prop_line.startswith('####'):
                    # Add description lines indented
                    result.append(f'  {prop_line}')
        
        # Add methods section if we have any
        if methods:
            if properties:  # Add spacing if we had properties
                result.append('')
            result.append('#### Methods')
            result.append('')
            result.extend(methods)
        
        return result, i
    
    def extract_member_section(self, lines: list[str], start_idx: int) -> tuple[list[str], int]:
        """Extract all lines belonging to a single class member."""
        result = []
        i = start_idx
        
        # Add the header line
        result.append(lines[i])
        i += 1
        
        # Add all following lines until we hit another header or class
        while i < len(lines):
            line = lines[i]
            if line.startswith('####') or line.startswith('###'):
                break
            result.append(line)
            i += 1
        
        return result, i
    
    def is_property(self, header_line: str) -> bool:
        """Determine if a class member is a property or method."""
        import re
        
        # Properties typically have type annotations with *: type* pattern
        if re.search(r'\*:\s*[^*]+\*', header_line):
            return True
        
        # Methods have parentheses
        if '(' in header_line and ')' in header_line:
            return False
        
        # Properties often have : followed by type info
        if ':' in header_line and not '(' in header_line:
            return True
        
        # Default to method if unclear
        return False

    def clean_markdown_content(self, content: str, filename: str) -> str:
        """Clean markdown content to be parser-friendly."""
        # First handle multi-line dictionary patterns
        content = self.clean_multiline_dictionaries(content)
        
        # Reorganize class content to separate properties from methods
        content = self.reorganize_class_content(content)
        
        # Fix header hierarchy (Example sections should be h4 under class headers)
        content = self.fix_header_hierarchy(content)
        
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
                
                # Skip module headers that duplicate the title
                if line.startswith('# ') and ' module' in line:
                    continue
                
            # Remove problematic patterns
            line = self.remove_problematic_patterns(line)
            
            cleaned_lines.append(line)
            
        # Add frontmatter
        module_name = filename.replace('.md', '')
        frontmatter = f'''---
title: {module_name}
description: API reference for {module_name} module
---

'''
        
        return frontmatter + '\n'.join(cleaned_lines)
        
    def clean_header(self, line: str) -> str:
        """Clean header lines to contain only class/method names."""
        # Extract just the class or method name from complex signatures
        
        # Pattern for class headers: "### *class* ClassName(...)" or "### class ClassName(...)"
        class_match = re.match(r'^(#+)\s*\*?class\*?\s+([^(]+)', line)
        if class_match:
            level, class_name = class_match.groups()
            # Extract just the class name (last part after the last dot) for readability
            simple_class_name = class_name.strip().split('.')[-1]
            return f"{level} class {simple_class_name}"
            
        # Pattern for method headers: "#### method_name(...)"
        method_match = re.match(r'^(#+)\s*([^(]+)\(', line)
        if method_match:
            level, method_name = method_match.groups()
            # Clean up the method name
            method_name = method_name.strip().split('.')[-1]  # Get just the method name
            # Remove any decorators or prefixes
            method_name = re.sub(r'^(static|class|abstract|property)\s+', '', method_name)
            return f"{level} {method_name}()"
            
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
        
        # Fix HTML-like tags (only actual HTML tags, not all < > characters)
        # Only replace if it looks like an HTML tag: <tagname> or </tagname>
        line = re.sub(r'<(/?\w+[^>]*)>', r'`<\1>`', line)
        
        # Fix Sphinx-generated blockquote markers that should be list continuations
        if line.startswith('> ') and not line.startswith('> **'):
            # This is likely a continuation of a bullet point, not a blockquote
            line = '  ' + line[2:]  # Replace '> ' with proper indentation
        
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
        
        # Fix specific problematic dictionary patterns
        if '{"Reasoning:": "bold blue",' in line or '"Thought:": "bold green"}' in line:
            # Replace the entire line with a simple description
            line = re.sub(r'.*\{"[^"]*":[^}]*\}.*', '    For example: (configuration dictionary)', line)
        
        # Fix ClassVar patterns
        line = re.sub(r'ClassVar\[([^\]]+)\]', r'ClassVar[\1]', line)
        
        # Fix template string patterns like ${variable}
        line = re.sub(r'\$\{[^}]+\}', '(variable)', line)
        
        # Fix asterisk in type annotations like "property name *: Type"
        line = re.sub(r' \*:', ':', line)
        
        # Fix any remaining curly braces that cause parsing issues
        if '{' in line and '}' in line:
            line = re.sub(r'\{[^}]*\}', '(configuration object)', line)
        
        # Note: All cross-reference link conversion logic removed - we now just strip links entirely
        class_to_module = {
            'Agent': 'agent',
            'AgentBase': 'agent', 
            'AgentContext': 'agent',
            'Conversation': 'conversation',
            'BaseConversation': 'conversation',
            'LocalConversation': 'conversation',
            'RemoteConversation': 'conversation',
            'ConversationState': 'conversation',
            'ConversationStats': 'conversation',
            'Event': 'event',
            'LLMConvertibleEvent': 'event',
            'MessageEvent': 'event',
            'LLM': 'llm',
            'LLMRegistry': 'llm',
            'LLMResponse': 'llm',
            'Message': 'llm',
            'ImageContent': 'llm',
            'TextContent': 'llm',
            'ThinkingBlock': 'llm',
            'RedactedThinkingBlock': 'llm',
            'Metrics': 'llm',
            'RegistryEvent': 'llm',
            'SecurityManager': 'security',
            'Tool': 'tool',
            'ToolDefinition': 'tool',
            'Action': 'tool',
            'Observation': 'tool',
            'Workspace': 'workspace',
            'BaseWorkspace': 'workspace',
            'LocalWorkspace': 'workspace',
            'RemoteWorkspace': 'workspace',
            'WorkspaceFile': 'workspace',
            'WorkspaceFileEdit': 'workspace',
            'WorkspaceFileEditResult': 'workspace',
            'WorkspaceFileReadResult': 'workspace',
            'WorkspaceFileWriteResult': 'workspace',
            'WorkspaceListResult': 'workspace',
            'WorkspaceSearchResult': 'workspace',
            'WorkspaceSearchResultItem': 'workspace',
            'WorkspaceUploadResult': 'workspace',
            'WorkspaceWriteResult': 'workspace',
        }

        # Fix anchor links - convert full module path anchors to simple class format
        # Pattern: openhands.sdk.module.mdx#openhands.sdk.module.ClassName -> openhands.sdk.module#class-classname
        def convert_anchor(match):
            module_path = match.group(1)
            full_class_path = match.group(2)
            class_name = full_class_path.split('.')[-1].lower()
            return f'openhands.sdk.{module_path}#class-{class_name}'
        
        line = re.sub(r'openhands\.sdk\.([^)#]+)\.mdx#openhands\.sdk\.\1\.([^)]+)', convert_anchor, line)
        
        # Also handle the .md# pattern before converting to .mdx
        line = re.sub(r'openhands\.sdk\.([^)#]+)\.md#openhands\.sdk\.\1\.([^)]+)', convert_anchor, line)

        # Fix links pointing to the removed top-level openhands.sdk.md page
        # Pattern: openhands.sdk.md#openhands.sdk.ClassName -> openhands.sdk.module#class-classname
        def convert_toplevel_anchor(match):
            full_class_path = match.group(1)
            class_name = full_class_path.split('.')[-1]
            
            # Find the correct module for this class
            if class_name in class_to_module:
                module = class_to_module[class_name]
                class_name_lower = class_name.lower()
                return f'openhands.sdk.{module}#class-{class_name_lower}'
            else:
                # Fallback: try to guess module from class name
                class_name_lower = class_name.lower()
                return f'openhands.sdk.{class_name_lower}#class-{class_name_lower}'

        line = re.sub(r'openhands\.sdk\.md#openhands\.sdk\.([^)]+)', convert_toplevel_anchor, line)

        # Fix same-file anchor references (e.g., #openhands.sdk.llm.LLM -> #class-llm)
        def convert_same_file_anchor(match):
            full_class_path = match.group(1)
            class_name = full_class_path.split('.')[-1].lower()
            return f'#class-{class_name}'

        line = re.sub(r'#openhands\.sdk\.[^.]+\.([^)]+)', convert_same_file_anchor, line)
        
        # Fix invalid http:// links
        line = re.sub(r'\[http://\]\(http://\)', 'http://', line)
        
        # Remove Python console prompt prefixes from examples
        line = re.sub(r'^>`>`>` ', '', line)
        
        # Remove all cross-reference links - just keep the class names as plain text
        # Pattern: [ClassName](openhands.sdk.module#class-classname) -> ClassName
        line = re.sub(r'\[([^\]]+)\]\(openhands\.sdk\.[^)]+\)', r'\1', line)

        # Clean up malformed property entries with empty names
        if '- ``:' in line and 'property ' in line:
            # Extract the property name and type from malformed entries like:
            # - ``: property service_to_llm : dict[str, [LLM](#openhands.sdk.llm.LLM)]
            match = re.search(r'- ``: property (\w+) : (.+)', line)
            if match:
                prop_name = match.group(1)
                prop_type = match.group(2)
                line = f'- `{prop_name}`: {prop_type}'
        
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

        # Also update the main docs.json file
        self.update_main_docs_json([entry.strip('"') for entry in nav_entries])
        
        logger.info(f"Generated navigation for {len(nav_entries)} API reference files")

    def update_main_docs_json(self, nav_entries):
        """Update the main docs.json file with the new API reference navigation."""
        docs_json_path = self.docs_dir / "docs.json"
        
        if not docs_json_path.exists():
            logger.warning("docs.json not found, skipping main navigation update")
            return
        
        try:
            with open(docs_json_path, 'r') as f:
                docs_config = json.load(f)
            
            # Find and update the API Reference section
            updated = False
            for tab in docs_config.get("navigation", {}).get("tabs", []):
                if tab.get("tab") == "SDK":
                    for page in tab.get("pages", []):
                        if isinstance(page, dict) and page.get("group") == "API Reference":
                            page["pages"] = nav_entries
                            updated = True
                            logger.info("Updated API Reference navigation in docs.json")
                            break
                    if updated:
                        break
            
            if updated:
                with open(docs_json_path, 'w') as f:
                    json.dump(docs_config, f, indent=2)
            else:
                logger.warning("Could not find API Reference section in docs.json to update")
                
        except Exception as e:
            logger.error(f"Error updating docs.json: {e}")
        
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