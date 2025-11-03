## `openhands.sdk.conversation`

**Modules:**

- [**base**](#openhands.sdk.conversation.base) –
- [**conversation**](#openhands.sdk.conversation.conversation) –
- [**conversation_stats**](#openhands.sdk.conversation.conversation_stats) –
- [**event_store**](#openhands.sdk.conversation.event_store) –
- [**events_list_base**](#openhands.sdk.conversation.events_list_base) –
- [**exceptions**](#openhands.sdk.conversation.exceptions) –
- [**fifo_lock**](#openhands.sdk.conversation.fifo_lock) – FIFO Lock implementation that guarantees first-in-first-out access ordering.
- [**impl**](#openhands.sdk.conversation.impl) –
- [**persistence_const**](#openhands.sdk.conversation.persistence_const) –
- [**response_utils**](#openhands.sdk.conversation.response_utils) – Utility functions for extracting agent responses from conversation events.
- [**secret_registry**](#openhands.sdk.conversation.secret_registry) – Secrets manager for handling sensitive data in conversations.
- [**secret_source**](#openhands.sdk.conversation.secret_source) –
- [**serialization_diff**](#openhands.sdk.conversation.serialization_diff) –
- [**state**](#openhands.sdk.conversation.state) –
- [**stuck_detector**](#openhands.sdk.conversation.stuck_detector) –
- [**title_utils**](#openhands.sdk.conversation.title_utils) – Utility functions for generating conversation titles.
- [**types**](#openhands.sdk.conversation.types) –
- [**visualizer**](#openhands.sdk.conversation.visualizer) –

**Classes:**

- [**BaseConversation**](#openhands.sdk.conversation.BaseConversation) –
- [**Conversation**](#openhands.sdk.conversation.Conversation) – Factory entrypoint that returns a LocalConversation or RemoteConversation.
- [**ConversationState**](#openhands.sdk.conversation.ConversationState) –
- [**ConversationVisualizer**](#openhands.sdk.conversation.ConversationVisualizer) – Handles visualization of conversation events with Rich formatting.
- [**EventLog**](#openhands.sdk.conversation.EventLog) –
- [**EventsListBase**](#openhands.sdk.conversation.EventsListBase) – Abstract base class for event lists that can be appended to.
- [**LocalConversation**](#openhands.sdk.conversation.LocalConversation) –
- [**RemoteConversation**](#openhands.sdk.conversation.RemoteConversation) –
- [**SecretRegistry**](#openhands.sdk.conversation.SecretRegistry) – Manages secrets and injects them into bash commands when needed.
- [**StuckDetector**](#openhands.sdk.conversation.StuckDetector) – Detects when an agent is stuck in repetitive or unproductive patterns.

**Functions:**

- [**get_agent_final_response**](#openhands.sdk.conversation.get_agent_final_response) – Extract the final response from the agent.

**Attributes:**

- [**ConversationCallbackType**](#openhands.sdk.conversation.ConversationCallbackType) –

### `openhands.sdk.conversation.BaseConversation`

Bases: <code>[ABC](#abc.ABC)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.BaseConversation.close) –
- [**compose_callbacks**](#openhands.sdk.conversation.BaseConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.BaseConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.BaseConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.BaseConversation.pause) –
- [**reject_pending_actions**](#openhands.sdk.conversation.BaseConversation.reject_pending_actions) –
- [**run**](#openhands.sdk.conversation.BaseConversation.run) –
- [**send_message**](#openhands.sdk.conversation.BaseConversation.send_message) –
- [**set_confirmation_policy**](#openhands.sdk.conversation.BaseConversation.set_confirmation_policy) –
- [**update_secrets**](#openhands.sdk.conversation.BaseConversation.update_secrets) –

**Attributes:**

- [**confirmation_policy_active**](#openhands.sdk.conversation.BaseConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.BaseConversation.conversation_stats) (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats)</code>) –
- [**id**](#openhands.sdk.conversation.BaseConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.BaseConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**state**](#openhands.sdk.conversation.BaseConversation.state) (<code>[ConversationStateProtocol](#openhands.sdk.conversation.base.ConversationStateProtocol)</code>) –

#### `openhands.sdk.conversation.BaseConversation.close`

```python
close()
```

#### `openhands.sdk.conversation.BaseConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

#### `openhands.sdk.conversation.BaseConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

#### `openhands.sdk.conversation.BaseConversation.conversation_stats`

```python
conversation_stats: ConversationStats
```

#### `openhands.sdk.conversation.BaseConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.llm.LLM) | None</code>) – Optional LLM to use for title generation. If not provided,
  uses the agent's LLM.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If no user messages are found in the conversation.

#### `openhands.sdk.conversation.BaseConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

#### `openhands.sdk.conversation.BaseConversation.id`

```python
id: ConversationID
```

#### `openhands.sdk.conversation.BaseConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

#### `openhands.sdk.conversation.BaseConversation.pause`

```python
pause()
```

#### `openhands.sdk.conversation.BaseConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

#### `openhands.sdk.conversation.BaseConversation.run`

```python
run()
```

#### `openhands.sdk.conversation.BaseConversation.send_message`

```python
send_message(message)
```

#### `openhands.sdk.conversation.BaseConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

#### `openhands.sdk.conversation.BaseConversation.state`

```python
state: ConversationStateProtocol
```

#### `openhands.sdk.conversation.BaseConversation.update_secrets`

```python
update_secrets(secrets)
```

### `openhands.sdk.conversation.Conversation`

Factory entrypoint that returns a LocalConversation or RemoteConversation.

<details class="usage" open markdown="1">
<summary>Usage</summary>

- Conversation(agent=...) -> LocalConversation
- Conversation(agent=..., host="http://...") -> RemoteConversation

</details>

### `openhands.sdk.conversation.ConversationCallbackType`

```python
ConversationCallbackType = Callable[[Event], None]
```

### `openhands.sdk.conversation.ConversationState`

Bases: <code>[OpenHandsModel](#openhands.sdk.utils.models.OpenHandsModel)</code>

**Functions:**

- [**acquire**](#openhands.sdk.conversation.ConversationState.acquire) – Acquire the lock.
- [**create**](#openhands.sdk.conversation.ConversationState.create) – If base_state.json exists: resume (attach EventLog,
- [**get_unmatched_actions**](#openhands.sdk.conversation.ConversationState.get_unmatched_actions) – Find actions in the event history that don't have matching observations.
- [**locked**](#openhands.sdk.conversation.ConversationState.locked) – Return True if the lock is currently held by any thread.
- [**model_dump_json**](#openhands.sdk.conversation.ConversationState.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.conversation.ConversationState.model_json_schema) –
- [**model_post_init**](#openhands.sdk.conversation.ConversationState.model_post_init) –
- [**model_validate**](#openhands.sdk.conversation.ConversationState.model_validate) –
- [**model_validate_json**](#openhands.sdk.conversation.ConversationState.model_validate_json) –
- [**owned**](#openhands.sdk.conversation.ConversationState.owned) – Return True if the lock is currently held by the calling thread.
- [**release**](#openhands.sdk.conversation.ConversationState.release) – Release the lock.
- [**set_on_state_change**](#openhands.sdk.conversation.ConversationState.set_on_state_change) – Set a callback to be called when state changes.

**Attributes:**

- [**activated_knowledge_skills**](#openhands.sdk.conversation.ConversationState.activated_knowledge_skills) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**agent**](#openhands.sdk.conversation.ConversationState.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**agent_status**](#openhands.sdk.conversation.ConversationState.agent_status) (<code>[AgentExecutionStatus](#openhands.sdk.conversation.state.AgentExecutionStatus)</code>) –
- [**confirmation_policy**](#openhands.sdk.conversation.ConversationState.confirmation_policy) (<code>[ConfirmationPolicyBase](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)</code>) –
- [**events**](#openhands.sdk.conversation.ConversationState.events) (<code>[EventLog](#openhands.sdk.conversation.event_store.EventLog)</code>) –
- [**id**](#openhands.sdk.conversation.ConversationState.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**max_iterations**](#openhands.sdk.conversation.ConversationState.max_iterations) (<code>[int](#int)</code>) –
- [**persistence_dir**](#openhands.sdk.conversation.ConversationState.persistence_dir) (<code>[str](#str) | None</code>) –
- [**secret_registry**](#openhands.sdk.conversation.ConversationState.secret_registry) (<code>[SecretRegistry](#openhands.sdk.conversation.secret_registry.SecretRegistry)</code>) –
- [**stats**](#openhands.sdk.conversation.ConversationState.stats) (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats)</code>) –
- [**stuck_detection**](#openhands.sdk.conversation.ConversationState.stuck_detection) (<code>[bool](#bool)</code>) –
- [**workspace**](#openhands.sdk.conversation.ConversationState.workspace) (<code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>) –

#### `openhands.sdk.conversation.ConversationState.acquire`

```python
acquire(blocking=True, timeout=-1)
```

Acquire the lock.

**Parameters:**

- **blocking** (<code>[bool](#bool)</code>) – If True, block until lock is acquired. If False, return
  immediately.
- **timeout** (<code>[float](#float)</code>) – Maximum time to wait for lock (ignored if blocking=False).
  -1 means wait indefinitely.

**Returns:**

- <code>[bool](#bool)</code> – True if lock was acquired, False otherwise.

#### `openhands.sdk.conversation.ConversationState.activated_knowledge_skills`

```python
activated_knowledge_skills: list[str] = Field(default_factory=list, description='List of activated knowledge skills name')
```

#### `openhands.sdk.conversation.ConversationState.agent`

```python
agent: AgentBase = Field(..., description='The agent running in the conversation. This is persisted to allow resuming conversations and check agent configuration to handle e.g., tool changes, LLM changes, etc.')
```

#### `openhands.sdk.conversation.ConversationState.agent_status`

```python
agent_status: AgentExecutionStatus = Field(default=(AgentExecutionStatus.IDLE))
```

#### `openhands.sdk.conversation.ConversationState.confirmation_policy`

```python
confirmation_policy: ConfirmationPolicyBase = NeverConfirm()
```

#### `openhands.sdk.conversation.ConversationState.create`

```python
create(id, agent, workspace, persistence_dir=None, max_iterations=500, stuck_detection=True)
```

If base_state.json exists: resume (attach EventLog,
reconcile agent, enforce id).
Else: create fresh (agent required), persist base, and return.

#### `openhands.sdk.conversation.ConversationState.events`

```python
events: EventLog
```

#### `openhands.sdk.conversation.ConversationState.get_unmatched_actions`

```python
get_unmatched_actions(events)
```

Find actions in the event history that don't have matching observations.

This method identifies ActionEvents that don't have corresponding
ObservationEvents or UserRejectObservations, which typically indicates
actions that are pending confirmation or execution.

**Parameters:**

- **events** (<code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.base.Event)\]</code>) – List of events to search through

**Returns:**

- <code>[list](#list)\[[ActionEvent](#openhands.sdk.event.ActionEvent)\]</code> – List of ActionEvent objects that don't have corresponding observations,
- <code>[list](#list)\[[ActionEvent](#openhands.sdk.event.ActionEvent)\]</code> – in chronological order

#### `openhands.sdk.conversation.ConversationState.id`

```python
id: ConversationID = Field(description='Unique conversation ID')
```

#### `openhands.sdk.conversation.ConversationState.locked`

```python
locked()
```

Return True if the lock is currently held by any thread.

#### `openhands.sdk.conversation.ConversationState.max_iterations`

```python
max_iterations: int = Field(default=500, gt=0, description='Maximum number of iterations the agent can perform in a single run.')
```

#### `openhands.sdk.conversation.ConversationState.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.conversation.ConversationState.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.conversation.ConversationState.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.conversation.ConversationState.model_validate`

```python
model_validate(*args, **kwargs)
```

#### `openhands.sdk.conversation.ConversationState.model_validate_json`

```python
model_validate_json(*args, **kwargs)
```

#### `openhands.sdk.conversation.ConversationState.owned`

```python
owned()
```

Return True if the lock is currently held by the calling thread.

#### `openhands.sdk.conversation.ConversationState.persistence_dir`

```python
persistence_dir: str | None = Field(default='workspace/conversations', description='Directory for persisting conversation state and events. If None, conversation will not be persisted.')
```

#### `openhands.sdk.conversation.ConversationState.release`

```python
release()
```

Release the lock.

**Raises:**

- <code>[RuntimeError](#RuntimeError)</code> – If the current thread doesn't own the lock.

#### `openhands.sdk.conversation.ConversationState.secret_registry`

```python
secret_registry: SecretRegistry = Field(default_factory=SecretRegistry, description='Registry for handling secrets and sensitive data', validation_alias=(AliasChoices('secret_registry', 'secrets_manager')), serialization_alias='secret_registry')
```

#### `openhands.sdk.conversation.ConversationState.set_on_state_change`

```python
set_on_state_change(callback)
```

Set a callback to be called when state changes.

**Parameters:**

- **callback** (<code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType) | None</code>) – A function that takes an Event (ConversationStateUpdateEvent)
  or None to remove the callback

#### `openhands.sdk.conversation.ConversationState.stats`

```python
stats: ConversationStats = Field(default_factory=ConversationStats, description='Conversation statistics for tracking LLM metrics')
```

#### `openhands.sdk.conversation.ConversationState.stuck_detection`

```python
stuck_detection: bool = Field(default=True, description='Whether to enable stuck detection for the agent.')
```

#### `openhands.sdk.conversation.ConversationState.workspace`

```python
workspace: BaseWorkspace = Field(..., description='Working directory for agent operations and tool execution')
```

### `openhands.sdk.conversation.ConversationVisualizer`

```python
ConversationVisualizer(highlight_regex=None, skip_user_messages=False, conversation_stats=None, name_for_visualization=None)
```

Handles visualization of conversation events with Rich formatting.

Provides Rich-formatted output with panels and complete content display.

**Functions:**

- [**on_event**](#openhands.sdk.conversation.ConversationVisualizer.on_event) – Main event handler that displays events with Rich formatting.

**Parameters:**

- **highlight_regex** (<code>[dict](#dict)\[[str](#str), [str](#str)\] | None</code>) – Dictionary mapping regex patterns to Rich color styles
  for highlighting keywords in the visualizer.
  For example: {"Reasoning:": "bold blue",
  "Thought:": "bold green"}
- **skip_user_messages** (<code>[bool](#bool)</code>) – If True, skip displaying user messages. Useful for
  scenarios where user input is not relevant to show.
- **conversation_stats** (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats) | None</code>) – ConversationStats object to display metrics information.
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.

#### `openhands.sdk.conversation.ConversationVisualizer.on_event`

```python
on_event(event)
```

Main event handler that displays events with Rich formatting.

### `openhands.sdk.conversation.EventLog`

```python
EventLog(fs, dir_path=EVENTS_DIR)
```

Bases: <code>[EventsListBase](#openhands.sdk.conversation.events_list_base.EventsListBase)</code>

**Functions:**

- [**append**](#openhands.sdk.conversation.EventLog.append) –
- [**get_id**](#openhands.sdk.conversation.EventLog.get_id) – Return the event_id for a given index.
- [**get_index**](#openhands.sdk.conversation.EventLog.get_index) – Return the integer index for a given event_id.

#### `openhands.sdk.conversation.EventLog.append`

```python
append(event)
```

#### `openhands.sdk.conversation.EventLog.get_id`

```python
get_id(idx)
```

Return the event_id for a given index.

#### `openhands.sdk.conversation.EventLog.get_index`

```python
get_index(event_id)
```

Return the integer index for a given event_id.

### `openhands.sdk.conversation.EventsListBase`

Bases: <code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.Event)\]</code>, <code>[ABC](#abc.ABC)</code>

Abstract base class for event lists that can be appended to.

This provides a common interface for both local EventLog and remote
RemoteEventsList implementations, avoiding circular imports in protocols.

**Functions:**

- [**append**](#openhands.sdk.conversation.EventsListBase.append) – Add a new event to the list.

#### `openhands.sdk.conversation.EventsListBase.append`

```python
append(event)
```

Add a new event to the list.

### `openhands.sdk.conversation.LocalConversation`

```python
LocalConversation(agent, workspace, persistence_dir=None, conversation_id=None, callbacks=None, max_iteration_per_run=500, stuck_detection=True, visualize=True, name_for_visualization=None, secrets=None, **_)
```

Bases: <code>[BaseConversation](#openhands.sdk.conversation.base.BaseConversation)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.LocalConversation.close) – Close the conversation and clean up all tool executors.
- [**compose_callbacks**](#openhands.sdk.conversation.LocalConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.LocalConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.LocalConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.LocalConversation.pause) – Pause agent execution.
- [**reject_pending_actions**](#openhands.sdk.conversation.LocalConversation.reject_pending_actions) – Reject all pending actions from the agent.
- [**run**](#openhands.sdk.conversation.LocalConversation.run) – Runs the conversation until the agent finishes.
- [**send_message**](#openhands.sdk.conversation.LocalConversation.send_message) – Send a message to the agent.
- [**set_confirmation_policy**](#openhands.sdk.conversation.LocalConversation.set_confirmation_policy) – Set the confirmation policy and store it in conversation state.
- [**update_secrets**](#openhands.sdk.conversation.LocalConversation.update_secrets) – Add secrets to the conversation.

**Attributes:**

- [**agent**](#openhands.sdk.conversation.LocalConversation.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**confirmation_policy_active**](#openhands.sdk.conversation.LocalConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.LocalConversation.conversation_stats) –
- [**id**](#openhands.sdk.conversation.LocalConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) – Get the unique ID of the conversation.
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.LocalConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**llm_registry**](#openhands.sdk.conversation.LocalConversation.llm_registry) (<code>[LLMRegistry](#openhands.sdk.llm.llm_registry.LLMRegistry)</code>) –
- [**max_iteration_per_run**](#openhands.sdk.conversation.LocalConversation.max_iteration_per_run) (<code>[int](#int)</code>) –
- [**state**](#openhands.sdk.conversation.LocalConversation.state) (<code>[ConversationState](#openhands.sdk.conversation.state.ConversationState)</code>) – Get the conversation state.
- [**stuck_detector**](#openhands.sdk.conversation.LocalConversation.stuck_detector) (<code>[StuckDetector](#openhands.sdk.conversation.stuck_detector.StuckDetector) | None</code>) – Get the stuck detector instance if enabled.
- [**workspace**](#openhands.sdk.conversation.LocalConversation.workspace) (<code>[LocalWorkspace](#openhands.sdk.workspace.LocalWorkspace)</code>) –

**Parameters:**

- **agent** (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) – The agent to use for the conversation
- **workspace** (<code>[str](#str) | [LocalWorkspace](#openhands.sdk.workspace.LocalWorkspace)</code>) – Working directory for agent operations and tool execution
- **persistence_dir** (<code>[str](#str) | None</code>) – Directory for persisting conversation state and events
- **conversation_id** (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID) | None</code>) – Optional ID for the conversation. If provided, will
  be used to identify the conversation. The user might want to
  suffix their persistent filestore with this ID.
- **callbacks** (<code>[list](#list)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\] | None</code>) – Optional list of callback functions to handle events
- **max_iteration_per_run** (<code>[int](#int)</code>) – Maximum number of iterations per run
- **visualize** (<code>[bool](#bool)</code>) – Whether to enable default visualization. If True, adds
  a default visualizer callback. If False, relies on
  application to provide visualization through callbacks.
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.
- **stuck_detection** (<code>[bool](#bool)</code>) – Whether to enable stuck detection

#### `openhands.sdk.conversation.LocalConversation.agent`

```python
agent: AgentBase = agent
```

#### `openhands.sdk.conversation.LocalConversation.close`

```python
close()
```

Close the conversation and clean up all tool executors.

#### `openhands.sdk.conversation.LocalConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

#### `openhands.sdk.conversation.LocalConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

#### `openhands.sdk.conversation.LocalConversation.conversation_stats`

```python
conversation_stats
```

#### `openhands.sdk.conversation.LocalConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.LLM) | None</code>) – Optional LLM to use for title generation. If not provided,
  uses self.agent.llm.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If no user messages are found in the conversation.

#### `openhands.sdk.conversation.LocalConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

#### `openhands.sdk.conversation.LocalConversation.id`

```python
id: ConversationID
```

Get the unique ID of the conversation.

#### `openhands.sdk.conversation.LocalConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

#### `openhands.sdk.conversation.LocalConversation.llm_registry`

```python
llm_registry: LLMRegistry = LLMRegistry()
```

#### `openhands.sdk.conversation.LocalConversation.max_iteration_per_run`

```python
max_iteration_per_run: int = max_iteration_per_run
```

#### `openhands.sdk.conversation.LocalConversation.pause`

```python
pause()
```

Pause agent execution.

This method can be called from any thread to request that the agent
pause execution. The pause will take effect at the next iteration
of the run loop (between agent steps).

Note: If called during an LLM completion, the pause will not take
effect until the current LLM call completes.

#### `openhands.sdk.conversation.LocalConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

Reject all pending actions from the agent.

This is a non-invasive method to reject actions between run() calls.
Also clears the agent_waiting_for_confirmation flag.

#### `openhands.sdk.conversation.LocalConversation.run`

```python
run()
```

Runs the conversation until the agent finishes.

In confirmation mode:

- First call: creates actions but doesn't execute them, stops and waits
- Second call: executes pending actions (implicit confirmation)

In normal mode:

- Creates and executes actions immediately

Can be paused between steps

#### `openhands.sdk.conversation.LocalConversation.send_message`

```python
send_message(message)
```

Send a message to the agent.

**Parameters:**

- **message** (<code>[str](#str) | [Message](#openhands.sdk.llm.Message)</code>) – Either a string (which will be converted to a user message)
  or a Message object

#### `openhands.sdk.conversation.LocalConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

Set the confirmation policy and store it in conversation state.

#### `openhands.sdk.conversation.LocalConversation.state`

```python
state: ConversationState
```

Get the conversation state.

It returns a protocol that has a subset of ConversationState methods
and properties. We will have the ability to access the same properties
of ConversationState on a remote conversation object.
But we won't be able to access methods that mutate the state.

#### `openhands.sdk.conversation.LocalConversation.stuck_detector`

```python
stuck_detector: StuckDetector | None
```

Get the stuck detector instance if enabled.

#### `openhands.sdk.conversation.LocalConversation.update_secrets`

```python
update_secrets(secrets)
```

Add secrets to the conversation.

**Parameters:**

- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\]</code>) – Dictionary mapping secret keys to values or no-arg callables.
  SecretValue = str | Callable\[[], str\]. Callables are invoked lazily
  when a command references the secret key.

#### `openhands.sdk.conversation.LocalConversation.workspace`

```python
workspace: LocalWorkspace = workspace
```

### `openhands.sdk.conversation.RemoteConversation`

```python
RemoteConversation(agent, workspace, conversation_id=None, callbacks=None, max_iteration_per_run=500, stuck_detection=True, visualize=False, name_for_visualization=None, secrets=None, **_)
```

Bases: <code>[BaseConversation](#openhands.sdk.conversation.base.BaseConversation)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.RemoteConversation.close) –
- [**compose_callbacks**](#openhands.sdk.conversation.RemoteConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.RemoteConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.RemoteConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.RemoteConversation.pause) –
- [**reject_pending_actions**](#openhands.sdk.conversation.RemoteConversation.reject_pending_actions) –
- [**run**](#openhands.sdk.conversation.RemoteConversation.run) –
- [**send_message**](#openhands.sdk.conversation.RemoteConversation.send_message) –
- [**set_confirmation_policy**](#openhands.sdk.conversation.RemoteConversation.set_confirmation_policy) –
- [**update_secrets**](#openhands.sdk.conversation.RemoteConversation.update_secrets) –

**Attributes:**

- [**agent**](#openhands.sdk.conversation.RemoteConversation.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**confirmation_policy_active**](#openhands.sdk.conversation.RemoteConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.RemoteConversation.conversation_stats) (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats)</code>) – Get conversation stats from remote server.
- [**id**](#openhands.sdk.conversation.RemoteConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.RemoteConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**max_iteration_per_run**](#openhands.sdk.conversation.RemoteConversation.max_iteration_per_run) (<code>[int](#int)</code>) –
- [**state**](#openhands.sdk.conversation.RemoteConversation.state) (<code>[RemoteState](#openhands.sdk.conversation.impl.remote_conversation.RemoteState)</code>) – Access to remote conversation state.
- [**stuck_detector**](#openhands.sdk.conversation.RemoteConversation.stuck_detector) – Stuck detector for compatibility.
- [**workspace**](#openhands.sdk.conversation.RemoteConversation.workspace) (<code>[RemoteWorkspace](#openhands.sdk.workspace.RemoteWorkspace)</code>) –

**Parameters:**

- **agent** (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) – Agent configuration (will be sent to the server)
- **workspace** (<code>[RemoteWorkspace](#openhands.sdk.workspace.RemoteWorkspace)</code>) – The working directory for agent operations and tool execution.
- **conversation_id** (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID) | None</code>) – Optional existing conversation id to attach to
- **callbacks** (<code>[list](#list)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\] | None</code>) – Optional callbacks to receive events (not yet streamed)
- **max_iteration_per_run** (<code>[int](#int)</code>) – Max iterations configured on server
- **stuck_detection** (<code>[bool](#bool)</code>) – Whether to enable stuck detection on server
- **visualize** (<code>[bool](#bool)</code>) – Whether to enable the default visualizer callback
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.
- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\] | None</code>) – Optional secrets to initialize the conversation with

#### `openhands.sdk.conversation.RemoteConversation.agent`

```python
agent: AgentBase = agent
```

#### `openhands.sdk.conversation.RemoteConversation.close`

```python
close()
```

#### `openhands.sdk.conversation.RemoteConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

#### `openhands.sdk.conversation.RemoteConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

#### `openhands.sdk.conversation.RemoteConversation.conversation_stats`

```python
conversation_stats: ConversationStats
```

Get conversation stats from remote server.

#### `openhands.sdk.conversation.RemoteConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.LLM) | None</code>) – Optional LLM to use for title generation. If provided, its usage_id
  will be sent to the server. If not provided, uses the agent's LLM.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

#### `openhands.sdk.conversation.RemoteConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

#### `openhands.sdk.conversation.RemoteConversation.id`

```python
id: ConversationID
```

#### `openhands.sdk.conversation.RemoteConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

#### `openhands.sdk.conversation.RemoteConversation.max_iteration_per_run`

```python
max_iteration_per_run: int = max_iteration_per_run
```

#### `openhands.sdk.conversation.RemoteConversation.pause`

```python
pause()
```

#### `openhands.sdk.conversation.RemoteConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

#### `openhands.sdk.conversation.RemoteConversation.run`

```python
run()
```

#### `openhands.sdk.conversation.RemoteConversation.send_message`

```python
send_message(message)
```

#### `openhands.sdk.conversation.RemoteConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

#### `openhands.sdk.conversation.RemoteConversation.state`

```python
state: RemoteState
```

Access to remote conversation state.

#### `openhands.sdk.conversation.RemoteConversation.stuck_detector`

```python
stuck_detector
```

Stuck detector for compatibility.
Not implemented for remote conversations.

#### `openhands.sdk.conversation.RemoteConversation.update_secrets`

```python
update_secrets(secrets)
```

#### `openhands.sdk.conversation.RemoteConversation.workspace`

```python
workspace: RemoteWorkspace = workspace
```

### `openhands.sdk.conversation.SecretRegistry`

Bases: <code>[OpenHandsModel](#openhands.sdk.utils.models.OpenHandsModel)</code>

Manages secrets and injects them into bash commands when needed.

The secret registry stores a mapping of secret keys to SecretSources
that retrieve the actual secret values. When a bash command is about to be
executed, it scans the command for any secret keys and injects the corresponding
environment variables.

Secret sources will redact / encrypt their sensitive values as appropriate when
serializing, depending on the content of the context. If a context is present
and contains a 'cipher' object, this is used for encryption. If it contains a
boolean 'expose_secrets' flag set to True, secrets are dunped in plain text.
Otherwise secrets are redacted.

Additionally, it tracks the latest exported values to enable consistent masking
even when callable secrets fail on subsequent calls.

**Functions:**

- [**find_secrets_in_text**](#openhands.sdk.conversation.SecretRegistry.find_secrets_in_text) – Find all secret keys mentioned in the given text.
- [**get_secrets_as_env_vars**](#openhands.sdk.conversation.SecretRegistry.get_secrets_as_env_vars) – Get secrets that should be exported as environment variables for a command.
- [**mask_secrets_in_output**](#openhands.sdk.conversation.SecretRegistry.mask_secrets_in_output) – Mask secret values in the given text.
- [**model_dump_json**](#openhands.sdk.conversation.SecretRegistry.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.conversation.SecretRegistry.model_json_schema) –
- [**model_post_init**](#openhands.sdk.conversation.SecretRegistry.model_post_init) –
- [**model_validate**](#openhands.sdk.conversation.SecretRegistry.model_validate) –
- [**model_validate_json**](#openhands.sdk.conversation.SecretRegistry.model_validate_json) –
- [**update_secrets**](#openhands.sdk.conversation.SecretRegistry.update_secrets) – Add or update secrets in the manager.

**Attributes:**

- [**secret_sources**](#openhands.sdk.conversation.SecretRegistry.secret_sources) (<code>[dict](#dict)\[[str](#str), [SecretSource](#openhands.sdk.conversation.secret_source.SecretSource)\]</code>) –

#### `openhands.sdk.conversation.SecretRegistry.find_secrets_in_text`

```python
find_secrets_in_text(text)
```

Find all secret keys mentioned in the given text.

**Parameters:**

- **text** (<code>[str](#str)</code>) – The text to search for secret keys

**Returns:**

- <code>[set](#set)\[[str](#str)\]</code> – Set of secret keys found in the text

#### `openhands.sdk.conversation.SecretRegistry.get_secrets_as_env_vars`

```python
get_secrets_as_env_vars(command)
```

Get secrets that should be exported as environment variables for a command.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to check for secret references

**Returns:**

- <code>[dict](#dict)\[[str](#str), [str](#str)\]</code> – Dictionary of environment variables to export (key -> value)

#### `openhands.sdk.conversation.SecretRegistry.mask_secrets_in_output`

```python
mask_secrets_in_output(text)
```

Mask secret values in the given text.

This method uses both the current exported values and attempts to get
fresh values from callables to ensure comprehensive masking.

**Parameters:**

- **text** (<code>[str](#str)</code>) – The text to mask secrets in

**Returns:**

- <code>[str](#str)</code> – Text with secret values replaced by <secret-hidden>

#### `openhands.sdk.conversation.SecretRegistry.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.conversation.SecretRegistry.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.conversation.SecretRegistry.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.conversation.SecretRegistry.model_validate`

```python
model_validate(*args, **kwargs)
```

#### `openhands.sdk.conversation.SecretRegistry.model_validate_json`

```python
model_validate_json(*args, **kwargs)
```

#### `openhands.sdk.conversation.SecretRegistry.secret_sources`

```python
secret_sources: dict[str, SecretSource] = Field(default_factory=dict)
```

#### `openhands.sdk.conversation.SecretRegistry.update_secrets`

```python
update_secrets(secrets)
```

Add or update secrets in the manager.

**Parameters:**

- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\]</code>) – Dictionary mapping secret keys to either string values
  or callable functions that return string values

### `openhands.sdk.conversation.StuckDetector`

```python
StuckDetector(state)
```

Detects when an agent is stuck in repetitive or unproductive patterns.

This detector analyzes the conversation history to identify various stuck patterns:

1. Repeating action-observation cycles
1. Repeating action-error cycles
1. Agent monologue (repeated messages without user input)
1. Repeating alternating action-observation patterns
1. Context window errors indicating memory issues

**Functions:**

- [**is_stuck**](#openhands.sdk.conversation.StuckDetector.is_stuck) – Check if the agent is currently stuck.

**Attributes:**

- [**state**](#openhands.sdk.conversation.StuckDetector.state) (<code>[ConversationState](#openhands.sdk.conversation.state.ConversationState)</code>) –

#### `openhands.sdk.conversation.StuckDetector.is_stuck`

```python
is_stuck()
```

Check if the agent is currently stuck.

#### `openhands.sdk.conversation.StuckDetector.state`

```python
state: ConversationState = state
```

### `openhands.sdk.conversation.base`

**Classes:**

- [**BaseConversation**](#openhands.sdk.conversation.base.BaseConversation) –
- [**ConversationStateProtocol**](#openhands.sdk.conversation.base.ConversationStateProtocol) – Protocol defining the interface for conversation state objects.

#### `openhands.sdk.conversation.base.BaseConversation`

Bases: <code>[ABC](#abc.ABC)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.base.BaseConversation.close) –
- [**compose_callbacks**](#openhands.sdk.conversation.base.BaseConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.base.BaseConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.base.BaseConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.base.BaseConversation.pause) –
- [**reject_pending_actions**](#openhands.sdk.conversation.base.BaseConversation.reject_pending_actions) –
- [**run**](#openhands.sdk.conversation.base.BaseConversation.run) –
- [**send_message**](#openhands.sdk.conversation.base.BaseConversation.send_message) –
- [**set_confirmation_policy**](#openhands.sdk.conversation.base.BaseConversation.set_confirmation_policy) –
- [**update_secrets**](#openhands.sdk.conversation.base.BaseConversation.update_secrets) –

**Attributes:**

- [**confirmation_policy_active**](#openhands.sdk.conversation.base.BaseConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.base.BaseConversation.conversation_stats) (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats)</code>) –
- [**id**](#openhands.sdk.conversation.base.BaseConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.base.BaseConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**state**](#openhands.sdk.conversation.base.BaseConversation.state) (<code>[ConversationStateProtocol](#openhands.sdk.conversation.base.ConversationStateProtocol)</code>) –

##### `openhands.sdk.conversation.base.BaseConversation.close`

```python
close()
```

##### `openhands.sdk.conversation.base.BaseConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

##### `openhands.sdk.conversation.base.BaseConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

##### `openhands.sdk.conversation.base.BaseConversation.conversation_stats`

```python
conversation_stats: ConversationStats
```

##### `openhands.sdk.conversation.base.BaseConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.llm.LLM) | None</code>) – Optional LLM to use for title generation. If not provided,
  uses the agent's LLM.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If no user messages are found in the conversation.

##### `openhands.sdk.conversation.base.BaseConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

##### `openhands.sdk.conversation.base.BaseConversation.id`

```python
id: ConversationID
```

##### `openhands.sdk.conversation.base.BaseConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

##### `openhands.sdk.conversation.base.BaseConversation.pause`

```python
pause()
```

##### `openhands.sdk.conversation.base.BaseConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

##### `openhands.sdk.conversation.base.BaseConversation.run`

```python
run()
```

##### `openhands.sdk.conversation.base.BaseConversation.send_message`

```python
send_message(message)
```

##### `openhands.sdk.conversation.base.BaseConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

##### `openhands.sdk.conversation.base.BaseConversation.state`

```python
state: ConversationStateProtocol
```

##### `openhands.sdk.conversation.base.BaseConversation.update_secrets`

```python
update_secrets(secrets)
```

#### `openhands.sdk.conversation.base.ConversationStateProtocol`

Bases: <code>[Protocol](#typing.Protocol)</code>

Protocol defining the interface for conversation state objects.

**Attributes:**

- [**activated_knowledge_skills**](#openhands.sdk.conversation.base.ConversationStateProtocol.activated_knowledge_skills) (<code>[list](#list)\[[str](#str)\]</code>) – List of activated knowledge skills.
- [**agent**](#openhands.sdk.conversation.base.ConversationStateProtocol.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) – The agent running in the conversation.
- [**agent_status**](#openhands.sdk.conversation.base.ConversationStateProtocol.agent_status) (<code>[AgentExecutionStatus](#openhands.sdk.conversation.state.AgentExecutionStatus)</code>) – The current agent execution status.
- [**confirmation_policy**](#openhands.sdk.conversation.base.ConversationStateProtocol.confirmation_policy) (<code>[ConfirmationPolicyBase](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)</code>) – The confirmation policy.
- [**events**](#openhands.sdk.conversation.base.ConversationStateProtocol.events) (<code>[EventsListBase](#openhands.sdk.conversation.events_list_base.EventsListBase)</code>) – Access to the events list.
- [**id**](#openhands.sdk.conversation.base.ConversationStateProtocol.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) – The conversation ID.
- [**persistence_dir**](#openhands.sdk.conversation.base.ConversationStateProtocol.persistence_dir) (<code>[str](#str) | None</code>) – The persistence directory from the FileStore.
- [**workspace**](#openhands.sdk.conversation.base.ConversationStateProtocol.workspace) (<code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>) – The workspace for agent operations and tool execution.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.activated_knowledge_skills`

```python
activated_knowledge_skills: list[str]
```

List of activated knowledge skills.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.agent`

```python
agent: AgentBase
```

The agent running in the conversation.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.agent_status`

```python
agent_status: AgentExecutionStatus
```

The current agent execution status.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.confirmation_policy`

```python
confirmation_policy: ConfirmationPolicyBase
```

The confirmation policy.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.events`

```python
events: EventsListBase
```

Access to the events list.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.id`

```python
id: ConversationID
```

The conversation ID.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.persistence_dir`

```python
persistence_dir: str | None
```

The persistence directory from the FileStore.

If None, it means the conversation is not being persisted.

##### `openhands.sdk.conversation.base.ConversationStateProtocol.workspace`

```python
workspace: BaseWorkspace
```

The workspace for agent operations and tool execution.

### `openhands.sdk.conversation.conversation`

**Classes:**

- [**Conversation**](#openhands.sdk.conversation.conversation.Conversation) – Factory entrypoint that returns a LocalConversation or RemoteConversation.

**Attributes:**

- [**logger**](#openhands.sdk.conversation.conversation.logger) –

#### `openhands.sdk.conversation.conversation.Conversation`

Factory entrypoint that returns a LocalConversation or RemoteConversation.

<details class="usage" open markdown="1">
<summary>Usage</summary>

- Conversation(agent=...) -> LocalConversation
- Conversation(agent=..., host="http://...") -> RemoteConversation

</details>

#### `openhands.sdk.conversation.conversation.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.conversation_stats`

**Classes:**

- [**ConversationStats**](#openhands.sdk.conversation.conversation_stats.ConversationStats) – Track per-LLM usage metrics observed during conversations.

**Attributes:**

- [**RESTORED_SERVICES_DEPRECATION_MSG**](#openhands.sdk.conversation.conversation_stats.RESTORED_SERVICES_DEPRECATION_MSG) –
- [**SERVICE_TO_USAGE_DEPRECATION_MSG**](#openhands.sdk.conversation.conversation_stats.SERVICE_TO_USAGE_DEPRECATION_MSG) –
- [**logger**](#openhands.sdk.conversation.conversation_stats.logger) –

#### `openhands.sdk.conversation.conversation_stats.ConversationStats`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Track per-LLM usage metrics observed during conversations.

**Functions:**

- [**get_combined_metrics**](#openhands.sdk.conversation.conversation_stats.ConversationStats.get_combined_metrics) –
- [**get_metrics_for_service**](#openhands.sdk.conversation.conversation_stats.ConversationStats.get_metrics_for_service) –
- [**get_metrics_for_usage**](#openhands.sdk.conversation.conversation_stats.ConversationStats.get_metrics_for_usage) –
- [**register_llm**](#openhands.sdk.conversation.conversation_stats.ConversationStats.register_llm) –

**Attributes:**

- [**service_to_metrics**](#openhands.sdk.conversation.conversation_stats.ConversationStats.service_to_metrics) (<code>[dict](#dict)\[[str](#str), [Metrics](#openhands.sdk.llm.utils.metrics.Metrics)\]</code>) –
- [**usage_to_metrics**](#openhands.sdk.conversation.conversation_stats.ConversationStats.usage_to_metrics) (<code>[dict](#dict)\[[str](#str), [Metrics](#openhands.sdk.llm.utils.metrics.Metrics)\]</code>) –

##### `openhands.sdk.conversation.conversation_stats.ConversationStats.get_combined_metrics`

```python
get_combined_metrics()
```

##### `openhands.sdk.conversation.conversation_stats.ConversationStats.get_metrics_for_service`

```python
get_metrics_for_service(service_id)
```

##### `openhands.sdk.conversation.conversation_stats.ConversationStats.get_metrics_for_usage`

```python
get_metrics_for_usage(usage_id)
```

##### `openhands.sdk.conversation.conversation_stats.ConversationStats.register_llm`

```python
register_llm(event)
```

##### `openhands.sdk.conversation.conversation_stats.ConversationStats.service_to_metrics`

```python
service_to_metrics: dict[str, Metrics]
```

##### `openhands.sdk.conversation.conversation_stats.ConversationStats.usage_to_metrics`

```python
usage_to_metrics: dict[str, Metrics] = Field(default_factory=dict, validation_alias=(AliasChoices('usage_to_metrics', 'service_to_metrics')), serialization_alias='usage_to_metrics', description='Active usage metrics tracked by the registry.')
```

#### `openhands.sdk.conversation.conversation_stats.RESTORED_SERVICES_DEPRECATION_MSG`

```python
RESTORED_SERVICES_DEPRECATION_MSG = 'ConversationStats._restored_services is deprecated; use _restored_usage_ids instead.'
```

#### `openhands.sdk.conversation.conversation_stats.SERVICE_TO_USAGE_DEPRECATION_MSG`

```python
SERVICE_TO_USAGE_DEPRECATION_MSG = 'ConversationStats.service_to_metrics is deprecated; use usage_to_metrics instead.'
```

#### `openhands.sdk.conversation.conversation_stats.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.event_store`

**Classes:**

- [**EventLog**](#openhands.sdk.conversation.event_store.EventLog) –

**Attributes:**

- [**logger**](#openhands.sdk.conversation.event_store.logger) –

#### `openhands.sdk.conversation.event_store.EventLog`

```python
EventLog(fs, dir_path=EVENTS_DIR)
```

Bases: <code>[EventsListBase](#openhands.sdk.conversation.events_list_base.EventsListBase)</code>

**Functions:**

- [**append**](#openhands.sdk.conversation.event_store.EventLog.append) –
- [**get_id**](#openhands.sdk.conversation.event_store.EventLog.get_id) – Return the event_id for a given index.
- [**get_index**](#openhands.sdk.conversation.event_store.EventLog.get_index) – Return the integer index for a given event_id.

##### `openhands.sdk.conversation.event_store.EventLog.append`

```python
append(event)
```

##### `openhands.sdk.conversation.event_store.EventLog.get_id`

```python
get_id(idx)
```

Return the event_id for a given index.

##### `openhands.sdk.conversation.event_store.EventLog.get_index`

```python
get_index(event_id)
```

Return the integer index for a given event_id.

#### `openhands.sdk.conversation.event_store.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.events_list_base`

**Classes:**

- [**EventsListBase**](#openhands.sdk.conversation.events_list_base.EventsListBase) – Abstract base class for event lists that can be appended to.

#### `openhands.sdk.conversation.events_list_base.EventsListBase`

Bases: <code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.Event)\]</code>, <code>[ABC](#abc.ABC)</code>

Abstract base class for event lists that can be appended to.

This provides a common interface for both local EventLog and remote
RemoteEventsList implementations, avoiding circular imports in protocols.

**Functions:**

- [**append**](#openhands.sdk.conversation.events_list_base.EventsListBase.append) – Add a new event to the list.

##### `openhands.sdk.conversation.events_list_base.EventsListBase.append`

```python
append(event)
```

Add a new event to the list.

### `openhands.sdk.conversation.exceptions`

**Classes:**

- [**ConversationRunError**](#openhands.sdk.conversation.exceptions.ConversationRunError) – Raised when a conversation run fails.

#### `openhands.sdk.conversation.exceptions.ConversationRunError`

```python
ConversationRunError(conversation_id, original_exception, message=None)
```

Bases: <code>[RuntimeError](#RuntimeError)</code>

Raised when a conversation run fails.

Carries the conversation_id to make resuming/debugging easier while
preserving the original exception via exception chaining.

**Attributes:**

- [**conversation_id**](#openhands.sdk.conversation.exceptions.ConversationRunError.conversation_id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**original_exception**](#openhands.sdk.conversation.exceptions.ConversationRunError.original_exception) (<code>[BaseException](#BaseException)</code>) –

##### `openhands.sdk.conversation.exceptions.ConversationRunError.conversation_id`

```python
conversation_id: ConversationID = conversation_id
```

##### `openhands.sdk.conversation.exceptions.ConversationRunError.original_exception`

```python
original_exception: BaseException = original_exception
```

### `openhands.sdk.conversation.fifo_lock`

FIFO Lock implementation that guarantees first-in-first-out access ordering.

This provides fair lock access where threads acquire the lock in the exact order
they requested it, preventing starvation that can occur with standard RLock.

**Classes:**

- [**FIFOLock**](#openhands.sdk.conversation.fifo_lock.FIFOLock) – A reentrant lock that guarantees FIFO (first-in-first-out) access ordering.

#### `openhands.sdk.conversation.fifo_lock.FIFOLock`

```python
FIFOLock()
```

A reentrant lock that guarantees FIFO (first-in-first-out) access ordering.

Unlike Python's standard RLock, this lock ensures that threads acquire
the lock in the exact order they requested it, providing fairness and
preventing lock starvation.

Features:

- Reentrant: Same thread can acquire multiple times
- FIFO ordering: Threads get lock in request order
- Context manager support: Use with 'with' statement
- Thread-safe: Safe for concurrent access

**Functions:**

- [**acquire**](#openhands.sdk.conversation.fifo_lock.FIFOLock.acquire) – Acquire the lock.
- [**locked**](#openhands.sdk.conversation.fifo_lock.FIFOLock.locked) – Return True if the lock is currently held by any thread.
- [**owned**](#openhands.sdk.conversation.fifo_lock.FIFOLock.owned) – Return True if the lock is currently held by the calling thread.
- [**release**](#openhands.sdk.conversation.fifo_lock.FIFOLock.release) – Release the lock.

##### `openhands.sdk.conversation.fifo_lock.FIFOLock.acquire`

```python
acquire(blocking=True, timeout=-1)
```

Acquire the lock.

**Parameters:**

- **blocking** (<code>[bool](#bool)</code>) – If True, block until lock is acquired. If False, return
  immediately.
- **timeout** (<code>[float](#float)</code>) – Maximum time to wait for lock (ignored if blocking=False).
  -1 means wait indefinitely.

**Returns:**

- <code>[bool](#bool)</code> – True if lock was acquired, False otherwise.

##### `openhands.sdk.conversation.fifo_lock.FIFOLock.locked`

```python
locked()
```

Return True if the lock is currently held by any thread.

##### `openhands.sdk.conversation.fifo_lock.FIFOLock.owned`

```python
owned()
```

Return True if the lock is currently held by the calling thread.

##### `openhands.sdk.conversation.fifo_lock.FIFOLock.release`

```python
release()
```

Release the lock.

**Raises:**

- <code>[RuntimeError](#RuntimeError)</code> – If the current thread doesn't own the lock.

### `openhands.sdk.conversation.get_agent_final_response`

```python
get_agent_final_response(events)
```

Extract the final response from the agent.

An agent can end a conversation in two ways:

1. By calling the finish tool
1. By returning a text message with no tool calls

**Parameters:**

- **events** (<code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.base.Event)\]</code>) – List of conversation events to search through.

**Returns:**

- <code>[str](#str)</code> – The final response message from the agent, or empty string if not found.

### `openhands.sdk.conversation.impl`

**Modules:**

- [**local_conversation**](#openhands.sdk.conversation.impl.local_conversation) –
- [**remote_conversation**](#openhands.sdk.conversation.impl.remote_conversation) –

**Classes:**

- [**LocalConversation**](#openhands.sdk.conversation.impl.LocalConversation) –
- [**RemoteConversation**](#openhands.sdk.conversation.impl.RemoteConversation) –

#### `openhands.sdk.conversation.impl.LocalConversation`

```python
LocalConversation(agent, workspace, persistence_dir=None, conversation_id=None, callbacks=None, max_iteration_per_run=500, stuck_detection=True, visualize=True, name_for_visualization=None, secrets=None, **_)
```

Bases: <code>[BaseConversation](#openhands.sdk.conversation.base.BaseConversation)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.impl.LocalConversation.close) – Close the conversation and clean up all tool executors.
- [**compose_callbacks**](#openhands.sdk.conversation.impl.LocalConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.impl.LocalConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.impl.LocalConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.impl.LocalConversation.pause) – Pause agent execution.
- [**reject_pending_actions**](#openhands.sdk.conversation.impl.LocalConversation.reject_pending_actions) – Reject all pending actions from the agent.
- [**run**](#openhands.sdk.conversation.impl.LocalConversation.run) – Runs the conversation until the agent finishes.
- [**send_message**](#openhands.sdk.conversation.impl.LocalConversation.send_message) – Send a message to the agent.
- [**set_confirmation_policy**](#openhands.sdk.conversation.impl.LocalConversation.set_confirmation_policy) – Set the confirmation policy and store it in conversation state.
- [**update_secrets**](#openhands.sdk.conversation.impl.LocalConversation.update_secrets) – Add secrets to the conversation.

**Attributes:**

- [**agent**](#openhands.sdk.conversation.impl.LocalConversation.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**confirmation_policy_active**](#openhands.sdk.conversation.impl.LocalConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.impl.LocalConversation.conversation_stats) –
- [**id**](#openhands.sdk.conversation.impl.LocalConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) – Get the unique ID of the conversation.
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.impl.LocalConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**llm_registry**](#openhands.sdk.conversation.impl.LocalConversation.llm_registry) (<code>[LLMRegistry](#openhands.sdk.llm.llm_registry.LLMRegistry)</code>) –
- [**max_iteration_per_run**](#openhands.sdk.conversation.impl.LocalConversation.max_iteration_per_run) (<code>[int](#int)</code>) –
- [**state**](#openhands.sdk.conversation.impl.LocalConversation.state) (<code>[ConversationState](#openhands.sdk.conversation.state.ConversationState)</code>) – Get the conversation state.
- [**stuck_detector**](#openhands.sdk.conversation.impl.LocalConversation.stuck_detector) (<code>[StuckDetector](#openhands.sdk.conversation.stuck_detector.StuckDetector) | None</code>) – Get the stuck detector instance if enabled.
- [**workspace**](#openhands.sdk.conversation.impl.LocalConversation.workspace) (<code>[LocalWorkspace](#openhands.sdk.workspace.LocalWorkspace)</code>) –

**Parameters:**

- **agent** (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) – The agent to use for the conversation
- **workspace** (<code>[str](#str) | [LocalWorkspace](#openhands.sdk.workspace.LocalWorkspace)</code>) – Working directory for agent operations and tool execution
- **persistence_dir** (<code>[str](#str) | None</code>) – Directory for persisting conversation state and events
- **conversation_id** (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID) | None</code>) – Optional ID for the conversation. If provided, will
  be used to identify the conversation. The user might want to
  suffix their persistent filestore with this ID.
- **callbacks** (<code>[list](#list)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\] | None</code>) – Optional list of callback functions to handle events
- **max_iteration_per_run** (<code>[int](#int)</code>) – Maximum number of iterations per run
- **visualize** (<code>[bool](#bool)</code>) – Whether to enable default visualization. If True, adds
  a default visualizer callback. If False, relies on
  application to provide visualization through callbacks.
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.
- **stuck_detection** (<code>[bool](#bool)</code>) – Whether to enable stuck detection

##### `openhands.sdk.conversation.impl.LocalConversation.agent`

```python
agent: AgentBase = agent
```

##### `openhands.sdk.conversation.impl.LocalConversation.close`

```python
close()
```

Close the conversation and clean up all tool executors.

##### `openhands.sdk.conversation.impl.LocalConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

##### `openhands.sdk.conversation.impl.LocalConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

##### `openhands.sdk.conversation.impl.LocalConversation.conversation_stats`

```python
conversation_stats
```

##### `openhands.sdk.conversation.impl.LocalConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.LLM) | None</code>) – Optional LLM to use for title generation. If not provided,
  uses self.agent.llm.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If no user messages are found in the conversation.

##### `openhands.sdk.conversation.impl.LocalConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

##### `openhands.sdk.conversation.impl.LocalConversation.id`

```python
id: ConversationID
```

Get the unique ID of the conversation.

##### `openhands.sdk.conversation.impl.LocalConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

##### `openhands.sdk.conversation.impl.LocalConversation.llm_registry`

```python
llm_registry: LLMRegistry = LLMRegistry()
```

##### `openhands.sdk.conversation.impl.LocalConversation.max_iteration_per_run`

```python
max_iteration_per_run: int = max_iteration_per_run
```

##### `openhands.sdk.conversation.impl.LocalConversation.pause`

```python
pause()
```

Pause agent execution.

This method can be called from any thread to request that the agent
pause execution. The pause will take effect at the next iteration
of the run loop (between agent steps).

Note: If called during an LLM completion, the pause will not take
effect until the current LLM call completes.

##### `openhands.sdk.conversation.impl.LocalConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

Reject all pending actions from the agent.

This is a non-invasive method to reject actions between run() calls.
Also clears the agent_waiting_for_confirmation flag.

##### `openhands.sdk.conversation.impl.LocalConversation.run`

```python
run()
```

Runs the conversation until the agent finishes.

In confirmation mode:

- First call: creates actions but doesn't execute them, stops and waits
- Second call: executes pending actions (implicit confirmation)

In normal mode:

- Creates and executes actions immediately

Can be paused between steps

##### `openhands.sdk.conversation.impl.LocalConversation.send_message`

```python
send_message(message)
```

Send a message to the agent.

**Parameters:**

- **message** (<code>[str](#str) | [Message](#openhands.sdk.llm.Message)</code>) – Either a string (which will be converted to a user message)
  or a Message object

##### `openhands.sdk.conversation.impl.LocalConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

Set the confirmation policy and store it in conversation state.

##### `openhands.sdk.conversation.impl.LocalConversation.state`

```python
state: ConversationState
```

Get the conversation state.

It returns a protocol that has a subset of ConversationState methods
and properties. We will have the ability to access the same properties
of ConversationState on a remote conversation object.
But we won't be able to access methods that mutate the state.

##### `openhands.sdk.conversation.impl.LocalConversation.stuck_detector`

```python
stuck_detector: StuckDetector | None
```

Get the stuck detector instance if enabled.

##### `openhands.sdk.conversation.impl.LocalConversation.update_secrets`

```python
update_secrets(secrets)
```

Add secrets to the conversation.

**Parameters:**

- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\]</code>) – Dictionary mapping secret keys to values or no-arg callables.
  SecretValue = str | Callable\[[], str\]. Callables are invoked lazily
  when a command references the secret key.

##### `openhands.sdk.conversation.impl.LocalConversation.workspace`

```python
workspace: LocalWorkspace = workspace
```

#### `openhands.sdk.conversation.impl.RemoteConversation`

```python
RemoteConversation(agent, workspace, conversation_id=None, callbacks=None, max_iteration_per_run=500, stuck_detection=True, visualize=False, name_for_visualization=None, secrets=None, **_)
```

Bases: <code>[BaseConversation](#openhands.sdk.conversation.base.BaseConversation)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.impl.RemoteConversation.close) –
- [**compose_callbacks**](#openhands.sdk.conversation.impl.RemoteConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.impl.RemoteConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.impl.RemoteConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.impl.RemoteConversation.pause) –
- [**reject_pending_actions**](#openhands.sdk.conversation.impl.RemoteConversation.reject_pending_actions) –
- [**run**](#openhands.sdk.conversation.impl.RemoteConversation.run) –
- [**send_message**](#openhands.sdk.conversation.impl.RemoteConversation.send_message) –
- [**set_confirmation_policy**](#openhands.sdk.conversation.impl.RemoteConversation.set_confirmation_policy) –
- [**update_secrets**](#openhands.sdk.conversation.impl.RemoteConversation.update_secrets) –

**Attributes:**

- [**agent**](#openhands.sdk.conversation.impl.RemoteConversation.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**confirmation_policy_active**](#openhands.sdk.conversation.impl.RemoteConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.impl.RemoteConversation.conversation_stats) (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats)</code>) – Get conversation stats from remote server.
- [**id**](#openhands.sdk.conversation.impl.RemoteConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.impl.RemoteConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**max_iteration_per_run**](#openhands.sdk.conversation.impl.RemoteConversation.max_iteration_per_run) (<code>[int](#int)</code>) –
- [**state**](#openhands.sdk.conversation.impl.RemoteConversation.state) (<code>[RemoteState](#openhands.sdk.conversation.impl.remote_conversation.RemoteState)</code>) – Access to remote conversation state.
- [**stuck_detector**](#openhands.sdk.conversation.impl.RemoteConversation.stuck_detector) – Stuck detector for compatibility.
- [**workspace**](#openhands.sdk.conversation.impl.RemoteConversation.workspace) (<code>[RemoteWorkspace](#openhands.sdk.workspace.RemoteWorkspace)</code>) –

**Parameters:**

- **agent** (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) – Agent configuration (will be sent to the server)
- **workspace** (<code>[RemoteWorkspace](#openhands.sdk.workspace.RemoteWorkspace)</code>) – The working directory for agent operations and tool execution.
- **conversation_id** (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID) | None</code>) – Optional existing conversation id to attach to
- **callbacks** (<code>[list](#list)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\] | None</code>) – Optional callbacks to receive events (not yet streamed)
- **max_iteration_per_run** (<code>[int](#int)</code>) – Max iterations configured on server
- **stuck_detection** (<code>[bool](#bool)</code>) – Whether to enable stuck detection on server
- **visualize** (<code>[bool](#bool)</code>) – Whether to enable the default visualizer callback
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.
- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\] | None</code>) – Optional secrets to initialize the conversation with

##### `openhands.sdk.conversation.impl.RemoteConversation.agent`

```python
agent: AgentBase = agent
```

##### `openhands.sdk.conversation.impl.RemoteConversation.close`

```python
close()
```

##### `openhands.sdk.conversation.impl.RemoteConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

##### `openhands.sdk.conversation.impl.RemoteConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

##### `openhands.sdk.conversation.impl.RemoteConversation.conversation_stats`

```python
conversation_stats: ConversationStats
```

Get conversation stats from remote server.

##### `openhands.sdk.conversation.impl.RemoteConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.LLM) | None</code>) – Optional LLM to use for title generation. If provided, its usage_id
  will be sent to the server. If not provided, uses the agent's LLM.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

##### `openhands.sdk.conversation.impl.RemoteConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

##### `openhands.sdk.conversation.impl.RemoteConversation.id`

```python
id: ConversationID
```

##### `openhands.sdk.conversation.impl.RemoteConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

##### `openhands.sdk.conversation.impl.RemoteConversation.max_iteration_per_run`

```python
max_iteration_per_run: int = max_iteration_per_run
```

##### `openhands.sdk.conversation.impl.RemoteConversation.pause`

```python
pause()
```

##### `openhands.sdk.conversation.impl.RemoteConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

##### `openhands.sdk.conversation.impl.RemoteConversation.run`

```python
run()
```

##### `openhands.sdk.conversation.impl.RemoteConversation.send_message`

```python
send_message(message)
```

##### `openhands.sdk.conversation.impl.RemoteConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

##### `openhands.sdk.conversation.impl.RemoteConversation.state`

```python
state: RemoteState
```

Access to remote conversation state.

##### `openhands.sdk.conversation.impl.RemoteConversation.stuck_detector`

```python
stuck_detector
```

Stuck detector for compatibility.
Not implemented for remote conversations.

##### `openhands.sdk.conversation.impl.RemoteConversation.update_secrets`

```python
update_secrets(secrets)
```

##### `openhands.sdk.conversation.impl.RemoteConversation.workspace`

```python
workspace: RemoteWorkspace = workspace
```

#### `openhands.sdk.conversation.impl.local_conversation`

**Classes:**

- [**LocalConversation**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation) –

**Attributes:**

- [**logger**](#openhands.sdk.conversation.impl.local_conversation.logger) –

##### `openhands.sdk.conversation.impl.local_conversation.LocalConversation`

```python
LocalConversation(agent, workspace, persistence_dir=None, conversation_id=None, callbacks=None, max_iteration_per_run=500, stuck_detection=True, visualize=True, name_for_visualization=None, secrets=None, **_)
```

Bases: <code>[BaseConversation](#openhands.sdk.conversation.base.BaseConversation)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.close) – Close the conversation and clean up all tool executors.
- [**compose_callbacks**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.pause) – Pause agent execution.
- [**reject_pending_actions**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.reject_pending_actions) – Reject all pending actions from the agent.
- [**run**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.run) – Runs the conversation until the agent finishes.
- [**send_message**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.send_message) – Send a message to the agent.
- [**set_confirmation_policy**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.set_confirmation_policy) – Set the confirmation policy and store it in conversation state.
- [**update_secrets**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.update_secrets) – Add secrets to the conversation.

**Attributes:**

- [**agent**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**confirmation_policy_active**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.conversation_stats) –
- [**id**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) – Get the unique ID of the conversation.
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**llm_registry**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.llm_registry) (<code>[LLMRegistry](#openhands.sdk.llm.llm_registry.LLMRegistry)</code>) –
- [**max_iteration_per_run**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.max_iteration_per_run) (<code>[int](#int)</code>) –
- [**state**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.state) (<code>[ConversationState](#openhands.sdk.conversation.state.ConversationState)</code>) – Get the conversation state.
- [**stuck_detector**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.stuck_detector) (<code>[StuckDetector](#openhands.sdk.conversation.stuck_detector.StuckDetector) | None</code>) – Get the stuck detector instance if enabled.
- [**workspace**](#openhands.sdk.conversation.impl.local_conversation.LocalConversation.workspace) (<code>[LocalWorkspace](#openhands.sdk.workspace.LocalWorkspace)</code>) –

**Parameters:**

- **agent** (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) – The agent to use for the conversation
- **workspace** (<code>[str](#str) | [LocalWorkspace](#openhands.sdk.workspace.LocalWorkspace)</code>) – Working directory for agent operations and tool execution
- **persistence_dir** (<code>[str](#str) | None</code>) – Directory for persisting conversation state and events
- **conversation_id** (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID) | None</code>) – Optional ID for the conversation. If provided, will
  be used to identify the conversation. The user might want to
  suffix their persistent filestore with this ID.
- **callbacks** (<code>[list](#list)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\] | None</code>) – Optional list of callback functions to handle events
- **max_iteration_per_run** (<code>[int](#int)</code>) – Maximum number of iterations per run
- **visualize** (<code>[bool](#bool)</code>) – Whether to enable default visualization. If True, adds
  a default visualizer callback. If False, relies on
  application to provide visualization through callbacks.
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.
- **stuck_detection** (<code>[bool](#bool)</code>) – Whether to enable stuck detection

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.agent`

```python
agent: AgentBase = agent
```

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.close`

```python
close()
```

Close the conversation and clean up all tool executors.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.conversation_stats`

```python
conversation_stats
```

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.LLM) | None</code>) – Optional LLM to use for title generation. If not provided,
  uses self.agent.llm.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If no user messages are found in the conversation.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.id`

```python
id: ConversationID
```

Get the unique ID of the conversation.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.llm_registry`

```python
llm_registry: LLMRegistry = LLMRegistry()
```

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.max_iteration_per_run`

```python
max_iteration_per_run: int = max_iteration_per_run
```

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.pause`

```python
pause()
```

Pause agent execution.

This method can be called from any thread to request that the agent
pause execution. The pause will take effect at the next iteration
of the run loop (between agent steps).

Note: If called during an LLM completion, the pause will not take
effect until the current LLM call completes.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

Reject all pending actions from the agent.

This is a non-invasive method to reject actions between run() calls.
Also clears the agent_waiting_for_confirmation flag.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.run`

```python
run()
```

Runs the conversation until the agent finishes.

In confirmation mode:

- First call: creates actions but doesn't execute them, stops and waits
- Second call: executes pending actions (implicit confirmation)

In normal mode:

- Creates and executes actions immediately

Can be paused between steps

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.send_message`

```python
send_message(message)
```

Send a message to the agent.

**Parameters:**

- **message** (<code>[str](#str) | [Message](#openhands.sdk.llm.Message)</code>) – Either a string (which will be converted to a user message)
  or a Message object

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

Set the confirmation policy and store it in conversation state.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.state`

```python
state: ConversationState
```

Get the conversation state.

It returns a protocol that has a subset of ConversationState methods
and properties. We will have the ability to access the same properties
of ConversationState on a remote conversation object.
But we won't be able to access methods that mutate the state.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.stuck_detector`

```python
stuck_detector: StuckDetector | None
```

Get the stuck detector instance if enabled.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.update_secrets`

```python
update_secrets(secrets)
```

Add secrets to the conversation.

**Parameters:**

- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\]</code>) – Dictionary mapping secret keys to values or no-arg callables.
  SecretValue = str | Callable\[[], str\]. Callables are invoked lazily
  when a command references the secret key.

###### `openhands.sdk.conversation.impl.local_conversation.LocalConversation.workspace`

```python
workspace: LocalWorkspace = workspace
```

##### `openhands.sdk.conversation.impl.local_conversation.logger`

```python
logger = get_logger(__name__)
```

#### `openhands.sdk.conversation.impl.remote_conversation`

**Classes:**

- [**RemoteConversation**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation) –
- [**RemoteEventsList**](#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList) – A list-like, read-only view of remote conversation events.
- [**RemoteState**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState) – A state-like interface for accessing remote conversation state.
- [**WebSocketCallbackClient**](#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient) – Minimal WS client: connects, forwards events, retries on error.

**Attributes:**

- [**logger**](#openhands.sdk.conversation.impl.remote_conversation.logger) –

##### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation`

```python
RemoteConversation(agent, workspace, conversation_id=None, callbacks=None, max_iteration_per_run=500, stuck_detection=True, visualize=False, name_for_visualization=None, secrets=None, **_)
```

Bases: <code>[BaseConversation](#openhands.sdk.conversation.base.BaseConversation)</code>

**Functions:**

- [**close**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.close) –
- [**compose_callbacks**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.compose_callbacks) – Compose multiple callbacks into a single callback function.
- [**generate_title**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.generate_title) – Generate a title for the conversation based on the first user message.
- [**get_persistence_dir**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.get_persistence_dir) – Get the persistence directory for the conversation.
- [**pause**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.pause) –
- [**reject_pending_actions**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.reject_pending_actions) –
- [**run**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.run) –
- [**send_message**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.send_message) –
- [**set_confirmation_policy**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.set_confirmation_policy) –
- [**update_secrets**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.update_secrets) –

**Attributes:**

- [**agent**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**confirmation_policy_active**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.confirmation_policy_active) (<code>[bool](#bool)</code>) –
- [**conversation_stats**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.conversation_stats) (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats)</code>) – Get conversation stats from remote server.
- [**id**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**is_confirmation_mode_active**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.is_confirmation_mode_active) (<code>[bool](#bool)</code>) – Check if confirmation mode is active.
- [**max_iteration_per_run**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.max_iteration_per_run) (<code>[int](#int)</code>) –
- [**state**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.state) (<code>[RemoteState](#openhands.sdk.conversation.impl.remote_conversation.RemoteState)</code>) – Access to remote conversation state.
- [**stuck_detector**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.stuck_detector) – Stuck detector for compatibility.
- [**workspace**](#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.workspace) (<code>[RemoteWorkspace](#openhands.sdk.workspace.RemoteWorkspace)</code>) –

**Parameters:**

- **agent** (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) – Agent configuration (will be sent to the server)
- **workspace** (<code>[RemoteWorkspace](#openhands.sdk.workspace.RemoteWorkspace)</code>) – The working directory for agent operations and tool execution.
- **conversation_id** (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID) | None</code>) – Optional existing conversation id to attach to
- **callbacks** (<code>[list](#list)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\] | None</code>) – Optional callbacks to receive events (not yet streamed)
- **max_iteration_per_run** (<code>[int](#int)</code>) – Max iterations configured on server
- **stuck_detection** (<code>[bool](#bool)</code>) – Whether to enable stuck detection on server
- **visualize** (<code>[bool](#bool)</code>) – Whether to enable the default visualizer callback
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.
- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\] | None</code>) – Optional secrets to initialize the conversation with

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.agent`

```python
agent: AgentBase = agent
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.close`

```python
close()
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.compose_callbacks`

```python
compose_callbacks(callbacks)
```

Compose multiple callbacks into a single callback function.

**Parameters:**

- **callbacks** (<code>[Iterable](#collections.abc.Iterable)\[[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)\]</code>) – An iterable of callback functions

**Returns:**

- <code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code> – A single callback function that calls all provided callbacks

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.confirmation_policy_active`

```python
confirmation_policy_active: bool
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.conversation_stats`

```python
conversation_stats: ConversationStats
```

Get conversation stats from remote server.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.generate_title`

```python
generate_title(llm=None, max_length=50)
```

Generate a title for the conversation based on the first user message.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.LLM) | None</code>) – Optional LLM to use for title generation. If provided, its usage_id
  will be sent to the server. If not provided, uses the agent's LLM.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.get_persistence_dir`

```python
get_persistence_dir(persistence_base_dir, conversation_id)
```

Get the persistence directory for the conversation.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.id`

```python
id: ConversationID
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.is_confirmation_mode_active`

```python
is_confirmation_mode_active: bool
```

Check if confirmation mode is active.

Returns True if BOTH conditions are met:

1. The agent has a security analyzer set (not None)
1. The confirmation policy is active

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.max_iteration_per_run`

```python
max_iteration_per_run: int = max_iteration_per_run
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.pause`

```python
pause()
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.reject_pending_actions`

```python
reject_pending_actions(reason='User rejected the action')
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.run`

```python
run()
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.send_message`

```python
send_message(message)
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.set_confirmation_policy`

```python
set_confirmation_policy(policy)
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.state`

```python
state: RemoteState
```

Access to remote conversation state.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.stuck_detector`

```python
stuck_detector
```

Stuck detector for compatibility.
Not implemented for remote conversations.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.update_secrets`

```python
update_secrets(secrets)
```

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.workspace`

```python
workspace: RemoteWorkspace = workspace
```

##### `openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList`

```python
RemoteEventsList(client, conversation_id)
```

Bases: <code>[EventsListBase](#openhands.sdk.conversation.events_list_base.EventsListBase)</code>

A list-like, read-only view of remote conversation events.

On first access it fetches existing events from the server. Afterwards,
it relies on the WebSocket stream to incrementally append new events.

**Functions:**

- [**add_event**](#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.add_event) – Add a new event to the local cache (called by WebSocket callback).
- [**append**](#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.append) – Add a new event to the list (for compatibility with EventLog interface).
- [**create_default_callback**](#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.create_default_callback) – Create a default callback that adds events to this list.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.add_event`

```python
add_event(event)
```

Add a new event to the local cache (called by WebSocket callback).

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.append`

```python
append(event)
```

Add a new event to the list (for compatibility with EventLog interface).

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.create_default_callback`

```python
create_default_callback()
```

Create a default callback that adds events to this list.

##### `openhands.sdk.conversation.impl.remote_conversation.RemoteState`

```python
RemoteState(client, conversation_id)
```

Bases: <code>[ConversationStateProtocol](#openhands.sdk.conversation.base.ConversationStateProtocol)</code>

A state-like interface for accessing remote conversation state.

**Functions:**

- [**create_state_update_callback**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.create_state_update_callback) – Create a callback that updates state from ConversationStateUpdateEvent.
- [**model_dump**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.model_dump) – Get a dictionary representation of the remote state.
- [**model_dump_json**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.model_dump_json) – Get a JSON representation of the remote state.
- [**update_state_from_event**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.update_state_from_event) – Update cached state from a ConversationStateUpdateEvent.

**Attributes:**

- [**activated_knowledge_skills**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.activated_knowledge_skills) (<code>[list](#list)\[[str](#str)\]</code>) – List of activated knowledge skills.
- [**agent**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.agent) – The agent configuration (fetched from remote).
- [**agent_status**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.agent_status) (<code>[AgentExecutionStatus](#openhands.sdk.conversation.state.AgentExecutionStatus)</code>) – The current agent execution status.
- [**confirmation_policy**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.confirmation_policy) (<code>[ConfirmationPolicyBase](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)</code>) – The confirmation policy.
- [**events**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.events) (<code>[RemoteEventsList](#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList)</code>) – Access to the events list.
- [**id**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) – The conversation ID.
- [**persistence_dir**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.persistence_dir) – The persistence directory (fetched from remote).
- [**workspace**](#openhands.sdk.conversation.impl.remote_conversation.RemoteState.workspace) – The working directory (fetched from remote).

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.activated_knowledge_skills`

```python
activated_knowledge_skills: list[str]
```

List of activated knowledge skills.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.agent`

```python
agent
```

The agent configuration (fetched from remote).

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.agent_status`

```python
agent_status: AgentExecutionStatus
```

The current agent execution status.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.confirmation_policy`

```python
confirmation_policy: ConfirmationPolicyBase
```

The confirmation policy.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.create_state_update_callback`

```python
create_state_update_callback()
```

Create a callback that updates state from ConversationStateUpdateEvent.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.events`

```python
events: RemoteEventsList
```

Access to the events list.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.id`

```python
id: ConversationID
```

The conversation ID.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.model_dump`

```python
model_dump(**_kwargs)
```

Get a dictionary representation of the remote state.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.model_dump_json`

```python
model_dump_json(**kwargs)
```

Get a JSON representation of the remote state.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.persistence_dir`

```python
persistence_dir
```

The persistence directory (fetched from remote).

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.update_state_from_event`

```python
update_state_from_event(event)
```

Update cached state from a ConversationStateUpdateEvent.

###### `openhands.sdk.conversation.impl.remote_conversation.RemoteState.workspace`

```python
workspace
```

The working directory (fetched from remote).

##### `openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient`

```python
WebSocketCallbackClient(host, conversation_id, callback, api_key=None)
```

Minimal WS client: connects, forwards events, retries on error.

**Functions:**

- [**start**](#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.start) –
- [**stop**](#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.stop) –

**Attributes:**

- [**api_key**](#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.api_key) (<code>[str](#str) | None</code>) –
- [**callback**](#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.callback) (<code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType)</code>) –
- [**conversation_id**](#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.conversation_id) (<code>[str](#str)</code>) –
- [**host**](#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.host) (<code>[str](#str)</code>) –

###### `openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.api_key`

```python
api_key: str | None = api_key
```

###### `openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.callback`

```python
callback: ConversationCallbackType = callback
```

###### `openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.conversation_id`

```python
conversation_id: str = conversation_id
```

###### `openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.host`

```python
host: str = host
```

###### `openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.start`

```python
start()
```

###### `openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.stop`

```python
stop()
```

##### `openhands.sdk.conversation.impl.remote_conversation.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.persistence_const`

**Attributes:**

- [**BASE_STATE**](#openhands.sdk.conversation.persistence_const.BASE_STATE) –
- [**EVENTS_DIR**](#openhands.sdk.conversation.persistence_const.EVENTS_DIR) –
- [**EVENT_FILE_PATTERN**](#openhands.sdk.conversation.persistence_const.EVENT_FILE_PATTERN) –
- [**EVENT_NAME_RE**](#openhands.sdk.conversation.persistence_const.EVENT_NAME_RE) –

#### `openhands.sdk.conversation.persistence_const.BASE_STATE`

```python
BASE_STATE = 'base_state.json'
```

#### `openhands.sdk.conversation.persistence_const.EVENTS_DIR`

```python
EVENTS_DIR = 'events'
```

#### `openhands.sdk.conversation.persistence_const.EVENT_FILE_PATTERN`

```python
EVENT_FILE_PATTERN = 'event-{idx:05d}-{event_id}.json'
```

#### `openhands.sdk.conversation.persistence_const.EVENT_NAME_RE`

```python
EVENT_NAME_RE = re.compile('^event-(?P<idx>\\d{5})-(?P<event_id>[0-9a-fA-F\\-]{8,})\\.json$')
```

### `openhands.sdk.conversation.response_utils`

Utility functions for extracting agent responses from conversation events.

**Functions:**

- [**get_agent_final_response**](#openhands.sdk.conversation.response_utils.get_agent_final_response) – Extract the final response from the agent.

#### `openhands.sdk.conversation.response_utils.get_agent_final_response`

```python
get_agent_final_response(events)
```

Extract the final response from the agent.

An agent can end a conversation in two ways:

1. By calling the finish tool
1. By returning a text message with no tool calls

**Parameters:**

- **events** (<code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.base.Event)\]</code>) – List of conversation events to search through.

**Returns:**

- <code>[str](#str)</code> – The final response message from the agent, or empty string if not found.

### `openhands.sdk.conversation.secret_registry`

Secrets manager for handling sensitive data in conversations.

**Classes:**

- [**SecretRegistry**](#openhands.sdk.conversation.secret_registry.SecretRegistry) – Manages secrets and injects them into bash commands when needed.

**Attributes:**

- [**SecretValue**](#openhands.sdk.conversation.secret_registry.SecretValue) –
- [**logger**](#openhands.sdk.conversation.secret_registry.logger) –

#### `openhands.sdk.conversation.secret_registry.SecretRegistry`

Bases: <code>[OpenHandsModel](#openhands.sdk.utils.models.OpenHandsModel)</code>

Manages secrets and injects them into bash commands when needed.

The secret registry stores a mapping of secret keys to SecretSources
that retrieve the actual secret values. When a bash command is about to be
executed, it scans the command for any secret keys and injects the corresponding
environment variables.

Secret sources will redact / encrypt their sensitive values as appropriate when
serializing, depending on the content of the context. If a context is present
and contains a 'cipher' object, this is used for encryption. If it contains a
boolean 'expose_secrets' flag set to True, secrets are dunped in plain text.
Otherwise secrets are redacted.

Additionally, it tracks the latest exported values to enable consistent masking
even when callable secrets fail on subsequent calls.

**Functions:**

- [**find_secrets_in_text**](#openhands.sdk.conversation.secret_registry.SecretRegistry.find_secrets_in_text) – Find all secret keys mentioned in the given text.
- [**get_secrets_as_env_vars**](#openhands.sdk.conversation.secret_registry.SecretRegistry.get_secrets_as_env_vars) – Get secrets that should be exported as environment variables for a command.
- [**mask_secrets_in_output**](#openhands.sdk.conversation.secret_registry.SecretRegistry.mask_secrets_in_output) – Mask secret values in the given text.
- [**model_dump_json**](#openhands.sdk.conversation.secret_registry.SecretRegistry.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.conversation.secret_registry.SecretRegistry.model_json_schema) –
- [**model_post_init**](#openhands.sdk.conversation.secret_registry.SecretRegistry.model_post_init) –
- [**model_validate**](#openhands.sdk.conversation.secret_registry.SecretRegistry.model_validate) –
- [**model_validate_json**](#openhands.sdk.conversation.secret_registry.SecretRegistry.model_validate_json) –
- [**update_secrets**](#openhands.sdk.conversation.secret_registry.SecretRegistry.update_secrets) – Add or update secrets in the manager.

**Attributes:**

- [**secret_sources**](#openhands.sdk.conversation.secret_registry.SecretRegistry.secret_sources) (<code>[dict](#dict)\[[str](#str), [SecretSource](#openhands.sdk.conversation.secret_source.SecretSource)\]</code>) –

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.find_secrets_in_text`

```python
find_secrets_in_text(text)
```

Find all secret keys mentioned in the given text.

**Parameters:**

- **text** (<code>[str](#str)</code>) – The text to search for secret keys

**Returns:**

- <code>[set](#set)\[[str](#str)\]</code> – Set of secret keys found in the text

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.get_secrets_as_env_vars`

```python
get_secrets_as_env_vars(command)
```

Get secrets that should be exported as environment variables for a command.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to check for secret references

**Returns:**

- <code>[dict](#dict)\[[str](#str), [str](#str)\]</code> – Dictionary of environment variables to export (key -> value)

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.mask_secrets_in_output`

```python
mask_secrets_in_output(text)
```

Mask secret values in the given text.

This method uses both the current exported values and attempts to get
fresh values from callables to ensure comprehensive masking.

**Parameters:**

- **text** (<code>[str](#str)</code>) – The text to mask secrets in

**Returns:**

- <code>[str](#str)</code> – Text with secret values replaced by <secret-hidden>

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.model_validate`

```python
model_validate(*args, **kwargs)
```

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.model_validate_json`

```python
model_validate_json(*args, **kwargs)
```

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.secret_sources`

```python
secret_sources: dict[str, SecretSource] = Field(default_factory=dict)
```

##### `openhands.sdk.conversation.secret_registry.SecretRegistry.update_secrets`

```python
update_secrets(secrets)
```

Add or update secrets in the manager.

**Parameters:**

- **secrets** (<code>[Mapping](#collections.abc.Mapping)\[[str](#str), [SecretValue](#openhands.sdk.conversation.secret_registry.SecretValue)\]</code>) – Dictionary mapping secret keys to either string values
  or callable functions that return string values

#### `openhands.sdk.conversation.secret_registry.SecretValue`

```python
SecretValue = str | SecretSource
```

#### `openhands.sdk.conversation.secret_registry.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.secret_source`

**Classes:**

- [**LookupSecret**](#openhands.sdk.conversation.secret_source.LookupSecret) – A secret looked up from some external url
- [**SecretSource**](#openhands.sdk.conversation.secret_source.SecretSource) – Source for a named secret which may be obtained dynamically
- [**StaticSecret**](#openhands.sdk.conversation.secret_source.StaticSecret) – A secret stored locally

#### `openhands.sdk.conversation.secret_source.LookupSecret`

Bases: <code>[SecretSource](#openhands.sdk.conversation.secret_source.SecretSource)</code>

A secret looked up from some external url

**Functions:**

- [**get_serializable_type**](#openhands.sdk.conversation.secret_source.LookupSecret.get_serializable_type) – Custom method to get the union of all currently loaded
- [**get_value**](#openhands.sdk.conversation.secret_source.LookupSecret.get_value) –
- [**model_dump_json**](#openhands.sdk.conversation.secret_source.LookupSecret.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.conversation.secret_source.LookupSecret.model_json_schema) –
- [**model_post_init**](#openhands.sdk.conversation.secret_source.LookupSecret.model_post_init) –
- [**model_rebuild**](#openhands.sdk.conversation.secret_source.LookupSecret.model_rebuild) –
- [**model_validate**](#openhands.sdk.conversation.secret_source.LookupSecret.model_validate) –
- [**model_validate_json**](#openhands.sdk.conversation.secret_source.LookupSecret.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.conversation.secret_source.LookupSecret.resolve_kind) –

**Attributes:**

- [**description**](#openhands.sdk.conversation.secret_source.LookupSecret.description) (<code>[str](#str) | None</code>) –
- [**headers**](#openhands.sdk.conversation.secret_source.LookupSecret.headers) (<code>[dict](#dict)\[[str](#str), [str](#str)\]</code>) –
- [**kind**](#openhands.sdk.conversation.secret_source.LookupSecret.kind) (<code>[str](#str)</code>) –
- [**url**](#openhands.sdk.conversation.secret_source.LookupSecret.url) (<code>[str](#str)</code>) –

##### `openhands.sdk.conversation.secret_source.LookupSecret.description`

```python
description: str | None = Field(default=None, description='Optional description for this secret')
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.conversation.secret_source.LookupSecret.get_value`

```python
get_value()
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.headers`

```python
headers: dict[str, str] = Field(default_factory=dict)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.conversation.secret_source.LookupSecret.url`

```python
url: str
```

#### `openhands.sdk.conversation.secret_source.SecretSource`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Source for a named secret which may be obtained dynamically

**Functions:**

- [**get_serializable_type**](#openhands.sdk.conversation.secret_source.SecretSource.get_serializable_type) – Custom method to get the union of all currently loaded
- [**get_value**](#openhands.sdk.conversation.secret_source.SecretSource.get_value) – Get the value of a secret in plain text
- [**model_dump_json**](#openhands.sdk.conversation.secret_source.SecretSource.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.conversation.secret_source.SecretSource.model_json_schema) –
- [**model_post_init**](#openhands.sdk.conversation.secret_source.SecretSource.model_post_init) –
- [**model_rebuild**](#openhands.sdk.conversation.secret_source.SecretSource.model_rebuild) –
- [**model_validate**](#openhands.sdk.conversation.secret_source.SecretSource.model_validate) –
- [**model_validate_json**](#openhands.sdk.conversation.secret_source.SecretSource.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.conversation.secret_source.SecretSource.resolve_kind) –

**Attributes:**

- [**description**](#openhands.sdk.conversation.secret_source.SecretSource.description) (<code>[str](#str) | None</code>) –
- [**kind**](#openhands.sdk.conversation.secret_source.SecretSource.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.conversation.secret_source.SecretSource.description`

```python
description: str | None = Field(default=None, description='Optional description for this secret')
```

##### `openhands.sdk.conversation.secret_source.SecretSource.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.conversation.secret_source.SecretSource.get_value`

```python
get_value()
```

Get the value of a secret in plain text

##### `openhands.sdk.conversation.secret_source.SecretSource.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.conversation.secret_source.SecretSource.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.conversation.secret_source.SecretSource.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.SecretSource.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.conversation.secret_source.SecretSource.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.conversation.secret_source.SecretSource.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.SecretSource.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.SecretSource.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.conversation.secret_source.StaticSecret`

Bases: <code>[SecretSource](#openhands.sdk.conversation.secret_source.SecretSource)</code>

A secret stored locally

**Functions:**

- [**get_serializable_type**](#openhands.sdk.conversation.secret_source.StaticSecret.get_serializable_type) – Custom method to get the union of all currently loaded
- [**get_value**](#openhands.sdk.conversation.secret_source.StaticSecret.get_value) –
- [**model_dump_json**](#openhands.sdk.conversation.secret_source.StaticSecret.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.conversation.secret_source.StaticSecret.model_json_schema) –
- [**model_post_init**](#openhands.sdk.conversation.secret_source.StaticSecret.model_post_init) –
- [**model_rebuild**](#openhands.sdk.conversation.secret_source.StaticSecret.model_rebuild) –
- [**model_validate**](#openhands.sdk.conversation.secret_source.StaticSecret.model_validate) –
- [**model_validate_json**](#openhands.sdk.conversation.secret_source.StaticSecret.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.conversation.secret_source.StaticSecret.resolve_kind) –

**Attributes:**

- [**description**](#openhands.sdk.conversation.secret_source.StaticSecret.description) (<code>[str](#str) | None</code>) –
- [**kind**](#openhands.sdk.conversation.secret_source.StaticSecret.kind) (<code>[str](#str)</code>) –
- [**value**](#openhands.sdk.conversation.secret_source.StaticSecret.value) (<code>[SecretStr](#pydantic.SecretStr)</code>) –

##### `openhands.sdk.conversation.secret_source.StaticSecret.description`

```python
description: str | None = Field(default=None, description='Optional description for this secret')
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.conversation.secret_source.StaticSecret.get_value`

```python
get_value()
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.conversation.secret_source.StaticSecret.value`

```python
value: SecretStr
```

### `openhands.sdk.conversation.serialization_diff`

### `openhands.sdk.conversation.state`

**Classes:**

- [**AgentExecutionStatus**](#openhands.sdk.conversation.state.AgentExecutionStatus) – Enum representing the current execution state of the agent.
- [**ConversationState**](#openhands.sdk.conversation.state.ConversationState) –

**Attributes:**

- [**logger**](#openhands.sdk.conversation.state.logger) –

#### `openhands.sdk.conversation.state.AgentExecutionStatus`

Bases: <code>[str](#str)</code>, <code>[Enum](#enum.Enum)</code>

Enum representing the current execution state of the agent.

**Attributes:**

- [**ERROR**](#openhands.sdk.conversation.state.AgentExecutionStatus.ERROR) –
- [**FINISHED**](#openhands.sdk.conversation.state.AgentExecutionStatus.FINISHED) –
- [**IDLE**](#openhands.sdk.conversation.state.AgentExecutionStatus.IDLE) –
- [**PAUSED**](#openhands.sdk.conversation.state.AgentExecutionStatus.PAUSED) –
- [**RUNNING**](#openhands.sdk.conversation.state.AgentExecutionStatus.RUNNING) –
- [**STUCK**](#openhands.sdk.conversation.state.AgentExecutionStatus.STUCK) –
- [**WAITING_FOR_CONFIRMATION**](#openhands.sdk.conversation.state.AgentExecutionStatus.WAITING_FOR_CONFIRMATION) –

##### `openhands.sdk.conversation.state.AgentExecutionStatus.ERROR`

```python
ERROR = 'error'
```

##### `openhands.sdk.conversation.state.AgentExecutionStatus.FINISHED`

```python
FINISHED = 'finished'
```

##### `openhands.sdk.conversation.state.AgentExecutionStatus.IDLE`

```python
IDLE = 'idle'
```

##### `openhands.sdk.conversation.state.AgentExecutionStatus.PAUSED`

```python
PAUSED = 'paused'
```

##### `openhands.sdk.conversation.state.AgentExecutionStatus.RUNNING`

```python
RUNNING = 'running'
```

##### `openhands.sdk.conversation.state.AgentExecutionStatus.STUCK`

```python
STUCK = 'stuck'
```

##### `openhands.sdk.conversation.state.AgentExecutionStatus.WAITING_FOR_CONFIRMATION`

```python
WAITING_FOR_CONFIRMATION = 'waiting_for_confirmation'
```

#### `openhands.sdk.conversation.state.ConversationState`

Bases: <code>[OpenHandsModel](#openhands.sdk.utils.models.OpenHandsModel)</code>

**Functions:**

- [**acquire**](#openhands.sdk.conversation.state.ConversationState.acquire) – Acquire the lock.
- [**create**](#openhands.sdk.conversation.state.ConversationState.create) – If base_state.json exists: resume (attach EventLog,
- [**get_unmatched_actions**](#openhands.sdk.conversation.state.ConversationState.get_unmatched_actions) – Find actions in the event history that don't have matching observations.
- [**locked**](#openhands.sdk.conversation.state.ConversationState.locked) – Return True if the lock is currently held by any thread.
- [**model_dump_json**](#openhands.sdk.conversation.state.ConversationState.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.conversation.state.ConversationState.model_json_schema) –
- [**model_post_init**](#openhands.sdk.conversation.state.ConversationState.model_post_init) –
- [**model_validate**](#openhands.sdk.conversation.state.ConversationState.model_validate) –
- [**model_validate_json**](#openhands.sdk.conversation.state.ConversationState.model_validate_json) –
- [**owned**](#openhands.sdk.conversation.state.ConversationState.owned) – Return True if the lock is currently held by the calling thread.
- [**release**](#openhands.sdk.conversation.state.ConversationState.release) – Release the lock.
- [**set_on_state_change**](#openhands.sdk.conversation.state.ConversationState.set_on_state_change) – Set a callback to be called when state changes.

**Attributes:**

- [**activated_knowledge_skills**](#openhands.sdk.conversation.state.ConversationState.activated_knowledge_skills) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**agent**](#openhands.sdk.conversation.state.ConversationState.agent) (<code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>) –
- [**agent_status**](#openhands.sdk.conversation.state.ConversationState.agent_status) (<code>[AgentExecutionStatus](#openhands.sdk.conversation.state.AgentExecutionStatus)</code>) –
- [**confirmation_policy**](#openhands.sdk.conversation.state.ConversationState.confirmation_policy) (<code>[ConfirmationPolicyBase](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)</code>) –
- [**events**](#openhands.sdk.conversation.state.ConversationState.events) (<code>[EventLog](#openhands.sdk.conversation.event_store.EventLog)</code>) –
- [**id**](#openhands.sdk.conversation.state.ConversationState.id) (<code>[ConversationID](#openhands.sdk.conversation.types.ConversationID)</code>) –
- [**max_iterations**](#openhands.sdk.conversation.state.ConversationState.max_iterations) (<code>[int](#int)</code>) –
- [**persistence_dir**](#openhands.sdk.conversation.state.ConversationState.persistence_dir) (<code>[str](#str) | None</code>) –
- [**secret_registry**](#openhands.sdk.conversation.state.ConversationState.secret_registry) (<code>[SecretRegistry](#openhands.sdk.conversation.secret_registry.SecretRegistry)</code>) –
- [**stats**](#openhands.sdk.conversation.state.ConversationState.stats) (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats)</code>) –
- [**stuck_detection**](#openhands.sdk.conversation.state.ConversationState.stuck_detection) (<code>[bool](#bool)</code>) –
- [**workspace**](#openhands.sdk.conversation.state.ConversationState.workspace) (<code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>) –

##### `openhands.sdk.conversation.state.ConversationState.acquire`

```python
acquire(blocking=True, timeout=-1)
```

Acquire the lock.

**Parameters:**

- **blocking** (<code>[bool](#bool)</code>) – If True, block until lock is acquired. If False, return
  immediately.
- **timeout** (<code>[float](#float)</code>) – Maximum time to wait for lock (ignored if blocking=False).
  -1 means wait indefinitely.

**Returns:**

- <code>[bool](#bool)</code> – True if lock was acquired, False otherwise.

##### `openhands.sdk.conversation.state.ConversationState.activated_knowledge_skills`

```python
activated_knowledge_skills: list[str] = Field(default_factory=list, description='List of activated knowledge skills name')
```

##### `openhands.sdk.conversation.state.ConversationState.agent`

```python
agent: AgentBase = Field(..., description='The agent running in the conversation. This is persisted to allow resuming conversations and check agent configuration to handle e.g., tool changes, LLM changes, etc.')
```

##### `openhands.sdk.conversation.state.ConversationState.agent_status`

```python
agent_status: AgentExecutionStatus = Field(default=(AgentExecutionStatus.IDLE))
```

##### `openhands.sdk.conversation.state.ConversationState.confirmation_policy`

```python
confirmation_policy: ConfirmationPolicyBase = NeverConfirm()
```

##### `openhands.sdk.conversation.state.ConversationState.create`

```python
create(id, agent, workspace, persistence_dir=None, max_iterations=500, stuck_detection=True)
```

If base_state.json exists: resume (attach EventLog,
reconcile agent, enforce id).
Else: create fresh (agent required), persist base, and return.

##### `openhands.sdk.conversation.state.ConversationState.events`

```python
events: EventLog
```

##### `openhands.sdk.conversation.state.ConversationState.get_unmatched_actions`

```python
get_unmatched_actions(events)
```

Find actions in the event history that don't have matching observations.

This method identifies ActionEvents that don't have corresponding
ObservationEvents or UserRejectObservations, which typically indicates
actions that are pending confirmation or execution.

**Parameters:**

- **events** (<code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.base.Event)\]</code>) – List of events to search through

**Returns:**

- <code>[list](#list)\[[ActionEvent](#openhands.sdk.event.ActionEvent)\]</code> – List of ActionEvent objects that don't have corresponding observations,
- <code>[list](#list)\[[ActionEvent](#openhands.sdk.event.ActionEvent)\]</code> – in chronological order

##### `openhands.sdk.conversation.state.ConversationState.id`

```python
id: ConversationID = Field(description='Unique conversation ID')
```

##### `openhands.sdk.conversation.state.ConversationState.locked`

```python
locked()
```

Return True if the lock is currently held by any thread.

##### `openhands.sdk.conversation.state.ConversationState.max_iterations`

```python
max_iterations: int = Field(default=500, gt=0, description='Maximum number of iterations the agent can perform in a single run.')
```

##### `openhands.sdk.conversation.state.ConversationState.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.conversation.state.ConversationState.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.conversation.state.ConversationState.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.conversation.state.ConversationState.model_validate`

```python
model_validate(*args, **kwargs)
```

##### `openhands.sdk.conversation.state.ConversationState.model_validate_json`

```python
model_validate_json(*args, **kwargs)
```

##### `openhands.sdk.conversation.state.ConversationState.owned`

```python
owned()
```

Return True if the lock is currently held by the calling thread.

##### `openhands.sdk.conversation.state.ConversationState.persistence_dir`

```python
persistence_dir: str | None = Field(default='workspace/conversations', description='Directory for persisting conversation state and events. If None, conversation will not be persisted.')
```

##### `openhands.sdk.conversation.state.ConversationState.release`

```python
release()
```

Release the lock.

**Raises:**

- <code>[RuntimeError](#RuntimeError)</code> – If the current thread doesn't own the lock.

##### `openhands.sdk.conversation.state.ConversationState.secret_registry`

```python
secret_registry: SecretRegistry = Field(default_factory=SecretRegistry, description='Registry for handling secrets and sensitive data', validation_alias=(AliasChoices('secret_registry', 'secrets_manager')), serialization_alias='secret_registry')
```

##### `openhands.sdk.conversation.state.ConversationState.set_on_state_change`

```python
set_on_state_change(callback)
```

Set a callback to be called when state changes.

**Parameters:**

- **callback** (<code>[ConversationCallbackType](#openhands.sdk.conversation.types.ConversationCallbackType) | None</code>) – A function that takes an Event (ConversationStateUpdateEvent)
  or None to remove the callback

##### `openhands.sdk.conversation.state.ConversationState.stats`

```python
stats: ConversationStats = Field(default_factory=ConversationStats, description='Conversation statistics for tracking LLM metrics')
```

##### `openhands.sdk.conversation.state.ConversationState.stuck_detection`

```python
stuck_detection: bool = Field(default=True, description='Whether to enable stuck detection for the agent.')
```

##### `openhands.sdk.conversation.state.ConversationState.workspace`

```python
workspace: BaseWorkspace = Field(..., description='Working directory for agent operations and tool execution')
```

#### `openhands.sdk.conversation.state.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.stuck_detector`

**Classes:**

- [**StuckDetector**](#openhands.sdk.conversation.stuck_detector.StuckDetector) – Detects when an agent is stuck in repetitive or unproductive patterns.

**Attributes:**

- [**logger**](#openhands.sdk.conversation.stuck_detector.logger) –

#### `openhands.sdk.conversation.stuck_detector.StuckDetector`

```python
StuckDetector(state)
```

Detects when an agent is stuck in repetitive or unproductive patterns.

This detector analyzes the conversation history to identify various stuck patterns:

1. Repeating action-observation cycles
1. Repeating action-error cycles
1. Agent monologue (repeated messages without user input)
1. Repeating alternating action-observation patterns
1. Context window errors indicating memory issues

**Functions:**

- [**is_stuck**](#openhands.sdk.conversation.stuck_detector.StuckDetector.is_stuck) – Check if the agent is currently stuck.

**Attributes:**

- [**state**](#openhands.sdk.conversation.stuck_detector.StuckDetector.state) (<code>[ConversationState](#openhands.sdk.conversation.state.ConversationState)</code>) –

##### `openhands.sdk.conversation.stuck_detector.StuckDetector.is_stuck`

```python
is_stuck()
```

Check if the agent is currently stuck.

##### `openhands.sdk.conversation.stuck_detector.StuckDetector.state`

```python
state: ConversationState = state
```

#### `openhands.sdk.conversation.stuck_detector.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.title_utils`

Utility functions for generating conversation titles.

**Functions:**

- [**extract_first_user_message**](#openhands.sdk.conversation.title_utils.extract_first_user_message) – Extract the first user message from conversation events.
- [**generate_conversation_title**](#openhands.sdk.conversation.title_utils.generate_conversation_title) – Generate a title for a conversation based on the first user message.
- [**generate_fallback_title**](#openhands.sdk.conversation.title_utils.generate_fallback_title) – Generate a fallback title by truncating the first user message.
- [**generate_title_with_llm**](#openhands.sdk.conversation.title_utils.generate_title_with_llm) – Generate a conversation title using LLM.

**Attributes:**

- [**categories**](#openhands.sdk.conversation.title_utils.categories) –
- [**logger**](#openhands.sdk.conversation.title_utils.logger) –

#### `openhands.sdk.conversation.title_utils.categories`

```python
categories = [{'emoji': '💄', 'name': 'frontend', 'description': 'UI and style files'}, {'emoji': '👔', 'name': 'backend', 'description': 'Business logic'}, {'emoji': '✅', 'name': 'test', 'description': 'Tests'}, {'emoji': '👷', 'name': 'devops', 'description': 'CI build system'}, {'emoji': '🚀', 'name': 'deployment', 'description': 'Deploy stuff'}, {'emoji': '📦️', 'name': 'dependencies', 'description': 'Packages and dependencies'}, {'emoji': '🗃️', 'name': 'database', 'description': 'Database changes'}, {'emoji': '🔧', 'name': 'chores', 'description': 'Configuration and maintenance'}, {'emoji': '✨', 'name': 'features', 'description': 'New features'}, {'emoji': '🐛', 'name': 'bugfix', 'description': 'Bug fixes'}, {'emoji': '⚡️', 'name': 'performance', 'description': 'Performance improvements'}, {'emoji': '🔒️', 'name': 'security', 'description': 'Security fixes'}, {'emoji': '📝', 'name': 'documentation', 'description': 'Documentation'}, {'emoji': '♻️', 'name': 'refactor', 'description': 'Code refactoring'}]
```

#### `openhands.sdk.conversation.title_utils.extract_first_user_message`

```python
extract_first_user_message(events)
```

Extract the first user message from conversation events.

**Parameters:**

- **events** (<code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.base.Event)\]</code>) – List of conversation events.

**Returns:**

- <code>[str](#str) | None</code> – The first user message text, or None if no user message is found.

#### `openhands.sdk.conversation.title_utils.generate_conversation_title`

```python
generate_conversation_title(events, llm=None, max_length=50)
```

Generate a title for a conversation based on the first user message.

This is the main utility function that orchestrates the title generation process:

1. Extract the first user message from events
1. Try to generate title using LLM
1. Fall back to simple truncation if LLM fails

**Parameters:**

- **events** (<code>[Sequence](#collections.abc.Sequence)\[[Event](#openhands.sdk.event.base.Event)\]</code>) – List of conversation events.
- **llm** (<code>[LLM](#openhands.sdk.llm.LLM) | None</code>) – Optional LLM to use for title generation.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str)</code> – A generated title for the conversation.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If no user messages are found in the conversation events.

#### `openhands.sdk.conversation.title_utils.generate_fallback_title`

```python
generate_fallback_title(message, max_length=50)
```

Generate a fallback title by truncating the first user message.

**Parameters:**

- **message** (<code>[str](#str)</code>) – The first user message.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the title.

**Returns:**

- <code>[str](#str)</code> – A truncated title.

#### `openhands.sdk.conversation.title_utils.generate_title_with_llm`

```python
generate_title_with_llm(message, llm, max_length=50)
```

Generate a conversation title using LLM.

**Parameters:**

- **message** (<code>[str](#str)</code>) – The first user message to generate title from.
- **llm** (<code>[LLM](#openhands.sdk.llm.LLM)</code>) – The LLM to use for title generation.
- **max_length** (<code>[int](#int)</code>) – Maximum length of the generated title.

**Returns:**

- <code>[str](#str) | None</code> – Generated title, or None if LLM fails or returns empty response.

#### `openhands.sdk.conversation.title_utils.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.conversation.types`

**Attributes:**

- [**ConversationCallbackType**](#openhands.sdk.conversation.types.ConversationCallbackType) –
- [**ConversationID**](#openhands.sdk.conversation.types.ConversationID) – Type alias for conversation IDs.

#### `openhands.sdk.conversation.types.ConversationCallbackType`

```python
ConversationCallbackType = Callable[[Event], None]
```

#### `openhands.sdk.conversation.types.ConversationID`

```python
ConversationID = uuid.UUID
```

Type alias for conversation IDs.

### `openhands.sdk.conversation.visualizer`

**Classes:**

- [**ConversationVisualizer**](#openhands.sdk.conversation.visualizer.ConversationVisualizer) – Handles visualization of conversation events with Rich formatting.

**Functions:**

- [**create_default_visualizer**](#openhands.sdk.conversation.visualizer.create_default_visualizer) – Create a default conversation visualizer instance.

**Attributes:**

- [**DEFAULT_HIGHLIGHT_REGEX**](#openhands.sdk.conversation.visualizer.DEFAULT_HIGHLIGHT_REGEX) –

#### `openhands.sdk.conversation.visualizer.ConversationVisualizer`

```python
ConversationVisualizer(highlight_regex=None, skip_user_messages=False, conversation_stats=None, name_for_visualization=None)
```

Handles visualization of conversation events with Rich formatting.

Provides Rich-formatted output with panels and complete content display.

**Functions:**

- [**on_event**](#openhands.sdk.conversation.visualizer.ConversationVisualizer.on_event) – Main event handler that displays events with Rich formatting.

**Parameters:**

- **highlight_regex** (<code>[dict](#dict)\[[str](#str), [str](#str)\] | None</code>) – Dictionary mapping regex patterns to Rich color styles
  for highlighting keywords in the visualizer.
  For example: {"Reasoning:": "bold blue",
  "Thought:": "bold green"}
- **skip_user_messages** (<code>[bool](#bool)</code>) – If True, skip displaying user messages. Useful for
  scenarios where user input is not relevant to show.
- **conversation_stats** (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats) | None</code>) – ConversationStats object to display metrics information.
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.

##### `openhands.sdk.conversation.visualizer.ConversationVisualizer.on_event`

```python
on_event(event)
```

Main event handler that displays events with Rich formatting.

#### `openhands.sdk.conversation.visualizer.DEFAULT_HIGHLIGHT_REGEX`

```python
DEFAULT_HIGHLIGHT_REGEX = {'^Reasoning:': f'bold {_THOUGHT_COLOR}', '^Thought:': f'bold {_THOUGHT_COLOR}', '^Action:': f'bold {_ACTION_COLOR}', '^Arguments:': f'bold {_ACTION_COLOR}', '^Tool:': f'bold {_OBSERVATION_COLOR}', '^Result:': f'bold {_OBSERVATION_COLOR}', '^Rejection Reason:': f'bold {_ERROR_COLOR}', '\\*\\*(.*?)\\*\\*': 'bold', '\\*(.*?)\\*': 'italic'}
```

#### `openhands.sdk.conversation.visualizer.create_default_visualizer`

```python
create_default_visualizer(highlight_regex=None, conversation_stats=None, name_for_visualization=None, **kwargs)
```

Create a default conversation visualizer instance.

**Parameters:**

- **highlight_regex** (<code>[dict](#dict)\[[str](#str), [str](#str)\] | None</code>) – Dictionary mapping regex patterns to Rich color styles
  for highlighting keywords in the visualizer.
  For example: {"Reasoning:": "bold blue",
  "Thought:": "bold green"}
- **conversation_stats** (<code>[ConversationStats](#openhands.sdk.conversation.conversation_stats.ConversationStats) | None</code>) – ConversationStats object to display metrics information.
- **name_for_visualization** (<code>[str](#str) | None</code>) – Optional name to prefix in panel titles to identify
  which agent/conversation is speaking.
