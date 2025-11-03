---
title: openhands.sdk.tool.registry
description: API reference for openhands.sdk.tool.registry
---

# openhands.sdk.tool.registry module

<a id="module-openhands.sdk.tool.registry"></a>

### openhands.sdk.tool.registry.Resolver

A resolver produces ToolDefinition instances for given params.

**Parameters:**
  - **params** – Arbitrary parameters passed to the resolver. These are typically
    used to configure the ToolDefinition instances that are created.
  - **conversation** – Optional conversation state to get directories from.

Returns: A sequence of ToolDefinition instances. Most of the time this will be a
: single-item
  sequence, but in some cases a ToolDefinition.create may produce multiple tools
  (e.g., BrowserToolSet).

alias of [`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)], ConversationState], [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[`ToolDefinition`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0)]]

### openhands.sdk.tool.registry.register_tool(name: [str](https://docs.python.org/3/library/stdtypes.html#str), factory: [ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0) | [type](https://docs.python.org/3/library/functions.html#type)[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase)] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0)]]) → [None](https://docs.python.org/3/library/constants.html#None)

### openhands.sdk.tool.registry.resolve_tool(tool_spec: [Tool](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool), conv_state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.ConversationState)) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0)]

### openhands.sdk.tool.registry.list_registered_tools() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]
