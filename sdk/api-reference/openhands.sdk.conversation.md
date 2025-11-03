---
title: openhands.sdk.conversation
description: API reference for openhands.sdk.conversation
---

# openhands.sdk.conversation module

### class openhands.sdk.conversation.BaseConversation

Bases: `ABC`

Abstract base class for conversation implementations.

This class defines the interface that all conversation implementations must follow.
Conversations manage the interaction between users and agents, handling message
exchange, execution control, and state management.

#### abstractmethod close

#### static compose_callbacks

Compose multiple callbacks into a single callback function.

* Parameters:
  callbacks – An iterable of callback functions
* Returns:
  A single callback function that calls all provided callbacks

#### property confirmation_policy_active : bool

#### abstract property conversation_stats *: [ConversationStats]

#### abstractmethod generate_title

Generate a title for the conversation based on the first user message.

* Parameters:
  * llm – Optional LLM to use for title generation. If not provided,
    uses the agent’s LLM.
  * max_length – Maximum length of the generated title.
* Returns:
  A generated title for the conversation.
* Raises:
  ValueError – If no user messages are found in the conversation.

#### static get_persistence_dir

Get the persistence directory for the conversation.

#### abstract property id : UUID

#### property is_confirmation_mode_active : bool

Check if confirmation mode is active.

Returns True if BOTH conditions are met:
1. The agent has a security analyzer set (not None)
2. The confirmation policy is active

#### abstractmethod pause

#### abstractmethod reject_pending_actions

#### abstractmethod run

Execute the agent to process messages and perform actions.

This method runs the agent until it finishes processing the current
message or reaches the maximum iteration limit.

#### abstractmethod send_message

Send a message to the agent.

#### abstractmethod set_confirmation_policy

Set the confirmation policy for the conversation.

#### abstract property state : ConversationStateProtocol

#### abstractmethod update_secrets

### Conversation

### Conversation

Bases: `object`

Factory class for creating conversation instances with OpenHands agents.

This factory automatically creates either a LocalConversation or RemoteConversation
based on the workspace type provided. LocalConversation runs the agent locally,
while RemoteConversation connects to a remote agent server.

* Returns:
  LocalConversation if workspace is local, RemoteConversation if workspace
  is remote.

### Example

```pycon
>`>`>` from openhands.sdk import LLM, Agent, Conversation
>`>`>` llm = LLM(model="claude-sonnet-4-20250514", api_key=SecretStr("key"))
>`>`>` agent = Agent(llm=llm, tools=[])
>`>`>` conversation = Conversation(agent=agent, workspace="./workspace")
>`>`>` conversation.send_message("Hello!")
>`>`>` conversation.run()
```

### ConversationState

Bases: `OpenHandsModel`

#### acquire

Acquire the lock.

* Parameters:
  * blocking – If True, block until lock is acquired. If False, return
    immediately.
  * timeout – Maximum time to wait for lock (ignored if blocking=False).
    -1 means wait indefinitely.
* Returns:
  True if lock was acquired, False otherwise.

#### activated_knowledge_skills : list[str]

#### agent *: [AgentBase]

#### agent_status : AgentExecutionStatus

#### confirmation_policy : ConfirmationPolicyBase

#### classmethod create

If base_state.json exists: resume (attach EventLog,
: reconcile agent, enforce id).

Else: create fresh (agent required), persist base, and return.

#### property events *: [EventLog]

#### static get_unmatched_actions

Find actions in the event history that don’t have matching observations.

This method identifies ActionEvents that don’t have corresponding
ObservationEvents or UserRejectObservations, which typically indicates
actions that are pending confirmation or execution.

* Parameters:
  events – List of events to search through
* Returns:
  List of ActionEvent objects that don’t have corresponding observations,
  in chronological order

#### id : UUID

#### locked

Return True if the lock is currently held by any thread.

#### max_iterations : int

#### model_config : ClassVar[ConfigDict] = {}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### owned

Return True if the lock is currently held by the calling thread.

#### persistence_dir : str | None

#### release

Release the lock.

* Raises:
  RuntimeError – If the current thread doesn’t own the lock.

#### secret_registry *: [SecretRegistry]

#### set_on_state_change

Set a callback to be called when state changes.

* Parameters:
  callback – A function that takes an Event (ConversationStateUpdateEvent)
  or None to remove the callback

#### stats *: [ConversationStats]

#### stuck_detection : bool

#### workspace *: [BaseWorkspace]

### ConversationVisualizer

Bases: `object`

Handles visualization of conversation events with Rich formatting.

Provides Rich-formatted output with panels and complete content display.

#### __init__

Initialize the visualizer.

* Parameters:
  * highlight_regex – Dictionary mapping regex patterns to Rich color styles
    for highlighting keywords in the visualizer.
    For example: {“Reasoning:”: “bold blue”,
    “Thought:”: “bold green”}
  * skip_user_messages – If True, skip displaying user messages. Useful for
    scenarios where user input is not relevant to show.
  * conversation_stats – ConversationStats object to display metrics information.
  * name_for_visualization – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.

#### on_event

Main event handler that displays events with Rich formatting.

### EventLog

Bases: [`EventsListBase`](#openhands.sdk.conversation.EventsListBase)

#### __init__

#### append

Add a new event to the list.

#### get_id

Return the event_id for a given index.

#### get_index

Return the integer index for a given event_id.

### class openhands.sdk.conversation.EventsListBase

Bases: `Sequence`[[`Event`](openhands.sdk.event.md#openhands.sdk.event.Event)], `ABC`

Abstract base class for event lists that can be appended to.

This provides a common interface for both local EventLog and remote
RemoteEventsList implementations, avoiding circular imports in protocols.

#### abstractmethod append

Add a new event to the list.

### LocalConversation

Bases: [`BaseConversation`](#openhands.sdk.conversation.BaseConversation)

#### __init__

Initialize the conversation.

* Parameters:
  * agent – The agent to use for the conversation
  * workspace – Working directory for agent operations and tool execution
  * persistence_dir – Directory for persisting conversation state and events
  * conversation_id – Optional ID for the conversation. If provided, will
    be used to identify the conversation. The user might want to
    suffix their persistent filestore with this ID.
  * callbacks – Optional list of callback functions to handle events
  * max_iteration_per_run – Maximum number of iterations per run
  * visualize – Whether to enable default visualization. If True, adds
    a default visualizer callback. If False, relies on
    application to provide visualization through callbacks.
  * name_for_visualization – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.
  * stuck_detection – Whether to enable stuck detection

#### agent *: [AgentBase]

#### close

Close the conversation and clean up all tool executors.

#### property conversation_stats

#### generate_title

Generate a title for the conversation based on the first user message.

* Parameters:
  * llm – Optional LLM to use for title generation. If not provided,
    uses self.agent.llm.
  * max_length – Maximum length of the generated title.
* Returns:
  A generated title for the conversation.
* Raises:
  ValueError – If no user messages are found in the conversation.

#### property id : UUID

Get the unique ID of the conversation.

#### llm_registry *: [LLMRegistry]

#### max_iteration_per_run : int

#### pause

Pause agent execution.

This method can be called from any thread to request that the agent
pause execution. The pause will take effect at the next iteration
of the run loop (between agent steps).

Note: If called during an LLM completion, the pause will not take
effect until the current LLM call completes.

#### reject_pending_actions

Reject all pending actions from the agent.

This is a non-invasive method to reject actions between run() calls.
Also clears the agent_waiting_for_confirmation flag.

#### run

Runs the conversation until the agent finishes.

In confirmation mode:
- First call: creates actions but doesn’t execute them, stops and waits
- Second call: executes pending actions (implicit confirmation)

In normal mode:
- Creates and executes actions immediately

Can be paused between steps

#### send_message

Send a message to the agent.

* Parameters:
  message – Either a string (which will be converted to a user message)
  or a Message object

#### set_confirmation_policy

Set the confirmation policy and store it in conversation state.

#### property state *: [ConversationState]

Get the conversation state.

It returns a protocol that has a subset of ConversationState methods
and properties. We will have the ability to access the same properties
of ConversationState on a remote conversation object.
But we won’t be able to access methods that mutate the state.

#### property stuck_detector *: [StuckDetector]

Get the stuck detector instance if enabled.

#### update_secrets

Add secrets to the conversation.

* Parameters:
  secrets – Dictionary mapping secret keys to values or no-arg callables.
  SecretValue = str | Callable[[], str]. Callables are invoked lazily
  when a command references the secret key.

#### workspace *: [LocalWorkspace]

### RemoteConversation

Bases: [`BaseConversation`](#openhands.sdk.conversation.BaseConversation)

#### __init__

Remote conversation proxy that talks to an agent server.

* Parameters:
  * agent – Agent configuration (will be sent to the server)
  * workspace – The working directory for agent operations and tool execution.
  * conversation_id – Optional existing conversation id to attach to
  * callbacks – Optional callbacks to receive events (not yet streamed)
  * max_iteration_per_run – Max iterations configured on server
  * stuck_detection – Whether to enable stuck detection on server
  * visualize – Whether to enable the default visualizer callback
  * name_for_visualization – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.
  * secrets – Optional secrets to initialize the conversation with

#### agent *: [AgentBase]

#### close

#### property conversation_stats *: [ConversationStats]

Get conversation stats from remote server.

#### generate_title

Generate a title for the conversation based on the first user message.

* Parameters:
  * llm – Optional LLM to use for title generation. If provided, its usage_id
    will be sent to the server. If not provided, uses the agent’s LLM.
  * max_length – Maximum length of the generated title.
* Returns:
  A generated title for the conversation.

#### property id : UUID

#### max_iteration_per_run : int

#### pause

#### reject_pending_actions

#### run

Execute the agent to process messages and perform actions.

This method runs the agent until it finishes processing the current
message or reaches the maximum iteration limit.

#### send_message

Send a message to the agent.

#### set_confirmation_policy

Set the confirmation policy for the conversation.

#### property state : RemoteState

Access to remote conversation state.

#### property stuck_detector

Stuck detector for compatibility.
Not implemented for remote conversations.

#### update_secrets

#### workspace *: [RemoteWorkspace]

### SecretRegistry

Bases: `OpenHandsModel`

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

#### find_secrets_in_text

Find all secret keys mentioned in the given text.

* Parameters:
  text – The text to search for secret keys
* Returns:
  Set of secret keys found in the text

#### get_secrets_as_env_vars

Get secrets that should be exported as environment variables for a command.

* Parameters:
  command – The bash command to check for secret references
* Returns:
  Dictionary of environment variables to export (key ->` value)

#### mask_secrets_in_output

Mask secret values in the given text.

This method uses both the current exported values and attempts to get
fresh values from callables to ensure comprehensive masking.

* Parameters:
  text – The text to mask secrets in
* Returns:
  Text with secret values replaced by `<secret-hidden>`

#### model_config : ClassVar[ConfigDict] = {}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### secret_sources : dict[str, SecretSource]

#### update_secrets

Add or update secrets in the manager.

* Parameters:
  secrets – Dictionary mapping secret keys to either string values
  or callable functions that return string values

### StuckDetector

Bases: `object`

Detects when an agent is stuck in repetitive or unproductive patterns.

This detector analyzes the conversation history to identify various stuck patterns:
1. Repeating action-observation cycles
2. Repeating action-error cycles
3. Agent monologue (repeated messages without user input)
4. Repeating alternating action-observation patterns
5. Context window errors indicating memory issues

#### __init__

#### is_stuck

Check if the agent is currently stuck.

#### state *: [ConversationState]

### get_agent_final_response

Extract the final response from the agent.

An agent can end a conversation in two ways:
1. By calling the finish tool
2. By returning a text message with no tool calls

* Parameters:
  events – List of conversation events to search through.
* Returns:
  The final response message from the agent, or empty string if not found.
