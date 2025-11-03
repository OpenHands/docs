---
title: openhands.sdk.event.llm_convertible
description: API reference for openhands.sdk.event.llm_convertible
---

# openhands.sdk.event.llm_convertible package

<a id="module-openhands.sdk.event.llm_convertible"></a>

### *class* openhands.sdk.event.llm_convertible.SystemPromptEvent(\*, kind: ~typing.Literal['SystemPromptEvent'] = 'SystemPromptEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', system_prompt: ~openhands.sdk.llm.message.TextContent, tools: list[~litellm.types.llms.openai.ChatCompletionToolParam])

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

System prompt added by the agent.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for SystemPromptEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### *property* visualize *: Text*

Return Rich Text representation of this system prompt event.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### system_prompt *: [TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)*

#### tools *: [list](https://docs.python.org/3/library/stdtypes.html#list)[ChatCompletionToolParam]*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['SystemPromptEvent']*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.ActionEvent(\*, kind: ~typing.Literal['ActionEvent'] = 'ActionEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', thought: ~collections.abc.Sequence[~openhands.sdk.llm.message.TextContent], reasoning_content: str | None = None, thinking_blocks: list[~openhands.sdk.llm.message.ThinkingBlock | ~openhands.sdk.llm.message.RedactedThinkingBlock] = <factory>, responses_reasoning_item: ~openhands.sdk.llm.message.ReasoningItemModel | None = None, action: ~openhands.sdk.tool.schema.Action | None = None, tool_name: str, tool_call_id: str, tool_call: ~openhands.sdk.llm.message.MessageToolCall, llm_response_id: str, security_risk: ~openhands.sdk.security.risk.SecurityRisk = SecurityRisk.UNKNOWN)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for ActionEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

Individual message - may be incomplete for multi-action batches

#### *property* visualize *: Text*

Return Rich Text representation of this action event.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### thought *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)]*

#### reasoning_content *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### thinking_blocks *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[ThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)]*

#### responses_reasoning_item *: [ReasoningItemModel](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel) | [None](https://docs.python.org/3/library/constants.html#None)*

#### action *: [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action) | [None](https://docs.python.org/3/library/constants.html#None)*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call *: [MessageToolCall](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall)*

#### llm_response_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### security_risk *: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ActionEvent']*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.ObservationEvent(\*, kind: ~typing.Literal['ObservationEvent'] = 'ObservationEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str, observation: ~openhands.sdk.tool.schema.Observation, action_id: str)

Bases: [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for ObservationEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### *property* visualize *: Text*

Return Rich Text representation of this observation event.

#### observation *: [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)*

#### action_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ObservationEvent']*

#### source *: SourceType*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: ToolCallID*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.ObservationBaseEvent(\*, kind: ~typing.Literal['AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation'] = 'AgentErrorEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

Base class for anything as a response to a tool call.

Examples include tool execution, error, user reject.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.MessageEvent(\*, kind: ~typing.Literal['MessageEvent'] = 'MessageEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'], llm_message: ~openhands.sdk.llm.message.Message, llm_response_id: str | None = None, activated_skills: list[str] = <factory>, extended_content: list[~openhands.sdk.llm.message.TextContent] = <factory>)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

Message from either agent or user.

This is originally the “MessageAction”, but it suppose not to be tool call.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for MessageEvent.

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* reasoning_content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* thinking_blocks *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)]*

Return the Anthropic thinking blocks from the LLM message.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### *property* visualize *: Text*

Return Rich Text representation of this message event.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### llm_message *: [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)*

#### llm_response_id *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### activated_skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### extended_content *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)]*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MessageEvent']*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.AgentErrorEvent(\*, kind: ~typing.Literal['AgentErrorEvent'] = 'AgentErrorEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', tool_name: str, tool_call_id: str, error: str)

Bases: [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

Error triggered by the agent.

Note: This event should not contain model “thought” or “reasoning_content”. It
represents an error produced by the agent/scaffold, not model output.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for AgentErrorEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### *property* visualize *: Text*

Return Rich Text representation of this agent error event.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### error *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['AgentErrorEvent']*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: ToolCallID*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.UserRejectObservation(\*, kind: ~typing.Literal['UserRejectObservation'] = 'UserRejectObservation', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str, rejection_reason: str = 'User rejected the action', action_id: str)

Bases: [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

Observation when user rejects an action in confirmation mode.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for UserRejectObservation.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### *property* visualize *: Text*

Return Rich Text representation of this user rejection event.

#### rejection_reason *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### action_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['UserRejectObservation']*

#### source *: SourceType*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: ToolCallID*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

## Submodules

* [openhands.sdk.event.llm_convertible.action module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md)
  * [`ActionEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent)
    * [`ActionEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.source)
    * [`ActionEvent.thought`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.thought)
    * [`ActionEvent.reasoning_content`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.reasoning_content)
    * [`ActionEvent.thinking_blocks`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.thinking_blocks)
    * [`ActionEvent.responses_reasoning_item`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.responses_reasoning_item)
    * [`ActionEvent.action`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.action)
    * [`ActionEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.tool_name)
    * [`ActionEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.tool_call_id)
    * [`ActionEvent.tool_call`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.tool_call)
    * [`ActionEvent.llm_response_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.llm_response_id)
    * [`ActionEvent.security_risk`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.security_risk)
    * [`ActionEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.visualize)
    * [`ActionEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.to_llm_message)
    * [`ActionEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.__str__)
    * [`ActionEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.model_config)
    * [`ActionEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.kind)
    * [`ActionEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.id)
    * [`ActionEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent.timestamp)
* [openhands.sdk.event.llm_convertible.message module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md)
  * [`MessageEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent)
    * [`MessageEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.model_config)
    * [`MessageEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.source)
    * [`MessageEvent.llm_message`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.llm_message)
    * [`MessageEvent.llm_response_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.llm_response_id)
    * [`MessageEvent.activated_skills`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.activated_skills)
    * [`MessageEvent.extended_content`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.extended_content)
    * [`MessageEvent.reasoning_content`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.reasoning_content)
    * [`MessageEvent.thinking_blocks`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.thinking_blocks)
    * [`MessageEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.visualize)
    * [`MessageEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.to_llm_message)
    * [`MessageEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.__str__)
    * [`MessageEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.kind)
    * [`MessageEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.id)
    * [`MessageEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.message.md#openhands.sdk.event.llm_convertible.message.MessageEvent.timestamp)
* [openhands.sdk.event.llm_convertible.observation module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md)
  * [`ObservationBaseEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)
    * [`ObservationBaseEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent.source)
    * [`ObservationBaseEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent.tool_name)
    * [`ObservationBaseEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent.tool_call_id)
    * [`ObservationBaseEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent.model_config)
    * [`ObservationBaseEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent.id)
    * [`ObservationBaseEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent.timestamp)
    * [`ObservationBaseEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent.kind)
  * [`ObservationEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent)
    * [`ObservationEvent.observation`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.observation)
    * [`ObservationEvent.action_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.action_id)
    * [`ObservationEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.visualize)
    * [`ObservationEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.to_llm_message)
    * [`ObservationEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.__str__)
    * [`ObservationEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.model_config)
    * [`ObservationEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.kind)
    * [`ObservationEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.source)
    * [`ObservationEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.tool_name)
    * [`ObservationEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.tool_call_id)
    * [`ObservationEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.id)
    * [`ObservationEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.ObservationEvent.timestamp)
  * [`UserRejectObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation)
    * [`UserRejectObservation.rejection_reason`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.rejection_reason)
    * [`UserRejectObservation.action_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.action_id)
    * [`UserRejectObservation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.visualize)
    * [`UserRejectObservation.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.to_llm_message)
    * [`UserRejectObservation.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.__str__)
    * [`UserRejectObservation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.model_config)
    * [`UserRejectObservation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.kind)
    * [`UserRejectObservation.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.source)
    * [`UserRejectObservation.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.tool_name)
    * [`UserRejectObservation.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.tool_call_id)
    * [`UserRejectObservation.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.id)
    * [`UserRejectObservation.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.UserRejectObservation.timestamp)
  * [`AgentErrorEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent)
    * [`AgentErrorEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.source)
    * [`AgentErrorEvent.error`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.error)
    * [`AgentErrorEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.visualize)
    * [`AgentErrorEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.to_llm_message)
    * [`AgentErrorEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.__str__)
    * [`AgentErrorEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.model_config)
    * [`AgentErrorEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.kind)
    * [`AgentErrorEvent.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.tool_name)
    * [`AgentErrorEvent.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.tool_call_id)
    * [`AgentErrorEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.id)
    * [`AgentErrorEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.observation.md#openhands.sdk.event.llm_convertible.observation.AgentErrorEvent.timestamp)
* [openhands.sdk.event.llm_convertible.system module](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md)
  * [`SystemPromptEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent)
    * [`SystemPromptEvent.source`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.source)
    * [`SystemPromptEvent.system_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.system_prompt)
    * [`SystemPromptEvent.tools`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.tools)
    * [`SystemPromptEvent.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.visualize)
    * [`SystemPromptEvent.to_llm_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.to_llm_message)
    * [`SystemPromptEvent.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.__str__)
    * [`SystemPromptEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.model_config)
    * [`SystemPromptEvent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.kind)
    * [`SystemPromptEvent.id`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.id)
    * [`SystemPromptEvent.timestamp`](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.system.md#openhands.sdk.event.llm_convertible.system.SystemPromptEvent.timestamp)
