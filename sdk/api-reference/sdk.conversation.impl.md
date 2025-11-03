---
title: openhands.sdk.conversation.impl
description: API reference for openhands.sdk.conversation.impl
---

# openhands.sdk.conversation.impl package

<a id="module-openhands.sdk.conversation.impl"></a>

### *class* openhands.sdk.conversation.impl.LocalConversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [str](https://docs.python.org/3/library/stdtypes.html#str) | [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace), persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Bases: [`BaseConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation)

#### \_\_del_\_() → [None](https://docs.python.org/3/library/constants.html#None)

Ensure cleanup happens when conversation is destroyed.

#### \_\_init_\_(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [str](https://docs.python.org/3/library/stdtypes.html#str) | [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace), persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Initialize the conversation.

**Parameters:**
  - **agent** – The agent to use for the conversation
  - **workspace** – Working directory for agent operations and tool execution
  - **persistence_dir** – Directory for persisting conversation state and events
  - **conversation_id** – Optional ID for the conversation. If provided, will
    be used to identify the conversation. The user might want to
    suffix their persistent filestore with this ID.
  - **callbacks** – Optional list of callback functions to handle events
  - **max_iteration_per_run** – Maximum number of iterations per run
  - **visualize** – Whether to enable default visualization. If True, adds
    a default visualizer callback. If False, relies on
    application to provide visualization through callbacks.
  - **name_for_visualization** – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.
  - **stuck_detection** – Whether to enable stuck detection

#### close() → [None](https://docs.python.org/3/library/constants.html#None)

Close the conversation and clean up all tool executors.

#### *property* conversation_stats

#### generate_title(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a title for the conversation based on the first user message.

**Parameters:**
  - **llm** – Optional LLM to use for title generation. If not provided,
    uses self.agent.llm.
  - **max_length** – Maximum length of the generated title.
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

### *class* openhands.sdk.conversation.impl.RemoteConversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = False, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Bases: [`BaseConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation)

#### \_\_init_\_(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace), conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = False, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object)) → [None](https://docs.python.org/3/library/constants.html#None)

Remote conversation proxy that talks to an agent server.

**Parameters:**
  - **agent** – Agent configuration (will be sent to the server)
  - **workspace** – The working directory for agent operations and tool execution.
  - **conversation_id** – Optional existing conversation id to attach to
  - **callbacks** – Optional callbacks to receive events (not yet streamed)
  - **max_iteration_per_run** – Max iterations configured on server
  - **stuck_detection** – Whether to enable stuck detection on server
  - **visualize** – Whether to enable the default visualizer callback
  - **name_for_visualization** – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.
  - **secrets** – Optional secrets to initialize the conversation with

#### close() → [None](https://docs.python.org/3/library/constants.html#None)

#### *property* conversation_stats *: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)*

Get conversation stats from remote server.

#### generate_title(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a title for the conversation based on the first user message.

**Parameters:**
  - **llm** – Optional LLM to use for title generation. If provided, its usage_id
    will be sent to the server. If not provided, uses the agent’s LLM.
  - **max_length** – Maximum length of the generated title.
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

## Submodules

* [openhands.sdk.conversation.impl.local_conversation module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md)
  * [`LocalConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation)
    * [`LocalConversation.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.__init__)
    * [`LocalConversation.agent`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.agent)
    * [`LocalConversation.workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.workspace)
    * [`LocalConversation.max_iteration_per_run`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.max_iteration_per_run)
    * [`LocalConversation.llm_registry`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.llm_registry)
    * [`LocalConversation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.id)
    * [`LocalConversation.state`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.state)
    * [`LocalConversation.conversation_stats`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.conversation_stats)
    * [`LocalConversation.stuck_detector`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.stuck_detector)
    * [`LocalConversation.send_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.send_message)
    * [`LocalConversation.run()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.run)
    * [`LocalConversation.set_confirmation_policy()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.set_confirmation_policy)
    * [`LocalConversation.reject_pending_actions()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.reject_pending_actions)
    * [`LocalConversation.pause()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.pause)
    * [`LocalConversation.update_secrets()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.update_secrets)
    * [`LocalConversation.close()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.close)
    * [`LocalConversation.generate_title()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.generate_title)
    * [`LocalConversation.__del__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation.__del__)
* [openhands.sdk.conversation.impl.remote_conversation module](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md)
  * [`WebSocketCallbackClient`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient)
    * [`WebSocketCallbackClient.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.__init__)
    * [`WebSocketCallbackClient.host`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.host)
    * [`WebSocketCallbackClient.conversation_id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.conversation_id)
    * [`WebSocketCallbackClient.callback`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.callback)
    * [`WebSocketCallbackClient.api_key`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.api_key)
    * [`WebSocketCallbackClient.start()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.start)
    * [`WebSocketCallbackClient.stop()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.WebSocketCallbackClient.stop)
  * [`RemoteEventsList`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList)
    * [`RemoteEventsList.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.__init__)
    * [`RemoteEventsList.add_event()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.add_event)
    * [`RemoteEventsList.append()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.append)
    * [`RemoteEventsList.create_default_callback()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteEventsList.create_default_callback)
  * [`RemoteState`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState)
    * [`RemoteState.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.__init__)
    * [`RemoteState.update_state_from_event()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.update_state_from_event)
    * [`RemoteState.create_state_update_callback()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.create_state_update_callback)
    * [`RemoteState.events`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.events)
    * [`RemoteState.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.id)
    * [`RemoteState.agent_status`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.agent_status)
    * [`RemoteState.confirmation_policy`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.confirmation_policy)
    * [`RemoteState.activated_knowledge_skills`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.activated_knowledge_skills)
    * [`RemoteState.agent`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.agent)
    * [`RemoteState.workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.workspace)
    * [`RemoteState.persistence_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.persistence_dir)
    * [`RemoteState.model_dump()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.model_dump)
    * [`RemoteState.model_dump_json()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteState.model_dump_json)
  * [`RemoteConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation)
    * [`RemoteConversation.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.__init__)
    * [`RemoteConversation.agent`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.agent)
    * [`RemoteConversation.max_iteration_per_run`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.max_iteration_per_run)
    * [`RemoteConversation.workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.workspace)
    * [`RemoteConversation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.id)
    * [`RemoteConversation.state`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.state)
    * [`RemoteConversation.conversation_stats`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.conversation_stats)
    * [`RemoteConversation.stuck_detector`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.stuck_detector)
    * [`RemoteConversation.send_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.send_message)
    * [`RemoteConversation.run()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.run)
    * [`RemoteConversation.set_confirmation_policy()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.set_confirmation_policy)
    * [`RemoteConversation.reject_pending_actions()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.reject_pending_actions)
    * [`RemoteConversation.pause()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.pause)
    * [`RemoteConversation.update_secrets()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.update_secrets)
    * [`RemoteConversation.generate_title()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.generate_title)
    * [`RemoteConversation.close()`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.remote_conversation.md#openhands.sdk.conversation.impl.remote_conversation.RemoteConversation.close)
