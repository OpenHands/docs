# OpenHands SDK Documentation - Quick Reference

## 📁 Documentation Structure

```
docs/sdk/
│
├── 📘 index.mdx                    # Start here! Main entry point
│   ├── Why OpenHands SDK          ├─ Benefits & use cases
│   ├── Hello World Example        ├─ Quick start code
│   ├── Documentation Structure    ├─ Complete navigation
│   ├── Quick Start Paths          ├─ Role-based learning
│   └── Key Concepts              └─ Core principles
│
├── 📐 architecture.mdx             # System architecture
│   ├── High-Level Architecture   ├─ 5 main components
│   ├── Component Diagrams        ├─ 6 Mermaid diagrams
│   ├── Design Principles         ├─ Event sourcing, immutability
│   ├── Event Flow               ├─ Action-observation loop
│   └── Key Benefits             └─ 5 benefit categories
│
├── 🔧 core/
│   │
│   ├── overview.mdx               # Core components overview
│   │   ├── Component Interaction ├─ How components work together
│   │   ├── 5 Core Components    ├─ Detailed descriptions
│   │   ├── Event Flow           ├─ Sequence diagrams
│   │   ├── State Management     ├─ Event log visualization
│   │   └── Configuration        └─ Immutable config pattern
│   │
│   ├── state.mdx                  # ConversationState deep dive
│   │   ├── Event Sourcing       ├─ vs traditional state
│   │   ├── Event Hierarchy      ├─ 3-level structure
│   │   ├── State API            ├─ Create, persist, load
│   │   ├── Derived Properties   ├─ Status, history, metrics
│   │   ├── Event Replay         ├─ Time-travel debugging
│   │   ├── Reproducibility      ├─ Same events = same state
│   │   └── Pause/Resume         └─ Natural support
│   │
│   └── agent.mdx                  # Agent design & patterns
│       ├── Stateless Design     ├─ vs stateful comparison
│       ├── Core step() Method   ├─ Pure function
│       ├── Agent Configuration  ├─ Immutable config
│       ├── Default Agent        ├─ Production-ready
│       ├── Custom Agents        ├─ Planning, Chain-of-Thought
│       ├── Agent Delegation     ├─ Sub-agents & hierarchies
│       ├── Pause/Resume         ├─ Mechanism explained
│       ├── Observability        ├─ Callbacks & monitoring
│       └── Testing              └─ Easy unit testing
│
└── 🚀 advanced/
    │
    └── overview.mdx               # Advanced features & production
        ├── Context Management    ├─ Condensation, files, microagents
        ├── Workflow Features     ├─ TODO, titles, stuck detection
        ├── Security Features     ├─ Analyzer, policies, secrets
        ├── Production Deploy     ├─ Server, sandboxing, workspace
        └── Performance          └─ Metrics & optimization
```

## 🎯 Find What You Need

### "How do I get started?"
→ **[index.mdx](/sdk/index.mdx)** - Hello World example

### "How does the system work?"
→ **[architecture.mdx](/sdk/architecture.mdx)** - High-level overview with diagrams

### "What are the main components?"
→ **[core/overview.mdx](/sdk/core/overview.mdx)** - Component breakdown

### "How does event sourcing work?"
→ **[core/state.mdx](/sdk/core/state.mdx)** - Event-sourced state explained

### "How do I build a custom agent?"
→ **[core/agent.mdx](/sdk/core/agent.mdx)** - Agent patterns & examples

### "How do I reduce token costs?"
→ **[advanced/overview.mdx](/sdk/advanced/overview.mdx)** - Context condensation

### "How do I deploy to production?"
→ **[advanced/overview.mdx](/sdk/advanced/overview.mdx)** - Production features

### "How do I secure my agent?"
→ **[advanced/overview.mdx](/sdk/advanced/overview.mdx)** - Security section

## 📊 Content by Numbers

| Metric | Count |
|--------|-------|
| Documentation Pages | 6 |
| Mermaid Diagrams | 24 |
| Code Examples | 45+ |
| Total Lines | ~2,800 |

## 🎨 Diagram Directory

### Architecture (8 diagrams)
1. **High-Level System** - architecture.mdx
2. **Component Interaction** - core/overview.mdx
3. **Event Flow** - architecture.mdx
4. **5 Core Components** - architecture.mdx
5. **Event Store** - core/state.mdx
6. **State Derivation** - core/overview.mdx
7. **Agent Flow** - core/agent.mdx
8. **Production Server** - advanced/overview.mdx

### Event System (5 diagrams)
1. **Event Sourcing vs Traditional** - core/state.mdx
2. **Event Hierarchy** - core/state.mdx
3. **Event Store (Memory + Disk)** - core/state.mdx
4. **Status Transitions** - core/state.mdx
5. **Event Flow Sequence** - core/overview.mdx

### Agent Patterns (4 diagrams)
1. **Stateless vs Stateful** - core/agent.mdx
2. **Execution Flow** - core/agent.mdx
3. **Agent Delegation** - core/agent.mdx
4. **Agent Lifecycle** - core/agent.mdx

### Security (3 diagrams)
1. **Security Analyzer (Two-Tier)** - advanced/overview.mdx
2. **Risk Assessment** - architecture.mdx
3. **Confirmation Flow** - advanced/overview.mdx

### Production (4 diagrams)
1. **Production Server Architecture** - advanced/overview.mdx
2. **Container Sandboxing** - advanced/overview.mdx
3. **Interactive Workspace** - advanced/overview.mdx
4. **Client-Server Flow** - advanced/overview.mdx

## 🗺️ Learning Paths

### Path 1: Beginner (30 min)
```
index.mdx
  ↓
Hello World Example
  ↓
Run examples/01_hello_world.py
```

### Path 2: Developer (2 hours)
```
index.mdx
  ↓
architecture.mdx (overview)
  ↓
core/overview.mdx (components)
  ↓
core/state.mdx (events)
  ↓
core/agent.mdx (agents)
```

### Path 3: Advanced (4 hours)
```
Path 2 (above)
  ↓
advanced/overview.mdx (features)
  ↓
Implement custom agent
  ↓
Add custom tools
```

### Path 4: Production (1 day)
```
Path 2 (above)
  ↓
advanced/overview.mdx (security)
  ↓
advanced/overview.mdx (production)
  ↓
Deploy & monitor
```

## 🔑 Key Concepts Location

| Concept | Primary Location | Also See |
|---------|-----------------|----------|
| **Event Sourcing** | core/state.mdx | architecture.mdx |
| **Stateless Agents** | core/agent.mdx | architecture.mdx |
| **Immutability** | core/overview.mdx | core/agent.mdx |
| **LLM Abstraction** | architecture.mdx | core/overview.mdx |
| **Tool System** | architecture.mdx | core/overview.mdx |
| **Context Condensation** | advanced/overview.mdx | - |
| **Security** | advanced/overview.mdx | architecture.mdx |
| **Production** | advanced/overview.mdx | - |
| **Pause/Resume** | core/agent.mdx | core/state.mdx |
| **Sub-agents** | core/agent.mdx | - |

## 📝 Code Example Locations

### Hello World
- **Location**: index.mdx
- **Lines**: 18-43
- **Topics**: Basic setup, LLM config, agent creation

### Event Sourcing
- **Location**: core/state.mdx
- **Examples**: 
  - Creating state
  - Appending events
  - Loading from disk
  - Event replay

### Custom Agents
- **Location**: core/agent.mdx
- **Examples**:
  - PlanningAgent
  - ChainOfThoughtAgent
  - OrchestratorAgent (delegation)

### Context Management
- **Location**: advanced/overview.mdx
- **Examples**:
  - Auto condensation setup
  - Context files (repo.md)
  - Keyword-triggered microagents

### Security
- **Location**: advanced/overview.mdx
- **Examples**:
  - LLM security analyzer
  - Custom confirmation policies
  - Secrets management

### Production
- **Location**: advanced/overview.mdx
- **Examples**:
  - Server setup
  - Client usage (REST + WebSocket)
  - Container configuration

## 🎓 By User Role

### Researcher
**Focus**: Custom agents, reasoning patterns

**Start Here**:
1. index.mdx (Hello World)
2. architecture.mdx (Design principles)
3. core/agent.mdx (Custom agents)
4. advanced/overview.mdx (Advanced features)

**Key Topics**:
- Event replay for analysis
- Custom agent patterns
- LLM routing for A/B testing
- Microagents for prompt engineering

### Production Engineer
**Focus**: Deployment, security, reliability

**Start Here**:
1. index.mdx (Hello World)
2. advanced/overview.mdx (Security section)
3. advanced/overview.mdx (Production section)
4. architecture.mdx (System design)

**Key Topics**:
- Production server setup
- Container sandboxing
- Security analyzer
- Monitoring & metrics

### Integration Developer
**Focus**: API integration, tool development

**Start Here**:
1. index.mdx (Hello World)
2. core/state.mdx (Event system)
3. core/overview.mdx (Tool system)
4. advanced/overview.mdx (MCP integration)

**Key Topics**:
- Event structure
- Tool API
- MCP integration
- REST/WebSocket APIs

## 📖 Cross-Reference Map

```
index.mdx
├──→ architecture.mdx (system design)
├──→ core/overview.mdx (components)
├──→ advanced/overview.mdx (features)
└──→ GitHub examples

architecture.mdx
├──→ core/state.mdx (events detail)
├──→ core/agent.mdx (agent detail)
├──→ core/overview.mdx (component detail)
└──→ advanced/overview.mdx (production)

core/overview.mdx
├──→ core/state.mdx (state detail)
├──→ core/agent.mdx (agent detail)
└──→ advanced/overview.mdx (advanced patterns)

core/state.mdx
├──→ core/agent.mdx (stateless design)
└──→ advanced/overview.mdx (persistence)

core/agent.mdx
├──→ core/state.mdx (event system)
└──→ advanced/overview.mdx (custom patterns)

advanced/overview.mdx
├──→ core/state.mdx (events)
├──→ core/agent.mdx (agents)
└──→ architecture.mdx (design)
```

## 🔍 Search Keywords

### By Feature
- **Event sourcing**: core/state.mdx
- **Pause/resume**: core/agent.mdx, core/state.mdx
- **Custom agents**: core/agent.mdx
- **LLM routing**: architecture.mdx
- **Context condensation**: advanced/overview.mdx
- **Security**: advanced/overview.mdx, architecture.mdx
- **Production**: advanced/overview.mdx
- **MCP**: architecture.mdx, advanced/overview.mdx
- **Sub-agents**: core/agent.mdx
- **Testing**: core/agent.mdx

### By Component
- **ConversationState**: core/state.mdx
- **Agent**: core/agent.mdx
- **LLM**: architecture.mdx
- **Tools**: architecture.mdx
- **Conversation**: core/overview.mdx

### By Use Case
- **Debugging**: core/state.mdx (replay)
- **Cost reduction**: advanced/overview.mdx (condensation)
- **Deployment**: advanced/overview.mdx (production)
- **Security**: advanced/overview.mdx (analyzer)
- **Integration**: core/overview.mdx (tools)

## 🚀 Quick Actions

| I want to... | Go to... |
|-------------|----------|
| Get started quickly | index.mdx → Hello World |
| Understand the system | architecture.mdx |
| Learn event sourcing | core/state.mdx |
| Build custom agent | core/agent.mdx |
| Reduce token costs | advanced/overview.mdx |
| Deploy to production | advanced/overview.mdx |
| Secure my agent | advanced/overview.mdx |
| See code examples | Any page (45+ examples) |
| View diagrams | Any page (24 diagrams) |

## 📞 Support & Community

- **Documentation**: [docs.all-hands.dev](https://docs.all-hands.dev)
- **GitHub**: [All-Hands-AI/agent-sdk](https://github.com/All-Hands-AI/agent-sdk)
- **Examples**: [github.com/.../examples](https://github.com/All-Hands-AI/agent-sdk/tree/main/examples)
- **Issues**: [github.com/.../issues](https://github.com/All-Hands-AI/agent-sdk/issues)
- **Discord**: [discord.gg/ESHStjSjD4](https://discord.gg/ESHStjSjD4)

---

**Last Updated**: January 2025
**Documentation Version**: 1.0
**SDK Version**: 1.0.0
