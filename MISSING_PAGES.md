# Missing Documentation Pages

This document lists all documentation pages that are referenced in the docs but do not yet exist. These links are currently broken and need content to be created.

## SDK Architecture Pages

The following `/sdk/arch/` pages are referenced but don't exist:

### 1. `/sdk/arch/sdk-package` 
**Referenced in:**
- `sdk/guides/custom-tools.mdx` (line ~30): "SDK Package Architecture - Tool System" section
- `sdk/guides/custom-tools.mdx` (line ~310): "Next Steps" section

**Expected content:** Deep dive into the SDK package structure including:
- Tool system architecture and design principles
- Typed capabilities
- Other SDK components

### 2. `/sdk/arch/tools-package`
**Referenced in:**
- `sdk/guides/custom-tools.mdx` (line ~20): Introduction section
- `sdk/guides/custom-tools.mdx` (line ~310): "Next Steps" section  
- `sdk/guides/hello-world.mdx` (line ~69): Tools explanation

**Expected content:** Built-in tools design philosophy and complete list of available tools

### 3. `/sdk/arch/agent-server-package`
**Referenced in:**
- `sdk/guides/agent-server/overview.mdx` (line ~154): "For architectural details" section

**Expected content:** Remote execution architecture and deployment details

### 4. `/sdk/arch/workspace-package`
**Referenced in:**
- `sdk/guides/agent-server/overview.mdx` (line ~155): "For architectural details" section
- `sdk/getting-started.mdx` (line ~52): "Explore Documentation" section

**Expected content:** Execution environments and isolation architecture

### 5. `/sdk/arch/sdk/overview`
**Referenced in:**
- `sdk/getting-started.mdx` (line ~50): "Explore Documentation" section

**Expected content:** Deep dive into SDK components

### 6. `/sdk/arch/tools/overview`
**Referenced in:**
- `sdk/getting-started.mdx` (line ~51): "Explore Documentation" section

**Expected content:** Overview of available tools

### 7. `/sdk/arch/overview`
**Referenced in:**
- `sdk/index.mdx` (line ~75): "Core Concepts" card

**Expected content:** General architecture overview covering agents, tools, workspaces, and more

## API Reference Pages

The following API reference pages are referenced but may not exist in the expected format:

### 1. `/sdk/guides/agent-server/api-reference/vscode/get-vscode-url`
**Referenced in:**
- `sdk/guides/agent-server/api-sandbox.mdx` (line ~97)
- `sdk/guides/agent-server/docker-sandbox.mdx` (line ~82)

**Status:** The OpenAPI spec at `openapi/agent-sdk.json` contains the `/vscode/url` endpoint, but the generated API reference path structure may not match the expected format.

### 2. `/sdk/guides/agent-server/api-reference/desktop/get-desktop-url`  
**Referenced in:**
- `sdk/guides/agent-server/api-sandbox.mdx` (line ~98)
- `sdk/guides/agent-server/docker-sandbox.mdx` (line ~83)

**Status:** The OpenAPI spec at `openapi/agent-sdk.json` contains the `/desktop/url` endpoint, but the generated API reference path structure may not match the expected format.

## Other Missing Pages

### 1. `/sdk/llms/configuration`
**Referenced in:**
- `openhands/usage/llms/llms.mdx`

**Expected content:** SDK-specific LLM configuration guide

### 2. `/sdk/guides/github-workflows/routine-maintenance`
**Referenced in:**
- `sdk/index.mdx` (line ~104): "GitHub Workflows" card

**Expected content:** Guide for using agents in GitHub workflows for routine maintenance tasks

## Summary

**Total missing pages:** 7 architecture pages + 2 API reference path issues + 2 guide pages

**Priority:**
1. High: Core architecture pages (`/sdk/arch/overview`, `/sdk/arch/tools-package`, `/sdk/arch/sdk-package`)
2. Medium: Package-specific architecture (`/sdk/arch/agent-server-package`, `/sdk/arch/workspace-package`)
3. Medium: Fix API reference path generation or update links to match actual generated paths
4. Medium: Guide pages (`/sdk/llms/configuration`, `/sdk/guides/github-workflows/routine-maintenance`)
5. Low: Alternative overview pages (`/sdk/arch/sdk/overview`, `/sdk/arch/tools/overview`)

**Note:** Path fixes made in this PR:
- `docker-sandboxed-server` → `docker-sandbox`
- `local-agent-server` → `local-server`
- `api-sandboxed-server` → `api-sandbox`
- `remote-agent-server/local-agent-server` → `agent-server/local-server`
