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

When reviewing documentation that references APIs, function signatures, class names, code examples,
or behavioral descriptions from an upstream repository, you **MUST** clone the corresponding repository
and verify the documentation against the actual source code. Do not trust that code examples or API
descriptions are accurate without checking.

**Every review comment and every approval MUST include evidence from the source code.** For each
documentation claim you verify (or flag as incorrect), provide a direct GitHub permalink to the
relevant source file and line(s). A review that simply says "looks good" without citing source
code is incomplete.

### Repositories to clone for verification

| Documentation path | Source repository | GitHub base URL |
|--------------------|-------------------|-----------------|
| `sdk/` | `OpenHands/software-agent-sdk` | `https://github.com/OpenHands/software-agent-sdk` |
| `openhands/` | `OpenHands/OpenHands` | `https://github.com/OpenHands/OpenHands` |
| CLI-related docs | `OpenHands/OpenHands-CLI` | `https://github.com/OpenHands/OpenHands-CLI` |

### Prefer upstream PR branches when linked

If the docs PR references an upstream PR or branch (for example, "SDK PR: https://github.com/OpenHands/software-agent-sdk/pull/2320"),
verify documentation against that PR's head branch instead of `main`. Treat the open PR as the source of truth for review and
**do not block** docs changes that intentionally match that branch, even if `main` differs. When in doubt, inspect the upstream
documentation sync workflow (for example, `software-agent-sdk/.github/workflows/sync-docs-code-blocks.yml`) to understand the intended
relationship between code and docs.
It's OK to approve a docs/ PR on the basis of a linked upstream PR, they will be merged in the right order.

### What to verify

- **Import paths** exist and export the documented symbols
- **Function/class signatures** match (parameter names, types, defaults, return types)
- **Field/attribute names** on data classes and models are correct
- **Supported values** (e.g., format strings like `"github:owner/repo"`) are actually handled in code
- **Behavioral descriptions** match the implementation logic
- **Prompt/context descriptions** distinguish between initial injection/construction, conversation-history inclusion, LLM context, and actual request transport. Flag ambiguous wording such as “sent with each request” unless the docs are intentionally describing transport-level behavior.
- **Example code** would actually run without errors

### How to verify

```bash
# Clone the relevant repo (use --depth=1 for speed)
git clone --depth=1 https://github.com/OpenHands/software-agent-sdk.git /tmp/agent-sdk

# If an upstream PR is referenced, use this command instead of the first one:
# Get the head branch name from the PR page or API (e.g., "feature-branch-name").
# git clone --depth=1 --branch feature-branch-name https://github.com/OpenHands/software-agent-sdk.git /tmp/agent-sdk

# Search for the documented symbols
grep -rn "function_name" /tmp/agent-sdk/
```

### Providing evidence in review comments (Required)

For **every** documentation change that describes code behavior, APIs, or implementation details,
your review MUST include a link to the corresponding source code as evidence. Use GitHub permalinks
(with commit SHA or branch) so links remain stable.

**Format for inline review comments:**

When commenting on a specific line or section of the documentation, include evidence like:

```
✅ Verified: `is_agentskills_format` field exists on the Skill class.
→ Source: https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/context.py#L42

🔴 Incorrect: The docs say `trigger=None` causes injection into `<REPO_CONTEXT>`, but the code
shows it injects into `<EXTRA_INFO>`.
→ Source: https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/agent.py#L150-L165
```

**Format for the overall review body:**

Include a "Source Verification" section that lists the key claims verified and their evidence:

```
## Source Verification

| Documentation Claim | Verified? | Source Evidence |
|---------------------|-----------|-----------------|
| Legacy skills with `trigger=None` are included in the initial system prompt and remain in LLM context for subsequent turns | ✅ | [agent.py#L150](permalink) |
| `load_skills_from_dir()` returns tuple of (skills, repo_skills) | ✅ | [context.py#L85](permalink) |
| AgentSkills format uses progressive disclosure | ❌ Incorrect | [agent.py#L200](permalink) shows... |
```

If you cannot find source code to verify a documentation claim, explicitly flag it:

```
⚠️ Unverified: Could not find source code for the claimed behavior of "X".
This should be verified before merging.
```

## Repository boundaries

Verify that documentation changes belong in this repository rather than a source repository. `OpenHands/OpenHands` owns Agent Canvas, `OpenHands/software-agent-sdk` owns the SDK/Agent Server and canonical API, `OpenHands/typescript-client` owns typed browser API access, `OpenHands/automation` owns scheduling and dispatch, and `OpenHands/extensions` owns reusable skills, plugins, automations, and integrations.

If a PR is opened in the wrong repository, explicitly recommend that it may need to be closed and moved to the repository that owns the change rather than merged here. Every PR must follow this repository's review guidance.

## Review Decisions

You **must** use the correct GitHub review `event` value when submitting your review.
Match the event to the severity of your findings:

- **`APPROVE`** — Use when the PR is good and has no blocking issues. You can still include non-blocking inline comments with an APPROVE event.
- **`REQUEST_CHANGES`** — Use when there are critical issues that must be fixed before merging (e.g., hallucinated APIs, incorrect signatures, broken examples).
- **`COMMENT`** — Use when you have feedback but are not explicitly approving or requesting changes (e.g., unverifiable claims, minor suggestions).

### When to APPROVE (`event: "APPROVE"`)
- Documentation-only style/formatting changes
- Accurate content verified against source code
- Changes that correctly sync with upstream code changes
- **Release PRs from @mamoodi**: If the PR author is @mamoodi and the changes are standard release updates (version bumps, changelog entries, etc.) with nothing suspicious, approve without requiring full source verification

### When to REQUEST_CHANGES (`event: "REQUEST_CHANGES"`)
- Hallucinated API surfaces (functions, parameters, classes that don't exist in source)
- Inaccurate signatures, return types, or field names verified against source code
- Example code that would not run or produces incorrect results
- Broken internal links or navigation entries

### When to COMMENT (`event: "COMMENT"`)
- Documentation claims that cannot be verified against source code (upstream not available)
- Minor suggestions or style nits that don't block merging
- Missing context that could mislead users but isn't critical

## General Guidelines

- Follow the conventions in `/openhands/DOC_STYLE_GUIDE.md`
- Ensure MDX frontmatter is present and well-formed
- Check that internal links use absolute doc paths (e.g., `/overview/quickstart`)
- Verify code blocks with file references use the correct sync format (see `sdk-guidelines.md`)

### SDK guide file naming convention

SDK guide files under `sdk/guides/` **must** use a category prefix:

- `llm-` for LLM-related guides (e.g., `llm-reasoning.mdx`, `llm-gpt5-preset.mdx`)
- `agent-` for Agent-related guides (e.g., `agent-custom.mdx`, `agent-settings.mdx`)
- `convo-` for Conversation-related guides (e.g., `convo-async.mdx`, `convo-persistence.mdx`)

Flag any new SDK guide that does not follow this naming convention.

## Enterprise

Apply these checks to changes under `enterprise/` and to the Enterprise tab in `docs.json`. Unless
a change states something inaccurate, these are non-blocking: use `COMMENT` with a suggested rewrite.

### Deployment positioning

- Recommend **Docker Compose for trials and proofs of concept** and **Kubernetes (Helm) for
  production**. Flag content that presents them differently.
- Enterprise docs cover self-hosted options only. Flag content that offers OpenHands Cloud as a
  deployment option.
- The VM install is a last resort. Flag new content that suggests or links to it as a deployment
  path. Existing VM install pages stay in the navigation, at the end of the Deployment section.

### Tone: inspire confidence

- State a limitation once, in plain inline text. Flag caveats that repeat across sections or pages
  (for example, a "use Kubernetes for production" reminder in the intro, a callout, and a closing
  "Next steps" section on the same page).
- Flag excessive `<Note>`, `<Warning>`, and `<Info>` blocks. Most information belongs in the body
  text. Reserve callouts for something the reader would otherwise get wrong.

### Keep instructions simple

- Prefer the shortest path that works. For the Docker Compose install, that is
  `git clone https://github.com/OpenHands/enterprise.git`, `cd enterprise`, and
  `docker compose up --wait`. Flag version lookups, file downloads, or extra flags that add steps
  without adding value.
- Point readers at the product's own flows instead of describing every click. For example, "Open
  `http://localhost:3100` and follow the onboarding flow to create your first user and configure
  your LLM provider" beats deep links to sign-up URLs or instructions to open Settings.
- Keep prerequisite lists short: name the tool or credential (Git, Docker and Docker Compose, an LLM
  API key) without explaining it.
- Verify Docker Compose and Helm claims (ports, variables, commands) against
  [`OpenHands/enterprise`](https://github.com/OpenHands/enterprise).

### Navigation

- The Enterprise tab is organized into Get Started, Deployment, Configuration, Integrations,
  Features, and Administration. New pages must go in the matching section. Flag pages added as
  long flat lists or in an unrelated section.
- Group related pages into nested groups, which Mintlify collapses by default. When a group has an
  overview page, set it as the group's `root` instead of listing it as a separate page.
- Keep sidebar labels short enough to fit on one line. When a page title is long, add a
  `sidebarTitle` to the frontmatter rather than shortening the page title (for example,
  "Running Docker in the Agent Sandbox" uses `sidebarTitle: "Docker in the Sandbox"`).
