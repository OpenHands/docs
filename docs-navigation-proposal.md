# OpenHands Documentation Navigation Restructure Proposal

## Executive Summary

This document proposes a restructured navigation for OpenHands documentation that aligns with Devin.ai's documentation structure. The key changes include:

1. **Merging CLI and Web tabs** into a single "Documentation" section
2. **Creating a new "Use Cases" tab** for tutorials and examples
3. **Reorganizing content** into logical groupings similar to Devin's approach
4. **Identifying gaps** that should be filled with new pages

---

## Current Structure Comparison

### Devin.ai Documentation Tabs
| Tab | Description |
|-----|-------------|
| **Documentation** | Main product documentation (Get Started, Guidelines, Onboarding, Working with Devin, Product Guides, Integrations, Admin) |
| **Use Cases & Tutorials** | Examples, use cases, prompts, tutorials |
| **API Reference** | REST API documentation with versions |
| **Release Notes** | Product changelog |
| **Enterprise** | Enterprise-specific features |

### OpenHands Current Tabs
| Tab | Description |
|-----|-------------|
| **Overview** | Introduction, quick start, FAQs, community |
| **Web** | Cloud, Local GUI, REST API, settings, advanced config |
| **CLI** | Installation, ways to run, cloud, extensions |
| **SDK** | Python SDK documentation |

---

## Proposed New Navigation Structure

### Tab 1: Getting Started
*Mirrors Devin's "Get Started" section within Documentation*

```
Getting Started
├── Introduction
├── Quick Start
├── First Projects
├── FAQs
├── Community
└── Contributing
```

### Tab 2: Documentation
*Merged CLI + Web with unified content*

```
Documentation
├── Setup & Installation
│   ├── OpenHands Cloud                    [EXISTING: openhands/usage/cloud/openhands-cloud]
│   ├── Local Installation (CLI)           [EXISTING: openhands/usage/cli/installation]
│   ├── Local GUI Setup                    [EXISTING: openhands/usage/run-openhands/local-setup]
│   └── Configuration Options              [EXISTING: openhands/usage/advanced/configuration-options]
│
├── Running OpenHands
│   ├── Terminal (TUI)                     [EXISTING: openhands/usage/cli/terminal]
│   ├── Web Interface                      [EXISTING: openhands/usage/cli/web-interface]
│   ├── Headless Mode                      [EXISTING: openhands/usage/cli/headless]
│   ├── GUI Server                         [EXISTING: openhands/usage/cli/gui-server]
│   └── IDE Integration (ACP)
│       ├── Overview                       [EXISTING: openhands/usage/cli/ide/overview]
│       ├── VS Code                        [EXISTING: openhands/usage/cli/ide/vscode]
│       ├── JetBrains                      [EXISTING: openhands/usage/cli/ide/jetbrains]
│       ├── Zed                            [EXISTING: openhands/usage/cli/ide/zed]
│       └── Toad                           [EXISTING: openhands/usage/cli/ide/toad]
│
├── Integrations                           [Mirrors Devin's Integrations section]
│   ├── Integrations Overview              [GAP: NEW PAGE NEEDED]
│   ├── GitHub                             [EXISTING: openhands/usage/cloud/github-installation]
│   ├── GitLab                             [EXISTING: openhands/usage/cloud/gitlab-installation]
│   ├── Bitbucket                          [EXISTING: openhands/usage/cloud/bitbucket-installation]
│   ├── Slack                              [EXISTING: openhands/usage/cloud/slack-installation]
│   ├── Project Management
│   │   ├── Jira                           [EXISTING: openhands/usage/cloud/project-management/jira-integration]
│   │   └── Linear                         [EXISTING: openhands/usage/cloud/project-management/linear-integration]
│   └── MCP Servers                        [EXISTING: openhands/usage/cli/mcp-servers]
│
├── Features & Configuration
│   ├── Key Features                       [EXISTING: openhands/usage/key-features]
│   ├── Skills (Microagents)
│   │   ├── Overview                       [EXISTING: overview/skills]
│   │   ├── Repository Skills              [EXISTING: overview/skills/repo]
│   │   ├── Keyword Skills                 [EXISTING: overview/skills/keyword]
│   │   ├── Organization Skills            [EXISTING: overview/skills/org]
│   │   └── Public Skills                  [EXISTING: overview/skills/public]
│   ├── Model Context Protocol (MCP)       [EXISTING: overview/model-context-protocol]
│   ├── Repository Customization           [EXISTING: openhands/usage/customization/repository]
│   └── Critic Extension                   [EXISTING: openhands/usage/cli/critic]
│
├── Settings                               [Unified settings section]
│   ├── Application Settings               [EXISTING: openhands/usage/settings/application-settings]
│   ├── LLM Settings                       [EXISTING: openhands/usage/settings/llm-settings]
│   ├── Integrations Settings              [EXISTING: openhands/usage/settings/integrations-settings]
│   ├── Secrets Settings                   [EXISTING: openhands/usage/settings/secrets-settings]
│   ├── API Keys Settings                  [EXISTING: openhands/usage/settings/api-keys-settings]
│   └── MCP Settings                       [EXISTING: openhands/usage/settings/mcp-settings]
│
├── Advanced Configuration
│   ├── LLM Configuration
│   │   ├── Overview                       [EXISTING: openhands/usage/llms/llms]
│   │   └── Providers
│   │       ├── OpenHands LLMs             [EXISTING: openhands/usage/llms/openhands-llms]
│   │       ├── Azure                      [EXISTING: openhands/usage/llms/azure-llms]
│   │       ├── Google                     [EXISTING: openhands/usage/llms/google-llms]
│   │       ├── Groq                       [EXISTING: openhands/usage/llms/groq]
│   │       ├── Local LLMs                 [EXISTING: openhands/usage/llms/local-llms]
│   │       ├── LiteLLM Proxy              [EXISTING: openhands/usage/llms/litellm-proxy]
│   │       ├── Moonshot                   [EXISTING: openhands/usage/llms/moonshot]
│   │       ├── OpenAI                     [EXISTING: openhands/usage/llms/openai-llms]
│   │       └── OpenRouter                 [EXISTING: openhands/usage/llms/openrouter]
│   ├── Runtime Configuration
│   │   ├── Overview                       [EXISTING: openhands/usage/runtimes/overview]
│   │   └── Providers
│   │       ├── Docker                     [EXISTING: openhands/usage/runtimes/docker]
│   │       ├── Remote                     [EXISTING: openhands/usage/runtimes/remote]
│   │       ├── Local                      [EXISTING: openhands/usage/runtimes/local]
│   │       └── Third-Party
│   │           ├── Modal                  [EXISTING: openhands/usage/runtimes/modal]
│   │           ├── Daytona                [EXISTING: openhands/usage/runtimes/daytona]
│   │           ├── Runloop                [EXISTING: openhands/usage/runtimes/runloop]
│   │           └── E2B                    [EXISTING: openhands/usage/runtimes/e2b]
│   ├── Custom Sandbox                     [EXISTING: openhands/usage/advanced/custom-sandbox-guide]
│   └── Search Engine Setup                [EXISTING: openhands/usage/advanced/search-engine-setup]
│
├── Best Practices                         [Mirrors Devin's Essential Guidelines]
│   ├── Prompting Best Practices           [EXISTING: openhands/usage/tips/prompting-best-practices]
│   ├── When to Use OpenHands              [GAP: NEW PAGE NEEDED - mirrors Devin's "When to Use Devin"]
│   ├── Writing Effective Instructions     [GAP: NEW PAGE NEEDED - mirrors "Instructing Devin Effectively"]
│   └── Good vs Bad Instructions           [GAP: NEW PAGE NEEDED - mirrors Devin's examples]
│
├── Cloud Features                         [Cloud-specific features]
│   ├── Cloud UI                           [EXISTING: openhands/usage/cloud/cloud-ui]
│   ├── Cloud API                          [EXISTING: openhands/usage/cloud/cloud-api]
│   └── CLI Cloud Mode                     [EXISTING: openhands/usage/cli/cloud]
│
├── Reference
│   ├── Command Reference                  [EXISTING: openhands/usage/cli/command-reference]
│   └── Resume Conversations               [EXISTING: openhands/usage/cli/resume]
│
└── Help
    ├── Troubleshooting                    [EXISTING: openhands/usage/troubleshooting/troubleshooting]
    └── Feedback                           [EXISTING: openhands/usage/troubleshooting/feedback]
```

### Tab 3: Use Cases
*NEW TAB - Mirrors Devin's "Use Cases & Tutorials"*

```
Use Cases
├── Overview                               [GAP: NEW PAGE NEEDED]
├── Best Practices                         [GAP: NEW PAGE NEEDED]
│
├── Use Cases                              [GAP: NEW SECTION NEEDED]
│   ├── Code Migrations                    [GAP: NEW PAGE NEEDED]
│   ├── Test Coverage Improvement          [GAP: NEW PAGE NEEDED]
│   ├── Bug Fixing & Debugging             [GAP: NEW PAGE NEEDED]
│   ├── Documentation Generation           [GAP: NEW PAGE NEEDED]
│   ├── Code Refactoring                   [GAP: NEW PAGE NEEDED]
│   └── API Integration                    [GAP: NEW PAGE NEEDED]
│
├── Tutorials
│   ├── First Projects                     [EXISTING: overview/first-projects - move here]
│   ├── Building a REST API                [GAP: NEW PAGE NEEDED]
│   ├── Adding Test Coverage               [GAP: NEW PAGE NEEDED]
│   ├── Containerizing Applications        [GAP: NEW PAGE NEEDED]
│   └── Frontend Development               [GAP: NEW PAGE NEEDED]
│
└── Prompt Library                         [GAP: NEW SECTION NEEDED]
    ├── Testing & Refactoring              [GAP: NEW PAGE NEEDED]
    ├── Data & Analysis                    [GAP: NEW PAGE NEEDED]
    └── Web Development                    [GAP: NEW PAGE NEEDED]
```

### Tab 4: SDK / API Reference
*Enhanced SDK section with REST API integrated*

```
SDK / API Reference
├── Software Agent SDK                     [EXISTING: sdk/index]
├── Getting Started                        [EXISTING: sdk/getting-started]
├── FAQ                                    [EXISTING: sdk/faq]
│
├── Guides
│   ├── Hello World                        [EXISTING: sdk/guides/hello-world]
│   ├── Custom Tools                       [EXISTING: sdk/guides/custom-tools]
│   ├── MCP Integration                    [EXISTING: sdk/guides/mcp]
│   ├── Skills & Context                   [EXISTING: sdk/guides/skill]
│   ├── Plugins                            [EXISTING: sdk/guides/plugins]
│   ├── Persistence                        [EXISTING: sdk/guides/convo-persistence]
│   ├── Context Condenser                  [EXISTING: sdk/guides/context-condenser]
│   ├── Sub-Agent Delegation               [EXISTING: sdk/guides/agent-delegation]
│   ├── Iterative Refinement               [EXISTING: sdk/guides/iterative-refinement]
│   ├── Security & Action Confirmation     [EXISTING: sdk/guides/security]
│   ├── Metrics Tracking                   [EXISTING: sdk/guides/metrics]
│   ├── Observability & Tracing            [EXISTING: sdk/guides/observability]
│   ├── Secret Registry                    [EXISTING: sdk/guides/secrets]
│   ├── Hooks                              [EXISTING: sdk/guides/hooks]
│   ├── Critic                             [EXISTING: sdk/guides/critic]
│   ├── Agent Configurations
│   │   ├── Custom Agent                   [EXISTING: sdk/guides/agent-custom]
│   │   ├── Browser Use                    [EXISTING: sdk/guides/agent-browser-use]
│   │   ├── ToM Agent                      [EXISTING: sdk/guides/agent-tom-agent]
│   │   ├── Interactive Terminal           [EXISTING: sdk/guides/agent-interactive-terminal]
│   │   └── Stuck Detector                 [EXISTING: sdk/guides/agent-stuck-detector]
│   ├── Conversation Management
│   │   ├── Async Conversations            [EXISTING: sdk/guides/convo-async]
│   │   ├── Pause and Resume               [EXISTING: sdk/guides/convo-pause-and-resume]
│   │   ├── Send Message While Running     [EXISTING: sdk/guides/convo-send-message-while-running]
│   │   ├── Ask Agent                      [EXISTING: sdk/guides/convo-ask-agent]
│   │   └── Custom Visualizer              [EXISTING: sdk/guides/convo-custom-visualizer]
│   ├── LLM Configuration
│   │   ├── Registry                       [EXISTING: sdk/guides/llm-registry]
│   │   ├── Routing                        [EXISTING: sdk/guides/llm-routing]
│   │   ├── Streaming                      [EXISTING: sdk/guides/llm-streaming]
│   │   ├── Reasoning                      [EXISTING: sdk/guides/llm-reasoning]
│   │   ├── Image Input                    [EXISTING: sdk/guides/llm-image-input]
│   │   └── Error Handling                 [EXISTING: sdk/guides/llm-error-handling]
│   ├── Agent Server
│   │   ├── Overview                       [EXISTING: sdk/guides/agent-server/overview]
│   │   ├── Local Server                   [EXISTING: sdk/guides/agent-server/local-server]
│   │   ├── Docker Sandbox                 [EXISTING: sdk/guides/agent-server/docker-sandbox]
│   │   ├── Apptainer Sandbox              [EXISTING: sdk/guides/agent-server/apptainer-sandbox]
│   │   ├── API Sandbox                    [EXISTING: sdk/guides/agent-server/api-sandbox]
│   │   ├── Cloud Workspace                [EXISTING: sdk/guides/agent-server/cloud-workspace]
│   │   └── Custom Tools                   [EXISTING: sdk/guides/agent-server/custom-tools]
│   └── GitHub Workflows
│       ├── PR Review                      [EXISTING: sdk/guides/github-workflows/pr-review]
│       ├── TODO Management                [EXISTING: sdk/guides/github-workflows/todo-management]
│       └── Assign Reviews                 [EXISTING: sdk/guides/github-workflows/assign-reviews]
│
├── Architecture
│   ├── Overview                           [EXISTING: sdk/arch/overview]
│   ├── Design Principles                  [EXISTING: sdk/arch/design]
│   ├── SDK Overview                       [EXISTING: sdk/arch/sdk]
│   └── Components
│       ├── Agent                          [EXISTING: sdk/arch/agent]
│       ├── Agent Server                   [EXISTING: sdk/arch/agent-server]
│       ├── Conversation                   [EXISTING: sdk/arch/conversation]
│       ├── Tool System                    [EXISTING: sdk/arch/tool-system]
│       ├── Events                         [EXISTING: sdk/arch/events]
│       ├── Workspace                      [EXISTING: sdk/arch/workspace]
│       ├── LLM                            [EXISTING: sdk/arch/llm]
│       ├── MCP                            [EXISTING: sdk/arch/mcp]
│       ├── Skill                          [EXISTING: sdk/arch/skill]
│       ├── Condenser                      [EXISTING: sdk/arch/condenser]
│       └── Security                       [EXISTING: sdk/arch/security]
│
├── Python API Reference
│   ├── openhands.sdk.agent                [EXISTING: sdk/api-reference/openhands.sdk.agent]
│   ├── openhands.sdk.conversation         [EXISTING: sdk/api-reference/openhands.sdk.conversation]
│   ├── openhands.sdk.event                [EXISTING: sdk/api-reference/openhands.sdk.event]
│   ├── openhands.sdk.llm                  [EXISTING: sdk/api-reference/openhands.sdk.llm]
│   ├── openhands.sdk.security             [EXISTING: sdk/api-reference/openhands.sdk.security]
│   ├── openhands.sdk.tool                 [EXISTING: sdk/api-reference/openhands.sdk.tool]
│   ├── openhands.sdk.utils                [EXISTING: sdk/api-reference/openhands.sdk.utils]
│   └── openhands.sdk.workspace            [EXISTING: sdk/api-reference/openhands.sdk.workspace]
│
└── REST API                               [Moved from Web tab]
    └── OpenAPI Reference                  [EXISTING: openapi/openapi.json]
```

---

## Gap Analysis

### Devin Documentation Structure Overview

Devin's Documentation section is organized into these key areas:

| Section | Purpose |
|---------|---------|
| **Get Started** | Introduction, First Session, Tutorial Library |
| **Essential Guidelines** | When to use, Effective instructions, Good vs bad examples, SDLC integration |
| **Onboarding** | Repo setup, Indexing, VPN, Knowledge onboarding, AGENTS.md |
| **Working with Agent** | Session tools, Slash commands, Ask mode, Advanced mode |
| **Product Guides** | Knowledge, Session insights, Secrets, Playbooks, Deployments, Team management |
| **Integrations** | All platform integrations (GitHub, Slack, Jira, etc.) |
| **Admin** | Security, Billing, Common issues |

---

### 🔴 HIGH PRIORITY Gaps - Core Onboarding & Workflow

These pages are **critical** for user success and enterprise adoption:

| Missing Page | Devin Equivalent | Why It's Critical |
|--------------|------------------|-------------------|
| **Your First Session** | `/get-started/first-run` | Step-by-step guide for starting first session, understanding interface, @ mentions, slash commands. Currently only partially covered in `quickstart.mdx`. |
| **SDLC Integration** | `/essential-guidelines/sdlc-integration` | How OpenHands fits into existing dev workflows (planning → dev → test → review → deploy). **Critical for enterprise adoption.** |
| **Workspace & Session Tools** | `/work-with-devin/devin-session-tools` | Understanding IDE, Browser, Shell tools during sessions; how to take over tasks, monitor progress. **Users need this to understand the workspace.** |
| **Repository Setup Guide** | `/onboard-devin/repo-setup` | Comprehensive guide for setting up lint commands, test commands, dependencies, environment variables. Current `repository.mdx` is incomplete. |

#### Recommended New Pages (HIGH Priority)

**1. Your First Session** (`overview/your-first-session.mdx`)
```
Content:
- Understanding the OpenHands interface (Chat, Terminal, Browser, Code Editor)
- Starting your first task
- Monitoring agent progress
- Taking over from the agent
- Common first-task examples with sample prompts
- Tips for successful first sessions
```

**2. SDLC Integration** (`openhands/usage/sdlc-integration.mdx`)
```
Content:
- Overview: Where OpenHands fits in your development workflow
- Planning phase: Codebase exploration, task scoping
- Development phase: Delegating tasks, parallel execution
- Testing phase: Running tests, generating test coverage
- Code review: PR creation and automated review
- Deployment: CI/CD integration
- Best practices for team integration
```

**3. Workspace & Session Tools** (`openhands/usage/workspace-tools.mdx`)
```
Content:
- Understanding the OpenHands workspace
- Terminal/Shell usage and monitoring
- Code editor integration
- Browser tool for web testing
- Progress tracking and session timeline
- Taking over a session
- Running your own commands
- Best practices for collaboration
```

**4. Repository Setup Guide** (`openhands/usage/repo-setup.mdx` - enhance existing)
```
Content:
- Setting up test commands
- Setting up lint commands  
- Configuring environment variables
- Dependencies management
- Custom setup scripts
- Per-repo configuration
- Troubleshooting common setup issues
```

---

### 🟠 MEDIUM PRIORITY Gaps - Feature Documentation

| Missing Page | Devin Equivalent | Description |
|--------------|------------------|-------------|
| **Playbooks / Reusable Prompts** | `/product-guides/creating-playbooks` | Reusable prompt templates for repeated tasks. Valuable for power users and teams. |
| **Slash Commands** | `/work-with-devin/slash-commands` | Built-in command shortcuts (/plan, /review, /test). If OpenHands supports similar, needs documentation. |
| **Ask Mode / Q&A Mode** | `/work-with-devin/ask-devin` | Lightweight mode for exploring codebase without making changes. Different interaction paradigm. |
| **Session Insights / Analytics** | `/product-guides/session-insights` | Analytics and debugging for sessions. Helpful for troubleshooting and improvement. |
| **Index a Repository** | `/onboard-devin/index-repo` | How the agent indexes and understands a codebase. Important for understanding capabilities. |
| **Limitations & Best Fit Tasks** | (from `/get-started/devin-intro`) | Clear documentation of current limitations and what tasks work best. |

#### Recommended New Pages (MEDIUM Priority)

**5. Limitations & Best Fit Tasks** (`openhands/usage/tips/limitations.mdx`)
```
Content:
- What OpenHands excels at (list with examples)
- Current limitations (honest assessment)
- Tasks to avoid or break down
- How to scope tasks appropriately
- Task complexity guidelines
```

**6. Playbooks / Reusable Prompts** (`openhands/usage/playbooks.mdx`)
```
Content:
- What are playbooks?
- Creating effective playbooks
- Sharing playbooks with your team
- Example playbooks for common tasks
- Best practices for playbook design
```

---

### 🟡 LOWER PRIORITY Gaps - Advanced Features

| Missing Page | Devin Equivalent | Description |
|--------------|------------------|-------------|
| **Advanced Mode / Batch Sessions** | `/work-with-devin/advanced-mode` | Running multiple sessions in parallel |
| **Deployments** | `/product-guides/deployment-capabilities` | How to deploy code the agent creates |
| **PR Templates** | `/integrations/pr-templates` | Customizing PR format for agent-created PRs |
| **VPN Configuration** | `/onboard-devin/vpn` | Connecting to private networks |
| **Team Management** | `/product-guides/invite-team` | Team invitations and permissions (Cloud-specific) |
| **Security Practices** | `/admin/security` | Security practices and compliance documentation |
| **Billing & Usage** | `/admin/billing` | Pricing and usage information (Cloud-specific) |
| **Common Issues** | `/admin/common-issues` | FAQ-style troubleshooting for common problems |

---

### Pages Already Created in This PR

The following gap pages have already been created:

| Page | Status |
|------|--------|
| ✅ Integrations Overview | `openhands/usage/integrations/overview.mdx` |
| ✅ When to Use OpenHands | `openhands/usage/tips/when-to-use-openhands.mdx` |
| ✅ Writing Effective Instructions | `openhands/usage/tips/effective-instructions.mdx` |
| ✅ Good vs Bad Instructions | `openhands/usage/tips/good-vs-bad-instructions.mdx` |
| ✅ Use Cases Overview | `use-cases/overview.mdx` |
| ✅ Use Cases Best Practices | `use-cases/best-practices.mdx` |
| ✅ Code Migrations Example | `use-cases/examples/code-migrations.mdx` |
| ✅ Test Coverage Example | `use-cases/examples/test-coverage.mdx` |
| ✅ Bug Fixing Example | `use-cases/examples/bug-fixing.mdx` |
| ✅ Documentation Example | `use-cases/examples/documentation.mdx` |
| ✅ Refactoring Example | `use-cases/examples/refactoring.mdx` |
| ✅ API Integration Example | `use-cases/examples/api-integration.mdx` |
| ✅ Tutorials (5 pages) | `use-cases/tutorials/*.mdx` |
| ✅ Prompt Library (3 pages) | `use-cases/prompts/*.mdx` |

### Pages Still Needed (Prioritized)

| Priority | Page | Recommended Path |
|----------|------|------------------|
| 🔴 HIGH | Your First Session | `overview/your-first-session.mdx` |
| 🔴 HIGH | SDLC Integration | `openhands/usage/sdlc-integration.mdx` |
| 🔴 HIGH | Workspace & Session Tools | `openhands/usage/workspace-tools.mdx` |
| 🔴 HIGH | Repository Setup Guide (enhanced) | `openhands/usage/repo-setup.mdx` |
| 🟠 MEDIUM | Limitations & Best Fit Tasks | `openhands/usage/tips/limitations.mdx` |
| 🟠 MEDIUM | Playbooks / Reusable Prompts | `openhands/usage/playbooks.mdx` |
| 🟡 LOW | Security Practices | `openhands/usage/admin/security.mdx` |
| 🟡 LOW | Common Issues | `openhands/usage/admin/common-issues.mdx` |

---

## CLI/Web Merge Strategy

### Features Available in Both CLI and Web
For these features, create a single unified page with platform-specific callouts:

```markdown
<Callout type="info" title="Platform Availability">
This feature is available in both the CLI and Web interface.
</Callout>
```

**Unified Features:**
- MCP Configuration
- LLM Settings
- Secrets Management
- Repository Customization
- Headless Mode execution

### CLI-Only Features
Add callout indicating CLI exclusivity:

```markdown
<Callout type="note" title="CLI Only">
This feature is currently only available in the OpenHands CLI.
</Callout>
```

**CLI-Only Features:**
- Terminal (TUI) mode
- IDE Integration (ACP)
- Command reference
- Resume conversations
- Critic extension

### Web/Cloud-Only Features
Add callout indicating Web/Cloud exclusivity:

```markdown
<Callout type="note" title="Cloud/Web Only">
This feature is only available in OpenHands Cloud or the Local GUI.
</Callout>
```

**Web/Cloud-Only Features:**
- Cloud UI interface
- Cloud API
- Slack integration
- Project management integrations (Jira, Linear)
- GitHub/GitLab/Bitbucket deep integrations

---

## Proposed docs.json Configuration

See the `docs-navigation-new.json` file for the complete Mintlify configuration.

---

## Implementation Notes

### Phase 1: Restructure Navigation
1. Update `docs.json` with new tab structure
2. Move existing pages to new locations (using redirects)
3. Add platform availability callouts to merged pages

### Phase 2: Fill High-Priority Gaps
1. Create Integrations Overview page
2. Create "When to Use OpenHands" page
3. Create "Writing Effective Instructions" page
4. Create "Good vs Bad Instructions" page
5. Create Use Cases Overview page

### Phase 3: Add Use Cases Content
1. Create tutorial content based on existing "First Projects"
2. Add code migration examples
3. Add test coverage tutorial
4. Create prompt library section

### Phase 4: Polish and Redirects
1. Set up redirects for moved pages
2. Update internal links
3. Test navigation flow
