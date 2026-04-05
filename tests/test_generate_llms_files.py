"""Regression tests for the llms file generator."""

import importlib.util
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).parent.parent / 'scripts' / 'generate-llms-files.py'
SPEC = importlib.util.spec_from_file_location('generate_llms_files', SCRIPT_PATH)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TestGenerateLlmsFiles:
    """Tests for the llms file generator script."""

    def test_llms_intro_uses_applications_wording(self):
        """The llms intro should continue to use 'applications documentation'."""
        pages = MODULE.iter_doc_pages()

        llms_text = MODULE.build_llms_txt(pages)

        assert (
            'The sections below intentionally separate OpenHands applications documentation '
            '(Web App Server / Cloud / CLI)' in llms_text
        )
        assert 'OpenHands product documentation' not in llms_text
