# Proposal: Simplify API Documentation Generation

## Problem Statement

The current `scripts/generate-api-docs.py` is **1,268 lines** with many fragile regex-based hacks to transform Sphinx markdown output into Mintlify-compatible MDX. Every edge case in docstrings requires a new fix.

### Current Hacks (partial list)

| Issue | Lines of Code | Description |
|-------|---------------|-------------|
| `*args`/`**kwargs` | ~30 | Sphinx outputs `\n*\n` in code blocks |
| HTML escaping | ~10 | `<br/>` tags need escaping for MDX |
| Blockquote markers | ~15 | `>` interpreted as MDX blockquotes |
| Shell comments | ~70 | `# comment` in examples → markdown headers |
| Curly braces | ~20 | `{...}` → JSX expressions |
| Cross-reference links | ~150 | Manual class-to-module mapping for 100+ classes |
| Type signatures | ~30 | Full signatures in headers need simplification |
| Property formatting | ~20 | `*property* name *: Type*` patterns |
| Multi-line dictionaries | ~50 | Dictionary literals break MDX |
| Example code blocks | ~100 | `pycon` blocks need proper handling |
| Class organization | ~100 | Separate properties from methods |

### Root Cause

**sphinx-markdown-builder** was designed for generic markdown, not Mintlify MDX. It produces output that requires extensive post-processing.

---

## Proposed Solution: Direct Python-to-MDX Generation

Replace Sphinx with direct Python introspection using `inspect` and `ast` modules.

### Benefits

1. **Simpler**: ~300 lines vs 1,268 lines
2. **Predictable**: No intermediate markdown to parse
3. **Faster**: No Sphinx build step
4. **Maintainable**: Easy to add new modules
5. **Correct**: Full control over output format

### Architecture

```
┌─────────────────────┐
│   software-agent-sdk │
│   (source code)      │
└──────────┬──────────┘
           │ import + inspect
           ▼
┌─────────────────────┐
│  generate-api-docs   │
│  (Python script)     │
│                      │
│  • inspect.signature │
│  • inspect.getdoc    │
│  • ast.parse         │
└──────────┬──────────┘
           │ direct MDX generation
           ▼
┌─────────────────────┐
│   sdk/api-reference  │
│   (MDX files)        │
└─────────────────────┘
```

### Implementation Phases

#### Phase 1: agent-sdk Docstring Standards (PR to software-agent-sdk)

Add docstring linting rules to enforce consistency:

```toml
# pyproject.toml
[tool.ruff.lint]
extend-select = [
    "D",      # pydocstyle
]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

Standardize docstring format:

```python
class LLM(BaseModel):
    """Language model interface for OpenHands agents.
    
    The LLM class provides a unified interface for interacting with 
    various language models through the litellm library.
    
    Attributes:
        model: Model name (e.g., "claude-sonnet-4-20250514").
        api_key: API key for authentication.
        base_url: Custom API base URL.
    
    Example:
        ```python
        from openhands.sdk import LLM
        llm = LLM(model="claude-sonnet-4-20250514", api_key="...")
        ```
    """
```

Key requirements:
- Use fenced code blocks (` ```python `) not `>>>` REPL style
- Use `Attributes:` section for class fields
- Mark shell config examples with ` ```bash `
- Escape MDX-sensitive characters in examples

#### Phase 2: New Generator Script (PR to docs)

Replace Sphinx-based generation with direct introspection:

```python
import inspect
import importlib
from pathlib import Path

def generate_module_docs(module_name: str) -> str:
    """Generate MDX documentation for a module."""
    module = importlib.import_module(module_name)
    
    mdx = f'''---
title: {module_name}
description: API reference for {module_name}
---

'''
    
    # Get public members from __all__ or filter by name
    members = get_public_members(module)
    
    for name, obj in members:
        if inspect.isclass(obj):
            mdx += generate_class_docs(name, obj)
        elif inspect.isfunction(obj):
            mdx += generate_function_docs(name, obj)
    
    return mdx

def generate_class_docs(name: str, cls) -> str:
    """Generate docs for a class."""
    sig = inspect.signature(cls)
    doc = inspect.getdoc(cls) or ""
    
    # Parse Google-style docstring
    parsed = parse_google_docstring(doc)
    
    mdx = f'''
---

### {name}

```python
class {name}{sig}
```

{parsed.description}

'''
    
    if parsed.attributes:
        mdx += "**Attributes:**\n\n"
        for attr in parsed.attributes:
            mdx += f"- `{attr.name}`: {attr.description}\n"
    
    if parsed.example:
        mdx += f"\n**Example:**\n\n{parsed.example}\n"
    
    # Methods
    for method_name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not method_name.startswith('_') or method_name == '__init__':
            mdx += generate_method_docs(method_name, method)
    
    return mdx
```

#### Phase 3: Migration

1. Run both generators in parallel during transition
2. Compare outputs to ensure parity
3. Remove old Sphinx-based generator
4. Update CI workflow

---

## Changes Required

### software-agent-sdk

| Change | Effort | Impact |
|--------|--------|--------|
| Add ruff docstring rules | Low | Catches issues at lint time |
| Update `LLM` docstrings | Medium | Most complex class |
| Update `Agent` docstrings | Medium | Core class |
| Update other modules | Low | Follow pattern |
| Convert REPL examples to fenced blocks | Low | ~20 occurrences |

### docs

| Change | Effort | Impact |
|--------|--------|--------|
| New `generate-api-docs-v2.py` | Medium | ~300 lines |
| Update CI workflow | Low | Point to new script |
| Remove old generator | Low | Delete 1268 lines |

---

## Example: Before and After

### Before (agent-sdk docstring)

```python
def completion(self, messages, tools=None, **kwargs):
    """Generate a completion from the language model.
    
    Example:
        >>> from openhands.sdk.llm import Message, TextContent
        >>> messages = [Message(role="user", content=[TextContent(text="Hello")])]
        >>> response = llm.completion(messages)
        >>> print(response.content)
    """
```

### After (agent-sdk docstring)

```python
def completion(self, messages, tools=None, **kwargs):
    """Generate a completion from the language model.
    
    Args:
        messages: List of conversation messages.
        tools: Optional list of tools available to the model.
        **kwargs: Additional arguments passed to the LLM API.
    
    Returns:
        LLMResponse containing the model's response and metadata.
    
    Example:
        ```python
        from openhands.sdk.llm import Message, TextContent
        messages = [Message(role="user", content=[TextContent(text="Hello")])]
        response = llm.completion(messages)
        print(response.content)
        ```
    """
```

### Generated MDX Output

```mdx
#### completion()

```python
def completion(
    self,
    messages: list[Message],
    tools: Sequence[ToolDefinition] | None = None,
    **kwargs
) -> LLMResponse
```

Generate a completion from the language model.

**Arguments:**

- `messages`: List of conversation messages.
- `tools`: Optional list of tools available to the model.
- `**kwargs`: Additional arguments passed to the LLM API.

**Returns:** LLMResponse containing the model's response and metadata.

**Example:**

```python
from openhands.sdk.llm import Message, TextContent
messages = [Message(role="user", content=[TextContent(text="Hello")])]
response = llm.completion(messages)
print(response.content)
```
```

---

## Timeline

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Phase 1: Docstring standards | 1-2 days | None |
| Phase 2: New generator | 2-3 days | Phase 1 merged |
| Phase 3: Migration | 1 day | Phase 2 tested |

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Docstring updates break existing docs | Run both generators in parallel |
| Missing edge cases | Compare old vs new output |
| Complex type annotations | Use `typing.get_type_hints()` |
| Private members exposed | Filter by `__all__` or naming |

---

## Decision Required

1. **Approve approach**: Direct introspection vs. alternative Sphinx config
2. **Docstring format**: Google-style vs. NumPy-style
3. **Scope**: All modules at once vs. incremental migration
