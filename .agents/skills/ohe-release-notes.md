---
name: ohe-release-notes
description: Generate consolidated OpenHands Enterprise release notes from multiple component repos
triggers:
  - ohe-release-notes
---

# OpenHands Enterprise Release Notes Generator

Generate a consolidated release notes page for an OpenHands Enterprise release by collecting and
merging GitHub release notes from all component repositories into a single page under `enterprise/`.

## When to use

Use this skill when asked to create or update Enterprise release notes. The user provides version
ranges for four components. If any are missing, ask before proceeding.

## Required inputs

Ask the user for **all four** component version ranges and the **Enterprise release version**:

| Input | Example | Description |
|-------|---------|-------------|
| Enterprise release version | `0.24.0` | The version number for the `## X.X.X` heading |
| automations | `1.1.5 to 1.1.5` | Previous → new version (same = no changes) |
| enterprise-server | `cloud-1.40.1 to 1.46.2` | Tags in `OpenHands/OpenHands` repo |
| runtime-api | `0.3.1 to 0.50` | Tags in `OpenHands/runtime-api` repo (prefixed `v` in GitHub) |
| OpenHands-Cloud | `0.13.3 to 0.24.0` | Tags in `OpenHands/OpenHands-Cloud` repo (prefixed `openhands/`) |

**software-agent-sdk** is derived automatically — you do NOT ask the user for it. See the
"Deriving the software-agent-sdk version range" section below.

If the user omits any of the four inputs above, ask:

> To generate the Enterprise release notes I need the previous and new version for each component:
> - **automations**: previous → new
> - **enterprise-server**: previous → new (tags are `cloud-X.Y.Z` in OpenHands/OpenHands)
> - **runtime-api**: previous → new (tags are `vX.Y.Z` in OpenHands/runtime-api)
> - **OpenHands-Cloud**: previous → new (tags are `openhands/X.Y.Z` in OpenHands/OpenHands-Cloud)
> - **Enterprise release version**: the version number for the heading (e.g. `0.25.0`)

## Component repositories and tag formats

| Component | GitHub Repo | Tag format | Example tags |
|-----------|-------------|------------|--------------|
| enterprise-server | `OpenHands/OpenHands` | `cloud-X.Y.Z` | `cloud-1.41.0`, `cloud-1.46.2` |
| runtime-api | `OpenHands/runtime-api` | `vX.Y.Z` | `v0.4.0`, `v0.5.0` |
| OpenHands-Cloud | `OpenHands/OpenHands-Cloud` | `openhands/X.Y.Z` | `openhands/0.14.0`, `openhands/0.24.0` |
| software-agent-sdk | `OpenHands/software-agent-sdk` | `vX.Y.Z` | `v1.35.0`, `v1.36.0` |
| automations | *(no repo — version noted only)* | — | — |

## Step-by-step procedure

### 1. Identify releases in range

For each component repo, list all GitHub releases and identify which fall **after** the previous
version and **up to and including** the new version.

Use the GitHub API to list releases:

```bash
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/{owner}/{repo}/releases?per_page=100" \
  | python3 -c "import json,sys; [print(r['tag_name']) for r in json.load(sys.stdin)]"
```

If the "previous" tag doesn't exist as a release, use the nearest earlier tag as the boundary.

### 2. Fetch release notes

For each release in range, fetch the body:

```bash
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}" \
  | python3 -c "import json,sys; print(json.load(sys.stdin).get('body',''))"
```

### 2b. Derive the software-agent-sdk version range

The `software-agent-sdk` version is pinned in the OpenHands-Cloud Helm chart. To find the range:

1. Fetch `charts/openhands/values.yaml` from the OpenHands-Cloud repo at the **old** OpenHands-Cloud
   tag (the "previous" version) and the **new** tag.
2. In each file, find the `global:` → `agentServerImage:` → `tag:` value (e.g. `1.34.0-python`).
3. Strip the `-python` suffix to get the SDK version number (e.g. `1.34.0`).
4. The SDK release range is everything after `v{old_version}` up to and including `v{new_version}`
   in the `OpenHands/software-agent-sdk` repo.

```bash
# Fetch the tag from a specific OpenHands-Cloud version
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/OpenHands/OpenHands-Cloud/contents/charts/openhands/values.yaml?ref=openhands/{version}" \
  | python3 -c "
import json, sys, base64
data = json.load(sys.stdin)
content = base64.b64decode(data['content']).decode()
lines = content.split('\n')
in_global = False
in_agent = False
for line in lines:
    if line.startswith('global:'):
        in_global = True
    if in_global and 'agentServerImage' in line:
        in_agent = True
    if in_agent and 'tag:' in line:
        print(line.strip())
        break
"
```

### 3. Categorize by component

Group bullet points **by component section**, with each section having its own Features, Bug Fixes,
and Maintenance sub-headings. The component sections are:

1. **Enterprise Server** — from `OpenHands/OpenHands`
2. **Software Agent SDK** — from `OpenHands/software-agent-sdk`
3. **Runtime API** — from `OpenHands/runtime-api`
4. **OpenHands Cloud (Helm Chart)** — from `OpenHands/OpenHands-Cloud`

Within each section, sort items into:
- **Features** — lines starting with `* feat`
- **Bug Fixes** — lines starting with `* fix`
- **Maintenance** — lines starting with `* chore`, `* ci`, `* build`, `* refactor`, `* test`, etc.

### 4. Filter out noise

Remove these automated/housekeeping lines that don't add value to customer-facing release notes:

| Pattern | Reason |
|---------|--------|
| `chore(main): release X.X.X` | Automated release PRs |
| `chore: bump SDK packages to vX.X.X` | Automated dependency bumps |
| `chore: bump SDK and agent-server to X.X.X` | Automated dependency bumps |
| `fix(backport): ...` | Backport cherry-picks (the original fix is already listed) |
| `feat: bump agent-server to ...` | Version bump PRs, not user-facing features |
| `feat: bump image tag to ...` | Version bump PRs, not user-facing features |
| `feat(openhands): bump image tag to ...` | Version bump PRs, not user-facing features |
| `feat(runtime-api): bump image tag to ...` | Version bump PRs, not user-facing features |
| `Release vX.Y.Z` | Automated release PRs in software-agent-sdk |
| `Verify ... model` | Model verification entries in software-agent-sdk |

### 5. Write the page

Create or update `enterprise/release-notes.mdx`. Prepend the new release at the top of the file
(after the frontmatter), so the most recent release appears first.

**Page structure:**

```mdx
---
title: Release Notes
description: Release notes for OpenHands Enterprise
icon: clipboard-list
---

## X.Y.Z

### Enterprise Server

#### Features
* feat: ... by @author in https://github.com/OpenHands/OpenHands/pull/...

#### Bug Fixes
* fix: ... by @author in https://github.com/OpenHands/OpenHands/pull/...

#### Maintenance
* ci: ... by @author in https://github.com/OpenHands/OpenHands/pull/...

---

### Software Agent SDK

#### Features
* feat: ... by @author in https://github.com/OpenHands/software-agent-sdk/pull/...

#### Bug Fixes
* fix: ... by @author in https://github.com/OpenHands/software-agent-sdk/pull/...

---

### Runtime API

#### Features
* feat: ... by @author in https://github.com/OpenHands/runtime-api/pull/...

---

### OpenHands Cloud (Helm Chart)

#### Features
* feat: ... by @author in https://github.com/OpenHands/OpenHands-Cloud/pull/...

#### Bug Fixes
* fix: ... by @author in https://github.com/OpenHands/OpenHands-Cloud/pull/...

## (previous release heading, if any)
...
```

**Key formatting rules:**
- Split by component section — each component gets its own `### Heading`
- Within each component, group by `#### Features`, `#### Bug Fixes`, `#### Maintenance`
- Separate component sections with `---` horizontal rules
- Keep the exact bullet text from the original release notes (author, PR link)
- If a category has zero items after filtering, omit that sub-heading entirely
- Also filter out `Release vX.Y.Z` and `Verify ... model` lines from SDK notes

### 6. Update navigation

Ensure `enterprise/release-notes` is listed in `docs.json` under the Enterprise tab. It should
appear in the `"OpenHands Enterprise"` group. If it's already there (from a previous release),
no change is needed.

### 7. Commit

```bash
git add enterprise/release-notes.mdx docs.json
git commit -m "Add Enterprise X.Y.Z release notes"
```
