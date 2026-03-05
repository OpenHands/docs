---
name: code-review
description: Code review guidelines for the OpenHands documentation repository
triggers:
  - /codereview
---

# Documentation Repository Code Review Guidelines

You are reviewing changes to the OpenHands documentation site (Mintlify). This repository documents
multiple source-of-truth codebases. Accuracy is critical.

## Source Code Verification (Required for SDK/CLI/App docs)

When reviewing documentation that references APIs, function signatures, class names, or code examples
from an upstream repository, you **MUST** clone the corresponding repository and verify the documentation
against the actual source code. Do not trust that code examples or API descriptions are accurate without
checking.

### Repositories to clone for verification

| Documentation path | Source repository |
|--------------------|-------------------|
| `sdk/` | `OpenHands/software-agent-sdk` |
| `openhands/` | `OpenHands/OpenHands` |
| CLI-related docs | `OpenHands/OpenHands-CLI` |

### What to verify

- **Import paths** exist and export the documented symbols
- **Function/class signatures** match (parameter names, types, defaults, return types)
- **Field/attribute names** on data classes and models are correct
- **Supported values** (e.g., format strings like `"github:owner/repo"`) are actually handled in code
- **Behavioral descriptions** match the implementation logic
- **Example code** would actually run without errors

### How to verify

```bash
# Clone the relevant repo (use --depth=1 for speed)
git clone --depth=1 https://github.com/OpenHands/software-agent-sdk.git /tmp/agent-sdk

# Search for the documented symbols
grep -rn "function_name" /tmp/agent-sdk/
```

## Review Decisions

### When to APPROVE
- Documentation-only style/formatting changes
- Accurate content verified against source code
- Changes that correctly sync with upstream code changes

### When to COMMENT
- Documentation claims that cannot be verified against source code
- Potentially hallucinated API surfaces (functions, parameters, classes that don't exist)
- Inaccurate signatures, return types, or field names
- Missing context that could mislead users

## General Guidelines

- Follow the conventions in `/openhands/DOC_STYLE_GUIDE.md`
- Ensure MDX frontmatter is present and well-formed
- Check that internal links use absolute doc paths (e.g., `/overview/quickstart`)
- Verify code blocks with file references use the correct sync format (see `sdk-guidelines.md`)
