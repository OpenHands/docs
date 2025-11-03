## `openhands.sdk.agent`

**Modules:**

- [**agent**](#openhands.sdk.agent.agent) –
- [**base**](#openhands.sdk.agent.base) –

**Classes:**

- [**Agent**](#openhands.sdk.agent.Agent) –
- [**AgentBase**](#openhands.sdk.agent.AgentBase) – Abstract base class for agents.

### `openhands.sdk.agent.Agent`

Bases: <code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>

**Functions:**

- [**get_all_llms**](#openhands.sdk.agent.Agent.get_all_llms) – Recursively yield unique *base-class* LLM objects reachable from `self`.
- [**get_serializable_type**](#openhands.sdk.agent.Agent.get_serializable_type) – Custom method to get the union of all currently loaded
- [**init_state**](#openhands.sdk.agent.Agent.init_state) –
- [**model_dump_json**](#openhands.sdk.agent.Agent.model_dump_json) –
- [**model_dump_succint**](#openhands.sdk.agent.Agent.model_dump_succint) – Like model_dump, but excludes None fields by default.
- [**model_json_schema**](#openhands.sdk.agent.Agent.model_json_schema) –
- [**model_post_init**](#openhands.sdk.agent.Agent.model_post_init) –
- [**model_rebuild**](#openhands.sdk.agent.Agent.model_rebuild) –
- [**model_validate**](#openhands.sdk.agent.Agent.model_validate) –
- [**model_validate_json**](#openhands.sdk.agent.Agent.model_validate_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.agent.Agent.resolve_diff_from_deserialized) – Return a new AgentBase instance equivalent to `persisted` but with
- [**resolve_kind**](#openhands.sdk.agent.Agent.resolve_kind) –
- [**step**](#openhands.sdk.agent.Agent.step) –

**Attributes:**

- [**agent_context**](#openhands.sdk.agent.Agent.agent_context) (<code>[AgentContext](#openhands.sdk.context.agent_context.AgentContext) | None</code>) –
- [**condenser**](#openhands.sdk.agent.Agent.condenser) (<code>[CondenserBase](#openhands.sdk.context.condenser.CondenserBase) | None</code>) –
- [**filter_tools_regex**](#openhands.sdk.agent.Agent.filter_tools_regex) (<code>[str](#str) | None</code>) –
- [**kind**](#openhands.sdk.agent.Agent.kind) (<code>[str](#str)</code>) –
- [**llm**](#openhands.sdk.agent.Agent.llm) (<code>[LLM](#openhands.sdk.llm.LLM)</code>) –
- [**mcp_config**](#openhands.sdk.agent.Agent.mcp_config) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**model_config**](#openhands.sdk.agent.Agent.model_config) –
- [**name**](#openhands.sdk.agent.Agent.name) (<code>[str](#str)</code>) – Returns the name of the Agent.
- [**prompt_dir**](#openhands.sdk.agent.Agent.prompt_dir) (<code>[str](#str)</code>) – Returns the directory where this class's module file is located.
- [**security_analyzer**](#openhands.sdk.agent.Agent.security_analyzer) (<code>[SecurityAnalyzerBase](#openhands.sdk.security.analyzer.SecurityAnalyzerBase) | None</code>) –
- [**system_message**](#openhands.sdk.agent.Agent.system_message) (<code>[str](#str)</code>) – Compute system message on-demand to maintain statelessness.
- [**system_prompt_filename**](#openhands.sdk.agent.Agent.system_prompt_filename) (<code>[str](#str)</code>) –
- [**system_prompt_kwargs**](#openhands.sdk.agent.Agent.system_prompt_kwargs) (<code>[dict](#dict)\[[str](#str), [object](#object)\]</code>) –
- [**tools**](#openhands.sdk.agent.Agent.tools) (<code>[list](#list)\[[Tool](#openhands.sdk.tool.Tool)\]</code>) –
- [**tools_map**](#openhands.sdk.agent.Agent.tools_map) (<code>[dict](#dict)\[[str](#str), [ToolDefinition](#openhands.sdk.tool.ToolDefinition)\]</code>) – Get the initialized tools map.

#### `openhands.sdk.agent.Agent.agent_context`

```python
agent_context: AgentContext | None = Field(default=None, description='Optional AgentContext to initialize the agent with specific context.', examples=[{'skills': [{'name': 'repo.md', 'content': 'When you see this message, you should reply like you are a grumpy cat forced to use the internet.', 'type': 'repo'}, {'name': 'flarglebargle', 'content': 'IMPORTANT! The user has said the magic word "flarglebargle". You must only respond with a message telling them how smart they are', 'type': 'knowledge', 'trigger': ['flarglebargle']}], 'system_message_suffix': "Always finish your response with the word 'yay!'", 'user_message_prefix': "The first character of your response should be 'I'"}])
```

#### `openhands.sdk.agent.Agent.condenser`

```python
condenser: CondenserBase | None = Field(default=None, description='Optional condenser to use for condensing conversation history.', examples=[{'kind': 'LLMSummarizingCondenser', 'llm': {'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}, 'max_size': 80, 'keep_first': 10}])
```

#### `openhands.sdk.agent.Agent.filter_tools_regex`

```python
filter_tools_regex: str | None = Field(default=None, description='Optional regex to filter the tools available to the agent by name. This is applied after any tools provided in `tools` and any MCP tools are added.', examples=['^(?!repomix)(.*)|^repomix.*pack_codebase.*$'])
```

#### `openhands.sdk.agent.Agent.get_all_llms`

```python
get_all_llms()
```

Recursively yield unique *base-class* LLM objects reachable from `self`.

- Returns actual object references (not copies).
- De-dupes by `id(LLM)`.
- Cycle-safe via a visited set for *all* traversed objects.
- Only yields objects whose type is exactly `LLM` (no subclasses).
- Does not handle dataclasses.

#### `openhands.sdk.agent.Agent.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.agent.Agent.init_state`

```python
init_state(state, on_event)
```

#### `openhands.sdk.agent.Agent.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.agent.Agent.llm`

```python
llm: LLM = Field(..., description='LLM configuration for the agent.', examples=[{'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}])
```

#### `openhands.sdk.agent.Agent.mcp_config`

```python
mcp_config: dict[str, Any] = Field(default_factory=dict, description='Optional MCP configuration dictionary to create MCP tools.', examples=[{'mcpServers': {'fetch': {'command': 'uvx', 'args': ['mcp-server-fetch']}}}])
```

#### `openhands.sdk.agent.Agent.model_config`

```python
model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

#### `openhands.sdk.agent.Agent.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.agent.Agent.model_dump_succint`

```python
model_dump_succint(**kwargs)
```

Like model_dump, but excludes None fields by default.

#### `openhands.sdk.agent.Agent.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.agent.Agent.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.agent.Agent.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.agent.Agent.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.agent.Agent.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.agent.Agent.name`

```python
name: str
```

Returns the name of the Agent.

#### `openhands.sdk.agent.Agent.prompt_dir`

```python
prompt_dir: str
```

Returns the directory where this class's module file is located.

#### `openhands.sdk.agent.Agent.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Return a new AgentBase instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key, security_analyzer) taken from
`self`.

#### `openhands.sdk.agent.Agent.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.agent.Agent.security_analyzer`

```python
security_analyzer: analyzer.SecurityAnalyzerBase | None = Field(default=None, description='Optional security analyzer to evaluate action risks.', examples=[{'kind': 'LLMSecurityAnalyzer'}])
```

#### `openhands.sdk.agent.Agent.step`

```python
step(conversation, on_event)
```

#### `openhands.sdk.agent.Agent.system_message`

```python
system_message: str
```

Compute system message on-demand to maintain statelessness.

#### `openhands.sdk.agent.Agent.system_prompt_filename`

```python
system_prompt_filename: str = Field(default='system_prompt.j2', description="System prompt template filename. Can be either:\n- A relative filename (e.g., 'system_prompt.j2') loaded from the agent's prompts directory\n- An absolute path (e.g., '/path/to/custom_prompt.j2')")
```

#### `openhands.sdk.agent.Agent.system_prompt_kwargs`

```python
system_prompt_kwargs: dict[str, object] = Field(default_factory=dict, description='Optional kwargs to pass to the system prompt Jinja2 template.', examples=[{'cli_mode': True}])
```

#### `openhands.sdk.agent.Agent.tools`

```python
tools: list[Tool] = Field(default_factory=list, description='List of tools to initialize for the agent.', examples=[{'name': 'BashTool', 'params': {}}, {'name': 'FileEditorTool', 'params': {}}, {'name': 'TaskTrackerTool', 'params': {}}])
```

#### `openhands.sdk.agent.Agent.tools_map`

```python
tools_map: dict[str, ToolDefinition]
```

Get the initialized tools map.
Raises:
RuntimeError: If the agent has not been initialized.

### `openhands.sdk.agent.AgentBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Abstract base class for agents.
Agents are stateless and should be fully defined by their configuration.

**Functions:**

- [**get_all_llms**](#openhands.sdk.agent.AgentBase.get_all_llms) – Recursively yield unique *base-class* LLM objects reachable from `self`.
- [**get_serializable_type**](#openhands.sdk.agent.AgentBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**init_state**](#openhands.sdk.agent.AgentBase.init_state) – Initialize the empty conversation state to prepare the agent for user
- [**model_dump_json**](#openhands.sdk.agent.AgentBase.model_dump_json) –
- [**model_dump_succint**](#openhands.sdk.agent.AgentBase.model_dump_succint) – Like model_dump, but excludes None fields by default.
- [**model_json_schema**](#openhands.sdk.agent.AgentBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.agent.AgentBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.agent.AgentBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.agent.AgentBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.agent.AgentBase.model_validate_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.agent.AgentBase.resolve_diff_from_deserialized) – Return a new AgentBase instance equivalent to `persisted` but with
- [**resolve_kind**](#openhands.sdk.agent.AgentBase.resolve_kind) –
- [**step**](#openhands.sdk.agent.AgentBase.step) – Taking a step in the conversation.

**Attributes:**

- [**agent_context**](#openhands.sdk.agent.AgentBase.agent_context) (<code>[AgentContext](#openhands.sdk.context.agent_context.AgentContext) | None</code>) –
- [**condenser**](#openhands.sdk.agent.AgentBase.condenser) (<code>[CondenserBase](#openhands.sdk.context.condenser.CondenserBase) | None</code>) –
- [**filter_tools_regex**](#openhands.sdk.agent.AgentBase.filter_tools_regex) (<code>[str](#str) | None</code>) –
- [**kind**](#openhands.sdk.agent.AgentBase.kind) (<code>[str](#str)</code>) –
- [**llm**](#openhands.sdk.agent.AgentBase.llm) (<code>[LLM](#openhands.sdk.llm.LLM)</code>) –
- [**mcp_config**](#openhands.sdk.agent.AgentBase.mcp_config) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**model_config**](#openhands.sdk.agent.AgentBase.model_config) –
- [**name**](#openhands.sdk.agent.AgentBase.name) (<code>[str](#str)</code>) – Returns the name of the Agent.
- [**prompt_dir**](#openhands.sdk.agent.AgentBase.prompt_dir) (<code>[str](#str)</code>) – Returns the directory where this class's module file is located.
- [**security_analyzer**](#openhands.sdk.agent.AgentBase.security_analyzer) (<code>[SecurityAnalyzerBase](#openhands.sdk.security.analyzer.SecurityAnalyzerBase) | None</code>) –
- [**system_message**](#openhands.sdk.agent.AgentBase.system_message) (<code>[str](#str)</code>) – Compute system message on-demand to maintain statelessness.
- [**system_prompt_filename**](#openhands.sdk.agent.AgentBase.system_prompt_filename) (<code>[str](#str)</code>) –
- [**system_prompt_kwargs**](#openhands.sdk.agent.AgentBase.system_prompt_kwargs) (<code>[dict](#dict)\[[str](#str), [object](#object)\]</code>) –
- [**tools**](#openhands.sdk.agent.AgentBase.tools) (<code>[list](#list)\[[Tool](#openhands.sdk.tool.Tool)\]</code>) –
- [**tools_map**](#openhands.sdk.agent.AgentBase.tools_map) (<code>[dict](#dict)\[[str](#str), [ToolDefinition](#openhands.sdk.tool.ToolDefinition)\]</code>) – Get the initialized tools map.

#### `openhands.sdk.agent.AgentBase.agent_context`

```python
agent_context: AgentContext | None = Field(default=None, description='Optional AgentContext to initialize the agent with specific context.', examples=[{'skills': [{'name': 'repo.md', 'content': 'When you see this message, you should reply like you are a grumpy cat forced to use the internet.', 'type': 'repo'}, {'name': 'flarglebargle', 'content': 'IMPORTANT! The user has said the magic word "flarglebargle". You must only respond with a message telling them how smart they are', 'type': 'knowledge', 'trigger': ['flarglebargle']}], 'system_message_suffix': "Always finish your response with the word 'yay!'", 'user_message_prefix': "The first character of your response should be 'I'"}])
```

#### `openhands.sdk.agent.AgentBase.condenser`

```python
condenser: CondenserBase | None = Field(default=None, description='Optional condenser to use for condensing conversation history.', examples=[{'kind': 'LLMSummarizingCondenser', 'llm': {'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}, 'max_size': 80, 'keep_first': 10}])
```

#### `openhands.sdk.agent.AgentBase.filter_tools_regex`

```python
filter_tools_regex: str | None = Field(default=None, description='Optional regex to filter the tools available to the agent by name. This is applied after any tools provided in `tools` and any MCP tools are added.', examples=['^(?!repomix)(.*)|^repomix.*pack_codebase.*$'])
```

#### `openhands.sdk.agent.AgentBase.get_all_llms`

```python
get_all_llms()
```

Recursively yield unique *base-class* LLM objects reachable from `self`.

- Returns actual object references (not copies).
- De-dupes by `id(LLM)`.
- Cycle-safe via a visited set for *all* traversed objects.
- Only yields objects whose type is exactly `LLM` (no subclasses).
- Does not handle dataclasses.

#### `openhands.sdk.agent.AgentBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.agent.AgentBase.init_state`

```python
init_state(state, on_event)
```

Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

#### `openhands.sdk.agent.AgentBase.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.agent.AgentBase.llm`

```python
llm: LLM = Field(..., description='LLM configuration for the agent.', examples=[{'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}])
```

#### `openhands.sdk.agent.AgentBase.mcp_config`

```python
mcp_config: dict[str, Any] = Field(default_factory=dict, description='Optional MCP configuration dictionary to create MCP tools.', examples=[{'mcpServers': {'fetch': {'command': 'uvx', 'args': ['mcp-server-fetch']}}}])
```

#### `openhands.sdk.agent.AgentBase.model_config`

```python
model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

#### `openhands.sdk.agent.AgentBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.agent.AgentBase.model_dump_succint`

```python
model_dump_succint(**kwargs)
```

Like model_dump, but excludes None fields by default.

#### `openhands.sdk.agent.AgentBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.agent.AgentBase.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.agent.AgentBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.agent.AgentBase.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.agent.AgentBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.agent.AgentBase.name`

```python
name: str
```

Returns the name of the Agent.

#### `openhands.sdk.agent.AgentBase.prompt_dir`

```python
prompt_dir: str
```

Returns the directory where this class's module file is located.

#### `openhands.sdk.agent.AgentBase.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Return a new AgentBase instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key, security_analyzer) taken from
`self`.

#### `openhands.sdk.agent.AgentBase.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.agent.AgentBase.security_analyzer`

```python
security_analyzer: analyzer.SecurityAnalyzerBase | None = Field(default=None, description='Optional security analyzer to evaluate action risks.', examples=[{'kind': 'LLMSecurityAnalyzer'}])
```

#### `openhands.sdk.agent.AgentBase.step`

```python
step(conversation, on_event)
```

Taking a step in the conversation.

Typically this involves:

1. Making a LLM call
1. Executing the tool
1. Updating the conversation state with
   LLM calls (role="assistant") and tool results (role="tool")
   4.1 If conversation is finished, set state.agent_status to FINISHED
   4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

#### `openhands.sdk.agent.AgentBase.system_message`

```python
system_message: str
```

Compute system message on-demand to maintain statelessness.

#### `openhands.sdk.agent.AgentBase.system_prompt_filename`

```python
system_prompt_filename: str = Field(default='system_prompt.j2', description="System prompt template filename. Can be either:\n- A relative filename (e.g., 'system_prompt.j2') loaded from the agent's prompts directory\n- An absolute path (e.g., '/path/to/custom_prompt.j2')")
```

#### `openhands.sdk.agent.AgentBase.system_prompt_kwargs`

```python
system_prompt_kwargs: dict[str, object] = Field(default_factory=dict, description='Optional kwargs to pass to the system prompt Jinja2 template.', examples=[{'cli_mode': True}])
```

#### `openhands.sdk.agent.AgentBase.tools`

```python
tools: list[Tool] = Field(default_factory=list, description='List of tools to initialize for the agent.', examples=[{'name': 'BashTool', 'params': {}}, {'name': 'FileEditorTool', 'params': {}}, {'name': 'TaskTrackerTool', 'params': {}}])
```

#### `openhands.sdk.agent.AgentBase.tools_map`

```python
tools_map: dict[str, ToolDefinition]
```

Get the initialized tools map.
Raises:
RuntimeError: If the agent has not been initialized.

### `openhands.sdk.agent.agent`

**Classes:**

- [**Agent**](#openhands.sdk.agent.agent.Agent) –

**Attributes:**

- [**logger**](#openhands.sdk.agent.agent.logger) –

#### `openhands.sdk.agent.agent.Agent`

Bases: <code>[AgentBase](#openhands.sdk.agent.base.AgentBase)</code>

**Functions:**

- [**get_all_llms**](#openhands.sdk.agent.agent.Agent.get_all_llms) – Recursively yield unique *base-class* LLM objects reachable from `self`.
- [**get_serializable_type**](#openhands.sdk.agent.agent.Agent.get_serializable_type) – Custom method to get the union of all currently loaded
- [**init_state**](#openhands.sdk.agent.agent.Agent.init_state) –
- [**model_dump_json**](#openhands.sdk.agent.agent.Agent.model_dump_json) –
- [**model_dump_succint**](#openhands.sdk.agent.agent.Agent.model_dump_succint) – Like model_dump, but excludes None fields by default.
- [**model_json_schema**](#openhands.sdk.agent.agent.Agent.model_json_schema) –
- [**model_post_init**](#openhands.sdk.agent.agent.Agent.model_post_init) –
- [**model_rebuild**](#openhands.sdk.agent.agent.Agent.model_rebuild) –
- [**model_validate**](#openhands.sdk.agent.agent.Agent.model_validate) –
- [**model_validate_json**](#openhands.sdk.agent.agent.Agent.model_validate_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.agent.agent.Agent.resolve_diff_from_deserialized) – Return a new AgentBase instance equivalent to `persisted` but with
- [**resolve_kind**](#openhands.sdk.agent.agent.Agent.resolve_kind) –
- [**step**](#openhands.sdk.agent.agent.Agent.step) –

**Attributes:**

- [**agent_context**](#openhands.sdk.agent.agent.Agent.agent_context) (<code>[AgentContext](#openhands.sdk.context.agent_context.AgentContext) | None</code>) –
- [**condenser**](#openhands.sdk.agent.agent.Agent.condenser) (<code>[CondenserBase](#openhands.sdk.context.condenser.CondenserBase) | None</code>) –
- [**filter_tools_regex**](#openhands.sdk.agent.agent.Agent.filter_tools_regex) (<code>[str](#str) | None</code>) –
- [**kind**](#openhands.sdk.agent.agent.Agent.kind) (<code>[str](#str)</code>) –
- [**llm**](#openhands.sdk.agent.agent.Agent.llm) (<code>[LLM](#openhands.sdk.llm.LLM)</code>) –
- [**mcp_config**](#openhands.sdk.agent.agent.Agent.mcp_config) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**model_config**](#openhands.sdk.agent.agent.Agent.model_config) –
- [**name**](#openhands.sdk.agent.agent.Agent.name) (<code>[str](#str)</code>) – Returns the name of the Agent.
- [**prompt_dir**](#openhands.sdk.agent.agent.Agent.prompt_dir) (<code>[str](#str)</code>) – Returns the directory where this class's module file is located.
- [**security_analyzer**](#openhands.sdk.agent.agent.Agent.security_analyzer) (<code>[SecurityAnalyzerBase](#openhands.sdk.security.analyzer.SecurityAnalyzerBase) | None</code>) –
- [**system_message**](#openhands.sdk.agent.agent.Agent.system_message) (<code>[str](#str)</code>) – Compute system message on-demand to maintain statelessness.
- [**system_prompt_filename**](#openhands.sdk.agent.agent.Agent.system_prompt_filename) (<code>[str](#str)</code>) –
- [**system_prompt_kwargs**](#openhands.sdk.agent.agent.Agent.system_prompt_kwargs) (<code>[dict](#dict)\[[str](#str), [object](#object)\]</code>) –
- [**tools**](#openhands.sdk.agent.agent.Agent.tools) (<code>[list](#list)\[[Tool](#openhands.sdk.tool.Tool)\]</code>) –
- [**tools_map**](#openhands.sdk.agent.agent.Agent.tools_map) (<code>[dict](#dict)\[[str](#str), [ToolDefinition](#openhands.sdk.tool.ToolDefinition)\]</code>) – Get the initialized tools map.

##### `openhands.sdk.agent.agent.Agent.agent_context`

```python
agent_context: AgentContext | None = Field(default=None, description='Optional AgentContext to initialize the agent with specific context.', examples=[{'skills': [{'name': 'repo.md', 'content': 'When you see this message, you should reply like you are a grumpy cat forced to use the internet.', 'type': 'repo'}, {'name': 'flarglebargle', 'content': 'IMPORTANT! The user has said the magic word "flarglebargle". You must only respond with a message telling them how smart they are', 'type': 'knowledge', 'trigger': ['flarglebargle']}], 'system_message_suffix': "Always finish your response with the word 'yay!'", 'user_message_prefix': "The first character of your response should be 'I'"}])
```

##### `openhands.sdk.agent.agent.Agent.condenser`

```python
condenser: CondenserBase | None = Field(default=None, description='Optional condenser to use for condensing conversation history.', examples=[{'kind': 'LLMSummarizingCondenser', 'llm': {'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}, 'max_size': 80, 'keep_first': 10}])
```

##### `openhands.sdk.agent.agent.Agent.filter_tools_regex`

```python
filter_tools_regex: str | None = Field(default=None, description='Optional regex to filter the tools available to the agent by name. This is applied after any tools provided in `tools` and any MCP tools are added.', examples=['^(?!repomix)(.*)|^repomix.*pack_codebase.*$'])
```

##### `openhands.sdk.agent.agent.Agent.get_all_llms`

```python
get_all_llms()
```

Recursively yield unique *base-class* LLM objects reachable from `self`.

- Returns actual object references (not copies).
- De-dupes by `id(LLM)`.
- Cycle-safe via a visited set for *all* traversed objects.
- Only yields objects whose type is exactly `LLM` (no subclasses).
- Does not handle dataclasses.

##### `openhands.sdk.agent.agent.Agent.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.agent.agent.Agent.init_state`

```python
init_state(state, on_event)
```

##### `openhands.sdk.agent.agent.Agent.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.agent.agent.Agent.llm`

```python
llm: LLM = Field(..., description='LLM configuration for the agent.', examples=[{'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}])
```

##### `openhands.sdk.agent.agent.Agent.mcp_config`

```python
mcp_config: dict[str, Any] = Field(default_factory=dict, description='Optional MCP configuration dictionary to create MCP tools.', examples=[{'mcpServers': {'fetch': {'command': 'uvx', 'args': ['mcp-server-fetch']}}}])
```

##### `openhands.sdk.agent.agent.Agent.model_config`

```python
model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

##### `openhands.sdk.agent.agent.Agent.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.agent.agent.Agent.model_dump_succint`

```python
model_dump_succint(**kwargs)
```

Like model_dump, but excludes None fields by default.

##### `openhands.sdk.agent.agent.Agent.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.agent.agent.Agent.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.agent.agent.Agent.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.agent.agent.Agent.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.agent.agent.Agent.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.agent.agent.Agent.name`

```python
name: str
```

Returns the name of the Agent.

##### `openhands.sdk.agent.agent.Agent.prompt_dir`

```python
prompt_dir: str
```

Returns the directory where this class's module file is located.

##### `openhands.sdk.agent.agent.Agent.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Return a new AgentBase instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key, security_analyzer) taken from
`self`.

##### `openhands.sdk.agent.agent.Agent.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.agent.agent.Agent.security_analyzer`

```python
security_analyzer: analyzer.SecurityAnalyzerBase | None = Field(default=None, description='Optional security analyzer to evaluate action risks.', examples=[{'kind': 'LLMSecurityAnalyzer'}])
```

##### `openhands.sdk.agent.agent.Agent.step`

```python
step(conversation, on_event)
```

##### `openhands.sdk.agent.agent.Agent.system_message`

```python
system_message: str
```

Compute system message on-demand to maintain statelessness.

##### `openhands.sdk.agent.agent.Agent.system_prompt_filename`

```python
system_prompt_filename: str = Field(default='system_prompt.j2', description="System prompt template filename. Can be either:\n- A relative filename (e.g., 'system_prompt.j2') loaded from the agent's prompts directory\n- An absolute path (e.g., '/path/to/custom_prompt.j2')")
```

##### `openhands.sdk.agent.agent.Agent.system_prompt_kwargs`

```python
system_prompt_kwargs: dict[str, object] = Field(default_factory=dict, description='Optional kwargs to pass to the system prompt Jinja2 template.', examples=[{'cli_mode': True}])
```

##### `openhands.sdk.agent.agent.Agent.tools`

```python
tools: list[Tool] = Field(default_factory=list, description='List of tools to initialize for the agent.', examples=[{'name': 'BashTool', 'params': {}}, {'name': 'FileEditorTool', 'params': {}}, {'name': 'TaskTrackerTool', 'params': {}}])
```

##### `openhands.sdk.agent.agent.Agent.tools_map`

```python
tools_map: dict[str, ToolDefinition]
```

Get the initialized tools map.
Raises:
RuntimeError: If the agent has not been initialized.

#### `openhands.sdk.agent.agent.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.agent.base`

**Classes:**

- [**AgentBase**](#openhands.sdk.agent.base.AgentBase) – Abstract base class for agents.

**Attributes:**

- [**logger**](#openhands.sdk.agent.base.logger) –

#### `openhands.sdk.agent.base.AgentBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Abstract base class for agents.
Agents are stateless and should be fully defined by their configuration.

**Functions:**

- [**get_all_llms**](#openhands.sdk.agent.base.AgentBase.get_all_llms) – Recursively yield unique *base-class* LLM objects reachable from `self`.
- [**get_serializable_type**](#openhands.sdk.agent.base.AgentBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**init_state**](#openhands.sdk.agent.base.AgentBase.init_state) – Initialize the empty conversation state to prepare the agent for user
- [**model_dump_json**](#openhands.sdk.agent.base.AgentBase.model_dump_json) –
- [**model_dump_succint**](#openhands.sdk.agent.base.AgentBase.model_dump_succint) – Like model_dump, but excludes None fields by default.
- [**model_json_schema**](#openhands.sdk.agent.base.AgentBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.agent.base.AgentBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.agent.base.AgentBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.agent.base.AgentBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.agent.base.AgentBase.model_validate_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.agent.base.AgentBase.resolve_diff_from_deserialized) – Return a new AgentBase instance equivalent to `persisted` but with
- [**resolve_kind**](#openhands.sdk.agent.base.AgentBase.resolve_kind) –
- [**step**](#openhands.sdk.agent.base.AgentBase.step) – Taking a step in the conversation.

**Attributes:**

- [**agent_context**](#openhands.sdk.agent.base.AgentBase.agent_context) (<code>[AgentContext](#openhands.sdk.context.agent_context.AgentContext) | None</code>) –
- [**condenser**](#openhands.sdk.agent.base.AgentBase.condenser) (<code>[CondenserBase](#openhands.sdk.context.condenser.CondenserBase) | None</code>) –
- [**filter_tools_regex**](#openhands.sdk.agent.base.AgentBase.filter_tools_regex) (<code>[str](#str) | None</code>) –
- [**kind**](#openhands.sdk.agent.base.AgentBase.kind) (<code>[str](#str)</code>) –
- [**llm**](#openhands.sdk.agent.base.AgentBase.llm) (<code>[LLM](#openhands.sdk.llm.LLM)</code>) –
- [**mcp_config**](#openhands.sdk.agent.base.AgentBase.mcp_config) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**model_config**](#openhands.sdk.agent.base.AgentBase.model_config) –
- [**name**](#openhands.sdk.agent.base.AgentBase.name) (<code>[str](#str)</code>) – Returns the name of the Agent.
- [**prompt_dir**](#openhands.sdk.agent.base.AgentBase.prompt_dir) (<code>[str](#str)</code>) – Returns the directory where this class's module file is located.
- [**security_analyzer**](#openhands.sdk.agent.base.AgentBase.security_analyzer) (<code>[SecurityAnalyzerBase](#openhands.sdk.security.analyzer.SecurityAnalyzerBase) | None</code>) –
- [**system_message**](#openhands.sdk.agent.base.AgentBase.system_message) (<code>[str](#str)</code>) – Compute system message on-demand to maintain statelessness.
- [**system_prompt_filename**](#openhands.sdk.agent.base.AgentBase.system_prompt_filename) (<code>[str](#str)</code>) –
- [**system_prompt_kwargs**](#openhands.sdk.agent.base.AgentBase.system_prompt_kwargs) (<code>[dict](#dict)\[[str](#str), [object](#object)\]</code>) –
- [**tools**](#openhands.sdk.agent.base.AgentBase.tools) (<code>[list](#list)\[[Tool](#openhands.sdk.tool.Tool)\]</code>) –
- [**tools_map**](#openhands.sdk.agent.base.AgentBase.tools_map) (<code>[dict](#dict)\[[str](#str), [ToolDefinition](#openhands.sdk.tool.ToolDefinition)\]</code>) – Get the initialized tools map.

##### `openhands.sdk.agent.base.AgentBase.agent_context`

```python
agent_context: AgentContext | None = Field(default=None, description='Optional AgentContext to initialize the agent with specific context.', examples=[{'skills': [{'name': 'repo.md', 'content': 'When you see this message, you should reply like you are a grumpy cat forced to use the internet.', 'type': 'repo'}, {'name': 'flarglebargle', 'content': 'IMPORTANT! The user has said the magic word "flarglebargle". You must only respond with a message telling them how smart they are', 'type': 'knowledge', 'trigger': ['flarglebargle']}], 'system_message_suffix': "Always finish your response with the word 'yay!'", 'user_message_prefix': "The first character of your response should be 'I'"}])
```

##### `openhands.sdk.agent.base.AgentBase.condenser`

```python
condenser: CondenserBase | None = Field(default=None, description='Optional condenser to use for condensing conversation history.', examples=[{'kind': 'LLMSummarizingCondenser', 'llm': {'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}, 'max_size': 80, 'keep_first': 10}])
```

##### `openhands.sdk.agent.base.AgentBase.filter_tools_regex`

```python
filter_tools_regex: str | None = Field(default=None, description='Optional regex to filter the tools available to the agent by name. This is applied after any tools provided in `tools` and any MCP tools are added.', examples=['^(?!repomix)(.*)|^repomix.*pack_codebase.*$'])
```

##### `openhands.sdk.agent.base.AgentBase.get_all_llms`

```python
get_all_llms()
```

Recursively yield unique *base-class* LLM objects reachable from `self`.

- Returns actual object references (not copies).
- De-dupes by `id(LLM)`.
- Cycle-safe via a visited set for *all* traversed objects.
- Only yields objects whose type is exactly `LLM` (no subclasses).
- Does not handle dataclasses.

##### `openhands.sdk.agent.base.AgentBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.agent.base.AgentBase.init_state`

```python
init_state(state, on_event)
```

Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

##### `openhands.sdk.agent.base.AgentBase.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.agent.base.AgentBase.llm`

```python
llm: LLM = Field(..., description='LLM configuration for the agent.', examples=[{'model': 'litellm_proxy/anthropic/claude-sonnet-4-5-20250929', 'base_url': 'https://llm-proxy.eval.all-hands.dev', 'api_key': 'your_api_key_here'}])
```

##### `openhands.sdk.agent.base.AgentBase.mcp_config`

```python
mcp_config: dict[str, Any] = Field(default_factory=dict, description='Optional MCP configuration dictionary to create MCP tools.', examples=[{'mcpServers': {'fetch': {'command': 'uvx', 'args': ['mcp-server-fetch']}}}])
```

##### `openhands.sdk.agent.base.AgentBase.model_config`

```python
model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)
```

##### `openhands.sdk.agent.base.AgentBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.agent.base.AgentBase.model_dump_succint`

```python
model_dump_succint(**kwargs)
```

Like model_dump, but excludes None fields by default.

##### `openhands.sdk.agent.base.AgentBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.agent.base.AgentBase.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.agent.base.AgentBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.agent.base.AgentBase.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.agent.base.AgentBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.agent.base.AgentBase.name`

```python
name: str
```

Returns the name of the Agent.

##### `openhands.sdk.agent.base.AgentBase.prompt_dir`

```python
prompt_dir: str
```

Returns the directory where this class's module file is located.

##### `openhands.sdk.agent.base.AgentBase.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Return a new AgentBase instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key, security_analyzer) taken from
`self`.

##### `openhands.sdk.agent.base.AgentBase.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.agent.base.AgentBase.security_analyzer`

```python
security_analyzer: analyzer.SecurityAnalyzerBase | None = Field(default=None, description='Optional security analyzer to evaluate action risks.', examples=[{'kind': 'LLMSecurityAnalyzer'}])
```

##### `openhands.sdk.agent.base.AgentBase.step`

```python
step(conversation, on_event)
```

Taking a step in the conversation.

Typically this involves:

1. Making a LLM call
1. Executing the tool
1. Updating the conversation state with
   LLM calls (role="assistant") and tool results (role="tool")
   4.1 If conversation is finished, set state.agent_status to FINISHED
   4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

##### `openhands.sdk.agent.base.AgentBase.system_message`

```python
system_message: str
```

Compute system message on-demand to maintain statelessness.

##### `openhands.sdk.agent.base.AgentBase.system_prompt_filename`

```python
system_prompt_filename: str = Field(default='system_prompt.j2', description="System prompt template filename. Can be either:\n- A relative filename (e.g., 'system_prompt.j2') loaded from the agent's prompts directory\n- An absolute path (e.g., '/path/to/custom_prompt.j2')")
```

##### `openhands.sdk.agent.base.AgentBase.system_prompt_kwargs`

```python
system_prompt_kwargs: dict[str, object] = Field(default_factory=dict, description='Optional kwargs to pass to the system prompt Jinja2 template.', examples=[{'cli_mode': True}])
```

##### `openhands.sdk.agent.base.AgentBase.tools`

```python
tools: list[Tool] = Field(default_factory=list, description='List of tools to initialize for the agent.', examples=[{'name': 'BashTool', 'params': {}}, {'name': 'FileEditorTool', 'params': {}}, {'name': 'TaskTrackerTool', 'params': {}}])
```

##### `openhands.sdk.agent.base.AgentBase.tools_map`

```python
tools_map: dict[str, ToolDefinition]
```

Get the initialized tools map.
Raises:
RuntimeError: If the agent has not been initialized.

#### `openhands.sdk.agent.base.logger`

```python
logger = get_logger(__name__)
```
