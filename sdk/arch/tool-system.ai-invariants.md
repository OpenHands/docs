## Invariants (Normative)

### ToolDefinition Naming

By default, tool names are derived from the class name:

- `TerminalTool` → `terminal`
- `FileEditorTool` → `file_editor`

Natural language invariant:

- Unless explicitly overridden, `ToolDefinition.name` is deterministic and stable across runs.

### Tool Registry

`register_tool(name, factory)` maintains a global name→resolver mapping.

Invariants:

- Tool names must be non-empty strings.
- A `ToolDefinition` instance can only be registered if it has a non-None `executor`.
- A `ToolDefinition` subclass can only be registered if it implements a concrete `create(...)` classmethod that returns `Sequence[ToolDefinition]`.
- Resolving an unregistered tool name must raise `KeyError`.

OCL-like (conceptual):

- `context ToolRegistry inv NonEmptyNames: name.trim().size() > 0`


### Executor Presence and Call Semantics

Natural language invariant:

- A `ToolDefinition` without an `executor` is not executable; attempts to call it must fail fast.
- All tool execution is performed in a `LocalConversation` context (even when invoked remotely) because the agent-server hosts the actual conversation that runs tools.

### Action/Observation Schemas are Validated

Natural language invariant:

- `Action` and `Observation` are Pydantic models; tool inputs are validated before execution, and tool results are **parsed/validated** into the declared observation model (if present). If the executor already returns the correct observation type, this is a no-op.


1. **[Tool (Spec)](https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/tool/spec.py)** - Configuration object with `name` (e.g., "BashTool") and `params` (e.g., `{"working_dir": "/workspace"}`)
2. **Resolver Lookup** - Registry finds the registered resolver for the tool name
3. **Factory Invocation** - Resolver calls the tool's `.create()` method with params and conversation state
4. **Instance Creation** - Tool instance(s) are created with configured executors
5. **Agent Usage** - Instances are added to the agent's tools_map for execution

**Registration Types:**

| Type | Registration | Resolver Behavior |
|------|-------------|-------------------|
| **Tool Instance** | `register_tool(name, instance)` | Returns the fixed instance (params not allowed) |
| **Tool Subclass** | `register_tool(name, ToolClass)` | Calls `ToolClass.create(**params, conv_state=state)` |
| **Factory Function** | `register_tool(name, factory)` | Calls `factory(**params, conv_state=state)` |

### File Organization

Tools follow a consistent file structure for maintainability:

```
openhands-tools/openhands/tools/my_tool/
├── __init__.py           # Export MyTool
├── definition.py         # Action, Observation, MyTool(ToolDefinition)
├── impl.py              # MyExecutor(ToolExecutor)
└── [other modules]      # Tool-specific utilities
```

**File Responsibilities:**

| File | Contains | Purpose |
|------|----------|---------|
| `definition.py` | Action, Observation, ToolDefinition subclass | Public API, schema definitions, factory method |
| `impl.py` | ToolExecutor implementation | Business logic, state management, execution |
| `__init__.py` | Tool exports | Package interface |

**Benefits:**
- **Separation of Concerns** - Public API separate from implementation
- **Avoid Circular Imports** - Import `impl` only inside `create()` method
- **Consistency** - All tools follow same structure for discoverability

**Example Reference:** See [`terminal/`](https://github.com/OpenHands/software-agent-sdk/tree/main/openhands-tools/openhands/tools/terminal) for complete implementation
