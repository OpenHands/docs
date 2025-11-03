---
title: openhands.sdk.event.conversation_state
description: API reference for openhands.sdk.event.conversation_state
---

# openhands.sdk.event.conversation_state module

<a id="module-openhands.sdk.event.conversation_state"></a>

Events related to conversation state updates.

### *class* openhands.sdk.event.conversation_state.ConversationStateUpdateEvent(\*, kind: ~typing.Literal['ConversationStateUpdateEvent'] = 'ConversationStateUpdateEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'environment', key: str = <factory>, value: ~typing.Any = <factory>)

Bases: [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)

Event that contains conversation state updates.

This event is sent via websocket whenever the conversation state changes,
allowing remote clients to stay in sync without making REST API calls.

All fields are serialized versions of the corresponding ConversationState fields
to ensure compatibility with websocket transmission.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### key *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### value *: [Any](https://docs.python.org/3/library/typing.html#typing.Any)*

#### *classmethod* validate_key(key)

#### *classmethod* validate_value(value, info)

#### *classmethod* from_conversation_state(state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.ConversationState)) → [ConversationStateUpdateEvent](#openhands.sdk.event.conversation_state.ConversationStateUpdateEvent)

Create a state update event from a ConversationState object.

This creates an event containing a snapshot of important state fields.

* **Parameters:**
  * **state** – The ConversationState to serialize
  * **conversation_id** – The conversation ID for the event
* **Returns:**
  A ConversationStateUpdateEvent with serialized state data

#### model_config *: ClassVar[ConfigDict]* *= {'extra': 'forbid', 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ConversationStateUpdateEvent']*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*
