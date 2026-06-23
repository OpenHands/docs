"""
Tests for the sync_code_blocks.py script functionality.

These tests ensure the backtick escaping logic works correctly to prevent
markdown rendering issues in documentation.
"""

import sys
from pathlib import Path

# Add the script directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / ".github" / "scripts"))

from sync_code_blocks import escape_embedded_backticks, extract_code_blocks, normalize_content


class TestEscapeEmbeddedBackticks:
    """Tests for the escape_embedded_backticks function."""

    def test_basic_triple_backticks(self):
        """Basic case: single triple backtick sequence gets escaped."""
        content = "Some code with ``` backticks"
        result = escape_embedded_backticks(content)
        # Should have zero-width spaces between backticks
        assert "```" not in result
        assert "`\u200b`\u200b`" in result

    def test_multiple_occurrences(self):
        """Multiple triple backtick sequences all get escaped."""
        content = "```python\ncode\n```\nMore ```text```"
        result = escape_embedded_backticks(content)
        # Original has 4 triple backticks: opening, closing, and two more in "```text```"
        assert result.count("`\u200b`\u200b`") == 4
        assert "```" not in result

    def test_idempotency(self):
        """Applying the function multiple times produces same result."""
        content = "Hello ``` world ``` test"
        once = escape_embedded_backticks(content)
        twice = escape_embedded_backticks(once)
        # Already escaped content should not be re-escaped
        # Since we replace "```" and the escaped version is "`​`​`" (with ZWS),
        # applying again should not find any more "```" to replace
        assert once == twice

    def test_four_backticks(self):
        """Four backticks should have three escaped and one regular."""
        content = "````"  # 4 backticks
        result = escape_embedded_backticks(content)
        # "````" -> "`​`​``" (first 3 escaped, 4th remains)
        assert "`\u200b`\u200b``" in result

    def test_five_backticks(self):
        """Five backticks: only one group of 3 is replaced, leaving 2."""
        content = "`````"  # 5 backticks
        result = escape_embedded_backticks(content)
        # str.replace() replaces non-overlapping occurrences from left to right
        # "`````" -> "`​`​`" + "``" (first 3 replaced, last 2 remain as regular backticks)
        assert result == "`\u200b`\u200b```"
        # One escaped group + 2 regular backticks remaining
        assert result.count("`\u200b`\u200b`") == 1

    def test_six_backticks(self):
        """Six backticks (two groups of three) both get escaped."""
        content = "``````"  # 6 backticks
        result = escape_embedded_backticks(content)
        # Should become two escaped groups
        assert "```" not in result
        assert result.count("`\u200b`\u200b`") == 2

    def test_empty_string(self):
        """Empty string returns empty string."""
        result = escape_embedded_backticks("")
        assert result == ""

    def test_none_like_empty(self):
        """Empty/falsy content returns as-is."""
        result = escape_embedded_backticks("")
        assert result == ""

    def test_no_backticks(self):
        """Content without triple backticks is unchanged."""
        content = "Regular code without triple backticks: ` `` `"
        result = escape_embedded_backticks(content)
        assert result == content

    def test_mixed_content(self):
        """Real-world example with markdown in Python string."""
        content = '''def example():
    """Example with markdown.
    
    ```python
    print("hello")
    ```
    """
    pass'''
        result = escape_embedded_backticks(content)
        assert "```python" not in result
        assert "`\u200b`\u200b`python" in result
        assert "```\n    \"\"\"" not in result

    def test_preserves_other_content(self):
        """Escaping preserves all other content exactly."""
        content = "Hello ``` world"
        result = escape_embedded_backticks(content)
        assert result == "Hello `\u200b`\u200b` world"


class TestExtractCodeBlocks:
    """Tests for the extract_code_blocks function."""

    def test_basic_python_block(self):
        """Extract a basic Python code block."""
        content = '''```python icon="python" expandable examples/test.py
print("hello")
```
'''
        blocks = extract_code_blocks(content)
        assert len(blocks) == 1
        assert blocks[0][0] == 'python'  # language
        assert blocks[0][1] == 'examples/test.py'  # file_ref
        assert 'print("hello")' in blocks[0][2]  # code_content

    def test_yaml_block(self):
        """Extract a YAML code block."""
        content = '''```yaml icon="yaml" examples/config.yml
key: value
```
'''
        blocks = extract_code_blocks(content)
        assert len(blocks) == 1
        assert blocks[0][0] == 'yaml'
        assert blocks[0][1] == 'examples/config.yml'

    def test_block_without_trailing_newline(self):
        """Handle code blocks without trailing newline before closing backticks."""
        content = '''```python icon="python" examples/test.py
code_without_trailing_newline```
'''
        blocks = extract_code_blocks(content)
        assert len(blocks) == 1
        assert 'code_without_trailing_newline' in blocks[0][2]

    def test_multiple_blocks(self):
        """Extract multiple code blocks."""
        content = '''```python examples/a.py
code a
```

```yaml examples/b.yaml
key: b
```
'''
        blocks = extract_code_blocks(content)
        assert len(blocks) == 2


class TestNormalizeContent:
    """Tests for the normalize_content function."""

    def test_removes_trailing_whitespace(self):
        """Trailing whitespace on lines is removed."""
        content = "line1   \nline2\t\n"
        result = normalize_content(content)
        assert result == "line1\nline2"

    def test_normalizes_line_endings(self):
        """Different line endings are normalized."""
        content = "line1\r\nline2\rline3"
        result = normalize_content(content)
        # splitlines() handles all line ending types
        lines = result.split('\n')
        assert len(lines) == 3
