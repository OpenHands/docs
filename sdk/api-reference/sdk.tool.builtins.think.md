---
title: openhands.sdk.tool.builtins.think
description: API reference for openhands.sdk.tool.builtins.think
---

# openhands.sdk.tool.builtins.think module

<a id="module-openhands.sdk.tool.builtins.think"></a>

### *class* openhands.sdk.tool.builtins.think.ThinkAction

**Parameters:**

- `kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkAction'] = 'ThinkAction'`
- `thought: [str](https://docs.python.org/3/library/stdtypes.html#str)`


Bases: [`Action`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

Action for logging a thought without making any changes.

#### thought *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* visualize *: Text*

Return Rich Text representation with thinking styling.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkAction']*

### *class* openhands.sdk.tool.builtins.think.ThinkObservation

**Parameters:**

- `kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkObservation'] = 'ThinkObservation'`
- `content: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Your thought has been logged.'`


Bases: [`Observation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Observation returned after logging a thought.

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* to_llm_content *: [Sequence]

**Parameters:**

- `https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent`


Get the observation string to show to the agent.

#### *property* visualize *: Text*

Return Rich Text representation - empty since action shows the thought.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkObservation']*

### *class* openhands.sdk.tool.builtins.think.ThinkExecutor

Bases: [`ToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)
