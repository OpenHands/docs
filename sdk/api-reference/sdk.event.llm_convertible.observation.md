---
title: openhands.sdk.event.llm_convertible.observation
description: API reference for openhands.sdk.event.llm_convertible.observation
---

# openhands.sdk.event.llm_convertible.observation module

<a id="module-openhands.sdk.event.llm_convertible.observation"></a>

### *class* openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent(\*, kind: ~typing.Literal['AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation'] = 'AgentErrorEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

Base class for anything as a response to a tool call.

Examples include tool execution, error, user reject.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.observation.ObservationEvent(\*, kind: ~typing.Literal['ObservationEvent'] = 'ObservationEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str, observation: ~openhands.sdk.tool.schema.Observation, action_id: str)

Bases: [`ObservationBaseEvent`](#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

#### observation *: [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)*

#### action_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* visualize *: Text*

Return Rich Text representation of this observation event.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for ObservationEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ObservationEvent']*

#### source *: SourceType*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: ToolCallID*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.observation.UserRejectObservation(\*, kind: ~typing.Literal['UserRejectObservation'] = 'UserRejectObservation', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', tool_name: str, tool_call_id: str, rejection_reason: str = 'User rejected the action', action_id: str)

Bases: [`ObservationBaseEvent`](#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

Observation when user rejects an action in confirmation mode.

#### rejection_reason *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### action_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* visualize *: Text*

Return Rich Text representation of this user rejection event.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for UserRejectObservation.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['UserRejectObservation']*

#### source *: SourceType*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: ToolCallID*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.llm_convertible.observation.AgentErrorEvent(\*, kind: ~typing.Literal['AgentErrorEvent'] = 'AgentErrorEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', tool_name: str, tool_call_id: str, error: str)

Bases: [`ObservationBaseEvent`](#openhands.sdk.event.llm_convertible.observation.ObservationBaseEvent)

Error triggered by the agent.

Note: This event should not contain model “thought” or “reasoning_content”. It
represents an error produced by the agent/scaffold, not model output.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### error *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* visualize *: Text*

Return Rich Text representation of this agent error event.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for AgentErrorEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['AgentErrorEvent']*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: ToolCallID*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*
