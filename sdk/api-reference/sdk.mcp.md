---
title: openhands.sdk.mcp
description: API reference for openhands.sdk.mcp
---

# openhands.sdk.mcp package

<a id="module-openhands.sdk.mcp"></a>

MCP (Model Context Protocol) integration for agent-sdk.

### *class* openhands.sdk.mcp.MCPClient(\*args, \*\*kwargs)

Bases: `Client`

Behaves exactly like fastmcp.Client (same constructor & async API),
but owns a background event loop and offers:

> - call_async_from_sync(awaitable_or_fn, 

>   ```
>   *
>   ```

>   args, timeout=None, 

>   ```
>   **
>   ```

>   kwargs)
> - call_sync_from_async(fn, 

>   ```
>   *
>   ```

>   args, 

>   ```
>   **
>   ```

>   kwargs)  # await this from async code

#### \_\_del_\_()

Cleanup on deletion.

#### \_\_init_\_(\*args, \*\*kwargs)

#### call_async_from_sync(awaitable_or_fn: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [Any](https://docs.python.org/3/library/typing.html#typing.Any), \*args, timeout: [float](https://docs.python.org/3/library/functions.html#float), \*\*kwargs) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)

Run a coroutine or async function on this client’s loop from sync code.

Usage:
: mcp.call_async_from_sync(async_fn, arg1, kw=…)
  mcp.call_async_from_sync(coro)

#### *async* call_sync_from_async(fn: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)], \*args, \*\*kwargs) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)

Await running a blocking function in the default threadpool from async code.

#### sync_close() → [None](https://docs.python.org/3/library/constants.html#None)

Synchronously close the MCP client and cleanup resources.

This will attempt to call the async close() method if available,
then shutdown the background event loop.

### *class* openhands.sdk.mcp.MCPToolDefinition(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolDefinition'] = 'MCPToolDefinition', name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str), action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)], observation_type: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None) = None, annotations: [ToolAnnotations](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None) = None, meta: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, executor: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()] = None, mcp_tool: Tool)

Bases: `ToolDefinition[MCPToolAction, MCPToolObservation]`

MCP Tool that wraps an MCP client and provides tool functionality.

#### \_\_call_\_(action: [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action), conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Execute the tool action using the MCP client.

We dynamically create a new MCPToolAction class with
the tool’s input schema to validate the action.

* **Parameters:**
  **action** – The action to execute.
* **Returns:**
  The observation result from executing the action.

#### action_from_arguments(arguments: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]) → [MCPToolAction](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction)

Create an MCPToolAction from parsed arguments with early validation.

We validate the raw arguments against the MCP tool’s input schema here so
Agent._get_action_event can catch ValidationError and surface an
AgentErrorEvent back to the model instead of crashing later during tool
execution. On success, we return MCPToolAction with sanitized arguments.

* **Parameters:**
  **arguments** – The parsed arguments from the tool call.
* **Returns:**
  The MCPToolAction instance with data populated from the arguments.
* **Raises:**
  **ValidationError** – If the arguments do not conform to the tool schema.

#### *classmethod* create(mcp_tool: Tool, mcp_client: [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient)) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[MCPToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition)]

Create a sequence of ToolDefinition instances.

TODO [https://github.com/OpenHands/agent-sdk/issues/493](https://github.com/OpenHands/agent-sdk/issues/493)
Refactor this - the ToolDefinition class should not have a concrete create()
implementation. Built-in tools should be refactored to not rely on this
method, and then this should be made abstract with @abstractmethod.

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_mcp_tool(input_schema: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, output_schema: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Convert a Tool to an MCP tool definition.

Allow overriding input/output schemas (usually by subclasses).

* **Parameters:**
  * **input_schema** – Optionally override the input schema.
  * **output_schema** – Optionally override the output schema.

#### to_openai_tool(add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Schema](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → ChatCompletionToolParam

Convert a Tool to an OpenAI tool.

For MCP, we dynamically create the action_type (type: Schema)
from the MCP tool input schema, and pass it to the parent method.
It will use the .model_fields from this pydantic model to
generate the OpenAI-compatible tool schema.

* **Parameters:**
  **add_security_risk_prediction** – Whether to add a security_risk field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.

#### mcp_tool *: Tool*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolDefinition']*

### *class* openhands.sdk.mcp.MCPToolAction(\*, kind: ~typing.Literal['MCPToolAction'] = 'MCPToolAction', data: dict[str, ~typing.Any] = <factory>)

Bases: [`Action`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

Schema for MCP input action.

It is just a thin wrapper around raw JSON and does
not do any validation.

Validation will be performed by MCPTool._\_call_\_
by constructing dynamically created Pydantic model
from the MCP tool input schema.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_mcp_arguments() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)

Return the data field as MCP tool call arguments.

This is used to convert this action to MCP tool call arguments.
The data field contains the dynamic fields from the tool call.

#### data *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolAction']*

### *class* openhands.sdk.mcp.MCPToolObservation(\*, kind: ~typing.Literal['MCPToolObservation'] = 'MCPToolObservation', content: list[~openhands.sdk.llm.message.TextContent | ~openhands.sdk.llm.message.ImageContent] = <factory>, is_error: bool = False, tool_name: str)

Bases: [`Observation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Observation from MCP tool execution.

#### *classmethod* from_call_tool_result(tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str), result: CallToolResult) → [MCPToolObservation](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation)

Create an MCPToolObservation from a CallToolResult.

#### model_config  : ClassVar[ConfigDict]*  = \{'extra': 'forbid', 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* to_llm_content *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

Format the observation for agent display.

#### *property* visualize *: Text*

Return Rich Text representation of this observation.

#### content *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

#### is_error *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolObservation']*

### *class* openhands.sdk.mcp.MCPToolExecutor(tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str), client: [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient))

Bases: [`ToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)

Executor for MCP tools.

#### \_\_call_\_(action: [MCPToolAction](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction), conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [MCPToolObservation](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation)

Execute an MCP tool call.

#### \_\_init_\_(tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str), client: [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient))

#### *async* call_tool(action: [MCPToolAction](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction)) → [MCPToolObservation](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation)

#### tool_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### client *: [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient)*

### openhands.sdk.mcp.create_mcp_tools(config: [dict](https://docs.python.org/3/library/stdtypes.html#dict) | MCPConfig, timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[MCPToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition)]

Create MCP tools from MCP configuration.

## Submodules

* [openhands.sdk.mcp.client module](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md)
  * [`MCPClient`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient)
    * [`MCPClient.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient.__init__)
    * [`MCPClient.call_async_from_sync()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient.call_async_from_sync)
    * [`MCPClient.call_sync_from_async()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient.call_sync_from_async)
    * [`MCPClient.sync_close()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient.sync_close)
    * [`MCPClient.__del__()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient.__del__)
* [openhands.sdk.mcp.definition module](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md)
  * [`MCPToolAction`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction)
    * [`MCPToolAction.data`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction.data)
    * [`MCPToolAction.to_mcp_arguments()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction.to_mcp_arguments)
    * [`MCPToolAction.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction.model_config)
    * [`MCPToolAction.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction.kind)
  * [`MCPToolObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation)
    * [`MCPToolObservation.content`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.content)
    * [`MCPToolObservation.is_error`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.is_error)
    * [`MCPToolObservation.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.tool_name)
    * [`MCPToolObservation.from_call_tool_result()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.from_call_tool_result)
    * [`MCPToolObservation.to_llm_content`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.to_llm_content)
    * [`MCPToolObservation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.visualize)
    * [`MCPToolObservation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.model_config)
    * [`MCPToolObservation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation.kind)
* [openhands.sdk.mcp.tool module](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md)
  * [`to_camel_case()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.to_camel_case)
  * [`MCPToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolExecutor)
    * [`MCPToolExecutor.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolExecutor.__init__)
    * [`MCPToolExecutor.tool_name`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolExecutor.tool_name)
    * [`MCPToolExecutor.client`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolExecutor.client)
    * [`MCPToolExecutor.call_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolExecutor.call_tool)
    * [`MCPToolExecutor.__call__()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolExecutor.__call__)
  * [`MCPToolDefinition`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition)
    * [`MCPToolDefinition.mcp_tool`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.mcp_tool)
    * [`MCPToolDefinition.__call__()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.__call__)
    * [`MCPToolDefinition.action_from_arguments()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.action_from_arguments)
    * [`MCPToolDefinition.create()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.create)
    * [`MCPToolDefinition.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.model_config)
    * [`MCPToolDefinition.to_mcp_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.to_mcp_tool)
    * [`MCPToolDefinition.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.kind)
    * [`MCPToolDefinition.name`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.name)
    * [`MCPToolDefinition.description`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.description)
    * [`MCPToolDefinition.action_type`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.action_type)
    * [`MCPToolDefinition.observation_type`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.observation_type)
    * [`MCPToolDefinition.annotations`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.annotations)
    * [`MCPToolDefinition.meta`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.meta)
    * [`MCPToolDefinition.executor`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.executor)
    * [`MCPToolDefinition.to_openai_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition.to_openai_tool)
* [openhands.sdk.mcp.utils module](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.utils.md)
  * [`log_handler()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.utils.md#openhands.sdk.mcp.utils.log_handler)
  * [`create_mcp_tools()`](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.utils.md#openhands.sdk.mcp.utils.create_mcp_tools)
