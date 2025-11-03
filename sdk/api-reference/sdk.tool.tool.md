---
title: openhands.sdk.tool.tool
description: API reference for openhands.sdk.tool.tool
---

# openhands.sdk.tool.tool module

<a id="module-openhands.sdk.tool.tool"></a>

### *class* openhands.sdk.tool.tool.ToolAnnotations(, title: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, readOnlyHint: [bool](https://docs.python.org/3/library/functions.html#bool) = False, destructiveHint: [bool](https://docs.python.org/3/library/functions.html#bool) = True, idempotentHint: [bool](https://docs.python.org/3/library/functions.html#bool) = False, openWorldHint: [bool](https://docs.python.org/3/library/functions.html#bool) = True)

Bases: `BaseModel`

Annotations to provide hints about the tool’s behavior.

Based on Model Context Protocol (MCP) spec:
[https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838)

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'frozen': True, 'title': 'openhands.sdk.tool.tool.ToolAnnotations'\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### title *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### readOnlyHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### destructiveHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### idempotentHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### openWorldHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

### *class* openhands.sdk.tool.tool.ToolExecutor

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC), [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)

Executor function type for a Tool.

#### *abstractmethod* \_\_call_\_(action: ActionT, conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → ObservationT

Execute the tool with the given action and return an observation.

* **Parameters:**
  * **action** – The action to execute, containing the parameters and context
    needed for the tool operation.
  * **conversation** – The conversation context for the tool execution.
    Note: This is typed as LocalConversation (not
    BaseConversation) because all tool executions happen
    within a LocalConversation context. Even when tools are
    invoked via RemoteConversation, the remote agent server
    creates a LocalConversation instance to handle the actual
    tool execution. See [https://github.com/OpenHands/agent-sdk/pull/925](https://github.com/OpenHands/agent-sdk/pull/925)
    for more details.
* **Returns:**
  An observation containing the results of the tool execution.

#### close() → [None](https://docs.python.org/3/library/constants.html#None)

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

### *class* openhands.sdk.tool.tool.ExecutableTool(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Protocol for tools that are guaranteed to have a non-None executor.

This eliminates the need for runtime None checks and type narrowing
when working with tools that are known to be executable.

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### executor *: [ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)[[Any](https://docs.python.org/3/library/typing.html#typing.Any), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*

#### \_\_call_\_(action: [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action), conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Execute the tool with the given action.

#### \_\_init_\_(\*args, \*\*kwargs)

### *class* openhands.sdk.tool.tool.ToolBase(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolDefinition', 'ToolDefinition', 'ToolDefinition[MCPToolAction, MCPToolObservation]'] = 'MCPToolDefinition', name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str), action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)], observation_type: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None) = None, annotations: [ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None) = None, meta: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, executor: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()] = None)

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC), [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)

Tool that wraps an executor function with input/output validation and schema.

- Normalize input/output schemas (class or dict) into both model+schema.
- Validate inputs before execute.
- Coerce outputs only if an output model is defined; else return vanilla JSON.
- Export MCP tool description.

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### description *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### action_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)]*

#### observation_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### annotations *: [ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None)*

#### meta *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### executor *: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()]*

#### *abstractmethod classmethod* create(\*args, \*\*kwargs) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Self](https://docs.python.org/3/library/typing.html#typing.Self)]

Create a sequence of Tool instances. Placeholder for subclasses.

This can be overridden in subclasses to provide custom initialization logic
: (e.g., typically initializing the executor with parameters).

* **Returns:**
  A sequence of Tool instances. Even single tools are returned as a sequence
  to provide a consistent interface and eliminate union return types.

#### *property* title *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### set_executor(executor: [ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)) → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

Create a new Tool instance with the given executor.

#### as_executable() → [ExecutableTool](#openhands.sdk.tool.tool.ExecutableTool)

Return this tool as an ExecutableTool, ensuring it has an executor.

This method eliminates the need for runtime None checks by guaranteeing
that the returned tool has a non-None executor.

* **Returns:**
  This tool instance, typed as ExecutableTool.
* **Raises:**
  [**NotImplementedError**](https://docs.python.org/3/library/exceptions.html#NotImplementedError) – If the tool has no executor.

#### action_from_arguments(arguments: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]) → [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

Create an action from parsed arguments.

This method can be overridden by subclasses to provide custom logic
for creating actions from arguments (e.g., for MCP tools).

* **Parameters:**
  **arguments** – The parsed arguments from the tool call.
* **Returns:**
  The action instance created from the arguments.

#### \_\_call_\_(action: ActionT, conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Validate input, execute, and coerce output.

We always return some Observation subclass, but not always the
generic ObservationT.

#### to_mcp_tool(input_schema: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, output_schema: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Convert a Tool to an MCP tool definition.

Allow overriding input/output schemas (usually by subclasses).

* **Parameters:**
  * **input_schema** – Optionally override the input schema.
  * **output_schema** – Optionally override the output schema.

#### to_openai_tool(add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Schema](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → ChatCompletionToolParam

Convert a Tool to an OpenAI tool.

* **Parameters:**
  * **add_security_risk_prediction** – Whether to add a security_risk field
    to the action schema for LLM to predict. This is useful for
    tools that may have safety risks, so the LLM can reason about
    the risk level before calling the tool.
  * **action_type** – Optionally override the action_type to use for the schema.
    This is useful for MCPTool to use a dynamically created action type
    based on the tool’s input schema.

#### to_responses_tool(add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Schema](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → FunctionToolParam

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ “type”: “function”, “name”: …, “description”: …, “parameters”: … }

#### *classmethod* resolve_kind(kind: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [type](https://docs.python.org/3/library/functions.html#type)

#### kind *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.tool.tool.ToolDefinition(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ToolDefinition'] = 'ToolDefinition', name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str), action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)], observation_type: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None) = None, annotations: [ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None) = None, meta: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, executor: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()] = None)

Bases: `ToolBase[TypeVar, TypeVar]`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)

Concrete tool class that inherits from ToolBase.

This class serves as a concrete implementation of ToolBase for cases where
you want to create a tool instance directly without implementing a custom
subclass. Built-in tools (like FinishTool, ThinkTool) are instantiated
directly from this class, while more complex tools (like BashTool,
FileEditorTool) inherit from this class and provide their own create()
method implementations.

#### *classmethod* create(\*args, \*\*kwargs) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Self](https://docs.python.org/3/library/typing.html#typing.Self)]

Create a sequence of ToolDefinition instances.

TODO [https://github.com/OpenHands/agent-sdk/issues/493](https://github.com/OpenHands/agent-sdk/issues/493)
Refactor this - the ToolDefinition class should not have a concrete create()
implementation. Built-in tools should be refactored to not rely on this
method, and then this should be made abstract with @abstractmethod.

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ToolDefinition']*

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### description *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### action_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.Action)]*

#### observation_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.Observation)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### annotations *: [ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None)*

#### meta *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any] | [None](https://docs.python.org/3/library/constants.html#None)*

#### executor *: SkipJsonSchema[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None)]*

### *class* openhands.sdk.tool.tool.ToolDefinition(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ToolDefinition'] = 'ToolDefinition', name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str), action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)], observation_type: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None) = None, annotations: [ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None) = None, meta: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, executor: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()] = None)

Bases: `ToolBase[TypeVar, TypeVar]`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)

Concrete tool class that inherits from ToolBase.

This class serves as a concrete implementation of ToolBase for cases where
you want to create a tool instance directly without implementing a custom
subclass. Built-in tools (like FinishTool, ThinkTool) are instantiated
directly from this class, while more complex tools (like BashTool,
FileEditorTool) inherit from this class and provide their own create()
method implementations.

#### *classmethod* create(\*args, \*\*kwargs) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Self](https://docs.python.org/3/library/typing.html#typing.Self)]

Create a sequence of ToolDefinition instances.

TODO [https://github.com/OpenHands/agent-sdk/issues/493](https://github.com/OpenHands/agent-sdk/issues/493)
Refactor this - the ToolDefinition class should not have a concrete create()
implementation. Built-in tools should be refactored to not rely on this
method, and then this should be made abstract with @abstractmethod.

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ToolDefinition']*

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### description *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### action_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.Action)]*

#### observation_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.Observation)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### annotations *: [ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None)*

#### meta *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any] | [None](https://docs.python.org/3/library/constants.html#None)*

#### executor *: SkipJsonSchema[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None)]*
