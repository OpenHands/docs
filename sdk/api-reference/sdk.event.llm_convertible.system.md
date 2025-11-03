---
title: openhands.sdk.event.llm_convertible.system
description: API reference for openhands.sdk.event.llm_convertible.system
---

# openhands.sdk.event.llm_convertible.system module

<a id="module-openhands.sdk.event.llm_convertible.system"></a>

### *class* openhands.sdk.event.llm_convertible.system.SystemPromptEvent(\*, kind: ~typing.Literal['SystemPromptEvent'] = 'SystemPromptEvent', id: str = <factory>, timestamp: str = <factory>, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', system_prompt: ~openhands.sdk.llm.message.TextContent, tools: list[~litellm.types.llms.openai.ChatCompletionToolParam])

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

System prompt added by the agent.

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### system_prompt *: [TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)*

#### tools *: [list](https://docs.python.org/3/library/stdtypes.html#list)[ChatCompletionToolParam]*

#### *property* visualize *: Text*

Return Rich Text representation of this system prompt event.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for SystemPromptEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['SystemPromptEvent']*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*
