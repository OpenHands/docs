---
title: openhands.sdk.mcp.definition
description: API reference for openhands.sdk.mcp.definition
---

# openhands.sdk.mcp.definition module

<a id="module-openhands.sdk.mcp.definition"></a>

MCPTool definition and implementation.

### *class* openhands.sdk.mcp.definition.MCPToolAction(\*, kind: ~typing.Literal['MCPToolAction'] = 'MCPToolAction', data: dict[str, ~typing.Any] = `<factory>`)

Bases: [`Action`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

Schema for MCP input action.

It is just a thin wrapper around raw JSON and does
not do any validation.

Validation will be performed by MCPTool._\_call_\_
by constructing dynamically created Pydantic model
from the MCP tool input schema.

#### data *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*

#### to_mcp_arguments() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)

Return the data field as MCP tool call arguments.

This is used to convert this action to MCP tool call arguments.
The data field contains the dynamic fields from the tool call.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolAction']*

### *class* openhands.sdk.mcp.definition.MCPToolObservation(\*, kind: ~typing.Literal['MCPToolObservation'] = 'MCPToolObservation', content: list[~openhands.sdk.llm.message.TextContent | ~openhands.sdk.llm.message.ImageContent] = `<factory>`, is_error: bool = False, tool_name: str)

Bases: [`Observation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Observation from MCP tool execution.

#### content *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

#### is_error *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *classmethod* from_call_tool_result(tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str), result: CallToolResult) → [MCPToolObservation](#openhands.sdk.mcp.definition.MCPToolObservation)

Create an MCPToolObservation from a CallToolResult.

#### *property* to_llm_content *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

Format the observation for agent display.

#### *property* visualize *: Text*

Return Rich Text representation of this observation.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolObservation']*
