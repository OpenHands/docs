"""Tests for sync_use_case_automations.py."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / ".github" / "scripts"))

from sync_use_case_automations import (
    REPO_ROOT,
    generate_card_section,
    parse_frontmatter,
    replace_marker_section,
)


class TestParseFrontmatter:
    def test_valid(self):
        text = "---\ntitle: Hello\nautomation:\n  icon: star\n  summary: A test\n---\nbody"
        fm = parse_frontmatter(text)
        assert fm["title"] == "Hello"
        assert fm["automation"]["icon"] == "star"
        assert fm["automation"]["summary"] == "A test"

    def test_no_frontmatter(self):
        assert parse_frontmatter("just body text") == {}

    def test_empty_frontmatter(self):
        assert parse_frontmatter("---\n---\nbody") == {}


class TestGenerateCardSection:
    def test_single_card(self):
        use_cases = [("my-page", "My Page Title", {"icon": "star", "summary": "Short desc."})]
        output = generate_card_section(use_cases)
        assert 'title="My Page Title"' in output
        assert 'icon="star"' in output
        assert 'href="/openhands/usage/use-cases/my-page#automate-this"' in output
        assert "Short desc." in output
        assert "<CardGroup" in output
        assert "</CardGroup>" in output

    def test_multiple_cards_preserve_order(self):
        cases = [
            ("aaa", "Alpha", {"icon": "a", "summary": "First"}),
            ("bbb", "Beta", {"icon": "b", "summary": "Second"}),
        ]
        output = generate_card_section(cases)
        assert output.index("Alpha") < output.index("Beta")

    def test_empty(self):
        output = generate_card_section([])
        assert "<CardGroup" in output
        assert "</CardGroup>" in output
        assert 'href=' not in output


class TestReplaceMarkerSection:
    TEMPLATE = (
        "before\n"
        "{/* BEGIN:test-marker */}\nold content\n{/* END:test-marker */}\n"
        "after"
    )
    DUMMY_PATH = REPO_ROOT / "fake-file.mdx"

    def test_replaces_content(self):
        result = replace_marker_section(self.TEMPLATE, "test-marker", "new stuff", self.DUMMY_PATH)
        assert "new stuff" in result
        assert "old content" not in result
        assert "before" in result
        assert "after" in result

    def test_preserves_markers(self):
        result = replace_marker_section(self.TEMPLATE, "test-marker", "X", self.DUMMY_PATH)
        assert "BEGIN:test-marker" in result
        assert "END:test-marker" in result

    def test_missing_begin_marker(self):
        content = "no markers here\n{/* END:test-marker */}"
        with pytest.raises(SystemExit):
            replace_marker_section(content, "test-marker", "X", self.DUMMY_PATH)

    def test_missing_end_marker(self):
        content = "{/* BEGIN:test-marker */}\nstuff"
        with pytest.raises(SystemExit):
            replace_marker_section(content, "test-marker", "X", self.DUMMY_PATH)

    def test_missing_both_markers(self):
        with pytest.raises(SystemExit):
            replace_marker_section("nothing here", "test-marker", "X", self.DUMMY_PATH)

    def test_begin_after_end(self):
        content = "{/* END:test-marker */}\n{/* BEGIN:test-marker */}"
        with pytest.raises(SystemExit):
            replace_marker_section(content, "test-marker", "X", self.DUMMY_PATH)

    def test_marker_with_comment(self):
        content = (
            "{/* BEGIN:test-marker — auto-generated */}\nold\n"
            "{/* END:test-marker */}"
        )
        result = replace_marker_section(content, "test-marker", "new", self.DUMMY_PATH)
        assert "new" in result
        assert "old" not in result
