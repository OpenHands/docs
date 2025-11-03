---
title: openhands.sdk.tool.builtins
description: API reference for openhands.sdk.tool.builtins
---

# openhands.sdk.tool.builtins package

<a id="module-openhands.sdk.tool.builtins"></a>

Implementing essential tools that doesn’t interact with the environment.

These are built in and are *required* for the agent to work.

For tools that require interacting with the environment, add them to openhands-tools.

### *class* openhands.sdk.tool.builtins.FinishAction(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishAction'] = 'FinishAction', message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`Action`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

#### model_config *: ClassVar[ConfigDict]* *= {'extra': 'forbid', 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* visualize *: Text*

Return Rich Text representation of this action.

#### message *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishAction']*

### *class* openhands.sdk.tool.builtins.FinishObservation(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishObservation'] = 'FinishObservation', message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`Observation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

#### model_config *: ClassVar[ConfigDict]* *= {'extra': 'forbid', 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* to_llm_content *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

Get the observation string to show to the agent.

#### *property* visualize *: Text*

Return Rich Text representation - empty since action shows the message.

#### message *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['FinishObservation']*

### *class* openhands.sdk.tool.builtins.FinishExecutor

Bases: [`ToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)

### *class* openhands.sdk.tool.builtins.ThinkAction(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkAction'] = 'ThinkAction', thought: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`Action`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

Action for logging a thought without making any changes.

#### model_config *: ClassVar[ConfigDict]* *= {'extra': 'forbid', 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* visualize *: Text*

Return Rich Text representation with thinking styling.

#### thought *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkAction']*

### *class* openhands.sdk.tool.builtins.ThinkObservation(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkObservation'] = 'ThinkObservation', content: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Your thought has been logged.')

Bases: [`Observation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Observation returned after logging a thought.

#### model_config *: ClassVar[ConfigDict]* *= {'extra': 'forbid', 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* to_llm_content *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

Get the observation string to show to the agent.

#### *property* visualize *: Text*

Return Rich Text representation - empty since action shows the thought.

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ThinkObservation']*

### *class* openhands.sdk.tool.builtins.ThinkExecutor

Bases: [`ToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)

## Submodules

* [openhands.sdk.tool.builtins.finish module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md)
  * [`FinishAction`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishAction)
    * [`FinishAction.message`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishAction.message)
    * [`FinishAction.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishAction.visualize)
    * [`FinishAction.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishAction.model_config)
    * [`FinishAction.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishAction.kind)
  * [`FinishObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishObservation)
    * [`FinishObservation.message`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishObservation.message)
    * [`FinishObservation.to_llm_content`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishObservation.to_llm_content)
    * [`FinishObservation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishObservation.visualize)
    * [`FinishObservation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishObservation.model_config)
    * [`FinishObservation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishObservation.kind)
  * [`FinishExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishExecutor)
* [openhands.sdk.tool.builtins.think module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md)
  * [`ThinkAction`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkAction)
    * [`ThinkAction.thought`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkAction.thought)
    * [`ThinkAction.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkAction.visualize)
    * [`ThinkAction.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkAction.model_config)
    * [`ThinkAction.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkAction.kind)
  * [`ThinkObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkObservation)
    * [`ThinkObservation.content`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkObservation.content)
    * [`ThinkObservation.to_llm_content`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkObservation.to_llm_content)
    * [`ThinkObservation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkObservation.visualize)
    * [`ThinkObservation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkObservation.model_config)
    * [`ThinkObservation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkObservation.kind)
  * [`ThinkExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkExecutor)
