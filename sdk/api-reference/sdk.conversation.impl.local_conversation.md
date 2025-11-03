---
title: openhands.sdk.conversation.impl.local_conversation
description: API reference for openhands.sdk.conversation.impl.local_conversation
---

# openhands.sdk.conversation.impl.local_conversation module

<a id="module-openhands.sdk.conversation.impl.local_conversation"></a>

### *class* openhands.sdk.conversation.impl.local_conversation.LocalConversation(agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [str](https://docs.python.org/3/library/stdtypes.html#str) | [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace), persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None, callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*\_: [object](https://docs.python.org/3/library/functions.html#object))

Bases: [`BaseConversation`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.base.md#openhands.sdk.conversation.base.BaseConversation)

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

#### agent *: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)*

#### workspace *: [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace)*

#### max_iteration_per_run *: [int](https://docs.python.org/3/library/functions.html#int)*

#### llm_registry *: [LLMRegistry](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry)*

#### *property* id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

Get the unique ID of the conversation.

#### *property* state *: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)*

Get the conversation state.

It returns a protocol that has a subset of ConversationState methods
and properties. We will have the ability to access the same properties
of ConversationState on a remote conversation object.
But we won’t be able to access methods that mutate the state.

#### *property* conversation_stats

#### *property* stuck_detector *: [StuckDetector](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.stuck_detector.md#openhands.sdk.conversation.stuck_detector.StuckDetector) | [None](https://docs.python.org/3/library/constants.html#None)*

Get the stuck detector instance if enabled.

#### send_message(message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)) → [None](https://docs.python.org/3/library/constants.html#None)

Send a message to the agent.

**Parameters:**
  **message** – Either a string (which will be converted to a user message)
  or a Message object

#### run() → [None](https://docs.python.org/3/library/constants.html#None)

Runs the conversation until the agent finishes.

In confirmation mode:
- First call: creates actions but doesn’t execute them, stops and waits
- Second call: executes pending actions (implicit confirmation)

In normal mode:
- Creates and executes actions immediately

Can be paused between steps

#### set_confirmation_policy(policy: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)) → [None](https://docs.python.org/3/library/constants.html#None)

Set the confirmation policy and store it in conversation state.

#### reject_pending_actions(reason: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User rejected the action') → [None](https://docs.python.org/3/library/constants.html#None)

Reject all pending actions from the agent.

This is a non-invasive method to reject actions between run() calls.
Also clears the agent_waiting_for_confirmation flag.

#### pause() → [None](https://docs.python.org/3/library/constants.html#None)

Pause agent execution.

This method can be called from any thread to request that the agent
pause execution. The pause will take effect at the next iteration
of the run loop (between agent steps).

Note: If called during an LLM completion, the pause will not take
effect until the current LLM call completes.

#### update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

Add secrets to the conversation.

**Parameters:**
  **secrets** – Dictionary mapping secret keys to values or no-arg callables.
  SecretValue = str | Callable[[], str]. Callables are invoked lazily
  when a command references the secret key.

#### close() → [None](https://docs.python.org/3/library/constants.html#None)

Close the conversation and clean up all tool executors.

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

#### \_\_del_\_() → [None](https://docs.python.org/3/library/constants.html#None)

Ensure cleanup happens when conversation is destroyed.
