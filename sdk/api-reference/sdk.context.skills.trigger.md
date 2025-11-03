---
title: openhands.sdk.context.skills.trigger
description: API reference for openhands.sdk.context.skills.trigger
---

# openhands.sdk.context.skills.trigger module

<a id="module-openhands.sdk.context.skills.trigger"></a>

Trigger types for skills.

This module defines different trigger types that determine when a skill
should be activated.

### *class* openhands.sdk.context.skills.trigger.BaseTrigger

Bases: `BaseModel`, [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for all trigger types.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.context.skills.trigger.KeywordTrigger

**Parameters:**

- `type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['keyword'] = 'keyword'`
- `keywords: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`


Bases: [`BaseTrigger`](#openhands.sdk.context.skills.trigger.BaseTrigger)

Trigger for keyword-based skills.

These skills are activated when specific keywords appear in the user’s query.

#### type *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['keyword']*

#### keywords *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.context.skills.trigger.TaskTrigger

**Parameters:**

- `type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['task'] = 'task'`
- `triggers: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`


Bases: [`BaseTrigger`](#openhands.sdk.context.skills.trigger.BaseTrigger)

Trigger for task-specific skills.

These skills are activated for specific task types and can modify prompts.

#### type *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['task']*

#### triggers *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
