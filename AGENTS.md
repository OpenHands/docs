# OpenHands Docs Repository (Mintlify)

This repo hosts the **unified documentation site** for the OpenHands ecosystem:

- **OpenHands Agent SDK** (SDK + REST API)
- **OpenHands CLI**
- **OpenHands Web/App** (GUI + Cloud + REST API)

The site is built with **Mintlify** and deployed automatically by Mintlify on pushes to `main`.

## Quick orientation

### Key files/directories

- `docs.json` — Mintlify site configuration (nav tabs, redirects, OpenAPI integration)
- `overview/` — high-level docs (intro, quickstart, community, skills overview)
- `openhands/usage/` — product docs for Web/Cloud/CLI/etc.
- `sdk/` — Agent SDK docs (guides, architecture, API reference pages)
- `openapi/` — OpenAPI specs consumed by Mintlify
  - `openapi/openapi.json` — OpenHands REST API schema
  - `openapi/agent-sdk.json` — Agent SDK agent-server schema (synced from `software-agent-sdk`)
- `scripts/` — automation for generating SDK API reference docs
- `.github/workflows/` — CI workflows (broken link checks, sync jobs)
- `.github/scripts/` — helper scripts used by CI
- `.agents/skills/` — prompt extensions for agents editing this repo (legacy: `.openhands/skills/`; formerly `microagents`)
- `tests/` — pytest checks for docs consistency (notably LLM pricing docs)


## llms.txt / llms-full.txt (V1-only)

Mintlify auto-generates `/llms.txt` and `/llms-full.txt`, but this repo **overrides** them by committing
`llms.txt` and `llms-full.txt` at the repo root.

We do this so LLMs get **V1-only** context while legacy V0 pages remain available for humans.

- Generator script: `scripts/generate-llms-files.py`
- Regenerate:
  ```bash
  ./scripts/generate-llms-files.py
  ```
- Exclusions: `openhands/usage/v0/` and any `V0*`-prefixed page files.

## Local development

### Preview the site

Mintlify uses the `mint` CLI.

```bash
npm install -g mintlify@latest
mint dev
```

Useful checks:

```bash
mint broken-links
```

### Python tooling (sync/generation scripts)

This repo includes Python scripts that generate or validate parts of the docs.

This repo isn’t a Python package (no `pyproject.toml`), so for one-off runs we prefer **`uv`** to create an ephemeral environment:

```bash
# Generate SDK API reference docs
uv run --with sphinx --with sphinx-markdown-builder --with myst-parser \
  python scripts/generate-api-docs.py

# Run pytest-based checks (only this repo's tests)
uv run --with pytest --with requests pytest -q tests/
```

(You can still use `pip install ...` if you prefer a long-lived local environment.)

## Cross-repo sync automation (important)

A lot of SDK documentation is **derived from** or **kept in sync with** `OpenHands/software-agent-sdk`.

### 1) Syncing code blocks from `software-agent-sdk/examples/*`

Script: `.github/scripts/sync_code_blocks.py`

- Scans all `.mdx` files for code blocks that include a file reference (Python and YAML supported).
- Replaces the block content with the content from the referenced file in a checked-out `agent-sdk/` folder.

Expected code block format (examples):

````mdx
```python icon="python" expandable examples/01_standalone_sdk/02_custom_tools.py
# content is auto-synced
```

```yaml icon="yaml" expandable examples/03_github_workflows/02_pr_review/workflow.yml
# content is auto-synced
```
````

Local run:

```bash
git clone https://github.com/OpenHands/software-agent-sdk.git agent-sdk
python .github/scripts/sync_code_blocks.py
rm -rf agent-sdk
```

CI: `.github/workflows/sync-docs-code-blocks.yml`

### 2) Generating SDK API reference pages

Script: `scripts/generate-api-docs.py`

- Uses **Sphinx** + `sphinx-markdown-builder` to generate Mintlify-friendly `.mdx` pages under `sdk/api-reference/`.

Local run:

```bash
uv run --with sphinx --with sphinx-markdown-builder --with myst-parser \
  python scripts/generate-api-docs.py
```

CI: also run by `.github/workflows/sync-docs-code-blocks.yml`

### 3) Syncing agent-sdk OpenAPI schema

Workflow: `.github/workflows/sync-agent-sdk-openapi.yml`

- Checks out `OpenHands/software-agent-sdk`
- Runs the agent-server OpenAPI generator
- Updates `openapi/agent-sdk.json` via an automated PR

## Docs writing conventions

- Most pages are `.mdx` with frontmatter:
  ```yaml
  ---
  title: ...
  description: ...
  ---
  ```
- Follow the style rules in `openhands/DOC_STYLE_GUIDE.md`.
- Use Mintlify components (`<Note>`, `<Warning>`, `<Tabs>`, etc.) where appropriate.
- When linking internally, prefer **absolute** doc paths (e.g. `/overview/quickstart`).

## LLM API Key Options

The SDK documentation maintains three ways for users to obtain LLM access:

1. **Direct Provider** - Bring your own API key from providers like Anthropic, OpenAI, etc.
2. **OpenHands Cloud** - Use OpenHands Cloud API keys (recommended for verified models)
3. **Third-party Subscription Login** - Authenticate with existing subscriptions (e.g., ChatGPT Plus/Pro via `LLM.subscription_login()`)

When documenting LLM setup or examples, ensure all three options are mentioned where appropriate:
- `sdk/getting-started.mdx` - Main getting started page with AccordionGroup
- `sdk/shared-snippets/how-to-run-example.mdx` - Shared snippet for running examples
- `sdk/guides/llm-subscriptions.mdx` - Dedicated guide for subscription login

## Validation

### LLM pricing table validation

There are *two* layers of protection for `openhands/usage/llms/openhands-llms.mdx`:

- CI workflow: `.github/workflows/validate-llm-pricing.yml` runs `.github/scripts/validate_llm_pricing.py`
- Local tests: `pytest -q` (see `tests/test_pricing_documentation.py`)

Run locally:

```bash
uv run --with pytest --with requests pytest -q tests/
```

## Related repos (source-of-truth)

- OpenHands Agent SDK: https://github.com/OpenHands/software-agent-sdk
- OpenHands CLI: https://github.com/OpenHands/OpenHands-CLI
- OpenHands (Web/App): https://github.com/OpenHands/OpenHands

When updating SDK features or examples, expect to update this repo too (especially under `sdk/`).
