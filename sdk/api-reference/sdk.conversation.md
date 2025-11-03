---
title: openhands.sdk.conversation
description: API reference for openhands.sdk.conversation
---

# openhands.sdk.conversation package

<a id="module-openhands.sdk.conversation"></a>

### *class* openhands.sdk.conversation.Conversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), , workspace: [str](https://docs.python.org/3/library/stdtypes.html#str) | [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace) = 'workspace/project', persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

### *class* openhands.sdk.conversation.Conversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), , workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Factory entrypoint that returns a LocalConversation or RemoteConversation.

Usage:
: - Conversation(agent=…) -> LocalConversation
  - Conversation(agent=…, host=”[http://](http://)…”) -> RemoteConversation

### *class* openhands.sdk.conversation.BaseConversation

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

#### *abstractmethod* close() → [None](https://docs.python.org/3/library/constants.html#None)

#### *static* compose_callbacks(callbacks: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]]) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]

Compose multiple callbacks into a single callback function.

**Parameters:**
  **callbacks** – An iterable of callback functions
**Returns:**
  A single callback function that calls all provided callbacks

#### *property* confirmation_policy_active *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### *abstract property* conversation_stats *: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)*

#### *abstractmethod* generate_title(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a title for the conversation based on the first user message.

**Parameters:**
  * **llm** – Optional LLM to use for title generation. If not provided,
    uses the agent’s LLM.
  * **max_length** – Maximum length of the generated title.
**Returns:**
  A generated title for the conversation.
**Raises:**
  [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) – If no user messages are found in the conversation.

#### *static* get_persistence_dir(persistence_base_dir: [str](https://docs.python.org/3/library/stdtypes.html#str), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Get the persistence directory for the conversation.

#### *abstract property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

#### *property* is_confirmation_mode_active *: [bool](https://docs.python.org/3/library/functions.html#bool)*

Check if confirmation mode is active.

Returns True if BOTH conditions are met:
1. The agent has a security analyzer set (not None)
2. The confirmation policy is active

#### *abstractmethod* pause() → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* reject_pending_actions(reason: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User rejected the action') → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* run() → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* send_message(message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)) → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* set_confirmation_policy(policy: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)) → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstract property* state *: [ConversationStateProtocol](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol)*

#### *abstractmethod* update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

### *class* openhands.sdk.conversation.ConversationState(\*, id: uuid.UUID, agent: openhands.sdk.agent.base.AgentBase, workspace: openhands.sdk.workspace.base.BaseWorkspace, persistence_dir: str | None = 'workspace/conversations', max_iterations: typing.Annotated[int, annotated_types.Gt(gt=0)] = 500, stuck_detection: bool = True, agent_status: openhands.sdk.conversation.state.AgentExecutionStatus = AgentExecutionStatus.IDLE, confirmation_policy: openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase = NeverConfirm(kind='NeverConfirm'), activated_knowledge_skills: list[str] = `<factory>`, stats: openhands.sdk.conversation.conversation_stats.ConversationStats = `<factory>`, secret_registry: openhands.sdk.conversation.secret_registry.SecretRegistry = `<factory>`)

Bases: [`OpenHandsModel`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel)

#### \_\_enter_\_() → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

Context manager entry.

#### \_\_exit_\_(exc_type: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_val: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_tb: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Context manager exit.

#### acquire(blocking: [bool](https://docs.python.org/3/library/functions.html#bool) = True, timeout: [float](https://docs.python.org/3/library/functions.html#float) = -1) → [bool](https://docs.python.org/3/library/functions.html#bool)

Acquire the lock.

**Parameters:**
  * **blocking** – If True, block until lock is acquired. If False, return
    immediately.
  * **timeout** – Maximum time to wait for lock (ignored if blocking=False).
    -1 means wait indefinitely.
**Returns:**
  True if lock was acquired, False otherwise.

#### *classmethod* create(id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID), agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [BaseWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace), persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iterations: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True) → [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)

If base_state.json exists: resume (attach EventLog,
: reconcile agent, enforce id).

Else: create fresh (agent required), persist base, and return.

#### *property* events *: [EventLog](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md#openhands.sdk.conversation.event_store.EventLog)*

#### *static* get_unmatched_actions(events: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[ActionEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent)]

Find actions in the event history that don’t have matching observations.

This method identifies ActionEvents that don’t have corresponding
ObservationEvents or UserRejectObservations, which typically indicates
actions that are pending confirmation or execution.

**Parameters:**
  **events** – List of events to search through
**Returns:**
  List of ActionEvent objects that don’t have corresponding observations,
  in chronological order

#### locked() → [bool](https://docs.python.org/3/library/functions.html#bool)

Return True if the lock is currently held by any thread.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### owned() → [bool](https://docs.python.org/3/library/functions.html#bool)

Return True if the lock is currently held by the calling thread.

#### release() → [None](https://docs.python.org/3/library/constants.html#None)

Release the lock.

**Raises:**
  [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) – If the current thread doesn’t own the lock.

#### set_on_state_change(callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None)) → [None](https://docs.python.org/3/library/constants.html#None)

Set a callback to be called when state changes.

**Parameters:**
  **callback** – A function that takes an Event (ConversationStateUpdateEvent)
  or None to remove the callback

#### id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

#### agent *: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)*

#### workspace *: [BaseWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)*

#### persistence_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### max_iterations *: [int](https://docs.python.org/3/library/functions.html#int)*

#### stuck_detection *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### agent_status *: [AgentExecutionStatus](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus)*

#### confirmation_policy *: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)*

#### activated_knowledge_skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### stats *: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)*

#### secret_registry *: [SecretRegistry](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry)*

### *class* openhands.sdk.conversation.ConversationVisualizer(highlight_regex: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None, skip_user_messages: [bool](https://docs.python.org/3/library/functions.html#bool) = False, conversation_stats: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats) | [None](https://docs.python.org/3/library/constants.html#None) = None, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Handles visualization of conversation events with Rich formatting.

Provides Rich-formatted output with panels and complete content display.

#### \_\_init_\_(highlight_regex: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None, skip_user_messages: [bool](https://docs.python.org/3/library/functions.html#bool) = False, conversation_stats: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats) | [None](https://docs.python.org/3/library/constants.html#None) = None, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Initialize the visualizer.

**Parameters:**
  * **highlight_regex** – Dictionary mapping regex patterns to Rich color styles
    for highlighting keywords in the visualizer.
    For example: {“Reasoning:”: “bold blue”,
    “Thought:”: “bold green”}
  * **skip_user_messages** – If True, skip displaying user messages. Useful for
    scenarios where user input is not relevant to show.
  * **conversation_stats** – ConversationStats object to display metrics information.
  * **name_for_visualization** – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.

#### on_event(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Main event handler that displays events with Rich formatting.

### *class* openhands.sdk.conversation.SecretRegistry(\*, secret_sources: dict[str, ~openhands.sdk.conversation.secret_source.SecretSource] = `<factory>`)

Bases: [`OpenHandsModel`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel)

Manages secrets and injects them into bash commands when needed.

The secret registry stores a mapping of secret keys to SecretSources
that retrieve the actual secret values. When a bash command is about to be
executed, it scans the command for any secret keys and injects the corresponding
environment variables.

Secret sources will redact / encrypt their sensitive values as appropriate when
serializing, depending on the content of the context. If a context is present
and contains a ‘cipher’ object, this is used for encryption. If it contains a
boolean ‘expose_secrets’ flag set to True, secrets are dunped in plain text.
Otherwise secrets are redacted.

Additionally, it tracks the latest exported values to enable consistent masking
even when callable secrets fail on subsequent calls.

#### find_secrets_in_text(text: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [set](https://docs.python.org/3/library/stdtypes.html#set)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Find all secret keys mentioned in the given text.

**Parameters:**
  **text** – The text to search for secret keys
**Returns:**
  Set of secret keys found in the text

#### get_secrets_as_env_vars(command: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]

Get secrets that should be exported as environment variables for a command.

**Parameters:**
  **command** – The bash command to check for secret references
**Returns:**
  Dictionary of environment variables to export (key -> value)

#### mask_secrets_in_output(text: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Mask secret values in the given text.

This method uses both the current exported values and attempts to get
fresh values from callables to ensure comprehensive masking.

**Parameters:**
  **text** – The text to mask secrets in
**Returns:**
  Text with secret values replaced by ``<secret-hidden>``

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

Add or update secrets in the manager.

**Parameters:**
  **secrets** – Dictionary mapping secret keys to either string values
  or callable functions that return string values

#### secret_sources *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]*

### *class* openhands.sdk.conversation.StuckDetector(state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState))

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Detects when an agent is stuck in repetitive or unproductive patterns.

This detector analyzes the conversation history to identify various stuck patterns:
1. Repeating action-observation cycles
2. Repeating action-error cycles
3. Agent monologue (repeated messages without user input)
4. Repeating alternating action-observation patterns
5. Context window errors indicating memory issues

#### \_\_init_\_(state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState))

#### is_stuck() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if the agent is currently stuck.

#### state *: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)*

### *class* openhands.sdk.conversation.EventLog(fs: [FileStore](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore), dir_path: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'events')

Bases: [`EventsListBase`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.events_list_base.md#openhands.sdk.conversation.events_list_base.EventsListBase)

#### \_\_init_\_(fs: [FileStore](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore), dir_path: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'events') → [None](https://docs.python.org/3/library/constants.html#None)

#### append(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Add a new event to the list.

#### get_id(idx: [int](https://docs.python.org/3/library/functions.html#int)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Return the event_id for a given index.

#### get_index(event_id: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [int](https://docs.python.org/3/library/functions.html#int)

Return the integer index for a given event_id.

### *class* openhands.sdk.conversation.LocalConversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [str](https://docs.python.org/3/library/stdtypes.html#str) | [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace), persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Bases: [`BaseConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation)

#### \_\_del_\_() → [None](https://docs.python.org/3/library/constants.html#None)

Ensure cleanup happens when conversation is destroyed.

#### \_\_init_\_(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [str](https://docs.python.org/3/library/stdtypes.html#str) | [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace), persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Initialize the conversation.

**Parameters:**
  * **agent** – The agent to use for the conversation
  * **workspace** – Working directory for agent operations and tool execution
  * **persistence_dir** – Directory for persisting conversation state and events
  * **conversation_id** – Optional ID for the conversation. If provided, will
    be used to identify the conversation. The user might want to
    suffix their persistent filestore with this ID.
  * **callbacks** – Optional list of callback functions to handle events
  * **max_iteration_per_run** – Maximum number of iterations per run
  * **visualize** – Whether to enable default visualization. If True, adds
    a default visualizer callback. If False, relies on
    application to provide visualization through callbacks.
  * **name_for_visualization** – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.
  * **stuck_detection** – Whether to enable stuck detection

#### close() → [None](https://docs.python.org/3/library/constants.html#None)

Close the conversation and clean up all tool executors.

#### *property* conversation_stats

#### generate_title(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a title for the conversation based on the first user message.

**Parameters:**
  * **llm** – Optional LLM to use for title generation. If not provided,
    uses self.agent.llm.
  * **max_length** – Maximum length of the generated title.
**Returns:**
  A generated title for the conversation.
**Raises:**
  [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) – If no user messages are found in the conversation.

#### *property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

Get the unique ID of the conversation.

#### pause() → [None](https://docs.python.org/3/library/constants.html#None)

Pause agent execution.

This method can be called from any thread to request that the agent
pause execution. The pause will take effect at the next iteration
of the run loop (between agent steps).

Note: If called during an LLM completion, the pause will not take
effect until the current LLM call completes.

#### reject_pending_actions(reason: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User rejected the action') → [None](https://docs.python.org/3/library/constants.html#None)

Reject all pending actions from the agent.

This is a non-invasive method to reject actions between run() calls.
Also clears the agent_waiting_for_confirmation flag.

#### run() → [None](https://docs.python.org/3/library/constants.html#None)

Runs the conversation until the agent finishes.

In confirmation mode:
- First call: creates actions but doesn’t execute them, stops and waits
- Second call: executes pending actions (implicit confirmation)

In normal mode:
- Creates and executes actions immediately

Can be paused between steps

#### send_message(message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)) → [None](https://docs.python.org/3/library/constants.html#None)

Send a message to the agent.

**Parameters:**
  **message** – Either a string (which will be converted to a user message)
  or a Message object

#### set_confirmation_policy(policy: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)) → [None](https://docs.python.org/3/library/constants.html#None)

Set the confirmation policy and store it in conversation state.

#### *property* state *: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)*

Get the conversation state.

It returns a protocol that has a subset of ConversationState methods
and properties. We will have the ability to access the same properties
of ConversationState on a remote conversation object.
But we won’t be able to access methods that mutate the state.

#### *property* stuck_detector *: [StuckDetector](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.stuck_detector.md#openhands.sdk.conversation.stuck_detector.StuckDetector) | [None](https://docs.python.org/3/library/constants.html#None)*

Get the stuck detector instance if enabled.

#### update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

Add secrets to the conversation.

**Parameters:**
  **secrets** – Dictionary mapping secret keys to values or no-arg callables.
  SecretValue = str | Callable[[], str]. Callables are invoked lazily
  when a command references the secret key.

#### agent *: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)*

#### workspace *: [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace)*

#### max_iteration_per_run *: [int](https://docs.python.org/3/library/functions.html#int)*

#### llm_registry *: [LLMRegistry](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry)*

### *class* openhands.sdk.conversation.RemoteConversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = False, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Bases: [`BaseConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation)

#### \_\_init_\_(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = False, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object)) → [None](https://docs.python.org/3/library/constants.html#None)

Remote conversation proxy that talks to an agent server.

**Parameters:**
  * **agent** – Agent configuration (will be sent to the server)
  * **workspace** – The working directory for agent operations and tool execution.
  * **conversation_id** – Optional existing conversation id to attach to
  * **callbacks** – Optional callbacks to receive events (not yet streamed)
  * **max_iteration_per_run** – Max iterations configured on server
  * **stuck_detection** – Whether to enable stuck detection on server
  * **visualize** – Whether to enable the default visualizer callback
  * **name_for_visualization** – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.
  * **secrets** – Optional secrets to initialize the conversation with

#### close() → [None](https://docs.python.org/3/library/constants.html#None)

#### *property* conversation_stats *: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)*

Get conversation stats from remote server.

#### generate_title(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a title for the conversation based on the first user message.

**Parameters:**
  * **llm** – Optional LLM to use for title generation. If provided, its usage_id
    will be sent to the server. If not provided, uses the agent’s LLM.
  * **max_length** – Maximum length of the generated title.
**Returns:**
  A generated title for the conversation.

#### *property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

#### pause() → [None](https://docs.python.org/3/library/constants.html#None)

#### reject_pending_actions(reason: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User rejected the action') → [None](https://docs.python.org/3/library/constants.html#None)

#### run() → [None](https://docs.python.org/3/library/constants.html#None)

#### send_message(message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)) → [None](https://docs.python.org/3/library/constants.html#None)

#### set_confirmation_policy(policy: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)) → [None](https://docs.python.org/3/library/constants.html#None)

#### *property* state *: [RemoteState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState)*

Access to remote conversation state.

#### *property* stuck_detector

Stuck detector for compatibility.
Not implemented for remote conversations.

#### update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

#### agent *: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)*

#### max_iteration_per_run *: [int](https://docs.python.org/3/library/functions.html#int)*

#### workspace *: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace)*

### *class* openhands.sdk.conversation.EventsListBase

Bases: [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for event lists that can be appended to.

This provides a common interface for both local EventLog and remote
RemoteEventsList implementations, avoiding circular imports in protocols.

#### *abstractmethod* append(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Add a new event to the list.

### openhands.sdk.conversation.get_agent_final_response(events: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)]) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Extract the final response from the agent.

An agent can end a conversation in two ways:
1. By calling the finish tool
2. By returning a text message with no tool calls

**Parameters:**
  **events** – List of conversation events to search through.
**Returns:**
  The final response message from the agent, or empty string if not found.

## Subpackages

* [openhands.sdk.conversation.impl package](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md)
  * [`LocalConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation)
    * [`LocalConversation.__del__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.__del__)
    * [`LocalConversation.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.__init__)
    * [`LocalConversation.close()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.close)
    * [`LocalConversation.conversation_stats`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.conversation_stats)
    * [`LocalConversation.generate_title()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.generate_title)
    * [`LocalConversation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.id)
    * [`LocalConversation.pause()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.pause)
    * [`LocalConversation.reject_pending_actions()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.reject_pending_actions)
    * [`LocalConversation.run()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.run)
    * [`LocalConversation.send_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.send_message)
    * [`LocalConversation.set_confirmation_policy()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.set_confirmation_policy)
    * [`LocalConversation.state`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.state)
    * [`LocalConversation.stuck_detector`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.stuck_detector)
    * [`LocalConversation.update_secrets()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.update_secrets)
    * [`LocalConversation.agent`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.agent)
    * [`LocalConversation.workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.workspace)
    * [`LocalConversation.max_iteration_per_run`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.max_iteration_per_run)
    * [`LocalConversation.llm_registry`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.LocalConversation.llm_registry)
  * [`RemoteConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation)
    * [`RemoteConversation.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.__init__)
    * [`RemoteConversation.close()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.close)
    * [`RemoteConversation.conversation_stats`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.conversation_stats)
    * [`RemoteConversation.generate_title()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.generate_title)
    * [`RemoteConversation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.id)
    * [`RemoteConversation.pause()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.pause)
    * [`RemoteConversation.reject_pending_actions()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.reject_pending_actions)
    * [`RemoteConversation.run()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.run)
    * [`RemoteConversation.send_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.send_message)
    * [`RemoteConversation.set_confirmation_policy()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.set_confirmation_policy)
    * [`RemoteConversation.state`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.state)
    * [`RemoteConversation.stuck_detector`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.stuck_detector)
    * [`RemoteConversation.update_secrets()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.update_secrets)
    * [`RemoteConversation.agent`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.agent)
    * [`RemoteConversation.max_iteration_per_run`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.max_iteration_per_run)
    * [`RemoteConversation.workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#openhands.sdk.conversation.impl.RemoteConversation.workspace)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.md#submodules)
    * [openhands.sdk.conversation.impl.local_conversation module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md)
      * [`LocalConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation)
    * [openhands.sdk.conversation.impl.remote_conversation module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md)
      * [`WebSocketCallbackClient`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient)
      * [`RemoteEventsList`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList)
      * [`RemoteState`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState)
      * [`RemoteConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation)

## Submodules

* [openhands.sdk.conversation.base module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md)
  * [`ConversationStateProtocol`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol)
    * [`ConversationStateProtocol.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.id)
    * [`ConversationStateProtocol.events`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.events)
    * [`ConversationStateProtocol.agent_status`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.agent_status)
    * [`ConversationStateProtocol.confirmation_policy`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.confirmation_policy)
    * [`ConversationStateProtocol.activated_knowledge_skills`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.activated_knowledge_skills)
    * [`ConversationStateProtocol.workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.workspace)
    * [`ConversationStateProtocol.persistence_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.persistence_dir)
    * [`ConversationStateProtocol.agent`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.agent)
    * [`ConversationStateProtocol.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol.__init__)
  * [`BaseConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation)
    * [`BaseConversation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.id)
    * [`BaseConversation.state`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.state)
    * [`BaseConversation.conversation_stats`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.conversation_stats)
    * [`BaseConversation.send_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.send_message)
    * [`BaseConversation.run()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.run)
    * [`BaseConversation.set_confirmation_policy()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.set_confirmation_policy)
    * [`BaseConversation.confirmation_policy_active`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.confirmation_policy_active)
    * [`BaseConversation.is_confirmation_mode_active`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.is_confirmation_mode_active)
    * [`BaseConversation.reject_pending_actions()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.reject_pending_actions)
    * [`BaseConversation.pause()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.pause)
    * [`BaseConversation.update_secrets()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.update_secrets)
    * [`BaseConversation.close()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.close)
    * [`BaseConversation.generate_title()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.generate_title)
    * [`BaseConversation.get_persistence_dir()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.get_persistence_dir)
    * [`BaseConversation.compose_callbacks()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation.compose_callbacks)
* [openhands.sdk.conversation.conversation module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation.md)
  * [`Conversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation.md#openhands.sdk.conversation.conversation.Conversation)
* [openhands.sdk.conversation.conversation_stats module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md)
  * [`ConversationStats`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)
    * [`ConversationStats.usage_to_metrics`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.usage_to_metrics)
    * [`ConversationStats.service_to_metrics`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.service_to_metrics)
    * [`ConversationStats.get_combined_metrics()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.get_combined_metrics)
    * [`ConversationStats.get_metrics_for_usage()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.get_metrics_for_usage)
    * [`ConversationStats.get_metrics_for_service()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.get_metrics_for_service)
    * [`ConversationStats.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.model_config)
    * [`ConversationStats.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.model_post_init)
    * [`ConversationStats.register_llm()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats.register_llm)
* [openhands.sdk.conversation.event_store module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md)
  * [`EventLog`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md#openhands.sdk.conversation.event_store.EventLog)
    * [`EventLog.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md#openhands.sdk.conversation.event_store.EventLog.__init__)
    * [`EventLog.get_index()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md#openhands.sdk.conversation.event_store.EventLog.get_index)
    * [`EventLog.get_id()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md#openhands.sdk.conversation.event_store.EventLog.get_id)
    * [`EventLog.append()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md#openhands.sdk.conversation.event_store.EventLog.append)
* [openhands.sdk.conversation.events_list_base module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.events_list_base.md)
  * [`EventsListBase`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.events_list_base.md#openhands.sdk.conversation.events_list_base.EventsListBase)
    * [`EventsListBase.append()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.events_list_base.md#openhands.sdk.conversation.events_list_base.EventsListBase.append)
* [openhands.sdk.conversation.exceptions module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.exceptions.md)
  * [`ConversationRunError`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.exceptions.md#openhands.sdk.conversation.exceptions.ConversationRunError)
    * [`ConversationRunError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.exceptions.md#openhands.sdk.conversation.exceptions.ConversationRunError.__init__)
    * [`ConversationRunError.conversation_id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.exceptions.md#openhands.sdk.conversation.exceptions.ConversationRunError.conversation_id)
    * [`ConversationRunError.original_exception`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.exceptions.md#openhands.sdk.conversation.exceptions.ConversationRunError.original_exception)
* [openhands.sdk.conversation.fifo_lock module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md)
  * [`FIFOLock`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock)
    * [`FIFOLock.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock.__init__)
    * [`FIFOLock.acquire()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock.acquire)
    * [`FIFOLock.release()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock.release)
    * [`FIFOLock.__enter__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock.__enter__)
    * [`FIFOLock.__exit__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock.__exit__)
    * [`FIFOLock.locked()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock.locked)
    * [`FIFOLock.owned()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.fifo_lock.md#openhands.sdk.conversation.fifo_lock.FIFOLock.owned)
* [openhands.sdk.conversation.persistence_const module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.persistence_const.md)
* [openhands.sdk.conversation.response_utils module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.response_utils.md)
  * [`get_agent_final_response()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.response_utils.md#openhands.sdk.conversation.response_utils.get_agent_final_response)
* [openhands.sdk.conversation.secret_registry module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md)
  * [`SecretRegistry`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry)
    * [`SecretRegistry.secret_sources`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry.secret_sources)
    * [`SecretRegistry.update_secrets()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry.update_secrets)
    * [`SecretRegistry.find_secrets_in_text()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry.find_secrets_in_text)
    * [`SecretRegistry.get_secrets_as_env_vars()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry.get_secrets_as_env_vars)
    * [`SecretRegistry.mask_secrets_in_output()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry.mask_secrets_in_output)
    * [`SecretRegistry.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry.model_config)
    * [`SecretRegistry.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry.model_post_init)
* [openhands.sdk.conversation.secret_source module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md)
  * [`SecretSource`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)
    * [`SecretSource.description`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource.description)
    * [`SecretSource.get_value()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource.get_value)
    * [`SecretSource.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource.model_config)
  * [`StaticSecret`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.StaticSecret)
    * [`StaticSecret.value`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.StaticSecret.value)
    * [`StaticSecret.get_value()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.StaticSecret.get_value)
    * [`StaticSecret.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.StaticSecret.model_config)
    * [`StaticSecret.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.StaticSecret.kind)
  * [`LookupSecret`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.LookupSecret)
    * [`LookupSecret.url`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.LookupSecret.url)
    * [`LookupSecret.headers`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.LookupSecret.headers)
    * [`LookupSecret.get_value()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.LookupSecret.get_value)
    * [`LookupSecret.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.LookupSecret.model_config)
    * [`LookupSecret.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.LookupSecret.kind)
* [openhands.sdk.conversation.serialization_diff module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.serialization_diff.md)
* [openhands.sdk.conversation.state module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md)
  * [`AgentExecutionStatus`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus)
    * [`AgentExecutionStatus.IDLE`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus.IDLE)
    * [`AgentExecutionStatus.RUNNING`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus.RUNNING)
    * [`AgentExecutionStatus.PAUSED`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus.PAUSED)
    * [`AgentExecutionStatus.WAITING_FOR_CONFIRMATION`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus.WAITING_FOR_CONFIRMATION)
    * [`AgentExecutionStatus.FINISHED`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus.FINISHED)
    * [`AgentExecutionStatus.ERROR`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus.ERROR)
    * [`AgentExecutionStatus.STUCK`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus.STUCK)
  * [`ConversationState`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)
    * [`ConversationState.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.id)
    * [`ConversationState.agent`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.agent)
    * [`ConversationState.workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.workspace)
    * [`ConversationState.persistence_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.persistence_dir)
    * [`ConversationState.max_iterations`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.max_iterations)
    * [`ConversationState.stuck_detection`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.stuck_detection)
    * [`ConversationState.agent_status`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.agent_status)
    * [`ConversationState.confirmation_policy`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.confirmation_policy)
    * [`ConversationState.activated_knowledge_skills`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.activated_knowledge_skills)
    * [`ConversationState.stats`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.stats)
    * [`ConversationState.secret_registry`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.secret_registry)
    * [`ConversationState.events`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.events)
    * [`ConversationState.set_on_state_change()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.set_on_state_change)
    * [`ConversationState.create()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.create)
    * [`ConversationState.get_unmatched_actions()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.get_unmatched_actions)
    * [`ConversationState.acquire()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.acquire)
    * [`ConversationState.release()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.release)
    * [`ConversationState.__enter__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.__enter__)
    * [`ConversationState.__exit__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.__exit__)
    * [`ConversationState.locked()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.locked)
    * [`ConversationState.owned()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.owned)
    * [`ConversationState.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.model_config)
    * [`ConversationState.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState.model_post_init)
* [openhands.sdk.conversation.stuck_detector module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.stuck_detector.md)
  * [`StuckDetector`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.stuck_detector.md#openhands.sdk.conversation.stuck_detector.StuckDetector)
    * [`StuckDetector.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.stuck_detector.md#openhands.sdk.conversation.stuck_detector.StuckDetector.__init__)
    * [`StuckDetector.state`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.stuck_detector.md#openhands.sdk.conversation.stuck_detector.StuckDetector.state)
    * [`StuckDetector.is_stuck()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.stuck_detector.md#openhands.sdk.conversation.stuck_detector.StuckDetector.is_stuck)
* [openhands.sdk.conversation.title_utils module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.title_utils.md)
  * [`extract_first_user_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.title_utils.md#openhands.sdk.conversation.title_utils.extract_first_user_message)
  * [`generate_title_with_llm()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.title_utils.md#openhands.sdk.conversation.title_utils.generate_title_with_llm)
  * [`generate_fallback_title()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.title_utils.md#openhands.sdk.conversation.title_utils.generate_fallback_title)
  * [`generate_conversation_title()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.title_utils.md#openhands.sdk.conversation.title_utils.generate_conversation_title)
* [openhands.sdk.conversation.types module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.types.md)
  * [`ConversationID`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.types.md#openhands.sdk.conversation.types.ConversationID)
* [openhands.sdk.conversation.visualizer module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.visualizer.md)
  * [`ConversationVisualizer`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.visualizer.md#openhands.sdk.conversation.visualizer.ConversationVisualizer)
    * [`ConversationVisualizer.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.visualizer.md#openhands.sdk.conversation.visualizer.ConversationVisualizer.__init__)
    * [`ConversationVisualizer.on_event()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.visualizer.md#openhands.sdk.conversation.visualizer.ConversationVisualizer.on_event)
  * [`create_default_visualizer()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.visualizer.md#openhands.sdk.conversation.visualizer.create_default_visualizer)
