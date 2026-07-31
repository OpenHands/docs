---
name: ohe-release-notes
description: Generate consolidated OpenHands Enterprise release notes from multiple component repos
triggers:
  - /ohe-release-notes
---

# OpenHands Enterprise Release Notes Generator

Generate a consolidated release notes page for an OpenHands Enterprise release by collecting and
merging GitHub release notes from all component repositories into a single page under `enterprise/`.

## Prerequisite: REPLICATED_API_KEY

This skill derives **all** component versions automatically from the Replicated Vendor API, so it
requires a `REPLICATED_API_KEY` environment variable with (at least) read access.

**Before doing anything else, verify the key exists and works:**

```bash
if [ -z "$REPLICATED_API_KEY" ]; then
  echo "MISSING"
else
  curl -s -o /dev/null -w "%{http_code}\n" \
    -H "Authorization: $REPLICATED_API_KEY" \
    "https://api.replicated.com/vendor/v3/apps"
fi
```

If the variable is missing (prints `MISSING`) or the request does not return `200`, **stop and ask
the user to add it** before proceeding:

> This skill needs a `REPLICATED_API_KEY` (read access is enough) to look up the component versions
> for each Enterprise release. Please add it as a secret and let me know when it's ready.

## When to use

Use this skill when asked to create or update Enterprise release notes. You derive every component
version yourself from Replicated.

## What you need to determine

The only thing you truly need is **which two Enterprise releases to diff**: the `previous` release
(already documented, usually the top `## X.Y.Z` heading in `enterprise/release-notes.mdx`) and the
`new` release (the target you're documenting). Everything else — the four component version ranges
plus the derived software-agent-sdk range — is derived from the Replicated release charts.

By default:
- **new** = the latest release on the Replicated `Stable` channel
- **previous** = the most recent release already documented at the top of `enterprise/release-notes.mdx`

## Step-by-step procedure

### 1. Derive component versions from Replicated

Each Replicated channel release bundles a set of Helm charts whose pinned image tags give you every
component version. The Enterprise release version itself equals the `openhands` chart version (which
is also the OpenHands-Cloud release version).

#### 1a. Find the app, channel, and the two release sequences

```bash
# App id + default channel id (Stable)
curl -s -H "Authorization: $REPLICATED_API_KEY" \
  "https://api.replicated.com/vendor/v3/apps" \
  | python3 -c "
import json,sys
for a in json.load(sys.stdin)['apps']:
    if a['slug']=='openhands':
        print('app', a['id'])
        for c in a['channels']:
            if c.get('isDefault'):
                print('channel', c['id'], '| current', c.get('currentVersion'))
"
```

```bash
# List releases on the channel to find the sequence numbers for the two versions
curl -s -H "Authorization: $REPLICATED_API_KEY" \
  "https://api.replicated.com/vendor/v3/app/{APP_ID}/channel/{CHANNEL_ID}/releases?pageSize=50" \
  | python3 -c "
import json,sys
for r in json.load(sys.stdin)['releases']:
    print(r.get('semver'), '| seq', r.get('sequence'), '| created', r.get('created'))
"
```

The Enterprise release version is the `semver` of the **new** release (e.g. `0.36.0`).

#### 1b. Read the pinned component versions from the OpenHands-Cloud chart

The `openhands` chart version equals the Enterprise release version and lives in the
`OpenHands/OpenHands-Cloud` repo under the tag `openhands/{version}`. Read the pinned tags at both
the **previous** and **new** versions to get each component's version range.

| Component                         | Where the tag is pinned (in `OpenHands/OpenHands-Cloud` at `openhands/{version}`)                                     | Notes                                   |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| **OpenHands-Cloud** (Helm chart)  | the release version itself (`charts/openhands/Chart.yaml` → `version`)                                                | equals the Enterprise release version   |
| **Enterprise Server**             | `charts/openhands/values.yaml` → top-level `image:` → `repository: ghcr.io/openhands/enterprise-server`, `tag:`       | see prefix note below                   |
| **Software Agent SDK**            | `charts/openhands/charts/runtime-api/values.yaml` → `repository: ghcr.io/openhands/agent-server`, `tag: X.Y.Z-python` | strip the `-python` suffix              |
| **Runtime API**                   | `charts/openhands/charts/runtime-api/values.yaml` → top-of-file `tag:` (the runtime-api image)                        | tags are `vX.Y.Z` in GitHub             |
| **Automation**                    | `charts/openhands/charts/automation/values.yaml` → top-of-file `tag:`                                                 | tags are plain `X.Y.Z` in GitHub        |

Fetch any of these files with the GitHub contents API:

```bash
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/OpenHands/OpenHands-Cloud/contents/{path}?ref=openhands/{version}" \
  | python3 -c "import json,sys,base64; print(base64.b64decode(json.load(sys.stdin)['content']).decode())"
```

Do this for both the **previous** and **new** Enterprise versions to build the range for each
component (previous → new).

#### 1c. Inform the user of the version jumps

You don't need the user to confirm before proceeding — just **inform** them of the derived version
jumps (previous → new for all five components) so they can double-check if they want to. Present the
table and continue generating the page. Example:

| Component | Previous | New |
|---|---|---|
| OpenHands-Cloud (Helm chart) | 0.28.0 | 0.36.0 |
| Enterprise Server | 1.47.1 | 1.49.0 |
| Software Agent SDK | 1.36.0 | 1.39.1 |
| Runtime API | 0.5.2 | 0.7.0 |
| Automation | 1.1.5 | 1.5.0 |

### 2. Identify GitHub releases in range

For each component repo, list all GitHub releases and identify which fall **after** the previous
version and **up to and including** the new version.

| Component           | Repo                           | GitHub tag format              |
|---------------------|--------------------------------|--------------------------------|
| Enterprise Server   | `OpenHands/enterprise`         | `X.Y.Z` (legacy `cloud-X.Y.Z`) |
| Software Agent SDK  | `OpenHands/software-agent-sdk` | `vX.Y.Z`                       |
| Runtime API         | `OpenHands/runtime-api`        | `vX.Y.Z`                       |
| Automation          | `OpenHands/automation`         | `X.Y.Z`                        |
| OpenHands-Cloud     | `OpenHands/OpenHands-Cloud`    | `openhands/X.Y.Z`              |

```bash
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/{owner}/{repo}/releases?per_page=100" \
  | python3 -c "import json,sys; [print(r['tag_name']) for r in json.load(sys.stdin)]"
```

### 3. Fetch release notes

For each release in range, fetch the body:

```bash
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}" \
  | python3 -c "import json,sys; print(json.load(sys.stdin).get('body',''))"
```

### 4. Categorize by component

Group bullet points **by component section**, with each section having its own Features, Bug Fixes,
and Maintenance sub-headings. The component sections are:

1. **Enterprise Server** — from `OpenHands/enterprise` (legacy: `OpenHands/OpenHands`)
2. **Software Agent SDK** — from `OpenHands/software-agent-sdk`
3. **Runtime API** — from `OpenHands/runtime-api`
4. **Automation** — from `OpenHands/automation`
5. **OpenHands Cloud (Helm Chart)** — from `OpenHands/OpenHands-Cloud`

Within each section, sort items into:
- **Features** — lines starting with `* feat`
- **Bug Fixes** — lines starting with `* fix`
- **Maintenance** — lines starting with `* chore`, `* ci`, `* build`, `* refactor`, `* test`, etc.

### 5. Filter out noise

Remove these automated/housekeeping lines that don't add value to customer-facing release notes:

| Pattern                                     | Reason                                                     |
|---------------------------------------------|------------------------------------------------------------|
| `chore(main): release X.X.X`                | Automated release PRs                                      |
| `chore: bump SDK packages to vX.X.X`        | Automated dependency bumps                                 |
| `chore: bump SDK and agent-server to X.X.X` | Automated dependency bumps                                 |
| `fix(backport): ...`                        | Backport cherry-picks (the original fix is already listed) |
| `feat: bump agent-server to ...`            | Version bump PRs, not user-facing features                 |
| `feat: bump image tag to ...`               | Version bump PRs, not user-facing features                 |
| `feat(openhands): bump image tag to ...`    | Version bump PRs, not user-facing features                 |
| `feat(runtime-api): bump image tag to ...`  | Version bump PRs, not user-facing features                 |
| `Release vX.Y.Z`                            | Automated release PRs in software-agent-sdk                |
| `Verify ... model`                          | Model verification entries in software-agent-sdk           |

### 6. Write the page

Create or update `enterprise/release-notes.mdx`. Prepend the new release at the top of the file
(after the frontmatter), so the most recent release appears first.

**Always write a short summary paragraph immediately under the `## X.Y.Z` heading**, before the
first `### Component` section. Read all of the changelog entries for the release and summarize what
the release encompasses. Keep it high-level and short (usually a single paragraph) — only call out
things genuinely worth highlighting like notable features, and don't enumerate individual fixes or
config flags. If the release contains only bug fixes and maintenance, just say something like
"This release was focused on stability and maintenance fixes."

**Page structure:**

```mdx
---
title: Release Notes
description: Release notes for OpenHands Enterprise
icon: clipboard-list
---

## X.Y.Z

<One or two short paragraphs summarizing what the release encompasses. Call out notable features;
if it's only bug fixes, say something like "This release was focused on stability and maintenance fixes.">

### Enterprise Server

#### Features
* feat: ... by @author in https://github.com/OpenHands/enterprise/pull/...

#### Bug Fixes
* fix: ... by @author in https://github.com/OpenHands/enterprise/pull/...

#### Maintenance
* ci: ... by @author in https://github.com/OpenHands/enterprise/pull/...

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

### Automation

#### Features
* feat: ... by @author in https://github.com/OpenHands/automation/pull/...

#### Bug Fixes
* fix: ... by @author in https://github.com/OpenHands/automation/pull/...

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
- Start each release with a short summary paragraph under the `## X.Y.Z` heading (see above)
- Split by component section — each component gets its own `### Heading`
- Within each component, group by `#### Features`, `#### Bug Fixes`, `#### Maintenance`
- Separate component sections with `---` horizontal rules
- Keep the exact bullet text from the original release notes (author, PR link)
- If a category has zero items after filtering, omit that sub-heading entirely

### 7. Update navigation

Ensure `enterprise/release-notes` is listed in `docs.json` under the Enterprise tab. It should
appear in the `"OpenHands Enterprise"` group. If it's already there (from a previous release),
no change is needed.

### 8. Commit

```bash
git add enterprise/release-notes.mdx docs.json
git commit -m "Add Enterprise X.Y.Z release notes"
```
