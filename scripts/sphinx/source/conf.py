
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
