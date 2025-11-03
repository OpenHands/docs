---
title: openhands.sdk.event.llm_convertible.action
description: API reference for openhands.sdk.event.llm_convertible.action
---

# openhands.sdk.event.llm_convertible.action module

<a id="module-openhands.sdk.event.llm_convertible.action"></a>

### *class* openhands.sdk.event.llm_convertible.action.ActionEvent(\*, kind: ~typing.Literal['ActionEvent'] = 'ActionEvent', id: str = `<factory>`, timestamp: str = `<factory>`, source: ~typing.Literal['agent', 'user', 'environment'] = 'agent', thought: ~collections.abc.Sequence[~openhands.sdk.llm.message.TextContent], reasoning_content: str | None = None, thinking_blocks: list[~openhands.sdk.llm.message.ThinkingBlock | ~openhands.sdk.llm.message.RedactedThinkingBlock] = `<factory>`, responses_reasoning_item: ~openhands.sdk.llm.message.ReasoningItemModel | None = None, action: ~openhands.sdk.tool.schema.Action | None = None, tool_name: str, tool_call_id: str, tool_call: ~openhands.sdk.llm.message.MessageToolCall, llm_response_id: str, security_risk: ~openhands.sdk.security.risk.SecurityRisk = SecurityRisk.UNKNOWN)

Bases: [`LLMConvertibleEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)

#### source *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['agent', 'user', 'environment']*

#### thought *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)]*

#### reasoning_content *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### thinking_blocks *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[ThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)]*

#### responses_reasoning_item *: [ReasoningItemModel](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel) | [None](https://docs.python.org/3/library/constants.html#None)*

#### action *: [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action) | [None](https://docs.python.org/3/library/constants.html#None)*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### tool_call *: [MessageToolCall](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall)*

#### llm_response_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### security_risk *: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)*

#### *property* visualize *: Text*

Return Rich Text representation of this action event.

#### to_llm_message() → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

Individual message - may be incomplete for multi-action batches

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Plain text string representation for ActionEvent.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ActionEvent']*

#### id *: EventID*

#### timestamp *: [str](https://docs.python.org/3/library/stdtypes.html#str)*
