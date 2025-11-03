---
title: openhands.sdk.event.user_action
description: API reference for openhands.sdk.event.user_action
---

# openhands.sdk.event.user_action module

<a id="module-openhands.sdk.event.user_action"></a>

### *class* openhands.sdk.event.user_action.PauseEvent(\*, kind: ~typing.Literal['PauseEvent'] = 'PauseEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'user')

Bases: [`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)

Event indicating that the agent execution was paused by user request.

#### source : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']

#### property visualize : Text

Return Rich Text representation of this pause event.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for PauseEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['PauseEvent']

#### id : EventID

#### timestamp : [str](https://docs.python.org/3/library/stdtypes.html#str)
