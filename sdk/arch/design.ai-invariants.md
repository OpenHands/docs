## Design Invariants (Normative)

This page describes the **architectural invariants** the SDK relies on. These are treated as *contracts* between components.

Where appropriate, we express invariants in a lightweight OCL-like notation:

- `context X inv Name: <predicate>`
- `pre:` / `post:` for pre/post-conditions

If an invariant cannot be expressed precisely in OCL without significant auxiliary modeling, we state it in precise natural language.

### Single Source of Truth for Runtime State

The SDK is designed so that **all runtime state that affects agent execution is representable as an event log plus a small, validated state snapshot**.

- **Configuration objects are immutable** (Pydantic `frozen=True` where applicable).
- **The only intentionally mutable entity is `ConversationState`**, which owns the event log, execution status, secrets registry, and persistence handles.

OCL-like:

- `context AgentBase inv StatelessConfiguration: self.model_config.frozen = true`
- `context Event inv Immutable: self.model_config.frozen = true`


Natural language invariant:

- `ConversationState` is the single coordination point for execution. Other objects may maintain private runtime caches, but **must not** be required to restore or replay a conversation.

### Workspace Boundary is the I/O Boundary

All side effects against the environment (filesystem, processes, git operations) must occur **through a Workspace** (local or remote), which becomes the **I/O boundary**.

- Tools may execute in different runtimes (local process vs inside agent-server), but *conceptually* they always operate against a workspace rooted at `workspace.working_dir`.

OCL-like:

- `context BaseWorkspace inv WorkingDirIsString: self.working_dir.oclIsTypeOf(String)`


### Event Log is the Execution Trace

The event stream is the single authoritative trace of what the agent *saw* and *did*.

Natural language invariant:

- Any agent decision that should be reproducible on replay must be representable as an `LLMConvertibleEvent` (for LLM context) plus associated non-LLM events (e.g., state updates, errors).

### Tool Calls are Explicit, Typed, and Linkable

The SDK assumes an explicit `Action -> Observation` pairing.

OCL-like (conceptual):

- `context ActionEvent inv HasToolCallId: self.tool_call_id <> null`
- `context ObservationEvent inv RefersToAction: self.action_id <> null`


Natural language invariant:

- Observations must be attributable to a specific action/tool call so that conversations can be audited, visualized, and resumed.

### Remote vs Local is an Execution Detail

The SDK makes *deployment mode* (local vs remote) a **runtime selection behind a common interface**, not two separate programming models.

- `Conversation(...)` returns either `LocalConversation` or `RemoteConversation` based on the provided workspace.
- User-facing code typically should not need to change when switching workspaces; you mostly swap configuration.

<Note>
This does **not** mean every optional method behaves identically across workspace types (e.g., `pause()` / `resume()` may be a no-op locally and meaningful remotely). The core conversation API (`send_message`, `run`, events) stays consistent.
</Note>
