## `openhands.sdk.tool`

OpenHands runtime package.

**Modules:**

- [**builtins**](#openhands.sdk.tool.builtins) – Implementing essential tools that doesn't interact with the environment.
- [**registry**](#openhands.sdk.tool.registry) –
- [**schema**](#openhands.sdk.tool.schema) –
- [**spec**](#openhands.sdk.tool.spec) –
- [**tool**](#openhands.sdk.tool.tool) –

**Classes:**

- [**Action**](#openhands.sdk.tool.Action) – Base schema for input action.
- [**ExecutableTool**](#openhands.sdk.tool.ExecutableTool) – Protocol for tools that are guaranteed to have a non-None executor.
- [**Observation**](#openhands.sdk.tool.Observation) – Base schema for output observation.
- [**Tool**](#openhands.sdk.tool.Tool) – Defines a tool to be initialized for the agent.
- [**ToolAnnotations**](#openhands.sdk.tool.ToolAnnotations) – Annotations to provide hints about the tool's behavior.
- [**ToolBase**](#openhands.sdk.tool.ToolBase) – Tool that wraps an executor function with input/output validation and schema.
- [**ToolDefinition**](#openhands.sdk.tool.ToolDefinition) – Concrete tool class that inherits from ToolBase.
- [**ToolExecutor**](#openhands.sdk.tool.ToolExecutor) – Executor function type for a Tool.

**Functions:**

- [**list_registered_tools**](#openhands.sdk.tool.list_registered_tools) –
- [**register_tool**](#openhands.sdk.tool.register_tool) –
- [**resolve_tool**](#openhands.sdk.tool.resolve_tool) –

**Attributes:**

- [**BUILT_IN_TOOLS**](#openhands.sdk.tool.BUILT_IN_TOOLS) –
- [**FinishTool**](#openhands.sdk.tool.FinishTool) –
- [**ThinkTool**](#openhands.sdk.tool.ThinkTool) –

### `openhands.sdk.tool.Action`

Bases: <code>[Schema](#openhands.sdk.tool.schema.Schema)</code>, <code>[ABC](#abc.ABC)</code>

Base schema for input action.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.Action.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.Action.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.Action.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.Action.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.Action.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.Action.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.Action.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.Action.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.Action.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.Action.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.Action.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.Action.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**visualize**](#openhands.sdk.tool.Action.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

#### `openhands.sdk.tool.Action.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

#### `openhands.sdk.tool.Action.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.tool.Action.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.tool.Action.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

#### `openhands.sdk.tool.Action.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.tool.Action.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.tool.Action.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.tool.Action.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.tool.Action.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.tool.Action.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.tool.Action.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.tool.Action.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

#### `openhands.sdk.tool.Action.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

### `openhands.sdk.tool.BUILT_IN_TOOLS`

```python
BUILT_IN_TOOLS = [FinishTool, ThinkTool]
```

### `openhands.sdk.tool.ExecutableTool`

Bases: <code>[Protocol](#typing.Protocol)</code>

Protocol for tools that are guaranteed to have a non-None executor.

This eliminates the need for runtime None checks and type narrowing
when working with tools that are known to be executable.

**Attributes:**

- [**executor**](#openhands.sdk.tool.ExecutableTool.executor) (<code>[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)\[[Any](#typing.Any), [Any](#typing.Any)\]</code>) –
- [**name**](#openhands.sdk.tool.ExecutableTool.name) (<code>[str](#str)</code>) –

#### `openhands.sdk.tool.ExecutableTool.executor`

```python
executor: ToolExecutor[Any, Any]
```

#### `openhands.sdk.tool.ExecutableTool.name`

```python
name: str
```

### `openhands.sdk.tool.FinishTool`

```python
FinishTool = ToolDefinition(name='finish', action_type=FinishAction, observation_type=FinishObservation, description=TOOL_DESCRIPTION, executor=(FinishExecutor()), annotations=(ToolAnnotations(title='finish', readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)))
```

### `openhands.sdk.tool.Observation`

Bases: <code>[Schema](#openhands.sdk.tool.schema.Schema)</code>, <code>[ABC](#abc.ABC)</code>

Base schema for output observation.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.Observation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.Observation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.Observation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.Observation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.Observation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.Observation.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.Observation.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.Observation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.Observation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.Observation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.Observation.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.Observation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.tool.Observation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.TextContent) | [ImageContent](#openhands.sdk.llm.ImageContent)\]</code>) – Get the observation string to show to the agent.
- [**visualize**](#openhands.sdk.tool.Observation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

#### `openhands.sdk.tool.Observation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

#### `openhands.sdk.tool.Observation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.tool.Observation.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.tool.Observation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

#### `openhands.sdk.tool.Observation.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.tool.Observation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.tool.Observation.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.tool.Observation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.tool.Observation.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.tool.Observation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.tool.Observation.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.tool.Observation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

Get the observation string to show to the agent.

#### `openhands.sdk.tool.Observation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

#### `openhands.sdk.tool.Observation.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

### `openhands.sdk.tool.ThinkTool`

```python
ThinkTool = ToolDefinition(name='think', description=THINK_DESCRIPTION, action_type=ThinkAction, observation_type=ThinkObservation, executor=(ThinkExecutor()), annotations=(ToolAnnotations(readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)))
```

### `openhands.sdk.tool.Tool`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Defines a tool to be initialized for the agent.

This is only used in agent-sdk for type schema for server use.

**Functions:**

- [**validate_name**](#openhands.sdk.tool.Tool.validate_name) – Validate that name is not empty.
- [**validate_params**](#openhands.sdk.tool.Tool.validate_params) – Convert None params to empty dict.

**Attributes:**

- [**name**](#openhands.sdk.tool.Tool.name) (<code>[str](#str)</code>) –
- [**params**](#openhands.sdk.tool.Tool.params) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –

#### `openhands.sdk.tool.Tool.name`

```python
name: str = Field(..., description="Name of the tool class, e.g., 'BashTool'. Import it from an `openhands.tools.<module>` subpackage.", examples=['BashTool', 'FileEditorTool', 'TaskTrackerTool'])
```

#### `openhands.sdk.tool.Tool.params`

```python
params: dict[str, Any] = Field(default_factory=dict, description="Parameters for the tool's .create() method, e.g., {'working_dir': '/app'}", examples=[{'working_dir': '/workspace'}])
```

#### `openhands.sdk.tool.Tool.validate_name`

```python
validate_name(v)
```

Validate that name is not empty.

#### `openhands.sdk.tool.Tool.validate_params`

```python
validate_params(v)
```

Convert None params to empty dict.

### `openhands.sdk.tool.ToolAnnotations`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Annotations to provide hints about the tool's behavior.

Based on Model Context Protocol (MCP) spec:
https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838

**Attributes:**

- [**destructiveHint**](#openhands.sdk.tool.ToolAnnotations.destructiveHint) (<code>[bool](#bool)</code>) –
- [**idempotentHint**](#openhands.sdk.tool.ToolAnnotations.idempotentHint) (<code>[bool](#bool)</code>) –
- [**model_config**](#openhands.sdk.tool.ToolAnnotations.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**openWorldHint**](#openhands.sdk.tool.ToolAnnotations.openWorldHint) (<code>[bool](#bool)</code>) –
- [**readOnlyHint**](#openhands.sdk.tool.ToolAnnotations.readOnlyHint) (<code>[bool](#bool)</code>) –
- [**title**](#openhands.sdk.tool.ToolAnnotations.title) (<code>[str](#str) | None</code>) –

#### `openhands.sdk.tool.ToolAnnotations.destructiveHint`

```python
destructiveHint: bool = Field(default=True, description='If true, the tool may perform destructive updates to its environment. If false, the tool performs only additive updates. (This property is meaningful only when `readOnlyHint == false`) Default: true')
```

#### `openhands.sdk.tool.ToolAnnotations.idempotentHint`

```python
idempotentHint: bool = Field(default=False, description='If true, calling the tool repeatedly with the same arguments will have no additional effect on the its environment. (This property is meaningful only when `readOnlyHint == false`) Default: false')
```

#### `openhands.sdk.tool.ToolAnnotations.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, title='openhands.sdk.tool.tool.ToolAnnotations')
```

#### `openhands.sdk.tool.ToolAnnotations.openWorldHint`

```python
openWorldHint: bool = Field(default=True, description="If true, this tool may interact with an 'open world' of external entities. If false, the tool's domain of interaction is closed. For example, the world of a web search tool is open, whereas that of a memory tool is not. Default: true")
```

#### `openhands.sdk.tool.ToolAnnotations.readOnlyHint`

```python
readOnlyHint: bool = Field(default=False, description='If true, the tool does not modify its environment. Default: false')
```

#### `openhands.sdk.tool.ToolAnnotations.title`

```python
title: str | None = Field(default=None, description='A human-readable title for the tool.')
```

### `openhands.sdk.tool.ToolBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Tool that wraps an executor function with input/output validation and schema.

- Normalize input/output schemas (class or dict) into both model+schema.
- Validate inputs before execute.
- Coerce outputs only if an output model is defined; else return vanilla JSON.
- Export MCP tool description.

**Functions:**

- [**action_from_arguments**](#openhands.sdk.tool.ToolBase.action_from_arguments) – Create an action from parsed arguments.
- [**as_executable**](#openhands.sdk.tool.ToolBase.as_executable) – Return this tool as an ExecutableTool, ensuring it has an executor.
- [**create**](#openhands.sdk.tool.ToolBase.create) – Create a sequence of Tool instances. Placeholder for subclasses.
- [**get_serializable_type**](#openhands.sdk.tool.ToolBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.ToolBase.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.ToolBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.ToolBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.ToolBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.ToolBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.ToolBase.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.ToolBase.resolve_kind) –
- [**set_executor**](#openhands.sdk.tool.ToolBase.set_executor) – Create a new Tool instance with the given executor.
- [**to_mcp_tool**](#openhands.sdk.tool.ToolBase.to_mcp_tool) – Convert a Tool to an MCP tool definition.
- [**to_openai_tool**](#openhands.sdk.tool.ToolBase.to_openai_tool) – Convert a Tool to an OpenAI tool.
- [**to_responses_tool**](#openhands.sdk.tool.ToolBase.to_responses_tool) – Convert a Tool to a Responses API function tool (LiteLLM typed).

**Attributes:**

- [**action_type**](#openhands.sdk.tool.ToolBase.action_type) (<code>[type](#type)\[[Action](#openhands.sdk.tool.schema.Action)\]</code>) –
- [**annotations**](#openhands.sdk.tool.ToolBase.annotations) (<code>[ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | None</code>) –
- [**description**](#openhands.sdk.tool.ToolBase.description) (<code>[str](#str)</code>) –
- [**executor**](#openhands.sdk.tool.ToolBase.executor) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | None\]</code>) –
- [**kind**](#openhands.sdk.tool.ToolBase.kind) (<code>[str](#str)</code>) –
- [**meta**](#openhands.sdk.tool.ToolBase.meta) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) –
- [**model_config**](#openhands.sdk.tool.ToolBase.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**name**](#openhands.sdk.tool.ToolBase.name) (<code>[str](#str)</code>) –
- [**observation_type**](#openhands.sdk.tool.ToolBase.observation_type) (<code>[type](#type)\[[Observation](#openhands.sdk.tool.schema.Observation)\] | None</code>) –
- [**title**](#openhands.sdk.tool.ToolBase.title) (<code>[str](#str)</code>) –

#### `openhands.sdk.tool.ToolBase.action_from_arguments`

```python
action_from_arguments(arguments)
```

Create an action from parsed arguments.

This method can be overridden by subclasses to provide custom logic
for creating actions from arguments (e.g., for MCP tools).

**Parameters:**

- **arguments** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The parsed arguments from the tool call.

**Returns:**

- <code>[Action](#openhands.sdk.tool.schema.Action)</code> – The action instance created from the arguments.

#### `openhands.sdk.tool.ToolBase.action_type`

```python
action_type: type[Action] = Field(repr=False)
```

#### `openhands.sdk.tool.ToolBase.annotations`

```python
annotations: ToolAnnotations | None = None
```

#### `openhands.sdk.tool.ToolBase.as_executable`

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

#### `openhands.sdk.tool.ToolBase.create`

```python
create(*args, **kwargs)
```

Create a sequence of Tool instances. Placeholder for subclasses.

This can be overridden in subclasses to provide custom initialization logic
(e.g., typically initializing the executor with parameters).

**Returns:**

- <code>[Sequence](#collections.abc.Sequence)\[[Self](#typing.Self)\]</code> – A sequence of Tool instances. Even single tools are returned as a sequence
- <code>[Sequence](#collections.abc.Sequence)\[[Self](#typing.Self)\]</code> – to provide a consistent interface and eliminate union return types.

#### `openhands.sdk.tool.ToolBase.description`

```python
description: str
```

#### `openhands.sdk.tool.ToolBase.executor`

```python
executor: SkipJsonSchema[ToolExecutor | None] = Field(default=None, repr=False, exclude=True)
```

#### `openhands.sdk.tool.ToolBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.tool.ToolBase.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.tool.ToolBase.meta`

```python
meta: dict[str, Any] | None = None
```

#### `openhands.sdk.tool.ToolBase.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

#### `openhands.sdk.tool.ToolBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.tool.ToolBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.tool.ToolBase.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.tool.ToolBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.tool.ToolBase.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.tool.ToolBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.tool.ToolBase.name`

```python
name: str
```

#### `openhands.sdk.tool.ToolBase.observation_type`

```python
observation_type: type[Observation] | None = Field(default=None, repr=False)
```

#### `openhands.sdk.tool.ToolBase.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.tool.ToolBase.set_executor`

```python
set_executor(executor)
```

Create a new Tool instance with the given executor.

#### `openhands.sdk.tool.ToolBase.title`

```python
title: str
```

#### `openhands.sdk.tool.ToolBase.to_mcp_tool`

```python
to_mcp_tool(input_schema=None, output_schema=None)
```

Convert a Tool to an MCP tool definition.

Allow overriding input/output schemas (usually by subclasses).

**Parameters:**

- **input_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the input schema.
- **output_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the output schema.

#### `openhands.sdk.tool.ToolBase.to_openai_tool`

```python
to_openai_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to an OpenAI tool.

**Parameters:**

- **add_security_risk_prediction** (<code>[bool](#bool)</code>) – Whether to add a `security_risk` field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.
- **action_type** (<code>[type](#type)\[[Schema](#openhands.sdk.tool.schema.Schema)\] | None</code>) – Optionally override the action_type to use for the schema.
  This is useful for MCPTool to use a dynamically created action type
  based on the tool's input schema.

#### `openhands.sdk.tool.ToolBase.to_responses_tool`

```python
to_responses_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ "type": "function", "name": ..., "description": ..., "parameters": ... }

### `openhands.sdk.tool.ToolDefinition`

Bases: <code>[ToolBase](#openhands.sdk.tool.tool.ToolBase)\[[ToolDefinition[ActionT]](#openhands.sdk.tool.tool.ToolDefinition%5BActionT%5D), [ToolDefinition[ObservationT]](#openhands.sdk.tool.tool.ToolDefinition%5BObservationT%5D)\]</code>

Concrete tool class that inherits from ToolBase.

This class serves as a concrete implementation of ToolBase for cases where
you want to create a tool instance directly without implementing a custom
subclass. Built-in tools (like FinishTool, ThinkTool) are instantiated
directly from this class, while more complex tools (like BashTool,
FileEditorTool) inherit from this class and provide their own create()
method implementations.

**Functions:**

- [**action_from_arguments**](#openhands.sdk.tool.ToolDefinition.action_from_arguments) – Create an action from parsed arguments.
- [**as_executable**](#openhands.sdk.tool.ToolDefinition.as_executable) – Return this tool as an ExecutableTool, ensuring it has an executor.
- [**create**](#openhands.sdk.tool.ToolDefinition.create) – Create a sequence of ToolDefinition instances.
- [**get_serializable_type**](#openhands.sdk.tool.ToolDefinition.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.ToolDefinition.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.ToolDefinition.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.ToolDefinition.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.ToolDefinition.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.ToolDefinition.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.ToolDefinition.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.ToolDefinition.resolve_kind) –
- [**set_executor**](#openhands.sdk.tool.ToolDefinition.set_executor) – Create a new Tool instance with the given executor.
- [**to_mcp_tool**](#openhands.sdk.tool.ToolDefinition.to_mcp_tool) – Convert a Tool to an MCP tool definition.
- [**to_openai_tool**](#openhands.sdk.tool.ToolDefinition.to_openai_tool) – Convert a Tool to an OpenAI tool.
- [**to_responses_tool**](#openhands.sdk.tool.ToolDefinition.to_responses_tool) – Convert a Tool to a Responses API function tool (LiteLLM typed).

**Attributes:**

- [**action_type**](#openhands.sdk.tool.ToolDefinition.action_type) (<code>[type](#type)\[[Action](#openhands.sdk.tool.schema.Action)\]</code>) –
- [**annotations**](#openhands.sdk.tool.ToolDefinition.annotations) (<code>[ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | None</code>) –
- [**description**](#openhands.sdk.tool.ToolDefinition.description) (<code>[str](#str)</code>) –
- [**executor**](#openhands.sdk.tool.ToolDefinition.executor) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | None\]</code>) –
- [**kind**](#openhands.sdk.tool.ToolDefinition.kind) (<code>[str](#str)</code>) –
- [**meta**](#openhands.sdk.tool.ToolDefinition.meta) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) –
- [**model_config**](#openhands.sdk.tool.ToolDefinition.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**name**](#openhands.sdk.tool.ToolDefinition.name) (<code>[str](#str)</code>) –
- [**observation_type**](#openhands.sdk.tool.ToolDefinition.observation_type) (<code>[type](#type)\[[Observation](#openhands.sdk.tool.schema.Observation)\] | None</code>) –
- [**title**](#openhands.sdk.tool.ToolDefinition.title) (<code>[str](#str)</code>) –

#### `openhands.sdk.tool.ToolDefinition.action_from_arguments`

```python
action_from_arguments(arguments)
```

Create an action from parsed arguments.

This method can be overridden by subclasses to provide custom logic
for creating actions from arguments (e.g., for MCP tools).

**Parameters:**

- **arguments** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The parsed arguments from the tool call.

**Returns:**

- <code>[Action](#openhands.sdk.tool.schema.Action)</code> – The action instance created from the arguments.

#### `openhands.sdk.tool.ToolDefinition.action_type`

```python
action_type: type[Action] = Field(repr=False)
```

#### `openhands.sdk.tool.ToolDefinition.annotations`

```python
annotations: ToolAnnotations | None = None
```

#### `openhands.sdk.tool.ToolDefinition.as_executable`

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

#### `openhands.sdk.tool.ToolDefinition.create`

```python
create(*args, **kwargs)
```

Create a sequence of ToolDefinition instances.

TODO https://github.com/OpenHands/agent-sdk/issues/493
Refactor this - the ToolDefinition class should not have a concrete create()
implementation. Built-in tools should be refactored to not rely on this
method, and then this should be made abstract with @abstractmethod.

#### `openhands.sdk.tool.ToolDefinition.description`

```python
description: str
```

#### `openhands.sdk.tool.ToolDefinition.executor`

```python
executor: SkipJsonSchema[ToolExecutor | None] = Field(default=None, repr=False, exclude=True)
```

#### `openhands.sdk.tool.ToolDefinition.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.tool.ToolDefinition.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.tool.ToolDefinition.meta`

```python
meta: dict[str, Any] | None = None
```

#### `openhands.sdk.tool.ToolDefinition.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

#### `openhands.sdk.tool.ToolDefinition.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.tool.ToolDefinition.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.tool.ToolDefinition.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.tool.ToolDefinition.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.tool.ToolDefinition.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.tool.ToolDefinition.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.tool.ToolDefinition.name`

```python
name: str
```

#### `openhands.sdk.tool.ToolDefinition.observation_type`

```python
observation_type: type[Observation] | None = Field(default=None, repr=False)
```

#### `openhands.sdk.tool.ToolDefinition.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.tool.ToolDefinition.set_executor`

```python
set_executor(executor)
```

Create a new Tool instance with the given executor.

#### `openhands.sdk.tool.ToolDefinition.title`

```python
title: str
```

#### `openhands.sdk.tool.ToolDefinition.to_mcp_tool`

```python
to_mcp_tool(input_schema=None, output_schema=None)
```

Convert a Tool to an MCP tool definition.

Allow overriding input/output schemas (usually by subclasses).

**Parameters:**

- **input_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the input schema.
- **output_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the output schema.

#### `openhands.sdk.tool.ToolDefinition.to_openai_tool`

```python
to_openai_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to an OpenAI tool.

**Parameters:**

- **add_security_risk_prediction** (<code>[bool](#bool)</code>) – Whether to add a `security_risk` field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.
- **action_type** (<code>[type](#type)\[[Schema](#openhands.sdk.tool.schema.Schema)\] | None</code>) – Optionally override the action_type to use for the schema.
  This is useful for MCPTool to use a dynamically created action type
  based on the tool's input schema.

#### `openhands.sdk.tool.ToolDefinition.to_responses_tool`

```python
to_responses_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ "type": "function", "name": ..., "description": ..., "parameters": ... }

### `openhands.sdk.tool.ToolExecutor`

Bases: <code>[ABC](#abc.ABC)</code>

Executor function type for a Tool.

**Functions:**

- [**close**](#openhands.sdk.tool.ToolExecutor.close) – Close the executor and clean up resources.

#### `openhands.sdk.tool.ToolExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

### `openhands.sdk.tool.builtins`

Implementing essential tools that doesn't interact with the environment.

These are built in and are *required* for the agent to work.

For tools that require interacting with the environment, add them to `openhands-tools`.

**Modules:**

- [**finish**](#openhands.sdk.tool.builtins.finish) –
- [**think**](#openhands.sdk.tool.builtins.think) –

**Classes:**

- [**FinishAction**](#openhands.sdk.tool.builtins.FinishAction) –
- [**FinishExecutor**](#openhands.sdk.tool.builtins.FinishExecutor) –
- [**FinishObservation**](#openhands.sdk.tool.builtins.FinishObservation) –
- [**ThinkAction**](#openhands.sdk.tool.builtins.ThinkAction) – Action for logging a thought without making any changes.
- [**ThinkExecutor**](#openhands.sdk.tool.builtins.ThinkExecutor) –
- [**ThinkObservation**](#openhands.sdk.tool.builtins.ThinkObservation) – Observation returned after logging a thought.

**Attributes:**

- [**BUILT_IN_TOOLS**](#openhands.sdk.tool.builtins.BUILT_IN_TOOLS) –
- [**FinishTool**](#openhands.sdk.tool.builtins.FinishTool) –
- [**ThinkTool**](#openhands.sdk.tool.builtins.ThinkTool) –

#### `openhands.sdk.tool.builtins.BUILT_IN_TOOLS`

```python
BUILT_IN_TOOLS = [FinishTool, ThinkTool]
```

#### `openhands.sdk.tool.builtins.FinishAction`

Bases: <code>[Action](#openhands.sdk.tool.tool.Action)</code>

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.FinishAction.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.FinishAction.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.FinishAction.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.FinishAction.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.FinishAction.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.FinishAction.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.FinishAction.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.FinishAction.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.FinishAction.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.FinishAction.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.builtins.FinishAction.kind) (<code>[str](#str)</code>) –
- [**message**](#openhands.sdk.tool.builtins.FinishAction.message) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.FinishAction.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.FinishAction.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

##### `openhands.sdk.tool.builtins.FinishAction.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.tool.builtins.FinishAction.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.builtins.FinishAction.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.builtins.FinishAction.message`

```python
message: str = Field(description='Final message to send to the user.')
```

##### `openhands.sdk.tool.builtins.FinishAction.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.tool.builtins.FinishAction.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.builtins.FinishAction.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.builtins.FinishAction.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.builtins.FinishAction.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.builtins.FinishAction.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.builtins.FinishAction.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.builtins.FinishAction.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.builtins.FinishAction.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.tool.builtins.FinishAction.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

#### `openhands.sdk.tool.builtins.FinishExecutor`

Bases: <code>[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)</code>

**Functions:**

- [**close**](#openhands.sdk.tool.builtins.FinishExecutor.close) – Close the executor and clean up resources.

##### `openhands.sdk.tool.builtins.FinishExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

#### `openhands.sdk.tool.builtins.FinishObservation`

Bases: <code>[Observation](#openhands.sdk.tool.tool.Observation)</code>

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.FinishObservation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.FinishObservation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.FinishObservation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.FinishObservation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.FinishObservation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.FinishObservation.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.FinishObservation.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.FinishObservation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.FinishObservation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.FinishObservation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.builtins.FinishObservation.kind) (<code>[str](#str)</code>) –
- [**message**](#openhands.sdk.tool.builtins.FinishObservation.message) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.FinishObservation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.tool.builtins.FinishObservation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)\]</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.FinishObservation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation - empty since action shows the message.

##### `openhands.sdk.tool.builtins.FinishObservation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.tool.builtins.FinishObservation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.builtins.FinishObservation.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.builtins.FinishObservation.message`

```python
message: str = Field(description='Final message sent to the user.')
```

##### `openhands.sdk.tool.builtins.FinishObservation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.tool.builtins.FinishObservation.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.builtins.FinishObservation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.builtins.FinishObservation.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.builtins.FinishObservation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.builtins.FinishObservation.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.builtins.FinishObservation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.builtins.FinishObservation.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.builtins.FinishObservation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

##### `openhands.sdk.tool.builtins.FinishObservation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.tool.builtins.FinishObservation.visualize`

```python
visualize: Text
```

Return Rich Text representation - empty since action shows the message.

#### `openhands.sdk.tool.builtins.FinishTool`

```python
FinishTool = ToolDefinition(name='finish', action_type=FinishAction, observation_type=FinishObservation, description=TOOL_DESCRIPTION, executor=(FinishExecutor()), annotations=(ToolAnnotations(title='finish', readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)))
```

#### `openhands.sdk.tool.builtins.ThinkAction`

Bases: <code>[Action](#openhands.sdk.tool.tool.Action)</code>

Action for logging a thought without making any changes.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.ThinkAction.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.ThinkAction.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.ThinkAction.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.ThinkAction.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.ThinkAction.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.ThinkAction.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.ThinkAction.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.ThinkAction.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.ThinkAction.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.ThinkAction.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.builtins.ThinkAction.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.ThinkAction.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**thought**](#openhands.sdk.tool.builtins.ThinkAction.thought) (<code>[str](#str)</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.ThinkAction.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation with thinking styling.

##### `openhands.sdk.tool.builtins.ThinkAction.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.tool.builtins.ThinkAction.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.builtins.ThinkAction.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.builtins.ThinkAction.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.tool.builtins.ThinkAction.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkAction.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkAction.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.builtins.ThinkAction.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.builtins.ThinkAction.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkAction.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkAction.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.builtins.ThinkAction.thought`

```python
thought: str = Field(description='The thought to log.')
```

##### `openhands.sdk.tool.builtins.ThinkAction.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.tool.builtins.ThinkAction.visualize`

```python
visualize: Text
```

Return Rich Text representation with thinking styling.

#### `openhands.sdk.tool.builtins.ThinkExecutor`

Bases: <code>[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)</code>

**Functions:**

- [**close**](#openhands.sdk.tool.builtins.ThinkExecutor.close) – Close the executor and clean up resources.

##### `openhands.sdk.tool.builtins.ThinkExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

#### `openhands.sdk.tool.builtins.ThinkObservation`

Bases: <code>[Observation](#openhands.sdk.tool.tool.Observation)</code>

Observation returned after logging a thought.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.ThinkObservation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.ThinkObservation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.ThinkObservation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.ThinkObservation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.ThinkObservation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.ThinkObservation.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.ThinkObservation.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.ThinkObservation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.ThinkObservation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.ThinkObservation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**content**](#openhands.sdk.tool.builtins.ThinkObservation.content) (<code>[str](#str)</code>) –
- [**kind**](#openhands.sdk.tool.builtins.ThinkObservation.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.ThinkObservation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.tool.builtins.ThinkObservation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)\]</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.ThinkObservation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation - empty since action shows the thought.

##### `openhands.sdk.tool.builtins.ThinkObservation.content`

```python
content: str = Field(default='Your thought has been logged.', description='Confirmation message.')
```

##### `openhands.sdk.tool.builtins.ThinkObservation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.tool.builtins.ThinkObservation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.builtins.ThinkObservation.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.builtins.ThinkObservation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.builtins.ThinkObservation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

##### `openhands.sdk.tool.builtins.ThinkObservation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.tool.builtins.ThinkObservation.visualize`

```python
visualize: Text
```

Return Rich Text representation - empty since action shows the thought.

#### `openhands.sdk.tool.builtins.ThinkTool`

```python
ThinkTool = ToolDefinition(name='think', description=THINK_DESCRIPTION, action_type=ThinkAction, observation_type=ThinkObservation, executor=(ThinkExecutor()), annotations=(ToolAnnotations(readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)))
```

#### `openhands.sdk.tool.builtins.finish`

**Classes:**

- [**FinishAction**](#openhands.sdk.tool.builtins.finish.FinishAction) –
- [**FinishExecutor**](#openhands.sdk.tool.builtins.finish.FinishExecutor) –
- [**FinishObservation**](#openhands.sdk.tool.builtins.finish.FinishObservation) –

**Attributes:**

- [**FinishTool**](#openhands.sdk.tool.builtins.finish.FinishTool) –
- [**TOOL_DESCRIPTION**](#openhands.sdk.tool.builtins.finish.TOOL_DESCRIPTION) –

##### `openhands.sdk.tool.builtins.finish.FinishAction`

Bases: <code>[Action](#openhands.sdk.tool.tool.Action)</code>

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.finish.FinishAction.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.finish.FinishAction.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.finish.FinishAction.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.finish.FinishAction.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.finish.FinishAction.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.finish.FinishAction.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.finish.FinishAction.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.finish.FinishAction.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.finish.FinishAction.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.finish.FinishAction.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.builtins.finish.FinishAction.kind) (<code>[str](#str)</code>) –
- [**message**](#openhands.sdk.tool.builtins.finish.FinishAction.message) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.finish.FinishAction.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.finish.FinishAction.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

###### `openhands.sdk.tool.builtins.finish.FinishAction.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

###### `openhands.sdk.tool.builtins.finish.FinishAction.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.tool.builtins.finish.FinishAction.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.message`

```python
message: str = Field(description='Final message to send to the user.')
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.resolve_kind`

```python
resolve_kind(kind)
```

###### `openhands.sdk.tool.builtins.finish.FinishAction.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

###### `openhands.sdk.tool.builtins.finish.FinishAction.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

##### `openhands.sdk.tool.builtins.finish.FinishExecutor`

Bases: <code>[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)</code>

**Functions:**

- [**close**](#openhands.sdk.tool.builtins.finish.FinishExecutor.close) – Close the executor and clean up resources.

###### `openhands.sdk.tool.builtins.finish.FinishExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

##### `openhands.sdk.tool.builtins.finish.FinishObservation`

Bases: <code>[Observation](#openhands.sdk.tool.tool.Observation)</code>

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.finish.FinishObservation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.finish.FinishObservation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.finish.FinishObservation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.finish.FinishObservation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.finish.FinishObservation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.finish.FinishObservation.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.finish.FinishObservation.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.finish.FinishObservation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.finish.FinishObservation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.finish.FinishObservation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.builtins.finish.FinishObservation.kind) (<code>[str](#str)</code>) –
- [**message**](#openhands.sdk.tool.builtins.finish.FinishObservation.message) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.finish.FinishObservation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.tool.builtins.finish.FinishObservation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)\]</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.finish.FinishObservation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation - empty since action shows the message.

###### `openhands.sdk.tool.builtins.finish.FinishObservation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

###### `openhands.sdk.tool.builtins.finish.FinishObservation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.tool.builtins.finish.FinishObservation.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.message`

```python
message: str = Field(description='Final message sent to the user.')
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.resolve_kind`

```python
resolve_kind(kind)
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

###### `openhands.sdk.tool.builtins.finish.FinishObservation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

###### `openhands.sdk.tool.builtins.finish.FinishObservation.visualize`

```python
visualize: Text
```

Return Rich Text representation - empty since action shows the message.

##### `openhands.sdk.tool.builtins.finish.FinishTool`

```python
FinishTool = ToolDefinition(name='finish', action_type=FinishAction, observation_type=FinishObservation, description=TOOL_DESCRIPTION, executor=(FinishExecutor()), annotations=(ToolAnnotations(title='finish', readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)))
```

##### `openhands.sdk.tool.builtins.finish.TOOL_DESCRIPTION`

```python
TOOL_DESCRIPTION = "Signals the completion of the current task or conversation.\n\nUse this tool when:\n- You have successfully completed the user's requested task\n- You cannot proceed further due to technical limitations or missing information\n\nThe message should include:\n- A clear summary of actions taken and their results\n- Any next steps for the user\n- Explanation if you're unable to complete the task\n- Any follow-up questions if more information is needed\n"
```

#### `openhands.sdk.tool.builtins.think`

**Classes:**

- [**ThinkAction**](#openhands.sdk.tool.builtins.think.ThinkAction) – Action for logging a thought without making any changes.
- [**ThinkExecutor**](#openhands.sdk.tool.builtins.think.ThinkExecutor) –
- [**ThinkObservation**](#openhands.sdk.tool.builtins.think.ThinkObservation) – Observation returned after logging a thought.

**Attributes:**

- [**THINK_DESCRIPTION**](#openhands.sdk.tool.builtins.think.THINK_DESCRIPTION) –
- [**ThinkTool**](#openhands.sdk.tool.builtins.think.ThinkTool) –

##### `openhands.sdk.tool.builtins.think.THINK_DESCRIPTION`

```python
THINK_DESCRIPTION = 'Use the tool to think about something. It will not obtain new information or make any changes to the repository, but just log the thought. Use it when complex reasoning or brainstorming is needed.\n\nCommon use cases:\n1. When exploring a repository and discovering the source of a bug, call this tool to brainstorm several unique ways of fixing the bug, and assess which change(s) are likely to be simplest and most effective.\n2. After receiving test results, use this tool to brainstorm ways to fix failing tests.\n3. When planning a complex refactoring, use this tool to outline different approaches and their tradeoffs.\n4. When designing a new feature, use this tool to think through architecture decisions and implementation details.\n5. When debugging a complex issue, use this tool to organize your thoughts and hypotheses.\n\nThe tool simply logs your thought process for better transparency and does not execute any code or make changes.'
```

##### `openhands.sdk.tool.builtins.think.ThinkAction`

Bases: <code>[Action](#openhands.sdk.tool.tool.Action)</code>

Action for logging a thought without making any changes.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.think.ThinkAction.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.think.ThinkAction.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.think.ThinkAction.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.think.ThinkAction.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.think.ThinkAction.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.think.ThinkAction.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.think.ThinkAction.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.think.ThinkAction.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.think.ThinkAction.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.think.ThinkAction.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.builtins.think.ThinkAction.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.think.ThinkAction.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**thought**](#openhands.sdk.tool.builtins.think.ThinkAction.thought) (<code>[str](#str)</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.think.ThinkAction.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation with thinking styling.

###### `openhands.sdk.tool.builtins.think.ThinkAction.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

###### `openhands.sdk.tool.builtins.think.ThinkAction.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.tool.builtins.think.ThinkAction.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.resolve_kind`

```python
resolve_kind(kind)
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.thought`

```python
thought: str = Field(description='The thought to log.')
```

###### `openhands.sdk.tool.builtins.think.ThinkAction.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

###### `openhands.sdk.tool.builtins.think.ThinkAction.visualize`

```python
visualize: Text
```

Return Rich Text representation with thinking styling.

##### `openhands.sdk.tool.builtins.think.ThinkExecutor`

Bases: <code>[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)</code>

**Functions:**

- [**close**](#openhands.sdk.tool.builtins.think.ThinkExecutor.close) – Close the executor and clean up resources.

###### `openhands.sdk.tool.builtins.think.ThinkExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).

##### `openhands.sdk.tool.builtins.think.ThinkObservation`

Bases: <code>[Observation](#openhands.sdk.tool.tool.Observation)</code>

Observation returned after logging a thought.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.builtins.think.ThinkObservation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.builtins.think.ThinkObservation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.builtins.think.ThinkObservation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.builtins.think.ThinkObservation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.builtins.think.ThinkObservation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.builtins.think.ThinkObservation.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.builtins.think.ThinkObservation.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.builtins.think.ThinkObservation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.builtins.think.ThinkObservation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.builtins.think.ThinkObservation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**content**](#openhands.sdk.tool.builtins.think.ThinkObservation.content) (<code>[str](#str)</code>) –
- [**kind**](#openhands.sdk.tool.builtins.think.ThinkObservation.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.builtins.think.ThinkObservation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.tool.builtins.think.ThinkObservation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)\]</code>) –
- [**visualize**](#openhands.sdk.tool.builtins.think.ThinkObservation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation - empty since action shows the thought.

###### `openhands.sdk.tool.builtins.think.ThinkObservation.content`

```python
content: str = Field(default='Your thought has been logged.', description='Confirmation message.')
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

###### `openhands.sdk.tool.builtins.think.ThinkObservation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.tool.builtins.think.ThinkObservation.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.resolve_kind`

```python
resolve_kind(kind)
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

###### `openhands.sdk.tool.builtins.think.ThinkObservation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

###### `openhands.sdk.tool.builtins.think.ThinkObservation.visualize`

```python
visualize: Text
```

Return Rich Text representation - empty since action shows the thought.

##### `openhands.sdk.tool.builtins.think.ThinkTool`

```python
ThinkTool = ToolDefinition(name='think', description=THINK_DESCRIPTION, action_type=ThinkAction, observation_type=ThinkObservation, executor=(ThinkExecutor()), annotations=(ToolAnnotations(readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)))
```

### `openhands.sdk.tool.list_registered_tools`

```python
list_registered_tools()
```

### `openhands.sdk.tool.register_tool`

```python
register_tool(name, factory)
```

### `openhands.sdk.tool.registry`

**Functions:**

- [**list_registered_tools**](#openhands.sdk.tool.registry.list_registered_tools) –
- [**register_tool**](#openhands.sdk.tool.registry.register_tool) –
- [**resolve_tool**](#openhands.sdk.tool.registry.resolve_tool) –

**Attributes:**

- [**Resolver**](#openhands.sdk.tool.registry.Resolver) – A resolver produces ToolDefinition instances for given params.

#### `openhands.sdk.tool.registry.Resolver`

```python
Resolver = Callable[[dict[str, Any], 'ConversationState'], Sequence[ToolDefinition]]
```

A resolver produces ToolDefinition instances for given params.

**Parameters:**

- **params** – Arbitrary parameters passed to the resolver. These are typically
  used to configure the ToolDefinition instances that are created.
- **conversation** – Optional conversation state to get directories from.

Returns: A sequence of ToolDefinition instances. Most of the time this will be a
single-item
sequence, but in some cases a ToolDefinition.create may produce multiple tools
(e.g., BrowserToolSet).

#### `openhands.sdk.tool.registry.list_registered_tools`

```python
list_registered_tools()
```

#### `openhands.sdk.tool.registry.register_tool`

```python
register_tool(name, factory)
```

#### `openhands.sdk.tool.registry.resolve_tool`

```python
resolve_tool(tool_spec, conv_state)
```

### `openhands.sdk.tool.resolve_tool`

```python
resolve_tool(tool_spec, conv_state)
```

### `openhands.sdk.tool.schema`

**Classes:**

- [**Action**](#openhands.sdk.tool.schema.Action) – Base schema for input action.
- [**Observation**](#openhands.sdk.tool.schema.Observation) – Base schema for output observation.
- [**Schema**](#openhands.sdk.tool.schema.Schema) – Base schema for input action / output observation.

**Functions:**

- [**py_type**](#openhands.sdk.tool.schema.py_type) – Map JSON schema types to Python types.

**Attributes:**

- [**S**](#openhands.sdk.tool.schema.S) –

#### `openhands.sdk.tool.schema.Action`

Bases: <code>[Schema](#openhands.sdk.tool.schema.Schema)</code>, <code>[ABC](#abc.ABC)</code>

Base schema for input action.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.schema.Action.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.schema.Action.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.schema.Action.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.schema.Action.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.schema.Action.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.schema.Action.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.schema.Action.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.schema.Action.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.schema.Action.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.schema.Action.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.schema.Action.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.schema.Action.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**visualize**](#openhands.sdk.tool.schema.Action.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

##### `openhands.sdk.tool.schema.Action.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.tool.schema.Action.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.schema.Action.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.schema.Action.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.tool.schema.Action.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.schema.Action.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.schema.Action.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.schema.Action.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.schema.Action.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.schema.Action.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.schema.Action.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.schema.Action.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.tool.schema.Action.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

#### `openhands.sdk.tool.schema.Observation`

Bases: <code>[Schema](#openhands.sdk.tool.schema.Schema)</code>, <code>[ABC](#abc.ABC)</code>

Base schema for output observation.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.schema.Observation.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.schema.Observation.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.schema.Observation.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.schema.Observation.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.schema.Observation.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.schema.Observation.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.schema.Observation.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.schema.Observation.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.schema.Observation.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.schema.Observation.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.schema.Observation.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.schema.Observation.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**to_llm_content**](#openhands.sdk.tool.schema.Observation.to_llm_content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.TextContent) | [ImageContent](#openhands.sdk.llm.ImageContent)\]</code>) – Get the observation string to show to the agent.
- [**visualize**](#openhands.sdk.tool.schema.Observation.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this action.

##### `openhands.sdk.tool.schema.Observation.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.tool.schema.Observation.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.schema.Observation.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.schema.Observation.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.tool.schema.Observation.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.schema.Observation.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.schema.Observation.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.schema.Observation.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.schema.Observation.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.schema.Observation.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.schema.Observation.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.schema.Observation.to_llm_content`

```python
to_llm_content: Sequence[TextContent | ImageContent]
```

Get the observation string to show to the agent.

##### `openhands.sdk.tool.schema.Observation.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

##### `openhands.sdk.tool.schema.Observation.visualize`

```python
visualize: Text
```

Return Rich Text representation of this action.

This method can be overridden by subclasses to customize visualization.
The base implementation displays all action fields systematically.

#### `openhands.sdk.tool.schema.S`

```python
S = TypeVar('S', bound='Schema')
```

#### `openhands.sdk.tool.schema.Schema`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>

Base schema for input action / output observation.

**Functions:**

- [**from_mcp_schema**](#openhands.sdk.tool.schema.Schema.from_mcp_schema) – Create a Schema subclass from an MCP/JSON Schema object.
- [**get_serializable_type**](#openhands.sdk.tool.schema.Schema.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.schema.Schema.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.schema.Schema.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.schema.Schema.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.schema.Schema.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.schema.Schema.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.schema.Schema.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.schema.Schema.resolve_kind) –
- [**to_mcp_schema**](#openhands.sdk.tool.schema.Schema.to_mcp_schema) – Convert to JSON schema format compatible with MCP.

**Attributes:**

- [**kind**](#openhands.sdk.tool.schema.Schema.kind) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.tool.schema.Schema.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –

##### `openhands.sdk.tool.schema.Schema.from_mcp_schema`

```python
from_mcp_schema(model_name, schema)
```

Create a Schema subclass from an MCP/JSON Schema object.

For non-required fields, we annotate as `T | None`
so explicit nulls are allowed.

##### `openhands.sdk.tool.schema.Schema.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.schema.Schema.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.schema.Schema.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', frozen=True)
```

##### `openhands.sdk.tool.schema.Schema.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.schema.Schema.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.schema.Schema.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.schema.Schema.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.schema.Schema.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.schema.Schema.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.schema.Schema.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.schema.Schema.to_mcp_schema`

```python
to_mcp_schema()
```

Convert to JSON schema format compatible with MCP.

#### `openhands.sdk.tool.schema.py_type`

```python
py_type(spec)
```

Map JSON schema types to Python types.

### `openhands.sdk.tool.spec`

**Classes:**

- [**Tool**](#openhands.sdk.tool.spec.Tool) – Defines a tool to be initialized for the agent.

#### `openhands.sdk.tool.spec.Tool`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Defines a tool to be initialized for the agent.

This is only used in agent-sdk for type schema for server use.

**Functions:**

- [**validate_name**](#openhands.sdk.tool.spec.Tool.validate_name) – Validate that name is not empty.
- [**validate_params**](#openhands.sdk.tool.spec.Tool.validate_params) – Convert None params to empty dict.

**Attributes:**

- [**name**](#openhands.sdk.tool.spec.Tool.name) (<code>[str](#str)</code>) –
- [**params**](#openhands.sdk.tool.spec.Tool.params) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –

##### `openhands.sdk.tool.spec.Tool.name`

```python
name: str = Field(..., description="Name of the tool class, e.g., 'BashTool'. Import it from an `openhands.tools.<module>` subpackage.", examples=['BashTool', 'FileEditorTool', 'TaskTrackerTool'])
```

##### `openhands.sdk.tool.spec.Tool.params`

```python
params: dict[str, Any] = Field(default_factory=dict, description="Parameters for the tool's .create() method, e.g., {'working_dir': '/app'}", examples=[{'working_dir': '/workspace'}])
```

##### `openhands.sdk.tool.spec.Tool.validate_name`

```python
validate_name(v)
```

Validate that name is not empty.

##### `openhands.sdk.tool.spec.Tool.validate_params`

```python
validate_params(v)
```

Convert None params to empty dict.

### `openhands.sdk.tool.tool`

**Classes:**

- [**ExecutableTool**](#openhands.sdk.tool.tool.ExecutableTool) – Protocol for tools that are guaranteed to have a non-None executor.
- [**ToolAnnotations**](#openhands.sdk.tool.tool.ToolAnnotations) – Annotations to provide hints about the tool's behavior.
- [**ToolBase**](#openhands.sdk.tool.tool.ToolBase) – Tool that wraps an executor function with input/output validation and schema.
- [**ToolDefinition**](#openhands.sdk.tool.tool.ToolDefinition) – Concrete tool class that inherits from ToolBase.
- [**ToolExecutor**](#openhands.sdk.tool.tool.ToolExecutor) – Executor function type for a Tool.

**Attributes:**

- [**ActionT**](#openhands.sdk.tool.tool.ActionT) –
- [**ObservationT**](#openhands.sdk.tool.tool.ObservationT) –

#### `openhands.sdk.tool.tool.ActionT`

```python
ActionT = TypeVar('ActionT', bound=Action)
```

#### `openhands.sdk.tool.tool.ExecutableTool`

Bases: <code>[Protocol](#typing.Protocol)</code>

Protocol for tools that are guaranteed to have a non-None executor.

This eliminates the need for runtime None checks and type narrowing
when working with tools that are known to be executable.

**Attributes:**

- [**executor**](#openhands.sdk.tool.tool.ExecutableTool.executor) (<code>[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor)\[[Any](#typing.Any), [Any](#typing.Any)\]</code>) –
- [**name**](#openhands.sdk.tool.tool.ExecutableTool.name) (<code>[str](#str)</code>) –

##### `openhands.sdk.tool.tool.ExecutableTool.executor`

```python
executor: ToolExecutor[Any, Any]
```

##### `openhands.sdk.tool.tool.ExecutableTool.name`

```python
name: str
```

#### `openhands.sdk.tool.tool.ObservationT`

```python
ObservationT = TypeVar('ObservationT', bound=Observation)
```

#### `openhands.sdk.tool.tool.ToolAnnotations`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Annotations to provide hints about the tool's behavior.

Based on Model Context Protocol (MCP) spec:
https://github.com/modelcontextprotocol/modelcontextprotocol/blob/caf3424488b10b4a7b1f8cb634244a450a1f4400/schema/2025-06-18/schema.ts#L838

**Attributes:**

- [**destructiveHint**](#openhands.sdk.tool.tool.ToolAnnotations.destructiveHint) (<code>[bool](#bool)</code>) –
- [**idempotentHint**](#openhands.sdk.tool.tool.ToolAnnotations.idempotentHint) (<code>[bool](#bool)</code>) –
- [**model_config**](#openhands.sdk.tool.tool.ToolAnnotations.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**openWorldHint**](#openhands.sdk.tool.tool.ToolAnnotations.openWorldHint) (<code>[bool](#bool)</code>) –
- [**readOnlyHint**](#openhands.sdk.tool.tool.ToolAnnotations.readOnlyHint) (<code>[bool](#bool)</code>) –
- [**title**](#openhands.sdk.tool.tool.ToolAnnotations.title) (<code>[str](#str) | None</code>) –

##### `openhands.sdk.tool.tool.ToolAnnotations.destructiveHint`

```python
destructiveHint: bool = Field(default=True, description='If true, the tool may perform destructive updates to its environment. If false, the tool performs only additive updates. (This property is meaningful only when `readOnlyHint == false`) Default: true')
```

##### `openhands.sdk.tool.tool.ToolAnnotations.idempotentHint`

```python
idempotentHint: bool = Field(default=False, description='If true, calling the tool repeatedly with the same arguments will have no additional effect on the its environment. (This property is meaningful only when `readOnlyHint == false`) Default: false')
```

##### `openhands.sdk.tool.tool.ToolAnnotations.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, title='openhands.sdk.tool.tool.ToolAnnotations')
```

##### `openhands.sdk.tool.tool.ToolAnnotations.openWorldHint`

```python
openWorldHint: bool = Field(default=True, description="If true, this tool may interact with an 'open world' of external entities. If false, the tool's domain of interaction is closed. For example, the world of a web search tool is open, whereas that of a memory tool is not. Default: true")
```

##### `openhands.sdk.tool.tool.ToolAnnotations.readOnlyHint`

```python
readOnlyHint: bool = Field(default=False, description='If true, the tool does not modify its environment. Default: false')
```

##### `openhands.sdk.tool.tool.ToolAnnotations.title`

```python
title: str | None = Field(default=None, description='A human-readable title for the tool.')
```

#### `openhands.sdk.tool.tool.ToolBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Tool that wraps an executor function with input/output validation and schema.

- Normalize input/output schemas (class or dict) into both model+schema.
- Validate inputs before execute.
- Coerce outputs only if an output model is defined; else return vanilla JSON.
- Export MCP tool description.

**Functions:**

- [**action_from_arguments**](#openhands.sdk.tool.tool.ToolBase.action_from_arguments) – Create an action from parsed arguments.
- [**as_executable**](#openhands.sdk.tool.tool.ToolBase.as_executable) – Return this tool as an ExecutableTool, ensuring it has an executor.
- [**create**](#openhands.sdk.tool.tool.ToolBase.create) – Create a sequence of Tool instances. Placeholder for subclasses.
- [**get_serializable_type**](#openhands.sdk.tool.tool.ToolBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.tool.ToolBase.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.tool.ToolBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.tool.ToolBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.tool.ToolBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.tool.ToolBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.tool.ToolBase.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.tool.ToolBase.resolve_kind) –
- [**set_executor**](#openhands.sdk.tool.tool.ToolBase.set_executor) – Create a new Tool instance with the given executor.
- [**to_mcp_tool**](#openhands.sdk.tool.tool.ToolBase.to_mcp_tool) – Convert a Tool to an MCP tool definition.
- [**to_openai_tool**](#openhands.sdk.tool.tool.ToolBase.to_openai_tool) – Convert a Tool to an OpenAI tool.
- [**to_responses_tool**](#openhands.sdk.tool.tool.ToolBase.to_responses_tool) – Convert a Tool to a Responses API function tool (LiteLLM typed).

**Attributes:**

- [**action_type**](#openhands.sdk.tool.tool.ToolBase.action_type) (<code>[type](#type)\[[Action](#openhands.sdk.tool.schema.Action)\]</code>) –
- [**annotations**](#openhands.sdk.tool.tool.ToolBase.annotations) (<code>[ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | None</code>) –
- [**description**](#openhands.sdk.tool.tool.ToolBase.description) (<code>[str](#str)</code>) –
- [**executor**](#openhands.sdk.tool.tool.ToolBase.executor) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | None\]</code>) –
- [**kind**](#openhands.sdk.tool.tool.ToolBase.kind) (<code>[str](#str)</code>) –
- [**meta**](#openhands.sdk.tool.tool.ToolBase.meta) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) –
- [**model_config**](#openhands.sdk.tool.tool.ToolBase.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**name**](#openhands.sdk.tool.tool.ToolBase.name) (<code>[str](#str)</code>) –
- [**observation_type**](#openhands.sdk.tool.tool.ToolBase.observation_type) (<code>[type](#type)\[[Observation](#openhands.sdk.tool.schema.Observation)\] | None</code>) –
- [**title**](#openhands.sdk.tool.tool.ToolBase.title) (<code>[str](#str)</code>) –

##### `openhands.sdk.tool.tool.ToolBase.action_from_arguments`

```python
action_from_arguments(arguments)
```

Create an action from parsed arguments.

This method can be overridden by subclasses to provide custom logic
for creating actions from arguments (e.g., for MCP tools).

**Parameters:**

- **arguments** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The parsed arguments from the tool call.

**Returns:**

- <code>[Action](#openhands.sdk.tool.schema.Action)</code> – The action instance created from the arguments.

##### `openhands.sdk.tool.tool.ToolBase.action_type`

```python
action_type: type[Action] = Field(repr=False)
```

##### `openhands.sdk.tool.tool.ToolBase.annotations`

```python
annotations: ToolAnnotations | None = None
```

##### `openhands.sdk.tool.tool.ToolBase.as_executable`

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

##### `openhands.sdk.tool.tool.ToolBase.create`

```python
create(*args, **kwargs)
```

Create a sequence of Tool instances. Placeholder for subclasses.

This can be overridden in subclasses to provide custom initialization logic
(e.g., typically initializing the executor with parameters).

**Returns:**

- <code>[Sequence](#collections.abc.Sequence)\[[Self](#typing.Self)\]</code> – A sequence of Tool instances. Even single tools are returned as a sequence
- <code>[Sequence](#collections.abc.Sequence)\[[Self](#typing.Self)\]</code> – to provide a consistent interface and eliminate union return types.

##### `openhands.sdk.tool.tool.ToolBase.description`

```python
description: str
```

##### `openhands.sdk.tool.tool.ToolBase.executor`

```python
executor: SkipJsonSchema[ToolExecutor | None] = Field(default=None, repr=False, exclude=True)
```

##### `openhands.sdk.tool.tool.ToolBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.tool.ToolBase.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.tool.ToolBase.meta`

```python
meta: dict[str, Any] | None = None
```

##### `openhands.sdk.tool.tool.ToolBase.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

##### `openhands.sdk.tool.tool.ToolBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.tool.ToolBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.tool.ToolBase.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.tool.ToolBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.tool.ToolBase.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.tool.ToolBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.tool.ToolBase.name`

```python
name: str
```

##### `openhands.sdk.tool.tool.ToolBase.observation_type`

```python
observation_type: type[Observation] | None = Field(default=None, repr=False)
```

##### `openhands.sdk.tool.tool.ToolBase.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.tool.ToolBase.set_executor`

```python
set_executor(executor)
```

Create a new Tool instance with the given executor.

##### `openhands.sdk.tool.tool.ToolBase.title`

```python
title: str
```

##### `openhands.sdk.tool.tool.ToolBase.to_mcp_tool`

```python
to_mcp_tool(input_schema=None, output_schema=None)
```

Convert a Tool to an MCP tool definition.

Allow overriding input/output schemas (usually by subclasses).

**Parameters:**

- **input_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the input schema.
- **output_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the output schema.

##### `openhands.sdk.tool.tool.ToolBase.to_openai_tool`

```python
to_openai_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to an OpenAI tool.

**Parameters:**

- **add_security_risk_prediction** (<code>[bool](#bool)</code>) – Whether to add a `security_risk` field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.
- **action_type** (<code>[type](#type)\[[Schema](#openhands.sdk.tool.schema.Schema)\] | None</code>) – Optionally override the action_type to use for the schema.
  This is useful for MCPTool to use a dynamically created action type
  based on the tool's input schema.

##### `openhands.sdk.tool.tool.ToolBase.to_responses_tool`

```python
to_responses_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ "type": "function", "name": ..., "description": ..., "parameters": ... }

#### `openhands.sdk.tool.tool.ToolDefinition`

Bases: <code>[ToolBase](#openhands.sdk.tool.tool.ToolBase)\[[ToolDefinition[ActionT]](#openhands.sdk.tool.tool.ToolDefinition%5BActionT%5D), [ToolDefinition[ObservationT]](#openhands.sdk.tool.tool.ToolDefinition%5BObservationT%5D)\]</code>

Concrete tool class that inherits from ToolBase.

This class serves as a concrete implementation of ToolBase for cases where
you want to create a tool instance directly without implementing a custom
subclass. Built-in tools (like FinishTool, ThinkTool) are instantiated
directly from this class, while more complex tools (like BashTool,
FileEditorTool) inherit from this class and provide their own create()
method implementations.

**Functions:**

- [**action_from_arguments**](#openhands.sdk.tool.tool.ToolDefinition.action_from_arguments) – Create an action from parsed arguments.
- [**as_executable**](#openhands.sdk.tool.tool.ToolDefinition.as_executable) – Return this tool as an ExecutableTool, ensuring it has an executor.
- [**create**](#openhands.sdk.tool.tool.ToolDefinition.create) – Create a sequence of ToolDefinition instances.
- [**get_serializable_type**](#openhands.sdk.tool.tool.ToolDefinition.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.tool.tool.ToolDefinition.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.tool.tool.ToolDefinition.model_json_schema) –
- [**model_post_init**](#openhands.sdk.tool.tool.ToolDefinition.model_post_init) –
- [**model_rebuild**](#openhands.sdk.tool.tool.ToolDefinition.model_rebuild) –
- [**model_validate**](#openhands.sdk.tool.tool.ToolDefinition.model_validate) –
- [**model_validate_json**](#openhands.sdk.tool.tool.ToolDefinition.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.tool.tool.ToolDefinition.resolve_kind) –
- [**set_executor**](#openhands.sdk.tool.tool.ToolDefinition.set_executor) – Create a new Tool instance with the given executor.
- [**to_mcp_tool**](#openhands.sdk.tool.tool.ToolDefinition.to_mcp_tool) – Convert a Tool to an MCP tool definition.
- [**to_openai_tool**](#openhands.sdk.tool.tool.ToolDefinition.to_openai_tool) – Convert a Tool to an OpenAI tool.
- [**to_responses_tool**](#openhands.sdk.tool.tool.ToolDefinition.to_responses_tool) – Convert a Tool to a Responses API function tool (LiteLLM typed).

**Attributes:**

- [**action_type**](#openhands.sdk.tool.tool.ToolDefinition.action_type) (<code>[type](#type)\[[Action](#openhands.sdk.tool.schema.Action)\]</code>) –
- [**annotations**](#openhands.sdk.tool.tool.ToolDefinition.annotations) (<code>[ToolAnnotations](#openhands.sdk.tool.tool.ToolAnnotations) | None</code>) –
- [**description**](#openhands.sdk.tool.tool.ToolDefinition.description) (<code>[str](#str)</code>) –
- [**executor**](#openhands.sdk.tool.tool.ToolDefinition.executor) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[ToolExecutor](#openhands.sdk.tool.tool.ToolExecutor) | None\]</code>) –
- [**kind**](#openhands.sdk.tool.tool.ToolDefinition.kind) (<code>[str](#str)</code>) –
- [**meta**](#openhands.sdk.tool.tool.ToolDefinition.meta) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) –
- [**model_config**](#openhands.sdk.tool.tool.ToolDefinition.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**name**](#openhands.sdk.tool.tool.ToolDefinition.name) (<code>[str](#str)</code>) –
- [**observation_type**](#openhands.sdk.tool.tool.ToolDefinition.observation_type) (<code>[type](#type)\[[Observation](#openhands.sdk.tool.schema.Observation)\] | None</code>) –
- [**title**](#openhands.sdk.tool.tool.ToolDefinition.title) (<code>[str](#str)</code>) –

##### `openhands.sdk.tool.tool.ToolDefinition.action_from_arguments`

```python
action_from_arguments(arguments)
```

Create an action from parsed arguments.

This method can be overridden by subclasses to provide custom logic
for creating actions from arguments (e.g., for MCP tools).

**Parameters:**

- **arguments** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The parsed arguments from the tool call.

**Returns:**

- <code>[Action](#openhands.sdk.tool.schema.Action)</code> – The action instance created from the arguments.

##### `openhands.sdk.tool.tool.ToolDefinition.action_type`

```python
action_type: type[Action] = Field(repr=False)
```

##### `openhands.sdk.tool.tool.ToolDefinition.annotations`

```python
annotations: ToolAnnotations | None = None
```

##### `openhands.sdk.tool.tool.ToolDefinition.as_executable`

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

##### `openhands.sdk.tool.tool.ToolDefinition.create`

```python
create(*args, **kwargs)
```

Create a sequence of ToolDefinition instances.

TODO https://github.com/OpenHands/agent-sdk/issues/493
Refactor this - the ToolDefinition class should not have a concrete create()
implementation. Built-in tools should be refactored to not rely on this
method, and then this should be made abstract with @abstractmethod.

##### `openhands.sdk.tool.tool.ToolDefinition.description`

```python
description: str
```

##### `openhands.sdk.tool.tool.ToolDefinition.executor`

```python
executor: SkipJsonSchema[ToolExecutor | None] = Field(default=None, repr=False, exclude=True)
```

##### `openhands.sdk.tool.tool.ToolDefinition.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.tool.tool.ToolDefinition.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.tool.tool.ToolDefinition.meta`

```python
meta: dict[str, Any] | None = None
```

##### `openhands.sdk.tool.tool.ToolDefinition.model_config`

```python
model_config: ConfigDict = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

##### `openhands.sdk.tool.tool.ToolDefinition.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.tool.tool.ToolDefinition.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.tool.tool.ToolDefinition.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.tool.tool.ToolDefinition.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.tool.tool.ToolDefinition.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.tool.tool.ToolDefinition.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.tool.tool.ToolDefinition.name`

```python
name: str
```

##### `openhands.sdk.tool.tool.ToolDefinition.observation_type`

```python
observation_type: type[Observation] | None = Field(default=None, repr=False)
```

##### `openhands.sdk.tool.tool.ToolDefinition.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.tool.tool.ToolDefinition.set_executor`

```python
set_executor(executor)
```

Create a new Tool instance with the given executor.

##### `openhands.sdk.tool.tool.ToolDefinition.title`

```python
title: str
```

##### `openhands.sdk.tool.tool.ToolDefinition.to_mcp_tool`

```python
to_mcp_tool(input_schema=None, output_schema=None)
```

Convert a Tool to an MCP tool definition.

Allow overriding input/output schemas (usually by subclasses).

**Parameters:**

- **input_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the input schema.
- **output_schema** (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\] | None</code>) – Optionally override the output schema.

##### `openhands.sdk.tool.tool.ToolDefinition.to_openai_tool`

```python
to_openai_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to an OpenAI tool.

**Parameters:**

- **add_security_risk_prediction** (<code>[bool](#bool)</code>) – Whether to add a `security_risk` field
  to the action schema for LLM to predict. This is useful for
  tools that may have safety risks, so the LLM can reason about
  the risk level before calling the tool.
- **action_type** (<code>[type](#type)\[[Schema](#openhands.sdk.tool.schema.Schema)\] | None</code>) – Optionally override the action_type to use for the schema.
  This is useful for MCPTool to use a dynamically created action type
  based on the tool's input schema.

##### `openhands.sdk.tool.tool.ToolDefinition.to_responses_tool`

```python
to_responses_tool(add_security_risk_prediction=False, action_type=None)
```

Convert a Tool to a Responses API function tool (LiteLLM typed).

For Responses API, function tools expect top-level keys:
{ "type": "function", "name": ..., "description": ..., "parameters": ... }

#### `openhands.sdk.tool.tool.ToolExecutor`

Bases: <code>[ABC](#abc.ABC)</code>

Executor function type for a Tool.

**Functions:**

- [**close**](#openhands.sdk.tool.tool.ToolExecutor.close) – Close the executor and clean up resources.

##### `openhands.sdk.tool.tool.ToolExecutor.close`

```python
close()
```

Close the executor and clean up resources.

Default implementation does nothing. Subclasses should override
this method to perform cleanup (e.g., closing connections,
terminating processes, etc.).
