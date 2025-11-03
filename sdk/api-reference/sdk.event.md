---
title: openhands.sdk.event
description: API reference for openhands.sdk.event
---

# openhands.sdk.event package

<a id="module-openhands.sdk.event"></a>

### class openhands.sdk.event.Event(kind: ~typing.Literal['Condensation', 'CondensationRequest', 'CondensationSummaryEvent', 'ConversationStateUpdateEvent', 'ActionEvent', 'MessageEvent', 'AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation', 'SystemPromptEvent', 'PauseEvent'] = 'Condensation', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'])

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for all events.

#### \_\_repr_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Developer-friendly representation.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for display.

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### property visualize : Text

Return Rich Text representation of this event.

This is a fallback implementation for unknown event types.
Subclasses should override this method to provide specific visualization.

#### id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### timestamp : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

### class openhands.sdk.event.LLMConvertibleEvent(kind: ~typing.Literal['CondensationSummaryEvent', 'ActionEvent', 'MessageEvent', 'AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation', 'SystemPromptEvent'] = 'CondensationSummaryEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'])

Bases: [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for events that can be converted to LLM messages.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation showing LLM message content.

#### static events_to_messages(events: [list](https://docs.python.org/3/library/stdtypes.html#list)[[LLMConvertibleEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]

Convert event stream to LLM message stream, handling multi-action batches

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### abstractmethod to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

### class openhands.sdk.event.SystemPromptEvent(kind: ~typing.Literal['SystemPromptEvent'] = 'SystemPromptEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', system_prompt: ~openhands.sdk.llm.message.TextContent, tools: list[~litellm.types.llms.openai.ChatCompletionToolParam])

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

System prompt added by the agent.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for SystemPromptEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### property visualize : Text

Return Rich Text representation of this system prompt event.

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### system_prompt : [TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)

#### tools : [list](https://docs.python.org/3/library/stdtypes.html#list)[ChatCompletionToolParam]

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['SystemPromptEvent']

### class openhands.sdk.event.ActionEvent(kind: typing.Literal['ActionEvent'] = 'ActionEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: typing.Literal['agent', 'user', 'environment'] = 'agent', thought: ~collections.abc.Sequence[openhands.sdk.llm.message.TextContent], reasoning_content: str | None = None, thinking_blocks: list[openhands.sdk.llm.message.ThinkingBlock | openhands.sdk.llm.message.RedactedThinkingBlock] = `<factory>`, responses_reasoning_item: openhands.sdk.llm.message.ReasoningItemModel | None = None, action: openhands.sdk.tool.schema.Action | None = None, tool_name: str, tool_call_id: str, tool_call: openhands.sdk.llm.message.MessageToolCall, llm_response_id: str, security_risk: openhands.sdk.security.risk.SecurityRisk = SecurityRisk.UNKNOWN)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for ActionEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

Individual message - may be incomplete for multi-action batches

#### property visualize : Text

Return Rich Text representation of this action event.

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### thought : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)]

#### reasoning_content : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### thinking_blocks : [list](https://docs.python.org/3/library/stdtypes.html#list)[[ThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)]

#### responses_reasoning_item : [ReasoningItemModel](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel) | [None](https://docs.python.org/3/library/constants.html#None)

#### action : [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action) | [None](https://docs.python.org/3/library/constants.html#None)

#### tool_name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### tool_call_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### tool_call : [MessageToolCall](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall)

#### llm_response_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### security_risk : [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ActionEvent']

### class openhands.sdk.event.ObservationEvent(kind: ~typing.Literal['ObservationEvent'] = 'ObservationEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str, observation: ~openhands.sdk.tool.schema.Observation, action_id: str)

Bases: [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for ObservationEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### property visualize : Text

Return Rich Text representation of this observation event.

#### observation : [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

#### action_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ObservationEvent']

### class openhands.sdk.event.ObservationBaseEvent(kind: ~typing.Literal['AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation'] = 'AgentErrorEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

Base class for anything as a response to a tool call.

Examples include tool execution, error, user reject.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### tool_name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### tool_call_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

### class openhands.sdk.event.MessageEvent(kind: ~typing.Literal['MessageEvent'] = 'MessageEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'], llm_message: ~openhands.sdk.llm.message.Message, llm_response_id: str | None = None, activated_skills: list[str] = `<factory>`, extended_content: list[~openhands.sdk.llm.message.TextContent] = `<factory>`)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

Message from either agent or user.

This is originally the “MessageAction”, but it suppose not to be tool call.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for MessageEvent.

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### property reasoning_content : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### property thinking_blocks : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)]

Return the Anthropic thinking blocks from the LLM message.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### property visualize : Text

Return Rich Text representation of this message event.

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### llm_message : [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### llm_response_id : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### activated_skills : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

#### extended_content : [list](https://docs.python.org/3/library/stdtypes.html#list)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)]

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MessageEvent']

### class openhands.sdk.event.AgentErrorEvent(kind: ~typing.Literal['AgentErrorEvent'] = 'AgentErrorEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', tool_name: str, tool_call_id: str, error: str)

Bases: [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

Error triggered by the agent.

Note: This event should not contain model “thought” or “reasoning_content”. It
represents an error produced by the agent/scaffold, not model output.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for AgentErrorEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### property visualize : Text

Return Rich Text representation of this agent error event.

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### error : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['AgentErrorEvent']

### class openhands.sdk.event.UserRejectObservation(kind: ~typing.Literal['UserRejectObservation'] = 'UserRejectObservation', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str, rejection_reason: str = 'User rejected the action', action_id: str)

Bases: [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

Observation when user rejects an action in confirmation mode.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for UserRejectObservation.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### property visualize : Text

Return Rich Text representation of this user rejection event.

#### rejection_reason : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### action_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['UserRejectObservation']

### class openhands.sdk.event.PauseEvent(kind: ~typing.Literal['PauseEvent'] = 'PauseEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'user')

Bases: [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)

Event indicating that the agent execution was paused by user request.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for PauseEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### property visualize : Text

Return Rich Text representation of this pause event.

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['PauseEvent']

### class openhands.sdk.event.Condensation(kind: ~typing.Literal['Condensation'] = 'Condensation', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', forgotten_event_ids: list[str] = `<factory>`, summary: str | None = None, summary_offset: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=0)] = None, llm_response_id: str)

Bases: [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)

This action indicates a condensation of the conversation history is happening.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### property visualize : Text

Return Rich Text representation of this event.

This is a fallback implementation for unknown event types.
Subclasses should override this method to provide specific visualization.

#### forgotten_event_ids : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

#### summary : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### summary_offset : [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)

#### llm_response_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['Condensation']

### class openhands.sdk.event.CondensationRequest(kind: ~typing.Literal['CondensationRequest'] = 'CondensationRequest', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment')

Bases: [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)

This action is used to request a condensation of the conversation history.

#### action

The action type, namely ActionType.CONDENSATION_REQUEST.

- **Type:**
  [str](https://docs.python.org/3/library/stdtypes.html#str)

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['CondensationRequest']

### class openhands.sdk.event.CondensationSummaryEvent(kind: ~typing.Literal['CondensationSummaryEvent'] = 'CondensationSummaryEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', summary: str)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

This event represents a summary generated by a condenser.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### summary : [str](https://docs.python.org/3/library/stdtypes.html#str)

The summary text.

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['CondensationSummaryEvent']

### class openhands.sdk.event.ConversationStateUpdateEvent(kind: ~typing.Literal['ConversationStateUpdateEvent'] = 'ConversationStateUpdateEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', key: str = `<factory>`, value: ~typing.Any = `<factory>`)

Bases: [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)

Event that contains conversation state updates.

This event is sent via websocket whenever the conversation state changes,
allowing remote clients to stay in sync without making REST API calls.

All fields are serialized versions of the corresponding ConversationState fields
to ensure compatibility with websocket transmission.

#### classmethod from_conversation_state(state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.ConversationState)) → [ConversationStateUpdateEvent](#openhands.sdk.event.ConversationStateUpdateEvent)

Create a state update event from a ConversationState object.

This creates an event containing a snapshot of important state fields.

Parameters:
  * state – The ConversationState to serialize
  * conversation_id – The conversation ID for the event
Returns:
  A ConversationStateUpdateEvent with serialized state data

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### classmethod validate_key(key)

#### classmethod validate_value(value, info)

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### key : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### value : [Any](https://docs.python.org/3/library/typing.html#typing.Any)

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ConversationStateUpdateEvent']

### openhands.sdk.event.EventID

alias of [`str`](https://docs.python.org/3/library/stdtypes.html#str)

### openhands.sdk.event.ToolCallID

alias of [`str`](https://docs.python.org/3/library/stdtypes.html#str)

## Subpackages

* [openhands.sdk.event.llm_convertible package](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md)
  * [`SystemPromptEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent)
    * [`SystemPromptEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.__str__)
    * [`SystemPromptEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.model_config)
    * [`SystemPromptEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.to_llm_message)
    * [`SystemPromptEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.visualize)
    * [`SystemPromptEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.source)
    * [`SystemPromptEvent.system_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.system_prompt)
    * [`SystemPromptEvent.tools`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.tools)
    * [`SystemPromptEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.kind)
    * [`SystemPromptEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.id)
    * [`SystemPromptEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.SystemPromptEvent.timestamp)
  * [`ActionEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent)
    * [`ActionEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.__str__)
    * [`ActionEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.model_config)
    * [`ActionEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.to_llm_message)
    * [`ActionEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.visualize)
    * [`ActionEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.source)
    * [`ActionEvent.thought`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.thought)
    * [`ActionEvent.reasoning_content`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.reasoning_content)
    * [`ActionEvent.thinking_blocks`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.thinking_blocks)
    * [`ActionEvent.responses_reasoning_item`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.responses_reasoning_item)
    * [`ActionEvent.action`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.action)
    * [`ActionEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.tool_name)
    * [`ActionEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.tool_call_id)
    * [`ActionEvent.tool_call`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.tool_call)
    * [`ActionEvent.llm_response_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.llm_response_id)
    * [`ActionEvent.security_risk`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.security_risk)
    * [`ActionEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.kind)
    * [`ActionEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.id)
    * [`ActionEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ActionEvent.timestamp)
  * [`ObservationEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent)
    * [`ObservationEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.__str__)
    * [`ObservationEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.model_config)
    * [`ObservationEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.to_llm_message)
    * [`ObservationEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.visualize)
    * [`ObservationEvent.observation`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.observation)
    * [`ObservationEvent.action_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.action_id)
    * [`ObservationEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.kind)
    * [`ObservationEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.source)
    * [`ObservationEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.tool_name)
    * [`ObservationEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.tool_call_id)
    * [`ObservationEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.id)
    * [`ObservationEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationEvent.timestamp)
  * [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent)
    * [`ObservationBaseEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent.model_config)
    * [`ObservationBaseEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent.source)
    * [`ObservationBaseEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent.tool_name)
    * [`ObservationBaseEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent.tool_call_id)
    * [`ObservationBaseEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent.id)
    * [`ObservationBaseEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent.timestamp)
    * [`ObservationBaseEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.ObservationBaseEvent.kind)
  * [`MessageEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent)
    * [`MessageEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.__str__)
    * [`MessageEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.model_config)
    * [`MessageEvent.reasoning_content`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.reasoning_content)
    * [`MessageEvent.thinking_blocks`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.thinking_blocks)
    * [`MessageEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.to_llm_message)
    * [`MessageEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.visualize)
    * [`MessageEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.source)
    * [`MessageEvent.llm_message`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.llm_message)
    * [`MessageEvent.llm_response_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.llm_response_id)
    * [`MessageEvent.activated_skills`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.activated_skills)
    * [`MessageEvent.extended_content`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.extended_content)
    * [`MessageEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.kind)
    * [`MessageEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.id)
    * [`MessageEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.MessageEvent.timestamp)
  * [`AgentErrorEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent)
    * [`AgentErrorEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.__str__)
    * [`AgentErrorEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.model_config)
    * [`AgentErrorEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.to_llm_message)
    * [`AgentErrorEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.visualize)
    * [`AgentErrorEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.source)
    * [`AgentErrorEvent.error`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.error)
    * [`AgentErrorEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.kind)
    * [`AgentErrorEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.tool_name)
    * [`AgentErrorEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.tool_call_id)
    * [`AgentErrorEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.id)
    * [`AgentErrorEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.AgentErrorEvent.timestamp)
  * [`UserRejectObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation)
    * [`UserRejectObservation.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.__str__)
    * [`UserRejectObservation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.model_config)
    * [`UserRejectObservation.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.to_llm_message)
    * [`UserRejectObservation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.visualize)
    * [`UserRejectObservation.rejection_reason`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.rejection_reason)
    * [`UserRejectObservation.action_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.action_id)
    * [`UserRejectObservation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.kind)
    * [`UserRejectObservation.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.source)
    * [`UserRejectObservation.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.tool_name)
    * [`UserRejectObservation.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.tool_call_id)
    * [`UserRejectObservation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.id)
    * [`UserRejectObservation.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#openhands.sdk.event.llm_convertible.UserRejectObservation.timestamp)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.md#submodules)
    * [openhands.sdk.event.llm_convertible.action module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md)
      * [`ActionEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent)
    * [openhands.sdk.event.llm_convertible.message module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md)
      * [`MessageEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent)
    * [openhands.sdk.event.llm_convertible.observation module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md)
      * [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)
      * [`ObservationEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent)
      * [`UserRejectObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation)
      * [`AgentErrorEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent)
    * [openhands.sdk.event.llm_convertible.system module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md)
      * [`SystemPromptEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent)

## Submodules

* [openhands.sdk.event.base module](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md)
  * [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)
    * [`Event.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.model_config)
    * [`Event.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.id)
    * [`Event.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.timestamp)
    * [`Event.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.source)
    * [`Event.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.visualize)
    * [`Event.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.__str__)
    * [`Event.__repr__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.__repr__)
    * [`Event.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event.kind)
  * [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)
    * [`LLMConvertibleEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.to_llm_message)
    * [`LLMConvertibleEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.__str__)
    * [`LLMConvertibleEvent.events_to_messages()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.events_to_messages)
    * [`LLMConvertibleEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.model_config)
    * [`LLMConvertibleEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.id)
    * [`LLMConvertibleEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.timestamp)
    * [`LLMConvertibleEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.source)
    * [`LLMConvertibleEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent.kind)
* [openhands.sdk.event.condenser module](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md)
  * [`Condensation`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation)
    * [`Condensation.forgotten_event_ids`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.forgotten_event_ids)
    * [`Condensation.summary`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.summary)
    * [`Condensation.summary_offset`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.summary_offset)
    * [`Condensation.llm_response_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.llm_response_id)
    * [`Condensation.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.source)
    * [`Condensation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.visualize)
    * [`Condensation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.model_config)
    * [`Condensation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.kind)
    * [`Condensation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.id)
    * [`Condensation.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation.timestamp)
  * [`CondensationRequest`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationRequest)
    * [`CondensationRequest.action`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationRequest.action)
    * [`CondensationRequest.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationRequest.source)
    * [`CondensationRequest.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationRequest.model_config)
    * [`CondensationRequest.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationRequest.kind)
    * [`CondensationRequest.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationRequest.id)
    * [`CondensationRequest.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationRequest.timestamp)
  * [`CondensationSummaryEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent)
    * [`CondensationSummaryEvent.summary`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent.summary)
    * [`CondensationSummaryEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent.source)
    * [`CondensationSummaryEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent.model_config)
    * [`CondensationSummaryEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent.to_llm_message)
    * [`CondensationSummaryEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent.kind)
    * [`CondensationSummaryEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent.id)
    * [`CondensationSummaryEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent.timestamp)
* [openhands.sdk.event.conversation_state module](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md)
  * [`ConversationStateUpdateEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent)
    * [`ConversationStateUpdateEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.source)
    * [`ConversationStateUpdateEvent.key`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.key)
    * [`ConversationStateUpdateEvent.value`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.value)
    * [`ConversationStateUpdateEvent.validate_key()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.validate_key)
    * [`ConversationStateUpdateEvent.validate_value()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.validate_value)
    * [`ConversationStateUpdateEvent.from_conversation_state()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.from_conversation_state)
    * [`ConversationStateUpdateEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.model_config)
    * [`ConversationStateUpdateEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.kind)
    * [`ConversationStateUpdateEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.id)
    * [`ConversationStateUpdateEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.conversation_state.md#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent.timestamp)
* [openhands.sdk.event.types module](https://github.com/OpenHands/software-agent-sdk/sdk.event.types.md)
  * [`EventID`](https://github.com/OpenHands/software-agent-sdk/sdk.event.types.md#openhands.sdk.event.types.EventID)
  * [`ToolCallID`](https://github.com/OpenHands/software-agent-sdk/sdk.event.types.md#openhands.sdk.event.types.ToolCallID)
* [openhands.sdk.event.user_action module](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md)
  * [`PauseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent)
    * [`PauseEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent.source)
    * [`PauseEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent.visualize)
    * [`PauseEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent.__str__)
    * [`PauseEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent.model_config)
    * [`PauseEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent.kind)
    * [`PauseEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent.id)
    * [`PauseEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.user_action.md#openhands.sdk.event.user_action.PauseEvent.timestamp)
