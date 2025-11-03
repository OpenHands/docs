---
title: openhands.sdk.tool
description: API reference for openhands.sdk.tool
---

# openhands.sdk.tool package

<a id="module-openhands.sdk.tool"></a>

OpenHands runtime package.

### *class* openhands.sdk.tool.Tool(\*, name: str, params: dict[str, ~typing.Any] = <factory>)

Bases: `BaseModel`

Defines a tool to be initialized for the agent.

This is only used in agent-sdk for type schema for server use.

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *classmethod* validate_name(v: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Validate that name is not empty.

#### *classmethod* validate_params(v: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None)) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Convert None params to empty dict.

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### params *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*

### *class* openhands.sdk.tool.ToolDefinition(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ToolDefinition'] = 'ToolDefinition', name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str), action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)], observation_type: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None) = None, annotations: [ToolAnnotations](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None) = None, meta: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, executor: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()] = None)

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

#### model_config *: ClassVar[ConfigDict]* *= {'arbitrary_types_allowed': True, 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ToolDefinition']*

### *class* openhands.sdk.tool.ToolBase(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolDefinition', 'ToolDefinition', 'ToolDefinition[MCPToolAction, MCPToolObservation]'] = 'MCPToolDefinition', name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str), action_type: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)], observation_type: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None) = None, annotations: [ToolAnnotations](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None) = None, meta: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None) = None, executor: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()] = None)

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC), [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)

Tool that wraps an executor function with input/output validation and schema.

- Normalize input/output schemas (class or dict) into both model+schema.
- Validate inputs before execute.
- Coerce outputs only if an output model is defined; else return vanilla JSON.
- Export MCP tool description.

#### \_\_call_\_(action: ActionT, conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Validate input, execute, and coerce output.

We always return some Observation subclass, but not always the
generic ObservationT.

#### action_from_arguments(arguments: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]) → [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)

Create an action from parsed arguments.

This method can be overridden by subclasses to provide custom logic
for creating actions from arguments (e.g., for MCP tools).

* **Parameters:**
  **arguments** – The parsed arguments from the tool call.
* **Returns:**
  The action instance created from the arguments.

#### as_executable() → [ExecutableTool](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ExecutableTool)

Return this tool as an ExecutableTool, ensuring it has an executor.

This method eliminates the need for runtime None checks by guaranteeing
that the returned tool has a non-None executor.

* **Returns:**
  This tool instance, typed as ExecutableTool.
* **Raises:**
  [**NotImplementedError**](https://docs.python.org/3/library/exceptions.html#NotImplementedError) – If the tool has no executor.

#### *abstractmethod classmethod* create(\*args, \*\*kwargs) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Self](https://docs.python.org/3/library/typing.html#typing.Self)]

Create a sequence of Tool instances. Placeholder for subclasses.

This can be overridden in subclasses to provide custom initialization logic
: (e.g., typically initializing the executor with parameters).

* **Returns:**
  A sequence of Tool instances. Even single tools are returned as a sequence
  to provide a consistent interface and eliminate union return types.

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {'arbitrary_types_allowed': True, 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *classmethod* resolve_kind(kind: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [type](https://docs.python.org/3/library/functions.html#type)

#### set_executor(executor: [ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)) → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

Create a new Tool instance with the given executor.

#### *property* title *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

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

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### description *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### action_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)]*

#### observation_type *: [type](https://docs.python.org/3/library/functions.html#type)[[Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### annotations *: [ToolAnnotations](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations) | [None](https://docs.python.org/3/library/constants.html#None)*

#### meta *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### executor *: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor) | [None](https://docs.python.org/3/library/constants.html#None), SkipJsonSchema()]*

### *class* openhands.sdk.tool.ToolAnnotations(, title: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, readOnlyHint: [bool](https://docs.python.org/3/library/functions.html#bool) = False, destructiveHint: [bool](https://docs.python.org/3/library/functions.html#bool) = True, idempotentHint: [bool](https://docs.python.org/3/library/functions.html#bool) = False, openWorldHint: [bool](https://docs.python.org/3/library/functions.html#bool) = True)

Bases: `BaseModel`

Annotations to provide hints about the tool’s behavior.

Based on Model Context Protocol (MCP) spec:
[https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838)

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {'frozen': True, 'title': 'openhands.sdk.tool.tool.ToolAnnotations'}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### title *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### readOnlyHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### destructiveHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### idempotentHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### openWorldHint *: [bool](https://docs.python.org/3/library/functions.html#bool)*

### *class* openhands.sdk.tool.ToolExecutor

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

### *class* openhands.sdk.tool.ExecutableTool(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Protocol for tools that are guaranteed to have a non-None executor.

This eliminates the need for runtime None checks and type narrowing
when working with tools that are known to be executable.

#### \_\_call_\_(action: [Action](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action), conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Observation](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)

Execute the tool with the given action.

#### \_\_init_\_(\*args, \*\*kwargs)

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### executor *: [ToolExecutor](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)[[Any](https://docs.python.org/3/library/typing.html#typing.Any), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*

### *class* openhands.sdk.tool.Action(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolAction', 'FinishAction', 'ThinkAction'] = 'MCPToolAction')

Bases: [`Schema`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base schema for input action.

#### model_config *: ClassVar[ConfigDict]* *= {'extra': 'forbid', 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* visualize *: Text*

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

### *class* openhands.sdk.tool.Observation(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['MCPToolObservation', 'FinishObservation', 'ThinkObservation'] = 'MCPToolObservation')

Bases: [`Schema`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base schema for output observation.

#### model_config *: ClassVar[ConfigDict]* *= {'extra': 'forbid', 'frozen': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *abstract property* to_llm_content *: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]*

Get the observation string to show to the agent.

#### *property* visualize *: Text*

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

### openhands.sdk.tool.register_tool(name: [str](https://docs.python.org/3/library/stdtypes.html#str), factory: [ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0) | [type](https://docs.python.org/3/library/functions.html#type)[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase)] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0)]]) → [None](https://docs.python.org/3/library/constants.html#None)

### openhands.sdk.tool.resolve_tool(tool_spec: [Tool](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool), conv_state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.ConversationState)) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0)]

### openhands.sdk.tool.list_registered_tools() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

## Subpackages

* [openhands.sdk.tool.builtins package](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md)
  * [`FinishAction`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishAction)
    * [`FinishAction.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishAction.model_config)
    * [`FinishAction.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishAction.visualize)
    * [`FinishAction.message`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishAction.message)
    * [`FinishAction.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishAction.kind)
  * [`FinishObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishObservation)
    * [`FinishObservation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishObservation.model_config)
    * [`FinishObservation.to_llm_content`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishObservation.to_llm_content)
    * [`FinishObservation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishObservation.visualize)
    * [`FinishObservation.message`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishObservation.message)
    * [`FinishObservation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishObservation.kind)
  * [`FinishExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.FinishExecutor)
  * [`ThinkAction`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkAction)
    * [`ThinkAction.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkAction.model_config)
    * [`ThinkAction.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkAction.visualize)
    * [`ThinkAction.thought`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkAction.thought)
    * [`ThinkAction.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkAction.kind)
  * [`ThinkObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkObservation)
    * [`ThinkObservation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkObservation.model_config)
    * [`ThinkObservation.to_llm_content`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkObservation.to_llm_content)
    * [`ThinkObservation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkObservation.visualize)
    * [`ThinkObservation.content`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkObservation.content)
    * [`ThinkObservation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkObservation.kind)
  * [`ThinkExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#openhands.sdk.tool.builtins.ThinkExecutor)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.md#submodules)
    * [openhands.sdk.tool.builtins.finish module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md)
      * [`FinishAction`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishAction)
      * [`FinishObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishObservation)
      * [`FinishExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.finish.md#openhands.sdk.tool.builtins.finish.FinishExecutor)
    * [openhands.sdk.tool.builtins.think module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md)
      * [`ThinkAction`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkAction)
      * [`ThinkObservation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkObservation)
      * [`ThinkExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.builtins.think.md#openhands.sdk.tool.builtins.think.ThinkExecutor)

## Submodules

* [openhands.sdk.tool.registry module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.registry.md)
  * [`Resolver`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.registry.md#openhands.sdk.tool.registry.Resolver)
  * [`register_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.registry.md#openhands.sdk.tool.registry.register_tool)
  * [`resolve_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.registry.md#openhands.sdk.tool.registry.resolve_tool)
  * [`list_registered_tools()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.registry.md#openhands.sdk.tool.registry.list_registered_tools)
* [openhands.sdk.tool.schema module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md)
  * [`py_type()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.py_type)
  * [`Schema`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema)
    * [`Schema.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema.model_config)
    * [`Schema.to_mcp_schema()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema.to_mcp_schema)
    * [`Schema.from_mcp_schema()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema.from_mcp_schema)
    * [`Schema.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Schema.kind)
  * [`Action`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action)
    * [`Action.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action.visualize)
    * [`Action.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action.model_config)
    * [`Action.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Action.kind)
  * [`Observation`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation)
    * [`Observation.to_llm_content`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation.to_llm_content)
    * [`Observation.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation.visualize)
    * [`Observation.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation.model_config)
    * [`Observation.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.schema.md#openhands.sdk.tool.schema.Observation.kind)
* [openhands.sdk.tool.spec module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md)
  * [`Tool`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool)
    * [`Tool.name`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool.name)
    * [`Tool.params`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool.params)
    * [`Tool.validate_name()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool.validate_name)
    * [`Tool.validate_params()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool.validate_params)
    * [`Tool.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool.model_config)
* [openhands.sdk.tool.tool module](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md)
  * [`ToolAnnotations`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations)
    * [`ToolAnnotations.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations.model_config)
    * [`ToolAnnotations.title`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations.title)
    * [`ToolAnnotations.readOnlyHint`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations.readOnlyHint)
    * [`ToolAnnotations.destructiveHint`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations.destructiveHint)
    * [`ToolAnnotations.idempotentHint`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations.idempotentHint)
    * [`ToolAnnotations.openWorldHint`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolAnnotations.openWorldHint)
  * [`ToolExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor)
    * [`ToolExecutor.__call__()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor.__call__)
    * [`ToolExecutor.close()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolExecutor.close)
  * [`ExecutableTool`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ExecutableTool)
    * [`ExecutableTool.name`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ExecutableTool.name)
    * [`ExecutableTool.executor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ExecutableTool.executor)
    * [`ExecutableTool.__call__()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ExecutableTool.__call__)
    * [`ExecutableTool.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ExecutableTool.__init__)
  * [`ToolBase`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase)
    * [`ToolBase.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.model_config)
    * [`ToolBase.name`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.name)
    * [`ToolBase.description`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.description)
    * [`ToolBase.action_type`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.action_type)
    * [`ToolBase.observation_type`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.observation_type)
    * [`ToolBase.annotations`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.annotations)
    * [`ToolBase.meta`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.meta)
    * [`ToolBase.executor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.executor)
    * [`ToolBase.create()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.create)
    * [`ToolBase.title`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.title)
    * [`ToolBase.set_executor()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.set_executor)
    * [`ToolBase.as_executable()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.as_executable)
    * [`ToolBase.action_from_arguments()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.action_from_arguments)
    * [`ToolBase.__call__()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.__call__)
    * [`ToolBase.to_mcp_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.to_mcp_tool)
    * [`ToolBase.to_openai_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.to_openai_tool)
    * [`ToolBase.to_responses_tool()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.to_responses_tool)
    * [`ToolBase.resolve_kind()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.resolve_kind)
    * [`ToolBase.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase.kind)
  * [`ToolDefinition`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition)
    * [`ToolDefinition.create()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.create)
    * [`ToolDefinition.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.model_config)
    * [`ToolDefinition.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.kind)
    * [`ToolDefinition.name`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.name)
    * [`ToolDefinition.description`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.description)
    * [`ToolDefinition.action_type`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.action_type)
    * [`ToolDefinition.observation_type`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.observation_type)
    * [`ToolDefinition.annotations`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.annotations)
    * [`ToolDefinition.meta`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.meta)
    * [`ToolDefinition.executor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolDefinition.executor)
  * [`ToolDefinition`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0)
    * [`ToolDefinition.create()`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id1)
    * [`ToolDefinition.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id2)
    * [`ToolDefinition.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id3)
    * [`ToolDefinition.name`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id4)
    * [`ToolDefinition.description`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id5)
    * [`ToolDefinition.action_type`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id6)
    * [`ToolDefinition.observation_type`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id7)
    * [`ToolDefinition.annotations`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id8)
    * [`ToolDefinition.meta`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id9)
    * [`ToolDefinition.executor`](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id10)
