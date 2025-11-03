# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------

# Add the openhands-sdk directory to the Python path
docs_root = Path(__file__).parent.parent.parent.parent
sdk_path = docs_root / "agent-sdk" / "openhands-sdk"
if sdk_path.exists():
    sys.path.insert(0, str(sdk_path))

# -- Project information -----------------------------------------------------

project = 'OpenHands SDK'
copyright = '2024, OpenHands Team'
author = 'OpenHands Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_markdown_builder',
]

# Templates path
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': None,
    '.md': 'myst_parser',
}

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for autodoc extension -------------------------------------------

# Automatically extract typehints
autodoc_typehints = 'description'
autodoc_typehints_description_target = 'documented'

# Include both class docstring and __init__ docstring
autoclass_content = 'both'

# Order members by source order
autodoc_member_order = 'bysource'

# Include private members if they have docstrings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# -- Options for napoleon extension ------------------------------------------

# Napoleon settings for Google and NumPy style docstrings
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

# -- Options for autosummary extension ---------------------------------------

autosummary_generate = True
autosummary_imported_members = True

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# -- Options for markdown builder --------------------------------------------

# Configure markdown builder for clean output
markdown_http_base = 'https://github.com/OpenHands/software-agent-sdk'
markdown_uri_doc_suffix = '.md'

# Suppress warnings for missing references in markdown output
suppress_warnings = ['ref.myst']

# -- Custom configuration for better markdown output -------------------------

def setup(app):
    """Custom setup function for better markdown generation."""
    # Add custom CSS for better rendering
    app.add_css_file('custom.css')
    
    # Configure markdown output
    app.connect('build-finished', cleanup_markdown_output)

def cleanup_markdown_output(app, exception):
    """Clean up markdown output for better Mintlify compatibility."""
    if app.builder.name != 'markdown':
        return
    
    build_dir = Path(app.outdir)
    
    # Process all markdown files
    for md_file in build_dir.glob('*.md'):
        if md_file.name == 'index.md':
            continue
            
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean up content for better Mintlify compatibility
        lines = content.split('\n')
        cleaned_lines = []
        
        skip_next = False
        for i, line in enumerate(lines):
            if skip_next:
                skip_next = False
                continue
                
            # Remove orphan directives
            if line.strip() == ':orphan:':
                continue
                
            # Clean up module headers
            if line.startswith('# ') and 'module' in line.lower():
                # Make module headers more readable
                module_name = line.replace('# ', '').replace(' module', '')
                line = f'# {module_name}'
            
            # Remove currentmodule directives
            if '.. currentmodule::' in line:
                continue
                
            # Clean up class and function signatures
            if line.startswith('## ') and ('class ' in line or 'def ' in line):
                # Simplify class/function headers
                line = line.replace('class ', '').replace('def ', '')
            
            cleaned_lines.append(line)
        
        # Write cleaned content back
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(cleaned_lines))