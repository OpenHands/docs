## Invariants (Normative)

### AgentBase: Configuration is Stateless and Immutable

Natural language invariant:

- An `AgentBase` instance is a **pure configuration object**. It may cache materialized `ToolDefinition` instances internally, but it must remain valid to re-create those tools from its declarative spec.

OCL-like:

- `context AgentBase inv Frozen: self.model_config.frozen = true`


### Initialization: System Prompt Precedes Any User Message

`Agent.init_state(state, on_event=...)` is responsible for creating the initial system prompt event.

Natural language invariant:

- A `ConversationState` must not contain a user `MessageEvent` before it contains a `SystemPromptEvent`.

OCL-like (conceptual):

- `context ConversationState inv SystemBeforeUser: self.events->select(e|e.oclIsKindOf(SystemPromptEvent))->size() >= 1 implies self.events->forAll(e| e.oclIsKindOf(MessageEvent) and e.source='user' implies e.index > systemPromptIndex )`


### Tool Materialization: Names Resolve to Registered ToolDefinitions

An `Agent` is configured with a list of tool *specs* (`openhands.sdk.tool.spec.Tool`) that reference registered `ToolDefinition` factories.

Natural language invariant:

- `resolve_tool(Tool(name=X))` must succeed (tool name present in registry) for all tools the agent intends to use.
- Tool factories must return a **sequence** of `ToolDefinition` instances; tool sets (e.g., browser tool sets) are represented as multi-element sequences.

### Multi-Tool Calls: Shared Thought Only on First ActionEvent

When an LLM returns parallel tool calls, the SDK represents this as multiple `ActionEvent`s that share the same `llm_response_id`.

Natural language invariant:

- For a batch of `ActionEvent`s with the same `llm_response_id`, only the first action carries `thought` / `reasoning_content` / `thinking_blocks`; subsequent actions must have empty `thought`.

OCL-like (as modeled in `event.base._combine_action_events`):

- `context ActionEvent inv BatchedThoughtOnlyFirst: (self.llm_response_id = other.llm_response_id and self <> first) implies self.thought->isEmpty()`


### Confirmation Mode: Requires Both Analyzer and Policy

`conversation.is_confirmation_mode_active` is true iff:

- A `SecurityAnalyzer` is configured, and
- The confirmation policy is not `NeverConfirm`.

OCL-like (conceptual):

- `context BaseConversation inv ConfirmationModeIff: self.is_confirmation_mode_active = (self.state.security_analyzer <> null and not self.state.confirmation_policy.oclIsKindOf(NeverConfirm))`


**Execution Modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| **Direct** | Execute immediately | Development, trusted environments |
| **Confirmation** | Store as pending, wait for user approval | High-risk actions, production |

**Security Integration:**

Before execution, the security analyzer evaluates each action:
- **Low Risk:** Execute immediately
- **Medium Risk:** Log warning, execute with monitoring
- **High Risk:** Block execution, request user confirmation
