---
title: openhands.sdk.conversation.impl.remote_conversation
description: API reference for openhands.sdk.conversation.impl.remote_conversation
---

# openhands.sdk.conversation.impl.remote_conversation module

<a id="module-openhands.sdk.conversation.impl.remote_conversation"></a>

### *class* openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient(host: [str](https://docs.python.org/3/library/stdtypes.html#str), conversation_id: [str](https://docs.python.org/3/library/stdtypes.html#str), callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)], api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Minimal WS client: connects, forwards events, retries on error.

#### \_\_init_\_(host: [str](https://docs.python.org/3/library/stdtypes.html#str), conversation_id: [str](https://docs.python.org/3/library/stdtypes.html#str), callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)], api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

#### host *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### conversation_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### callback *: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]*

#### api_key *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### start() → [None](https://docs.python.org/3/library/constants.html#None)

#### stop() → [None](https://docs.python.org/3/library/constants.html#None)

### *class* openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList(client: Client, conversation_id: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`EventsListBase`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.events_list_base.md#openhands.sdk.conversation.events_list_base.EventsListBase)

A list-like, read-only view of remote conversation events.

On first access it fetches existing events from the server. Afterwards,
it relies on the WebSocket stream to incrementally append new events.

#### \_\_init_\_(client: Client, conversation_id: [str](https://docs.python.org/3/library/stdtypes.html#str))

#### add_event(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Add a new event to the local cache (called by WebSocket callback).

#### append(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Add a new event to the list (for compatibility with EventLog interface).

#### create_default_callback() → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]

Create a default callback that adds events to this list.

### *class* openhands.sdk.conversation.impl.remote_conversation.RemoteState(client: Client, conversation_id: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`ConversationStateProtocol`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.ConversationStateProtocol)

A state-like interface for accessing remote conversation state.

#### \_\_init_\_(client: Client, conversation_id: [str](https://docs.python.org/3/library/stdtypes.html#str))

#### update_state_from_event(event: [ConversationStateUpdateEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent)) → [None](https://docs.python.org/3/library/constants.html#None)

Update cached state from a ConversationStateUpdateEvent.

#### create_state_update_callback() → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]

Create a callback that updates state from ConversationStateUpdateEvent.

#### *property* events *: [RemoteEventsList](#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList)*

Access to the events list.

#### *property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

The conversation ID.

#### *property* agent_status *: [AgentExecutionStatus](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.AgentExecutionStatus)*

The current agent execution status.

#### *property* confirmation_policy *: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)*

The confirmation policy.

#### *property* activated_knowledge_skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

List of activated knowledge skills.

#### *property* agent

The agent configuration (fetched from remote).

#### *property* workspace

The working directory (fetched from remote).

#### *property* persistence_dir

The persistence directory (fetched from remote).

#### model_dump(\*\*\_kwargs)

Get a dictionary representation of the remote state.

#### model_dump_json(\*\*kwargs)

Get a JSON representation of the remote state.

### *class* openhands.sdk.conversation.impl.remote_conversation.RemoteConversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = False, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Bases: [`BaseConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation)

#### \_\_init_\_(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = False, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object)) → [None](https://docs.python.org/3/library/constants.html#None)

Remote conversation proxy that talks to an agent server.

* **Parameters:**
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

#### agent *: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)*

#### max_iteration_per_run *: [int](https://docs.python.org/3/library/functions.html#int)*

#### workspace *: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace)*

#### *property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

#### *property* state *: [RemoteState](#openhands.sdk.conversation.impl.remote_conversation.RemoteState)*

Access to remote conversation state.

#### *property* conversation_stats *: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)*

Get conversation stats from remote server.

#### *property* stuck_detector

Stuck detector for compatibility.
Not implemented for remote conversations.

#### send_message(message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)) → [None](https://docs.python.org/3/library/constants.html#None)

#### run() → [None](https://docs.python.org/3/library/constants.html#None)

#### set_confirmation_policy(policy: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)) → [None](https://docs.python.org/3/library/constants.html#None)

#### reject_pending_actions(reason: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User rejected the action') → [None](https://docs.python.org/3/library/constants.html#None)

#### pause() → [None](https://docs.python.org/3/library/constants.html#None)

#### update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

#### generate_title(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a title for the conversation based on the first user message.

* **Parameters:**
  * **llm** – Optional LLM to use for title generation. If provided, its usage_id
    will be sent to the server. If not provided, uses the agent’s LLM.
  * **max_length** – Maximum length of the generated title.
* **Returns:**
  A generated title for the conversation.

#### close() → [None](https://docs.python.org/3/library/constants.html#None)
