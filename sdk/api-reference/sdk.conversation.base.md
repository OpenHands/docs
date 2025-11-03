---
title: openhands.sdk.conversation.base
description: API reference for openhands.sdk.conversation.base
---

# openhands.sdk.conversation.base module

<a id="module-openhands.sdk.conversation.base"></a>

### *class* openhands.sdk.conversation.base.ConversationStateProtocol(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Protocol defining the interface for conversation state objects.

#### *property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

The conversation ID.

#### *property* events *: [EventsListBase](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.events_list_base.md#openhands.sdk.conversation.events_list_base.EventsListBase)*

Access to the events list.

#### *property* agent_status *: [AgentExecutionStatus](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus)*

The current agent execution status.

#### *property* confirmation_policy *: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)*

The confirmation policy.

#### *property* activated_knowledge_skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

List of activated knowledge skills.

#### *property* workspace *: [BaseWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)*

The workspace for agent operations and tool execution.

#### *property* persistence_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

The persistence directory from the FileStore.

If None, it means the conversation is not being persisted.

#### *property* agent *: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.md#openhands.sdk.agent.AgentBase)*

The agent running in the conversation.

#### \_\_init_\_(\*args, \*\*kwargs)

### *class* openhands.sdk.conversation.base.BaseConversation

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

#### *abstract property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

#### *abstract property* state *: [ConversationStateProtocol](#openhands.sdk.conversation.base.ConversationStateProtocol)*

#### *abstract property* conversation_stats *: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)*

#### *abstractmethod* send_message(message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)) → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* run() → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* set_confirmation_policy(policy: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)) → [None](https://docs.python.org/3/library/constants.html#None)

#### *property* confirmation_policy_active *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### *property* is_confirmation_mode_active *: [bool](https://docs.python.org/3/library/functions.html#bool)*

Check if confirmation mode is active.

Returns True if BOTH conditions are met:
1. The agent has a security analyzer set (not None)
2. The confirmation policy is active

#### *abstractmethod* reject_pending_actions(reason: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User rejected the action') → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* pause() → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

#### *abstractmethod* close() → [None](https://docs.python.org/3/library/constants.html#None)

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

#### *static* compose_callbacks(callbacks: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]]) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]

Compose multiple callbacks into a single callback function.

**Parameters:**
  **callbacks** – An iterable of callback functions
**Returns:**
  A single callback function that calls all provided callbacks
