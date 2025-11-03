---
title: openhands.sdk.tool.schema
description: API reference for openhands.sdk.tool.schema
---

# openhands.sdk.tool.schema module

<a id="module-openhands.sdk.tool.schema"></a>

### openhands.sdk.tool.schema.py_type(spec: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)

Map JSON schema types to Python types.

### *class* openhands.sdk.tool.schema.Schema(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['Schema'] = 'Schema')

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin)

Base schema for input action / output observation.

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### classmethod to_mcp_schema() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Convert to JSON schema format compatible with MCP.

#### classmethod from_mcp_schema(model_name: [str](https://docs.python.org/3/library/stdtypes.html#str), schema: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]) → [type](https://docs.python.org/3/library/functions.html#type)[S]

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as T | None
so explicit nulls are allowed.

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['Schema']

### *class* openhands.sdk.tool.schema.Action(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolAction', 'FinishAction', 'ThinkAction'] = 'MCPToolAction')

Bases: [`Schema`](#openhands.sdk.tool.schema.Schema), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base schema for input action.

#### property visualize : Text

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [str](https://docs.python.org/3/library/stdtypes.html#str)

### *class* openhands.sdk.tool.schema.Observation(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolObservation', 'FinishObservation', 'ThinkObservation'] = 'MCPToolObservation')

Bases: [`Schema`](#openhands.sdk.tool.schema.Schema), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base schema for output observation.

#### abstract property to_llm_content : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]

Get the observation string to show to the agent.

#### property visualize : Text

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [str](https://docs.python.org/3/library/stdtypes.html#str)
