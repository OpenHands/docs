## Invariants (Normative)

### Conversation Factory: Workspace Chooses Implementation

Natural language invariant:

- `Conversation(...)` is a factory that returns `LocalConversation` unless the provided `workspace` is a `RemoteWorkspace`.
- When `workspace` is remote, `persistence_dir` must be unset (`None`).

OCL-like (conceptual):

- `context Conversation::__new__ pre RemoteNoPersistence: workspace.oclIsKindOf(RemoteWorkspace) implies persistence_dir = null`


### ConversationState: Validated Snapshot + Event Log

Natural language invariants:

- `ConversationState` is the **only** component intended to hold mutable execution status (`IDLE`, `RUNNING`, `WAITING_FOR_CONFIRMATION`, etc.).
- `ConversationState` owns persistence (`FileStore`) and the event store; all other components treat persistence as an implementation detail.

### Confirmation Mode Predicate

The SDK exposes a single predicate for confirmation mode:

- Confirmation mode is active iff `state.security_analyzer != None` **and** the confirmation policy is not `NeverConfirm`.

### ask_agent() Must Be Stateless

Natural language invariant (from the public contract):

- `BaseConversation.ask_agent(question)` **must not** append events, mutate execution status, or persist anything. It is safe to call concurrently with `run()`.

### Secrets Persistence Requires a Cipher

Natural language invariant:

- If `ConversationState` is persisted without a cipher, secret values are redacted and **cannot be recovered on restore**.

(Implication: use `Cipher` when persistence is enabled and you expect to resume with secrets intact.)
