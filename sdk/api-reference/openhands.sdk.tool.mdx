---
title: openhands.sdk.tool
description: API reference for openhands.sdk.tool
---

# openhands.sdk.tool module

OpenHands runtime package.

### Action

Bases: `Schema`, `ABC`

Base schema for input action.

#### kind : str

#### model_config : ClassVar[ConfigDict] = (configuration object)

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### property visualize : Text

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

### ExecutableTool

Bases: `Protocol`

Protocol for tools that are guaranteed to have a non-None executor.

This eliminates the need for runtime None checks and type narrowing
when working with tools that are known to be executable.

#### __init__

#### executor *: [ToolExecutor]

#### name : str

### Observation

Bases: `Schema`, `ABC`

Base schema for output observation.

#### kind : str

#### model_config : ClassVar[ConfigDict] = (configuration object)

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### abstract property to_llm_content *: Sequence[[TextContent]

Get the observation string to show to the agent.

#### property visualize : Text

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

### Tool

Bases: `BaseModel`

Defines a tool to be initialized for the agent.

This is only used in agent-sdk for type schema for server use.

#### model_config : ClassVar[ConfigDict] = {}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### name : str

#### params : dict[str, Any]

#### classmethod validate_name

Validate that name is not empty.

#### classmethod validate_params

Convert None params to empty dict.

### ToolAnnotations

Bases: `BaseModel`

Annotations to provide hints about the tool’s behavior.

Based on Model Context Protocol (MCP) spec:
[https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838)

#### destructiveHint : bool

#### idempotentHint : bool

#### model_config : ClassVar[ConfigDict] = (configuration object)

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### openWorldHint : bool

#### readOnlyHint : bool

#### title : str | None

### ToolBase

Bases: `DiscriminatedUnionMixin`, `ABC`, `Generic`

Base class for tools that agents can use to perform actions.

Tools wrap executor functions with input/output validation and schema definition.
They provide a standardized interface for agents to interact with external systems,
APIs, or perform specific operations.

Features:
- Normalize input/output schemas (class or dict) into both model+schema
- Validate inputs before execution
- Coerce outputs only if an output model is defined; else return vanilla JSON
- Export MCP (Model Context Protocol) tool descriptions

### Example

```pycon
>`>`>` from openhands.sdk.tool import ToolDefinition
>`>`>` tool = ToolDefinition(
...     name="echo",
...     description="Echo the input message",
...     action_type=EchoAction,
...     executor=echo_executor
... )
```

#### action_from_arguments

Create an action from parsed arguments.

This method can be overridden by subclasses to provide custom logic
for creating actions from arguments (e.g., for MCP tools).

* Parameters:
  arguments – The parsed arguments from the tool call.
* Returns:
  The action instance created from the arguments.

#### action_type *: type[[Action]

#### annotations *: [ToolAnnotations]

#### as_executable

Return this tool as an ExecutableTool, ensuring it has an executor.

This method eliminates the need for runtime None checks by guaranteeing
that the returned tool has a non-None executor.

* Returns:
  This tool instance, typed as ExecutableTool.
* Raises:
  NotImplementedError – If the tool has no executor.

#### abstractmethod classmethod create

Create a sequence of Tool instances. Placeholder for subclasses.

This can be overridden in subclasses to provide custom initialization logic
: (e.g., typically initializing the executor with parameters).

* Returns:
  A sequence of Tool instances. Even single tools are returned as a sequence
  to provide a consistent interface and eliminate union return types.

#### description : str

#### executor *: Annotated[[ToolExecutor]

#### kind : str

#### meta : dict[str, Any] | None

#### model_config : ClassVar[ConfigDict] = (configuration object)

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### name : str

#### observation_type *: type[[Observation]

#### classmethod resolve_kind

#### set_executor

Create a new Tool instance with the given executor.

#### property title : str

#### to_mcp_tool

Convert a Tool to an MCP tool definition.

Allow overriding input/output schemas (usually by subclasses).

* Parameters:
  * input_schema – Optionally override the input schema.
  * output_schema – Optionally override the output schema.

#### to_openai_tool

Convert a Tool to an OpenAI tool.

* Parameters:
  * add_security_risk_prediction – Whether to add a security_risk field
    to the action schema for LLM to predict. This is useful for
    tools that may have safety risks, so the LLM can reason about
    the risk level before calling the tool.
  * action_type – Optionally override the action_type to use for the schema.
    This is useful for MCPTool to use a dynamically created action type
    based on the tool’s input schema.

#### to_responses_tool

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ “type”: “function”, “name”: …, “description”: …, “parameters”: … }

### ToolDefinition

Bases: `ToolBase[TypeVar, TypeVar]`, `Generic`

Concrete tool class that inherits from ToolBase.

This class serves as a concrete implementation of ToolBase for cases where
you want to create a tool instance directly without implementing a custom
subclass. Built-in tools (like FinishTool, ThinkTool) are instantiated
directly from this class, while more complex tools (like BashTool,
FileEditorTool) inherit from this class and provide their own create()
method implementations.

#### action_type *: type[[Action]

#### annotations *: [ToolAnnotations]

#### classmethod create

Create a sequence of ToolDefinition instances.

TODO [https://github.com/OpenHands/agent-sdk/issues/493](https://github.com/OpenHands/agent-sdk/issues/493)
Refactor this - the ToolDefinition class should not have a concrete create()
implementation. Built-in tools should be refactored to not rely on this
method, and then this should be made abstract with @abstractmethod.

#### description : str

#### executor *: SkipJsonSchema[[ToolExecutor]

#### kind : Literal['ToolDefinition']

#### meta : dict[str, Any] | None

#### model_config : ClassVar[ConfigDict] = (configuration object)

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### name : str

#### observation_type *: type[[Observation]

### class openhands.sdk.tool.ToolExecutor

Bases: `ABC`, `Generic`

Executor function type for a Tool.

#### close

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

### list_registered_tools

### register_tool

### resolve_tool
