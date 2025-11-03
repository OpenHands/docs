---
title: openhands.sdk.event.llm_convertible.message
description: API reference for openhands.sdk.event.llm_convertible.message
---

# openhands.sdk.event.llm_convertible.message module

<a id="module-openhands.sdk.event.llm_convertible.message"></a>

### *class* openhands.sdk.event.llm_convertible.message.MessageEvent(\*, kind: ~typing.Literal['MessageEvent'] = 'MessageEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'], llm_message: ~openhands.sdk.llm.message.Message, llm_response_id: str | None = None, activated_skills: list[str] = `<factory>`, extended_content: list[~openhands.sdk.llm.message.TextContent] = `<factory>`)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

Message from either agent or user.

This is originally the “MessageAction”, but it suppose not to be tool call.

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### llm_message *: [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)*

#### llm_response_id *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### activated_skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### extended_content *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)]*

#### *property* reasoning_content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* thinking_blocks *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)]*

Return the Anthropic thinking blocks from the LLM message.

#### *property* visualize *: Text*

Return Rich Text representation of this message event.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for MessageEvent.

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MessageEvent']*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*
