## `openhands.sdk.mcp`

MCP (Model Context Protocol) integration for agent-sdk.

**Modules:**

- [**client**](#openhands.sdk.mcp.client) – Minimal sync helpers on top of fastmcp.Client, preserving original behavior.
- [**definition**](#openhands.sdk.mcp.definition) – MCPTool definition and implementation.
- [**tool**](#openhands.sdk.mcp.tool) – Utility functions for MCP integration.
- [**utils**](#openhands.sdk.mcp.utils) – Utility functions for MCP integration.

**Classes:**

- [**MCPClient**](#openhands.sdk.mcp.MCPClient) – Behaves exactly like fastmcp.Client (same constructor & async API),
- [**MCPToolAction**](#openhands.sdk.mcp.MCPToolAction) – Schema for MCP input action.
- [**MCPToolDefinition**](#openhands.sdk.mcp.MCPToolDefinition) – MCP Tool that wraps an MCP client and provides tool functionality.
- [**MCPToolExecutor**](#openhands.sdk.mcp.MCPToolExecutor) – Executor for MCP tools.
- [**MCPToolObservation**](#openhands.sdk.mcp.MCPToolObservation) – Observation from MCP tool execution.

**Functions:**

- [**create_mcp_tools**](#openhands.sdk.mcp.create_mcp_tools) – Create MCP tools from MCP configuration.

### `openhands.sdk.mcp.MCPClient`

```python
MCPClient(*args, **kwargs)
```

Bases: <code>[Client](#fastmcp.Client)</code>

Behaves exactly like fastmcp.Client (same constructor & async API),
but owns a background event loop and offers:

- call_async_from_sync(awaitable_or_fn, \*args, timeout=None, \*\*kwargs)
- call_sync_from_async(fn, \*args, \*\*kwargs) # await this from async code

**Functions:**

- [**call_async_from_sync**](#openhands.sdk.mcp.MCPClient.call_async_from_sync) – Run a coroutine or async function on this client's loop from sync code.
- [**call_sync_from_async**](#openhands.sdk.mcp.MCPClient.call_sync_from_async) – Await running a blocking function in the default threadpool from async code.
- [**sync_close**](#openhands.sdk.mcp.MCPClient.sync_close) – Synchronously close the MCP client and cleanup resources.

#### `openhands.sdk.mcp.MCPClient.call_async_from_sync`

```python
call_async_from_sync(awaitable_or_fn, *args, timeout, **kwargs)
```

Run a coroutine or async function on this client's loop from sync code.

<details class="usage" open markdown="1">
<summary>Usage</summary>

mcp.call_async_from_sync(async_fn, arg1, kw=...)
mcp.call_async_from_sync(coro)

</details>

#### `openhands.sdk.mcp.MCPClient.call_sync_from_async`

```python
call_sync_from_async(fn, *args, **kwargs)
```

Await running a blocking function in the default threadpool from async code.

#### `openhands.sdk.mcp.MCPClient.sync_close`

```python
sync_close()
```

Synchronously close the MCP client and cleanup resources.

This will attempt to call the async close() method if available,
then shutdown the background event loop.

### `openhands.sdk.mcp.MCPToolAction`

Bases: <code>[Action](#openhands.sdk.tool.schema.Action)</code>

Schema for MCP input action.

It is just a thin wrapper around raw JSON and does
not do any validation.

Validation will be performed by MCPTool.__call__
by constructing dynamically created Pydantic model
from the MCP tool input schema.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.mcp.MCPToolAction.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.mcp.MCPToolAction.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.mcp.MCPToolAction.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.mcp.MCPToolAction.model_json_schema) –
- [**model_post_init**](#openhands.sdk.mcp.MCPToolAction.model_post_init) –
- [**model_rebuild**](#openhands.sdk.mcp.MCPToolAction.model_rebuild) –
- [**model_validate**](#openhands.sdk.mcp.MCPToolAction.model_validate) –
- [**model_validate_json**](#openhands.sdk.mcp.MCPToolAction.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.mcp.MCPToolAction.resolve_kind) –
- [**to_mcp_arguments**](#openhands.sdk.mcp.MCPToolAction.to_mcp_arguments) – Return the data field as MCP tool call arguments.
- [**to_mcp_schema**](#openhands.sdk.mcp.MCPToolAction.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**data**](#openhands.sdk.mcp.MCPToolAction.data) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**kind**](#openhands.sdk.mcp.MCPToolAction.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.mcp.MCPToolAction.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**visualize**](#openhands.sdk.mcp.MCPToolAction.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

#### `openhands.sdk.mcp.MCPToolAction.data`

```python
data: dict[str, Any] = Field(default_factory=dict, description='Dynamic data fields from the tool call')
```

#### `openhands.sdk.mcp.MCPToolAction.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

#### `openhands.sdk.mcp.MCPToolAction.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.mcp.MCPToolAction.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.mcp.MCPToolAction.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

#### `openhands.sdk.mcp.MCPToolAction.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.mcp.MCPToolAction.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolAction.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.mcp.MCPToolAction.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.mcp.MCPToolAction.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolAction.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolAction.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.mcp.MCPToolAction.to_mcp_arguments`

```python
to_mcp_arguments()
```

Return the data field as MCP tool call arguments.

This is used to convert this action to MCP tool call arguments.
The data field contains the dynamic fields from the tool call.

#### `openhands.sdk.mcp.MCPToolAction.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

#### `openhands.sdk.mcp.MCPToolAction.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

### `openhands.sdk.mcp.MCPToolDefinition`

Bases: <code>[ToolDefinition](#openhands.sdk.tool.ToolDefinition)\[[MCPToolAction](#openhands.sdk.mcp.definition.MCPToolAction), [MCPToolObservation](#openhands.sdk.mcp.definition.MCPToolObservation)\]</code>

MCP Tool that wraps an MCP client and provides tool functionality.

**Functions:**

- [**action_from_arguments**](#openhands.sdk.mcp.MCPToolDefinition.action_from_arguments) – Create an MCPToolAction from parsed arguments with early validation.
- [**as_executable**](#openhands.sdk.mcp.MCPToolDefinition.as_executable) – Return this tool as an ExecutableTool, ensuring it has an executor.
- [**create**](#openhands.sdk.mcp.MCPToolDefinition.create) –
- [**get_serializable_type**](#openhands.sdk.mcp.MCPToolDefinition.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.mcp.MCPToolDefinition.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.mcp.MCPToolDefinition.model_json_schema) –
- [**model_post_init**](#openhands.sdk.mcp.MCPToolDefinition.model_post_init) –
- [**model_rebuild**](#openhands.sdk.mcp.MCPToolDefinition.model_rebuild) –
- [**model_validate**](#openhands.sdk.mcp.MCPToolDefinition.model_validate) –
- [**model_validate_json**](#openhands.sdk.mcp.MCPToolDefinition.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.mcp.MCPToolDefinition.resolve_kind) –
- [**set_executor**](#openhands.sdk.mcp.MCPToolDefinition.set_executor) – Create a new Tool instance with the given executor.
- [**to_mcp_tool**](#openhands.sdk.mcp.MCPToolDefinition.to_mcp_tool) –
- [**to_openai_tool**](#openhands.sdk.mcp.MCPToolDefinition.to_openai_tool) – Convert a Tool to an OpenAI tool.
- [**to_responses_tool**](#openhands.sdk.mcp.MCPToolDefinition.to_responses_tool) – Convert a Tool to a Responses API function tool (LiteLLM typed).

**Attributes:**

- [**action_type**](#openhands.sdk.mcp.MCPToolDefinition.action_type) (<code>[type](#type)\[[Action](#openhands.sdk.tool.schema.Action)\]</code>) –
- [**annotations**](#openhands.sdk.mcp.MCPToolDefinition.annotations) (<code>[ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | None</code>) –
- [**description**](#openhands.sdk.mcp.MCPToolDefinition.description) (<code>[str](#str)</code>) –
- [**executor**](#openhands.sdk.mcp.MCPToolDefinition.executor) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | None\]</code>) –
- [**kind**](#openhands.sdk.mcp.MCPToolDefinition.kind) (<code>[str](#str)</code>) –
- [**mcp_tool**](#openhands.sdk.mcp.MCPToolDefinition.mcp_tool) (<code>[Tool](#mcp.types.Tool)</code>) –
- [**meta**](#openhands.sdk.mcp.MCPToolDefinition.meta) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) –
- [**model_config**](#openhands.sdk.mcp.MCPToolDefinition.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**name**](#openhands.sdk.mcp.MCPToolDefinition.name) (<code>[str](#str)</code>) –
- [**observation_type**](#openhands.sdk.mcp.MCPToolDefinition.observation_type) (<code>[type](#type)\[[Observation](#openhands.sdk.tool.schema.Observation)\] | None</code>) –
- [**title**](#openhands.sdk.mcp.MCPToolDefinition.title) (<code>[str](#str)</code>) –

#### `openhands.sdk.mcp.MCPToolDefinition.action_from_arguments`

```python
action_from_arguments(arguments)
```

Create an MCPToolAction from parsed arguments with early validation.

We validate the raw arguments against the MCP tool's input schema here so
Agent.\_get_action_event can catch ValidationError and surface an
AgentErrorEvent back to the model instead of crashing later during tool
execution. On success, we return MCPToolAction with sanitized arguments.

**Parameters:**

- **arguments** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The parsed arguments from the tool call.

**Returns:**

- <code>[MCPToolAction](#openhands.sdk.mcp.definition.MCPToolAction)</code> – The MCPToolAction instance with data populated from the arguments.

**Raises:**

- <code>[ValidationError](#pydantic.ValidationError)</code> – If the arguments do not conform to the tool schema.

#### `openhands.sdk.mcp.MCPToolDefinition.action_type`

```python
action_type: type[Action] = Field(repr=False)
```

#### `openhands.sdk.mcp.MCPToolDefinition.annotations`

```python
annotations: ToolAnnotations | None = None
```

#### `openhands.sdk.mcp.MCPToolDefinition.as_executable`

```python
as_executable()
```

Return this tool as an ExecutableTool, ensuring it has an executor.

This method eliminates the need for runtime None checks by guaranteeing
that the returned tool has a non-None executor.

**Returns:**

- <code>[ExecutableTool](#openhands.sdk.tool.tool.ExecutableTool)</code> – This tool instance, typed as ExecutableTool.

**Raises:**

- <code>[NotImplementedError](#NotImplementedError)</code> – If the tool has no executor.

#### `openhands.sdk.mcp.MCPToolDefinition.create`

```python
create(mcp_tool, mcp_client)
```

#### `openhands.sdk.mcp.MCPToolDefinition.description`

```python
description: str
```

#### `openhands.sdk.mcp.MCPToolDefinition.executor`

```python
executor: SkipJsonSchema[ToolExecutor | None] = Field(default=None, repr=False, exclude=True)
```

#### `openhands.sdk.mcp.MCPToolDefinition.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.mcp.MCPToolDefinition.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.mcp.MCPToolDefinition.mcp_tool`

```python
mcp_tool: mcp.types.Tool = Field(description='The MCP tool definition.')
```

#### `openhands.sdk.mcp.MCPToolDefinition.meta`

```python
meta: dict[str, Any] | None = None
```

#### `openhands.sdk.mcp.MCPToolDefinition.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

#### `openhands.sdk.mcp.MCPToolDefinition.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.mcp.MCPToolDefinition.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolDefinition.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.mcp.MCPToolDefinition.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.mcp.MCPToolDefinition.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolDefinition.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolDefinition.name`

```python
name: str
```

#### `openhands.sdk.mcp.MCPToolDefinition.observation_type`

```python
observation_type: type[Observation] | None = Field(default=None, repr=False)
```

#### `openhands.sdk.mcp.MCPToolDefinition.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.mcp.MCPToolDefinition.set_executor`

```python
set_executor(executor)
```

Create a new Tool instance with the given executor.

#### `openhands.sdk.mcp.MCPToolDefinition.title`

```python
title: str
```

#### `openhands.sdk.mcp.MCPToolDefinition.to_mcp_tool`

```python
to_mcp_tool(input_schema=None, output_schema=None)
```

#### `openhands.sdk.mcp.MCPToolDefinition.to_openai_tool`

```python
to_openai_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to an OpenAI tool.

For MCP, we dynamically create the action_type (type: Schema)
from the MCP tool input schema, and pass it to the parent method.
It will use the .model_fields from this pydantic model to
generate the OpenAI-compatible tool schema.

**Parameters:**

- **add_security_risk_prediction** (<code>[bool](#bool)</code>) – Whether to add a `security_risk` field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.

#### `openhands.sdk.mcp.MCPToolDefinition.to_responses_tool`

```python
to_responses_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ "type": "function", "name": ..., "description": ..., "parameters": ... }

### `openhands.sdk.mcp.MCPToolExecutor`

```python
MCPToolExecutor(tool_name, client)
```

Bases: <code>[ToolExecutor](#openhands.sdk.tool.ToolExecutor)</code>

Executor for MCP tools.

**Functions:**

- [**call_tool**](#openhands.sdk.mcp.MCPToolExecutor.call_tool) –
- [**close**](#openhands.sdk.mcp.MCPToolExecutor.close) – Close the executor and clean up resources.

**Attributes:**

- [**client**](#openhands.sdk.mcp.MCPToolExecutor.client) (<code>[MCPClient](#openhands.sdk.mcp.client.MCPClient)</code>) –
- [**tool_name**](#openhands.sdk.mcp.MCPToolExecutor.tool_name) (<code>[str](#str)</code>) –

#### `openhands.sdk.mcp.MCPToolExecutor.call_tool`

```python
call_tool(action)
```

#### `openhands.sdk.mcp.MCPToolExecutor.client`

```python
client: MCPClient = client
```

#### `openhands.sdk.mcp.MCPToolExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

#### `openhands.sdk.mcp.MCPToolExecutor.tool_name`

```python
tool_name: str = tool_name
```

### `openhands.sdk.mcp.MCPToolObservation`

Bases: <code>[Observation](#openhands.sdk.tool.Observation)</code>

Observation from MCP tool execution.

**Functions:**

- [**from_call_tool_result**](#openhands.sdk.mcp.MCPToolObservation.from_call_tool_result) – Create an MCPToolObservation from a CallToolResult.
- [**from_mcp_schema**](#openhands.sdk.mcp.MCPToolObservation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.mcp.MCPToolObservation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.mcp.MCPToolObservation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.mcp.MCPToolObservation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.mcp.MCPToolObservation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.mcp.MCPToolObservation.model_rebuild) –
- [**model_validate**](#openhands.sdk.mcp.MCPToolObservation.model_validate) –
- [**model_validate_json**](#openhands.sdk.mcp.MCPToolObservation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.mcp.MCPToolObservation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.mcp.MCPToolObservation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**content**](#openhands.sdk.mcp.MCPToolObservation.content) (<code>[list](#list)\[[TextContent](#openhands.sdk.llm.TextContent) | [ImageContent](#openhands.sdk.llm.ImageContent)\]</code>) –
- [**is_error**](#openhands.sdk.mcp.MCPToolObservation.is_error) (<code>[bool](#bool)</code>) –
- [**kind**](#openhands.sdk.mcp.MCPToolObservation.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.mcp.MCPToolObservation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.mcp.MCPToolObservation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.TextContent) | [ImageContent](#openhands.sdk.llm.ImageContent)\]</code>) – Format the observation for agent display.
- [**tool_name**](#openhands.sdk.mcp.MCPToolObservation.tool_name) (<code>[str](#str)</code>) –
- [**visualize**](#openhands.sdk.mcp.MCPToolObservation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this observation.

#### `openhands.sdk.mcp.MCPToolObservation.content`

```python
content: list[TextContent | ImageContent] = Field(default_factory=list, description='Content returned from the MCP tool converted to LLM Ready TextContent or ImageContent')
```

#### `openhands.sdk.mcp.MCPToolObservation.from_call_tool_result`

```python
from_call_tool_result(tool_name, result)
```

Create an MCPToolObservation from a CallToolResult.

#### `openhands.sdk.mcp.MCPToolObservation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

#### `openhands.sdk.mcp.MCPToolObservation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.mcp.MCPToolObservation.is_error`

```python
is_error: bool = Field(default=False, description='Whether the call resulted in an error')
```

#### `openhands.sdk.mcp.MCPToolObservation.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.mcp.MCPToolObservation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

#### `openhands.sdk.mcp.MCPToolObservation.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.mcp.MCPToolObservation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolObservation.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.mcp.MCPToolObservation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.mcp.MCPToolObservation.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolObservation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.mcp.MCPToolObservation.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.mcp.MCPToolObservation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

Format the observation for agent display.

#### `openhands.sdk.mcp.MCPToolObservation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

#### `openhands.sdk.mcp.MCPToolObservation.tool_name`

```python
tool_name: str = Field(description='Name of the tool that was called')
```

#### `openhands.sdk.mcp.MCPToolObservation.visualize`

```python
visualize: Text
```

Return Rich Text representation of this observation.

### `openhands.sdk.mcp.client`

Minimal sync helpers on top of fastmcp.Client, preserving original behavior.

**Classes:**

- [**MCPClient**](#openhands.sdk.mcp.client.MCPClient) – Behaves exactly like fastmcp.Client (same constructor & async API),

#### `openhands.sdk.mcp.client.MCPClient`

```python
MCPClient(*args, **kwargs)
```

Bases: <code>[Client](#fastmcp.Client)</code>

Behaves exactly like fastmcp.Client (same constructor & async API),
but owns a background event loop and offers:

- call_async_from_sync(awaitable_or_fn, \*args, timeout=None, \*\*kwargs)
- call_sync_from_async(fn, \*args, \*\*kwargs) # await this from async code

**Functions:**

- [**call_async_from_sync**](#openhands.sdk.mcp.client.MCPClient.call_async_from_sync) – Run a coroutine or async function on this client's loop from sync code.
- [**call_sync_from_async**](#openhands.sdk.mcp.client.MCPClient.call_sync_from_async) – Await running a blocking function in the default threadpool from async code.
- [**sync_close**](#openhands.sdk.mcp.client.MCPClient.sync_close) – Synchronously close the MCP client and cleanup resources.

##### `openhands.sdk.mcp.client.MCPClient.call_async_from_sync`

```python
call_async_from_sync(awaitable_or_fn, *args, timeout, **kwargs)
```

Run a coroutine or async function on this client's loop from sync code.

<details class="usage" open markdown="1">
<summary>Usage</summary>

mcp.call_async_from_sync(async_fn, arg1, kw=...)
mcp.call_async_from_sync(coro)

</details>

##### `openhands.sdk.mcp.client.MCPClient.call_sync_from_async`

```python
call_sync_from_async(fn, *args, **kwargs)
```

Await running a blocking function in the default threadpool from async code.

##### `openhands.sdk.mcp.client.MCPClient.sync_close`

```python
sync_close()
```

Synchronously close the MCP client and cleanup resources.

This will attempt to call the async close() method if available,
then shutdown the background event loop.

### `openhands.sdk.mcp.create_mcp_tools`

```python
create_mcp_tools(config, timeout=30.0)
```

Create MCP tools from MCP configuration.

### `openhands.sdk.mcp.definition`

MCPTool definition and implementation.

**Classes:**

- [**MCPToolAction**](#openhands.sdk.mcp.definition.MCPToolAction) – Schema for MCP input action.
- [**MCPToolObservation**](#openhands.sdk.mcp.definition.MCPToolObservation) – Observation from MCP tool execution.

**Attributes:**

- [**logger**](#openhands.sdk.mcp.definition.logger) –

#### `openhands.sdk.mcp.definition.MCPToolAction`

Bases: <code>[Action](#openhands.sdk.tool.schema.Action)</code>

Schema for MCP input action.

It is just a thin wrapper around raw JSON and does
not do any validation.

Validation will be performed by MCPTool.__call__
by constructing dynamically created Pydantic model
from the MCP tool input schema.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.mcp.definition.MCPToolAction.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.mcp.definition.MCPToolAction.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.mcp.definition.MCPToolAction.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.mcp.definition.MCPToolAction.model_json_schema) –
- [**model_post_init**](#openhands.sdk.mcp.definition.MCPToolAction.model_post_init) –
- [**model_rebuild**](#openhands.sdk.mcp.definition.MCPToolAction.model_rebuild) –
- [**model_validate**](#openhands.sdk.mcp.definition.MCPToolAction.model_validate) –
- [**model_validate_json**](#openhands.sdk.mcp.definition.MCPToolAction.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.mcp.definition.MCPToolAction.resolve_kind) –
- [**to_mcp_arguments**](#openhands.sdk.mcp.definition.MCPToolAction.to_mcp_arguments) – Return the data field as MCP tool call arguments.
- [**to_mcp_schema**](#openhands.sdk.mcp.definition.MCPToolAction.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**data**](#openhands.sdk.mcp.definition.MCPToolAction.data) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**kind**](#openhands.sdk.mcp.definition.MCPToolAction.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.mcp.definition.MCPToolAction.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**visualize**](#openhands.sdk.mcp.definition.MCPToolAction.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

##### `openhands.sdk.mcp.definition.MCPToolAction.data`

```python
data: dict[str, Any] = Field(default_factory=dict, description='Dynamic data fields from the tool call')
```

##### `openhands.sdk.mcp.definition.MCPToolAction.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.mcp.definition.MCPToolAction.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.mcp.definition.MCPToolAction.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.mcp.definition.MCPToolAction.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.mcp.definition.MCPToolAction.to_mcp_arguments`

```python
to_mcp_arguments()
```

Return the data field as MCP tool call arguments.

This is used to convert this action to MCP tool call arguments.
The data field contains the dynamic fields from the tool call.

##### `openhands.sdk.mcp.definition.MCPToolAction.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.mcp.definition.MCPToolAction.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

#### `openhands.sdk.mcp.definition.MCPToolObservation`

Bases: <code>[Observation](#openhands.sdk.tool.Observation)</code>

Observation from MCP tool execution.

**Functions:**

- [**from_call_tool_result**](#openhands.sdk.mcp.definition.MCPToolObservation.from_call_tool_result) – Create an MCPToolObservation from a CallToolResult.
- [**from_mcp_schema**](#openhands.sdk.mcp.definition.MCPToolObservation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.mcp.definition.MCPToolObservation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.mcp.definition.MCPToolObservation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.mcp.definition.MCPToolObservation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.mcp.definition.MCPToolObservation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.mcp.definition.MCPToolObservation.model_rebuild) –
- [**model_validate**](#openhands.sdk.mcp.definition.MCPToolObservation.model_validate) –
- [**model_validate_json**](#openhands.sdk.mcp.definition.MCPToolObservation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.mcp.definition.MCPToolObservation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.mcp.definition.MCPToolObservation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**content**](#openhands.sdk.mcp.definition.MCPToolObservation.content) (<code>[list](#list)\[[TextContent](#openhands.sdk.llm.TextContent) | [ImageContent](#openhands.sdk.llm.ImageContent)\]</code>) –
- [**is_error**](#openhands.sdk.mcp.definition.MCPToolObservation.is_error) (<code>[bool](#bool)</code>) –
- [**kind**](#openhands.sdk.mcp.definition.MCPToolObservation.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.mcp.definition.MCPToolObservation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.mcp.definition.MCPToolObservation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.TextContent) | [ImageContent](#openhands.sdk.llm.ImageContent)\]</code>) – Format the observation for agent display.
- [**tool_name**](#openhands.sdk.mcp.definition.MCPToolObservation.tool_name) (<code>[str](#str)</code>) –
- [**visualize**](#openhands.sdk.mcp.definition.MCPToolObservation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this observation.

##### `openhands.sdk.mcp.definition.MCPToolObservation.content`

```python
content: list[TextContent | ImageContent] = Field(default_factory=list, description='Content returned from the MCP tool converted to LLM Ready TextContent or ImageContent')
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.from_call_tool_result`

```python
from_call_tool_result(tool_name, result)
```

Create an MCPToolObservation from a CallToolResult.

##### `openhands.sdk.mcp.definition.MCPToolObservation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.mcp.definition.MCPToolObservation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.mcp.definition.MCPToolObservation.is_error`

```python
is_error: bool = Field(default=False, description='Whether the call resulted in an error')
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

Format the observation for agent display.

##### `openhands.sdk.mcp.definition.MCPToolObservation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.mcp.definition.MCPToolObservation.tool_name`

```python
tool_name: str = Field(description='Name of the tool that was called')
```

##### `openhands.sdk.mcp.definition.MCPToolObservation.visualize`

```python
visualize: Text
```

Return Rich Text representation of this observation.

#### `openhands.sdk.mcp.definition.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.mcp.tool`

Utility functions for MCP integration.

**Classes:**

- [**MCPToolDefinition**](#openhands.sdk.mcp.tool.MCPToolDefinition) – MCP Tool that wraps an MCP client and provides tool functionality.
- [**MCPToolExecutor**](#openhands.sdk.mcp.tool.MCPToolExecutor) – Executor for MCP tools.

**Functions:**

- [**to_camel_case**](#openhands.sdk.mcp.tool.to_camel_case) –

**Attributes:**

- [**logger**](#openhands.sdk.mcp.tool.logger) –

#### `openhands.sdk.mcp.tool.MCPToolDefinition`

Bases: <code>[ToolDefinition](#openhands.sdk.tool.ToolDefinition)\[[MCPToolAction](#openhands.sdk.mcp.definition.MCPToolAction), [MCPToolObservation](#openhands.sdk.mcp.definition.MCPToolObservation)\]</code>

MCP Tool that wraps an MCP client and provides tool functionality.

**Functions:**

- [**action_from_arguments**](#openhands.sdk.mcp.tool.MCPToolDefinition.action_from_arguments) – Create an MCPToolAction from parsed arguments with early validation.
- [**as_executable**](#openhands.sdk.mcp.tool.MCPToolDefinition.as_executable) – Return this tool as an ExecutableTool, ensuring it has an executor.
- [**create**](#openhands.sdk.mcp.tool.MCPToolDefinition.create) –
- [**get_serializable_type**](#openhands.sdk.mcp.tool.MCPToolDefinition.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.mcp.tool.MCPToolDefinition.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.mcp.tool.MCPToolDefinition.model_json_schema) –
- [**model_post_init**](#openhands.sdk.mcp.tool.MCPToolDefinition.model_post_init) –
- [**model_rebuild**](#openhands.sdk.mcp.tool.MCPToolDefinition.model_rebuild) –
- [**model_validate**](#openhands.sdk.mcp.tool.MCPToolDefinition.model_validate) –
- [**model_validate_json**](#openhands.sdk.mcp.tool.MCPToolDefinition.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.mcp.tool.MCPToolDefinition.resolve_kind) –
- [**set_executor**](#openhands.sdk.mcp.tool.MCPToolDefinition.set_executor) – Create a new Tool instance with the given executor.
- [**to_mcp_tool**](#openhands.sdk.mcp.tool.MCPToolDefinition.to_mcp_tool) –
- [**to_openai_tool**](#openhands.sdk.mcp.tool.MCPToolDefinition.to_openai_tool) – Convert a Tool to an OpenAI tool.
- [**to_responses_tool**](#openhands.sdk.mcp.tool.MCPToolDefinition.to_responses_tool) – Convert a Tool to a Responses API function tool (LiteLLM typed).

**Attributes:**

- [**action_type**](#openhands.sdk.mcp.tool.MCPToolDefinition.action_type) (<code>[type](#type)\[[Action](#openhands.sdk.tool.schema.Action)\]</code>) –
- [**annotations**](#openhands.sdk.mcp.tool.MCPToolDefinition.annotations) (<code>[ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | None</code>) –
- [**description**](#openhands.sdk.mcp.tool.MCPToolDefinition.description) (<code>[str](#str)</code>) –
- [**executor**](#openhands.sdk.mcp.tool.MCPToolDefinition.executor) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | None\]</code>) –
- [**kind**](#openhands.sdk.mcp.tool.MCPToolDefinition.kind) (<code>[str](#str)</code>) –
- [**mcp_tool**](#openhands.sdk.mcp.tool.MCPToolDefinition.mcp_tool) (<code>[Tool](#mcp.types.Tool)</code>) –
- [**meta**](#openhands.sdk.mcp.tool.MCPToolDefinition.meta) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) –
- [**model_config**](#openhands.sdk.mcp.tool.MCPToolDefinition.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**name**](#openhands.sdk.mcp.tool.MCPToolDefinition.name) (<code>[str](#str)</code>) –
- [**observation_type**](#openhands.sdk.mcp.tool.MCPToolDefinition.observation_type) (<code>[type](#type)\[[Observation](#openhands.sdk.tool.schema.Observation)\] | None</code>) –
- [**title**](#openhands.sdk.mcp.tool.MCPToolDefinition.title) (<code>[str](#str)</code>) –

##### `openhands.sdk.mcp.tool.MCPToolDefinition.action_from_arguments`

```python
action_from_arguments(arguments)
```

Create an MCPToolAction from parsed arguments with early validation.

We validate the raw arguments against the MCP tool's input schema here so
Agent.\_get_action_event can catch ValidationError and surface an
AgentErrorEvent back to the model instead of crashing later during tool
execution. On success, we return MCPToolAction with sanitized arguments.

**Parameters:**

- **arguments** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The parsed arguments from the tool call.

**Returns:**

- <code>[MCPToolAction](#openhands.sdk.mcp.definition.MCPToolAction)</code> – The MCPToolAction instance with data populated from the arguments.

**Raises:**

- <code>[ValidationError](#pydantic.ValidationError)</code> – If the arguments do not conform to the tool schema.

##### `openhands.sdk.mcp.tool.MCPToolDefinition.action_type`

```python
action_type: type[Action] = Field(repr=False)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.annotations`

```python
annotations: ToolAnnotations | None = None
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.as_executable`

```python
as_executable()
```

Return this tool as an ExecutableTool, ensuring it has an executor.

This method eliminates the need for runtime None checks by guaranteeing
that the returned tool has a non-None executor.

**Returns:**

- <code>[ExecutableTool](#openhands.sdk.tool.tool.ExecutableTool)</code> – This tool instance, typed as ExecutableTool.

**Raises:**

- <code>[NotImplementedError](#NotImplementedError)</code> – If the tool has no executor.

##### `openhands.sdk.mcp.tool.MCPToolDefinition.create`

```python
create(mcp_tool, mcp_client)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.description`

```python
description: str
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.executor`

```python
executor: SkipJsonSchema[ToolExecutor | None] = Field(default=None, repr=False, exclude=True)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.mcp.tool.MCPToolDefinition.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.mcp_tool`

```python
mcp_tool: mcp.types.Tool = Field(description='The MCP tool definition.')
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.meta`

```python
meta: dict[str, Any] | None = None
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.name`

```python
name: str
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.observation_type`

```python
observation_type: type[Observation] | None = Field(default=None, repr=False)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.set_executor`

```python
set_executor(executor)
```

Create a new Tool instance with the given executor.

##### `openhands.sdk.mcp.tool.MCPToolDefinition.title`

```python
title: str
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.to_mcp_tool`

```python
to_mcp_tool(input_schema=None, output_schema=None)
```

##### `openhands.sdk.mcp.tool.MCPToolDefinition.to_openai_tool`

```python
to_openai_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to an OpenAI tool.

For MCP, we dynamically create the action_type (type: Schema)
from the MCP tool input schema, and pass it to the parent method.
It will use the .model_fields from this pydantic model to
generate the OpenAI-compatible tool schema.

**Parameters:**

- **add_security_risk_prediction** (<code>[bool](#bool)</code>) – Whether to add a `security_risk` field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.

##### `openhands.sdk.mcp.tool.MCPToolDefinition.to_responses_tool`

```python
to_responses_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ "type": "function", "name": ..., "description": ..., "parameters": ... }

#### `openhands.sdk.mcp.tool.MCPToolExecutor`

```python
MCPToolExecutor(tool_name, client)
```

Bases: <code>[ToolExecutor](#openhands.sdk.tool.ToolExecutor)</code>

Executor for MCP tools.

**Functions:**

- [**call_tool**](#openhands.sdk.mcp.tool.MCPToolExecutor.call_tool) –
- [**close**](#openhands.sdk.mcp.tool.MCPToolExecutor.close) – Close the executor and clean up resources.

**Attributes:**

- [**client**](#openhands.sdk.mcp.tool.MCPToolExecutor.client) (<code>[MCPClient](#openhands.sdk.mcp.client.MCPClient)</code>) –
- [**tool_name**](#openhands.sdk.mcp.tool.MCPToolExecutor.tool_name) (<code>[str](#str)</code>) –

##### `openhands.sdk.mcp.tool.MCPToolExecutor.call_tool`

```python
call_tool(action)
```

##### `openhands.sdk.mcp.tool.MCPToolExecutor.client`

```python
client: MCPClient = client
```

##### `openhands.sdk.mcp.tool.MCPToolExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

##### `openhands.sdk.mcp.tool.MCPToolExecutor.tool_name`

```python
tool_name: str = tool_name
```

#### `openhands.sdk.mcp.tool.logger`

```python
logger = get_logger(__name__)
```

#### `openhands.sdk.mcp.tool.to_camel_case`

```python
to_camel_case(s)
```

### `openhands.sdk.mcp.utils`

Utility functions for MCP integration.

**Functions:**

- [**create_mcp_tools**](#openhands.sdk.mcp.utils.create_mcp_tools) – Create MCP tools from MCP configuration.
- [**log_handler**](#openhands.sdk.mcp.utils.log_handler) – Handles incoming logs from the MCP server and forwards them

**Attributes:**

- [**LOGGING_LEVEL_MAP**](#openhands.sdk.mcp.utils.LOGGING_LEVEL_MAP) –
- [**logger**](#openhands.sdk.mcp.utils.logger) –

#### `openhands.sdk.mcp.utils.LOGGING_LEVEL_MAP`

```python
LOGGING_LEVEL_MAP = logging.getLevelNamesMapping()
```

#### `openhands.sdk.mcp.utils.create_mcp_tools`

```python
create_mcp_tools(config, timeout=30.0)
```

Create MCP tools from MCP configuration.

#### `openhands.sdk.mcp.utils.log_handler`

```python
log_handler(message)
```

Handles incoming logs from the MCP server and forwards them
to the standard Python logging system.

#### `openhands.sdk.mcp.utils.logger`

```python
logger = get_logger(__name__)
```
