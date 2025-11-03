---
title: openhands.sdk.tool.builtins.finish
description: API reference for openhands.sdk.tool.builtins.finish
---

# openhands.sdk.tool.builtins.finish module

<a id="module-openhands.sdk.tool.builtins.finish"></a>

### *class* openhands.sdk.tool.builtins.finish.FinishAction(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishAction'] = 'FinishAction', message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`Action`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

#### message *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* visualize *: Text*

Return Rich Text representation of this action.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishAction']*

### *class* openhands.sdk.tool.builtins.finish.FinishObservation(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishObservation'] = 'FinishObservation', message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`Observation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

#### message *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* to_llm_content *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

Get the observation string to show to the agent.

#### *property* visualize *: Text*

Return Rich Text representation - empty since action shows the message.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishObservation']*

### *class* openhands.sdk.tool.builtins.finish.FinishExecutor

Bases: [`ToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)
