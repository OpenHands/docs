---
title: openhands.sdk.mcp.tool
description: API reference for openhands.sdk.mcp.tool
---

# openhands.sdk.mcp.tool module

<a id="module-openhands.sdk.mcp.tool"></a>

Utility functions for MCP integration.

### openhands.sdk.mcp.tool.to_camel_case(s: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

### class openhands.sdk.mcp.tool.MCPToolExecutor(tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str), client: [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient))

Bases: [`ToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)

Executor for MCP tools.

#### \_\_init_\_(tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str), client: [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient))

#### tool_name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### client : [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient)

#### async call_tool(action: [MCPToolAction](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction)) → [MCPToolObservation](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation)

#### \_\_call_\_(action: [MCPToolAction](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction), conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [MCPToolObservation](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolObservation)

Execute an MCP tool call.

### class openhands.sdk.mcp.tool.MCPToolDefinition(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolDefinition'] = 'MCPToolDefinition', name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str), action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)], observation_type: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None) = None, annotations: [ToolAnnotations](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None) = None, meta: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, executor: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()] = None, mcp_tool: Tool)

Bases: `ToolDefinition[MCPToolAction, MCPToolObservation]`

MCP Tool that wraps an MCP client and provides tool functionality.

#### mcp_tool : Tool

#### \_\_call_\_(action: [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action), conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Execute the tool action using the MCP client.

We dynamically create a new MCPToolAction class with
the tool’s input schema to validate the action.

Parameters:
  action – The action to execute.
Returns:
  The observation result from executing the action.

#### action_from_arguments(arguments: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]) → [MCPToolAction](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.definition.md#openhands.sdk.mcp.definition.MCPToolAction)

Create an MCPToolAction from parsed arguments with early validation.

We validate the raw arguments against the MCP tool’s input schema here so
Agent._get_action_event can catch ValidationError and surface an
AgentErrorEvent back to the model instead of crashing later during tool
execution. On success, we return MCPToolAction with sanitized arguments.

Parameters:
  arguments – The parsed arguments from the tool call.
Returns:
  The MCPToolAction instance with data populated from the arguments.
Raises:
  ValidationError – If the arguments do not conform to the tool schema.

#### classmethod create(mcp_tool: Tool, mcp_client: [MCPClient](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.client.md#openhands.sdk.mcp.client.MCPClient)) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[MCPToolDefinition](#openhands.sdk.mcp.tool.MCPToolDefinition)]

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

Parameters:
  * input_schema – Optionally override the input schema.
  * output_schema – Optionally override the output schema.

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolDefinition']

#### name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### description : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### action_type : [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.Action)]

#### observation_type : [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.Observation)] | [None](https://docs.python.org/3/library/constants.html#None)

#### annotations : [ToolAnnotations](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None)

#### meta : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any] | [None](https://docs.python.org/3/library/constants.html#None)

#### executor : SkipJsonSchema[[ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None)]

#### to_openai_tool(add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Schema](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → ChatCompletionToolParam

Convert a Tool to an OpenAI tool.

For MCP, we dynamically create the action_type (type: Schema)
from the MCP tool input schema, and pass it to the parent method.
It will use the .model_fields from this pydantic model to
generate the OpenAI-compatible tool schema.

Parameters:
  add_security_risk_prediction – Whether to add a security_risk field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.
