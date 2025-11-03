---
title: openhands.sdk.event.base
description: API reference for openhands.sdk.event.base
---

# openhands.sdk.event.base module

<a id="module-openhands.sdk.event.base"></a>

### *class* openhands.sdk.event.base.Event

**Parameters:**

- `\*`
- `kind: ~typing.Literal['Condensation', 'CondensationRequest', 'CondensationSummaryEvent', 'ConversationStateUpdateEvent', 'ActionEvent', 'MessageEvent', 'AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation', 'SystemPromptEvent', 'PauseEvent'] = 'Condensation'`
- `id: str = `<factory>``
- `timestamp: str = `<factory>``
- `source: ~typing.Literal['agent', 'user', 'environment']`


Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for all events.

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### *property* visualize *: Text*

Return Rich Text representation of this event.

This is a fallback implementation for unknown event types.
Subclasses should override this method to provide specific visualization.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for display.

#### \_\_repr_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Developer-friendly representation.

#### kind *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.event.base.LLMConvertibleEvent

**Parameters:**

- `\*`
- `kind: ~typing.Literal['CondensationSummaryEvent', 'ActionEvent', 'MessageEvent', 'AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation', 'SystemPromptEvent'] = 'CondensationSummaryEvent'`
- `id: str = `<factory>``
- `timestamp: str = `<factory>``
- `source: ~typing.Literal['agent', 'user', 'environment']`


Bases: [`Event`](#openhands.sdk.event.base.Event), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for events that can be converted to LLM messages.

#### *abstractmethod* to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation showing LLM message content.

#### *static* events_to_messages

**Parameters:**

- `events: [list](https://docs.python.org/3/library/stdtypes.html#list)[[LLMConvertibleEvent](#openhands.sdk.event.base.LLMConvertibleEvent)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message`


Convert event stream to LLM message stream, handling multi-action batches

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### source *: SourceType*

#### kind *: [str](https://docs.python.org/3/library/stdtypes.html#str)*
