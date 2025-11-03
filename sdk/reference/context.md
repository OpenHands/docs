## `openhands.sdk.context`

**Modules:**

- [**agent_context**](#openhands.sdk.context.agent_context) –
- [**condenser**](#openhands.sdk.context.condenser) –
- [**prompts**](#openhands.sdk.context.prompts) –
- [**skills**](#openhands.sdk.context.skills) –
- [**view**](#openhands.sdk.context.view) –

**Classes:**

- [**AgentContext**](#openhands.sdk.context.AgentContext) – Central structure for managing prompt extension.
- [**BaseTrigger**](#openhands.sdk.context.BaseTrigger) – Base class for all trigger types.
- [**KeywordTrigger**](#openhands.sdk.context.KeywordTrigger) – Trigger for keyword-based skills.
- [**Skill**](#openhands.sdk.context.Skill) – A skill provides specialized knowledge or functionality.
- [**SkillKnowledge**](#openhands.sdk.context.SkillKnowledge) – Represents knowledge from a triggered skill.
- [**SkillValidationError**](#openhands.sdk.context.SkillValidationError) – Raised when there's a validation error in skill metadata.
- [**TaskTrigger**](#openhands.sdk.context.TaskTrigger) – Trigger for task-specific skills.

**Functions:**

- [**load_skills_from_dir**](#openhands.sdk.context.load_skills_from_dir) – Load all skills from the given directory.
- [**render_template**](#openhands.sdk.context.render_template) – Render a Jinja2 template.

### `openhands.sdk.context.AgentContext`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Central structure for managing prompt extension.

AgentContext unifies all the contextual inputs that shape how the system
extends and interprets user prompts. It combines both static environment
details and dynamic, user-activated extensions from skills.

Specifically, it provides:

- **Repository context / Repo Skills**: Information about the active codebase,
  branches, and repo-specific instructions contributed by repo skills.
- **Runtime context**: Current execution environment (hosts, working
  directory, secrets, date, etc.).
- **Conversation instructions**: Optional task- or channel-specific rules
  that constrain or guide the agent’s behavior across the session.
- **Knowledge Skills**: Extensible components that can be triggered by user input
  to inject knowledge or domain-specific guidance.

Together, these elements make AgentContext the primary container responsible
for assembling, formatting, and injecting all prompt-relevant context into
LLM interactions.

**Functions:**

- [**get_system_message_suffix**](#openhands.sdk.context.AgentContext.get_system_message_suffix) – Get the system message with repo skill content and custom suffix.
- [**get_user_message_suffix**](#openhands.sdk.context.AgentContext.get_user_message_suffix) – Augment the user’s message with knowledge recalled from skills.

**Attributes:**

- [**skills**](#openhands.sdk.context.AgentContext.skills) (<code>[list](#list)\[[Skill](#openhands.sdk.context.skills.Skill)\]</code>) –
- [**system_message_suffix**](#openhands.sdk.context.AgentContext.system_message_suffix) (<code>[str](#str) | None</code>) –
- [**user_message_suffix**](#openhands.sdk.context.AgentContext.user_message_suffix) (<code>[str](#str) | None</code>) –

#### `openhands.sdk.context.AgentContext.get_system_message_suffix`

```python
get_system_message_suffix()
```

Get the system message with repo skill content and custom suffix.

Custom suffix can typically includes:

- Repository information (repo name, branch name, PR number, etc.)
- Runtime information (e.g., available hosts, current date)
- Conversation instructions (e.g., user preferences, task details)
- Repository-specific instructions (collected from repo skills)

#### `openhands.sdk.context.AgentContext.get_user_message_suffix`

```python
get_user_message_suffix(user_message, skip_skill_names)
```

Augment the user’s message with knowledge recalled from skills.

This works by:

- Extracting the text content of the user message
- Matching skill triggers against the query
- Returning formatted knowledge and triggered skill names if relevant skills were triggered

#### `openhands.sdk.context.AgentContext.skills`

```python
skills: list[Skill] = Field(default_factory=list, description="List of available skills that can extend the user's input.")
```

#### `openhands.sdk.context.AgentContext.system_message_suffix`

```python
system_message_suffix: str | None = Field(default=None, description='Optional suffix to append to the system prompt.')
```

#### `openhands.sdk.context.AgentContext.user_message_suffix`

```python
user_message_suffix: str | None = Field(default=None, description="Optional suffix to append to the user's message.")
```

### `openhands.sdk.context.BaseTrigger`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>, <code>[ABC](#abc.ABC)</code>

Base class for all trigger types.

### `openhands.sdk.context.KeywordTrigger`

Bases: <code>[BaseTrigger](#openhands.sdk.context.skills.trigger.BaseTrigger)</code>

Trigger for keyword-based skills.

These skills are activated when specific keywords appear in the user's query.

**Attributes:**

- [**keywords**](#openhands.sdk.context.KeywordTrigger.keywords) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.context.KeywordTrigger.type) (<code>[Literal](#typing.Literal)['keyword']</code>) –

#### `openhands.sdk.context.KeywordTrigger.keywords`

```python
keywords: list[str]
```

#### `openhands.sdk.context.KeywordTrigger.type`

```python
type: Literal['keyword'] = 'keyword'
```

### `openhands.sdk.context.Skill`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

A skill provides specialized knowledge or functionality.

Skills use triggers to determine when they should be activated:

- None: Always active, for repository-specific guidelines
- KeywordTrigger: Activated when keywords appear in user messages
- TaskTrigger: Activated for specific tasks, may require user input

**Functions:**

- [**extract_variables**](#openhands.sdk.context.Skill.extract_variables) – Extract variables from the content.
- [**load**](#openhands.sdk.context.Skill.load) – Load a skill from a markdown file with frontmatter.
- [**match_trigger**](#openhands.sdk.context.Skill.match_trigger) – Match a trigger in the message.
- [**requires_user_input**](#openhands.sdk.context.Skill.requires_user_input) – Check if this skill requires user input.

**Attributes:**

- [**PATH_TO_THIRD_PARTY_SKILL_NAME**](#openhands.sdk.context.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME) (<code>[dict](#dict)\[[str](#str), [str](#str)\]</code>) –
- [**content**](#openhands.sdk.context.Skill.content) (<code>[str](#str)</code>) –
- [**inputs**](#openhands.sdk.context.Skill.inputs) (<code>[list](#list)\[[InputMetadata](#openhands.sdk.context.skills.types.InputMetadata)\]</code>) –
- [**mcp_tools**](#openhands.sdk.context.Skill.mcp_tools) (<code>[dict](#dict) | None</code>) –
- [**name**](#openhands.sdk.context.Skill.name) (<code>[str](#str)</code>) –
- [**source**](#openhands.sdk.context.Skill.source) (<code>[str](#str) | None</code>) –
- [**trigger**](#openhands.sdk.context.Skill.trigger) (<code>[TriggerType](#openhands.sdk.context.skills.skill.TriggerType) | None</code>) –

#### `openhands.sdk.context.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME`

```python
PATH_TO_THIRD_PARTY_SKILL_NAME: dict[str, str] = {'.cursorrules': 'cursorrules', 'agents.md': 'agents', 'agent.md': 'agents'}
```

#### `openhands.sdk.context.Skill.content`

```python
content: str
```

#### `openhands.sdk.context.Skill.extract_variables`

```python
extract_variables(content)
```

Extract variables from the content.

Variables are in the format ${variable_name}.

#### `openhands.sdk.context.Skill.inputs`

```python
inputs: list[InputMetadata] = Field(default_factory=list, description='Input metadata for the skill (task skills only)')
```

#### `openhands.sdk.context.Skill.load`

```python
load(path, skill_dir=None, file_content=None)
```

Load a skill from a markdown file with frontmatter.

The agent's name is derived from its path relative to the skill_dir.

#### `openhands.sdk.context.Skill.match_trigger`

```python
match_trigger(message)
```

Match a trigger in the message.

Returns the first trigger that matches the message, or None if no match.
Only applies to KeywordTrigger and TaskTrigger types.

#### `openhands.sdk.context.Skill.mcp_tools`

```python
mcp_tools: dict | None = Field(default=None, description='MCP tools configuration for the skill (repo skills only). It should conform to the MCPConfig schema: https://gofastmcp.com/clients/client#configuration-format')
```

#### `openhands.sdk.context.Skill.name`

```python
name: str
```

#### `openhands.sdk.context.Skill.requires_user_input`

```python
requires_user_input()
```

Check if this skill requires user input.

Returns True if the content contains variables in the format ${variable_name}.

#### `openhands.sdk.context.Skill.source`

```python
source: str | None = Field(default=None, description='The source path or identifier of the skill. When it is None, it is treated as a programmatically defined skill.')
```

#### `openhands.sdk.context.Skill.trigger`

```python
trigger: TriggerType | None
```

### `openhands.sdk.context.SkillKnowledge`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Represents knowledge from a triggered skill.

**Attributes:**

- [**content**](#openhands.sdk.context.SkillKnowledge.content) (<code>[str](#str)</code>) –
- [**name**](#openhands.sdk.context.SkillKnowledge.name) (<code>[str](#str)</code>) –
- [**trigger**](#openhands.sdk.context.SkillKnowledge.trigger) (<code>[str](#str)</code>) –

#### `openhands.sdk.context.SkillKnowledge.content`

```python
content: str = Field(description='The actual content/knowledge from the skill')
```

#### `openhands.sdk.context.SkillKnowledge.name`

```python
name: str = Field(description='The name of the skill that was triggered')
```

#### `openhands.sdk.context.SkillKnowledge.trigger`

```python
trigger: str = Field(description='The word that triggered this skill')
```

### `openhands.sdk.context.SkillValidationError`

```python
SkillValidationError(message='Skill validation failed')
```

Bases: <code>[SkillError](#openhands.sdk.context.skills.exceptions.SkillError)</code>

Raised when there's a validation error in skill metadata.

### `openhands.sdk.context.TaskTrigger`

Bases: <code>[BaseTrigger](#openhands.sdk.context.skills.trigger.BaseTrigger)</code>

Trigger for task-specific skills.

These skills are activated for specific task types and can modify prompts.

**Attributes:**

- [**triggers**](#openhands.sdk.context.TaskTrigger.triggers) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.context.TaskTrigger.type) (<code>[Literal](#typing.Literal)['task']</code>) –

#### `openhands.sdk.context.TaskTrigger.triggers`

```python
triggers: list[str]
```

#### `openhands.sdk.context.TaskTrigger.type`

```python
type: Literal['task'] = 'task'
```

### `openhands.sdk.context.agent_context`

**Classes:**

- [**AgentContext**](#openhands.sdk.context.agent_context.AgentContext) – Central structure for managing prompt extension.

**Attributes:**

- [**PROMPT_DIR**](#openhands.sdk.context.agent_context.PROMPT_DIR) –
- [**logger**](#openhands.sdk.context.agent_context.logger) –

#### `openhands.sdk.context.agent_context.AgentContext`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Central structure for managing prompt extension.

AgentContext unifies all the contextual inputs that shape how the system
extends and interprets user prompts. It combines both static environment
details and dynamic, user-activated extensions from skills.

Specifically, it provides:

- **Repository context / Repo Skills**: Information about the active codebase,
  branches, and repo-specific instructions contributed by repo skills.
- **Runtime context**: Current execution environment (hosts, working
  directory, secrets, date, etc.).
- **Conversation instructions**: Optional task- or channel-specific rules
  that constrain or guide the agent’s behavior across the session.
- **Knowledge Skills**: Extensible components that can be triggered by user input
  to inject knowledge or domain-specific guidance.

Together, these elements make AgentContext the primary container responsible
for assembling, formatting, and injecting all prompt-relevant context into
LLM interactions.

**Functions:**

- [**get_system_message_suffix**](#openhands.sdk.context.agent_context.AgentContext.get_system_message_suffix) – Get the system message with repo skill content and custom suffix.
- [**get_user_message_suffix**](#openhands.sdk.context.agent_context.AgentContext.get_user_message_suffix) – Augment the user’s message with knowledge recalled from skills.

**Attributes:**

- [**skills**](#openhands.sdk.context.agent_context.AgentContext.skills) (<code>[list](#list)\[[Skill](#openhands.sdk.context.skills.Skill)\]</code>) –
- [**system_message_suffix**](#openhands.sdk.context.agent_context.AgentContext.system_message_suffix) (<code>[str](#str) | None</code>) –
- [**user_message_suffix**](#openhands.sdk.context.agent_context.AgentContext.user_message_suffix) (<code>[str](#str) | None</code>) –

##### `openhands.sdk.context.agent_context.AgentContext.get_system_message_suffix`

```python
get_system_message_suffix()
```

Get the system message with repo skill content and custom suffix.

Custom suffix can typically includes:

- Repository information (repo name, branch name, PR number, etc.)
- Runtime information (e.g., available hosts, current date)
- Conversation instructions (e.g., user preferences, task details)
- Repository-specific instructions (collected from repo skills)

##### `openhands.sdk.context.agent_context.AgentContext.get_user_message_suffix`

```python
get_user_message_suffix(user_message, skip_skill_names)
```

Augment the user’s message with knowledge recalled from skills.

This works by:

- Extracting the text content of the user message
- Matching skill triggers against the query
- Returning formatted knowledge and triggered skill names if relevant skills were triggered

##### `openhands.sdk.context.agent_context.AgentContext.skills`

```python
skills: list[Skill] = Field(default_factory=list, description="List of available skills that can extend the user's input.")
```

##### `openhands.sdk.context.agent_context.AgentContext.system_message_suffix`

```python
system_message_suffix: str | None = Field(default=None, description='Optional suffix to append to the system prompt.')
```

##### `openhands.sdk.context.agent_context.AgentContext.user_message_suffix`

```python
user_message_suffix: str | None = Field(default=None, description="Optional suffix to append to the user's message.")
```

#### `openhands.sdk.context.agent_context.PROMPT_DIR`

```python
PROMPT_DIR = pathlib.Path(__file__).parent / 'prompts' / 'templates'
```

#### `openhands.sdk.context.agent_context.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.context.condenser`

**Modules:**

- [**base**](#openhands.sdk.context.condenser.base) –
- [**llm_summarizing_condenser**](#openhands.sdk.context.condenser.llm_summarizing_condenser) –
- [**no_op_condenser**](#openhands.sdk.context.condenser.no_op_condenser) –
- [**pipeline_condenser**](#openhands.sdk.context.condenser.pipeline_condenser) –

**Classes:**

- [**CondenserBase**](#openhands.sdk.context.condenser.CondenserBase) – Abstract condenser interface.
- [**LLMSummarizingCondenser**](#openhands.sdk.context.condenser.LLMSummarizingCondenser) –
- [**NoOpCondenser**](#openhands.sdk.context.condenser.NoOpCondenser) – Simple condenser that returns a view un-manipulated.
- [**PipelineCondenser**](#openhands.sdk.context.condenser.PipelineCondenser) – A condenser that applies a sequence of condensers in order.
- [**RollingCondenser**](#openhands.sdk.context.condenser.RollingCondenser) – Base class for a specialized condenser strategy that applies condensation to a

#### `openhands.sdk.context.condenser.CondenserBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Abstract condenser interface.

Condensers take a list of `Event` objects and reduce them into a potentially smaller
list.

Agents can use condensers to reduce the amount of events they need to consider when
deciding which action to take. To use a condenser, agents can call the
`condensed_history` method on the current `State` being considered and use the
results instead of the full history.

If the condenser returns a `Condensation` instead of a `View`, the agent should
return `Condensation.action` instead of producing its own action. On the next agent
step the condenser will use that condensation event to produce a new `View`.

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.CondenserBase.condense) – Condense a sequence of events into a potentially smaller list.
- [**get_serializable_type**](#openhands.sdk.context.condenser.CondenserBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.CondenserBase.handles_condensation_requests) – Whether this condenser handles explicit condensation requests.
- [**model_dump_json**](#openhands.sdk.context.condenser.CondenserBase.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.CondenserBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.CondenserBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.CondenserBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.CondenserBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.CondenserBase.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.CondenserBase.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.context.condenser.CondenserBase.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.context.condenser.CondenserBase.condense`

```python
condense(view)
```

Condense a sequence of events into a potentially smaller list.

New condenser strategies should override this method to implement their own
condensation logic. Call `self.add_metadata` in the implementation to record any
relevant per-condensation diagnostic information.

**Parameters:**

- **view** (<code>[View](#openhands.sdk.context.view.View)</code>) – A view of the history containing all events that should be condensed.

**Returns:**

- <code>[View](#openhands.sdk.context.view.View) | [Condensation](#openhands.sdk.event.condenser.Condensation)</code> – View | Condensation: A condensed view of the events or an event indicating
- <code>[View](#openhands.sdk.context.view.View) | [Condensation](#openhands.sdk.event.condenser.Condensation)</code> – the history has been condensed.

##### `openhands.sdk.context.condenser.CondenserBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.context.condenser.CondenserBase.handles_condensation_requests`

```python
handles_condensation_requests()
```

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent's own logic decides to do so (e.g. context
window exceeded).

**Returns:**

- **bool** (<code>[bool](#bool)</code>) – True if the condenser handles explicit condensation requests, False
- <code>[bool](#bool)</code> – otherwise.

##### `openhands.sdk.context.condenser.CondenserBase.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.context.condenser.CondenserBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.context.condenser.CondenserBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.context.condenser.CondenserBase.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.context.condenser.CondenserBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.context.condenser.CondenserBase.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.context.condenser.CondenserBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.context.condenser.CondenserBase.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.context.condenser.LLMSummarizingCondenser`

Bases: <code>[RollingCondenser](#openhands.sdk.context.condenser.base.RollingCondenser)</code>

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.condense) –
- [**get_condensation**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.get_condensation) –
- [**get_serializable_type**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.handles_condensation_requests) –
- [**model_dump_json**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.resolve_kind) –
- [**should_condense**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.should_condense) –
- [**validate_keep_first_vs_max_size**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.validate_keep_first_vs_max_size) –

**Attributes:**

- [**keep_first**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.keep_first) (<code>[int](#int)</code>) –
- [**kind**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.kind) (<code>[str](#str)</code>) –
- [**llm**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.llm) (<code>[LLM](#openhands.sdk.llm.LLM)</code>) –
- [**max_size**](#openhands.sdk.context.condenser.LLMSummarizingCondenser.max_size) (<code>[int](#int)</code>) –

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.condense`

```python
condense(view)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.get_condensation`

```python
get_condensation(view)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.keep_first`

```python
keep_first: int = Field(default=4, ge=0)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.llm`

```python
llm: LLM
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.max_size`

```python
max_size: int = Field(default=120, gt=0)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.should_condense`

```python
should_condense(view)
```

##### `openhands.sdk.context.condenser.LLMSummarizingCondenser.validate_keep_first_vs_max_size`

```python
validate_keep_first_vs_max_size()
```

#### `openhands.sdk.context.condenser.NoOpCondenser`

Bases: <code>[CondenserBase](#openhands.sdk.context.condenser.base.CondenserBase)</code>

Simple condenser that returns a view un-manipulated.

Primarily intended for testing purposes.

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.NoOpCondenser.condense) –
- [**get_serializable_type**](#openhands.sdk.context.condenser.NoOpCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.NoOpCondenser.handles_condensation_requests) – Whether this condenser handles explicit condensation requests.
- [**model_dump_json**](#openhands.sdk.context.condenser.NoOpCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.NoOpCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.NoOpCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.NoOpCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.NoOpCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.NoOpCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.NoOpCondenser.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.context.condenser.NoOpCondenser.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.context.condenser.NoOpCondenser.condense`

```python
condense(view)
```

##### `openhands.sdk.context.condenser.NoOpCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.context.condenser.NoOpCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent's own logic decides to do so (e.g. context
window exceeded).

**Returns:**

- **bool** (<code>[bool](#bool)</code>) – True if the condenser handles explicit condensation requests, False
- <code>[bool](#bool)</code> – otherwise.

##### `openhands.sdk.context.condenser.NoOpCondenser.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.context.condenser.NoOpCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.context.condenser.NoOpCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.context.condenser.NoOpCondenser.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.context.condenser.NoOpCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.context.condenser.NoOpCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.context.condenser.NoOpCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.context.condenser.NoOpCondenser.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.context.condenser.PipelineCondenser`

Bases: <code>[CondenserBase](#openhands.sdk.context.condenser.base.CondenserBase)</code>

A condenser that applies a sequence of condensers in order.

All condensers are defined primarily by their `condense` method, which takes a
`View` and returns either a new `View` or a `Condensation` event. That means we can
chain multiple condensers together by passing `View`s along and exiting early if any
condenser returns a `Condensation`.

For example:

```
# Use the pipeline condenser to chain multiple other condensers together
condenser = PipelineCondenser(condensers=[
    CondenserA(...),
    CondenserB(...),
    CondenserC(...),
])

result = condenser.condense(view)

# Doing the same thing without the pipeline condenser requires more boilerplate
# for the monadic chaining
other_result = view

if isinstance(other_result, View):
    other_result = CondenserA(...).condense(other_result)

if isinstance(other_result, View):
    other_result = CondenserB(...).condense(other_result)

if isinstance(other_result, View):
    other_result = CondenserC(...).condense(other_result)

assert result == other_result
```

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.PipelineCondenser.condense) –
- [**get_serializable_type**](#openhands.sdk.context.condenser.PipelineCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.PipelineCondenser.handles_condensation_requests) –
- [**model_dump_json**](#openhands.sdk.context.condenser.PipelineCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.PipelineCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.PipelineCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.PipelineCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.PipelineCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.PipelineCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.PipelineCondenser.resolve_kind) –

**Attributes:**

- [**condensers**](#openhands.sdk.context.condenser.PipelineCondenser.condensers) (<code>[list](#list)\[[CondenserBase](#openhands.sdk.context.condenser.base.CondenserBase)\]</code>) – The list of condensers to apply in order.
- [**kind**](#openhands.sdk.context.condenser.PipelineCondenser.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.context.condenser.PipelineCondenser.condense`

```python
condense(view)
```

##### `openhands.sdk.context.condenser.PipelineCondenser.condensers`

```python
condensers: list[CondenserBase]
```

The list of condensers to apply in order.

##### `openhands.sdk.context.condenser.PipelineCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.context.condenser.PipelineCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

##### `openhands.sdk.context.condenser.PipelineCondenser.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.context.condenser.PipelineCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.context.condenser.PipelineCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.context.condenser.PipelineCondenser.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.context.condenser.PipelineCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.context.condenser.PipelineCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.context.condenser.PipelineCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.context.condenser.PipelineCondenser.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.context.condenser.RollingCondenser`

Bases: <code>[PipelinableCondenserBase](#openhands.sdk.context.condenser.base.PipelinableCondenserBase)</code>, <code>[ABC](#abc.ABC)</code>

Base class for a specialized condenser strategy that applies condensation to a
rolling history.

The rolling history is generated by `View.from_events`, which analyzes all events in
the history and produces a `View` object representing what will be sent to the LLM.

If `should_condense` says so, the condenser is then responsible for generating a
`Condensation` object from the `View` object. This will be added to the event
history which should -- when given to `get_view` -- produce the condensed `View` to
be passed to the LLM.

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.RollingCondenser.condense) –
- [**get_condensation**](#openhands.sdk.context.condenser.RollingCondenser.get_condensation) – Get the condensation from a view.
- [**get_serializable_type**](#openhands.sdk.context.condenser.RollingCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.RollingCondenser.handles_condensation_requests) – Whether this condenser handles explicit condensation requests.
- [**model_dump_json**](#openhands.sdk.context.condenser.RollingCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.RollingCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.RollingCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.RollingCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.RollingCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.RollingCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.RollingCondenser.resolve_kind) –
- [**should_condense**](#openhands.sdk.context.condenser.RollingCondenser.should_condense) – Determine if a view should be condensed.

**Attributes:**

- [**kind**](#openhands.sdk.context.condenser.RollingCondenser.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.context.condenser.RollingCondenser.condense`

```python
condense(view)
```

##### `openhands.sdk.context.condenser.RollingCondenser.get_condensation`

```python
get_condensation(view)
```

Get the condensation from a view.

##### `openhands.sdk.context.condenser.RollingCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.context.condenser.RollingCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent's own logic decides to do so (e.g. context
window exceeded).

**Returns:**

- **bool** (<code>[bool](#bool)</code>) – True if the condenser handles explicit condensation requests, False
- <code>[bool](#bool)</code> – otherwise.

##### `openhands.sdk.context.condenser.RollingCondenser.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.context.condenser.RollingCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.context.condenser.RollingCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.context.condenser.RollingCondenser.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.context.condenser.RollingCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.context.condenser.RollingCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.context.condenser.RollingCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.context.condenser.RollingCondenser.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.context.condenser.RollingCondenser.should_condense`

```python
should_condense(view)
```

Determine if a view should be condensed.

#### `openhands.sdk.context.condenser.base`

**Classes:**

- [**CondenserBase**](#openhands.sdk.context.condenser.base.CondenserBase) – Abstract condenser interface.
- [**PipelinableCondenserBase**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase) – Abstract condenser interface which may be pipelined. (Since a pipeline
- [**RollingCondenser**](#openhands.sdk.context.condenser.base.RollingCondenser) – Base class for a specialized condenser strategy that applies condensation to a

**Attributes:**

- [**logger**](#openhands.sdk.context.condenser.base.logger) –

##### `openhands.sdk.context.condenser.base.CondenserBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Abstract condenser interface.

Condensers take a list of `Event` objects and reduce them into a potentially smaller
list.

Agents can use condensers to reduce the amount of events they need to consider when
deciding which action to take. To use a condenser, agents can call the
`condensed_history` method on the current `State` being considered and use the
results instead of the full history.

If the condenser returns a `Condensation` instead of a `View`, the agent should
return `Condensation.action` instead of producing its own action. On the next agent
step the condenser will use that condensation event to produce a new `View`.

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.base.CondenserBase.condense) – Condense a sequence of events into a potentially smaller list.
- [**get_serializable_type**](#openhands.sdk.context.condenser.base.CondenserBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.base.CondenserBase.handles_condensation_requests) – Whether this condenser handles explicit condensation requests.
- [**model_dump_json**](#openhands.sdk.context.condenser.base.CondenserBase.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.base.CondenserBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.base.CondenserBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.base.CondenserBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.base.CondenserBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.base.CondenserBase.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.base.CondenserBase.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.context.condenser.base.CondenserBase.kind) (<code>[str](#str)</code>) –

###### `openhands.sdk.context.condenser.base.CondenserBase.condense`

```python
condense(view)
```

Condense a sequence of events into a potentially smaller list.

New condenser strategies should override this method to implement their own
condensation logic. Call `self.add_metadata` in the implementation to record any
relevant per-condensation diagnostic information.

**Parameters:**

- **view** (<code>[View](#openhands.sdk.context.view.View)</code>) – A view of the history containing all events that should be condensed.

**Returns:**

- <code>[View](#openhands.sdk.context.view.View) | [Condensation](#openhands.sdk.event.condenser.Condensation)</code> – View | Condensation: A condensed view of the events or an event indicating
- <code>[View](#openhands.sdk.context.view.View) | [Condensation](#openhands.sdk.event.condenser.Condensation)</code> – the history has been condensed.

###### `openhands.sdk.context.condenser.base.CondenserBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.context.condenser.base.CondenserBase.handles_condensation_requests`

```python
handles_condensation_requests()
```

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent's own logic decides to do so (e.g. context
window exceeded).

**Returns:**

- **bool** (<code>[bool](#bool)</code>) – True if the condenser handles explicit condensation requests, False
- <code>[bool](#bool)</code> – otherwise.

###### `openhands.sdk.context.condenser.base.CondenserBase.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.context.condenser.base.CondenserBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.context.condenser.base.CondenserBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.context.condenser.base.CondenserBase.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.context.condenser.base.CondenserBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.context.condenser.base.CondenserBase.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.context.condenser.base.CondenserBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.context.condenser.base.CondenserBase.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.context.condenser.base.PipelinableCondenserBase`

Bases: <code>[CondenserBase](#openhands.sdk.context.condenser.base.CondenserBase)</code>

Abstract condenser interface which may be pipelined. (Since a pipeline
condenser should not nest another pipeline condenser)

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.condense) – Condense a sequence of events into a potentially smaller list.
- [**get_serializable_type**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.handles_condensation_requests) – Whether this condenser handles explicit condensation requests.
- [**model_dump_json**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.context.condenser.base.PipelinableCondenserBase.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.context.condenser.base.RollingCondenser`

Bases: <code>[PipelinableCondenserBase](#openhands.sdk.context.condenser.base.PipelinableCondenserBase)</code>, <code>[ABC](#abc.ABC)</code>

Base class for a specialized condenser strategy that applies condensation to a
rolling history.

The rolling history is generated by `View.from_events`, which analyzes all events in
the history and produces a `View` object representing what will be sent to the LLM.

If `should_condense` says so, the condenser is then responsible for generating a
`Condensation` object from the `View` object. This will be added to the event
history which should -- when given to `get_view` -- produce the condensed `View` to
be passed to the LLM.

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.base.RollingCondenser.condense) –
- [**get_condensation**](#openhands.sdk.context.condenser.base.RollingCondenser.get_condensation) – Get the condensation from a view.
- [**get_serializable_type**](#openhands.sdk.context.condenser.base.RollingCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.base.RollingCondenser.handles_condensation_requests) – Whether this condenser handles explicit condensation requests.
- [**model_dump_json**](#openhands.sdk.context.condenser.base.RollingCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.base.RollingCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.base.RollingCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.base.RollingCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.base.RollingCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.base.RollingCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.base.RollingCondenser.resolve_kind) –
- [**should_condense**](#openhands.sdk.context.condenser.base.RollingCondenser.should_condense) – Determine if a view should be condensed.

**Attributes:**

- [**kind**](#openhands.sdk.context.condenser.base.RollingCondenser.kind) (<code>[str](#str)</code>) –

###### `openhands.sdk.context.condenser.base.RollingCondenser.condense`

```python
condense(view)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.get_condensation`

```python
get_condensation(view)
```

Get the condensation from a view.

###### `openhands.sdk.context.condenser.base.RollingCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.context.condenser.base.RollingCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent's own logic decides to do so (e.g. context
window exceeded).

**Returns:**

- **bool** (<code>[bool](#bool)</code>) – True if the condenser handles explicit condensation requests, False
- <code>[bool](#bool)</code> – otherwise.

###### `openhands.sdk.context.condenser.base.RollingCondenser.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.resolve_kind`

```python
resolve_kind(kind)
```

###### `openhands.sdk.context.condenser.base.RollingCondenser.should_condense`

```python
should_condense(view)
```

Determine if a view should be condensed.

##### `openhands.sdk.context.condenser.base.logger`

```python
logger = getLogger(__name__)
```

#### `openhands.sdk.context.condenser.llm_summarizing_condenser`

**Classes:**

- [**LLMSummarizingCondenser**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser) –

##### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser`

Bases: <code>[RollingCondenser](#openhands.sdk.context.condenser.base.RollingCondenser)</code>

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.condense) –
- [**get_condensation**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.get_condensation) –
- [**get_serializable_type**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.handles_condensation_requests) –
- [**model_dump_json**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.resolve_kind) –
- [**should_condense**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.should_condense) –
- [**validate_keep_first_vs_max_size**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.validate_keep_first_vs_max_size) –

**Attributes:**

- [**keep_first**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.keep_first) (<code>[int](#int)</code>) –
- [**kind**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.kind) (<code>[str](#str)</code>) –
- [**llm**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.llm) (<code>[LLM](#openhands.sdk.llm.LLM)</code>) –
- [**max_size**](#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.max_size) (<code>[int](#int)</code>) –

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.condense`

```python
condense(view)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.get_condensation`

```python
get_condensation(view)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.keep_first`

```python
keep_first: int = Field(default=4, ge=0)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.llm`

```python
llm: LLM
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.max_size`

```python
max_size: int = Field(default=120, gt=0)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.resolve_kind`

```python
resolve_kind(kind)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.should_condense`

```python
should_condense(view)
```

###### `openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser.validate_keep_first_vs_max_size`

```python
validate_keep_first_vs_max_size()
```

#### `openhands.sdk.context.condenser.no_op_condenser`

**Classes:**

- [**NoOpCondenser**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser) – Simple condenser that returns a view un-manipulated.

##### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser`

Bases: <code>[CondenserBase](#openhands.sdk.context.condenser.base.CondenserBase)</code>

Simple condenser that returns a view un-manipulated.

Primarily intended for testing purposes.

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.condense) –
- [**get_serializable_type**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.handles_condensation_requests) – Whether this condenser handles explicit condensation requests.
- [**model_dump_json**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.kind) (<code>[str](#str)</code>) –

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.condense`

```python
condense(view)
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent's own logic decides to do so (e.g. context
window exceeded).

**Returns:**

- **bool** (<code>[bool](#bool)</code>) – True if the condenser handles explicit condensation requests, False
- <code>[bool](#bool)</code> – otherwise.

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.context.condenser.pipeline_condenser`

**Classes:**

- [**PipelineCondenser**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser) – A condenser that applies a sequence of condensers in order.

##### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser`

Bases: <code>[CondenserBase](#openhands.sdk.context.condenser.base.CondenserBase)</code>

A condenser that applies a sequence of condensers in order.

All condensers are defined primarily by their `condense` method, which takes a
`View` and returns either a new `View` or a `Condensation` event. That means we can
chain multiple condensers together by passing `View`s along and exiting early if any
condenser returns a `Condensation`.

For example:

```
# Use the pipeline condenser to chain multiple other condensers together
condenser = PipelineCondenser(condensers=[
    CondenserA(...),
    CondenserB(...),
    CondenserC(...),
])

result = condenser.condense(view)

# Doing the same thing without the pipeline condenser requires more boilerplate
# for the monadic chaining
other_result = view

if isinstance(other_result, View):
    other_result = CondenserA(...).condense(other_result)

if isinstance(other_result, View):
    other_result = CondenserB(...).condense(other_result)

if isinstance(other_result, View):
    other_result = CondenserC(...).condense(other_result)

assert result == other_result
```

**Functions:**

- [**condense**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.condense) –
- [**get_serializable_type**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.get_serializable_type) – Custom method to get the union of all currently loaded
- [**handles_condensation_requests**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.handles_condensation_requests) –
- [**model_dump_json**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_json_schema) –
- [**model_post_init**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_post_init) –
- [**model_rebuild**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_rebuild) –
- [**model_validate**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_validate) –
- [**model_validate_json**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.resolve_kind) –

**Attributes:**

- [**condensers**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.condensers) (<code>[list](#list)\[[CondenserBase](#openhands.sdk.context.condenser.base.CondenserBase)\]</code>) – The list of condensers to apply in order.
- [**kind**](#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.kind) (<code>[str](#str)</code>) –

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.condense`

```python
condense(view)
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.condensers`

```python
condensers: list[CondenserBase]
```

The list of condensers to apply in order.

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.handles_condensation_requests`

```python
handles_condensation_requests()
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_post_init`

```python
model_post_init(_context)
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser.resolve_kind`

```python
resolve_kind(kind)
```

### `openhands.sdk.context.load_skills_from_dir`

```python
load_skills_from_dir(skill_dir)
```

Load all skills from the given directory.

Note, legacy repo instructions will not be loaded here.

**Parameters:**

- **skill_dir** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the skills directory (e.g. .openhands/skills)

**Returns:**

- <code>[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]</code> – Tuple of (repo_skills, knowledge_skills) dictionaries.
- <code>[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]</code> – repo_skills have trigger=None, knowledge_skills have KeywordTrigger
- <code>[tuple](#tuple)\[[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\], [dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]\]</code> – or TaskTrigger.

### `openhands.sdk.context.prompts`

**Modules:**

- [**prompt**](#openhands.sdk.context.prompts.prompt) –

**Functions:**

- [**render_template**](#openhands.sdk.context.prompts.render_template) – Render a Jinja2 template.

#### `openhands.sdk.context.prompts.prompt`

**Functions:**

- [**refine**](#openhands.sdk.context.prompts.prompt.refine) –
- [**render_template**](#openhands.sdk.context.prompts.prompt.render_template) – Render a Jinja2 template.

##### `openhands.sdk.context.prompts.prompt.refine`

```python
refine(text)
```

##### `openhands.sdk.context.prompts.prompt.render_template`

```python
render_template(prompt_dir, template_name, **ctx)
```

Render a Jinja2 template.

**Parameters:**

- **prompt_dir** (<code>[str](#str)</code>) – The base directory for relative template paths.
- **template_name** (<code>[str](#str)</code>) – The template filename. Can be either:
- A relative filename (e.g., "system_prompt.j2") loaded from prompt_dir
- An absolute path (e.g., "/path/to/custom_prompt.j2")
- \*\***ctx** – Template context variables.

**Returns:**

- <code>[str](#str)</code> – Rendered template string.

**Raises:**

- <code>[FileNotFoundError](#FileNotFoundError)</code> – If the template file cannot be found.

#### `openhands.sdk.context.prompts.render_template`

```python
render_template(prompt_dir, template_name, **ctx)
```

Render a Jinja2 template.

**Parameters:**

- **prompt_dir** (<code>[str](#str)</code>) – The base directory for relative template paths.
- **template_name** (<code>[str](#str)</code>) – The template filename. Can be either:
- A relative filename (e.g., "system_prompt.j2") loaded from prompt_dir
- An absolute path (e.g., "/path/to/custom_prompt.j2")
- \*\***ctx** – Template context variables.

**Returns:**

- <code>[str](#str)</code> – Rendered template string.

**Raises:**

- <code>[FileNotFoundError](#FileNotFoundError)</code> – If the template file cannot be found.

### `openhands.sdk.context.render_template`

```python
render_template(prompt_dir, template_name, **ctx)
```

Render a Jinja2 template.

**Parameters:**

- **prompt_dir** (<code>[str](#str)</code>) – The base directory for relative template paths.
- **template_name** (<code>[str](#str)</code>) – The template filename. Can be either:
- A relative filename (e.g., "system_prompt.j2") loaded from prompt_dir
- An absolute path (e.g., "/path/to/custom_prompt.j2")
- \*\***ctx** – Template context variables.

**Returns:**

- <code>[str](#str)</code> – Rendered template string.

**Raises:**

- <code>[FileNotFoundError](#FileNotFoundError)</code> – If the template file cannot be found.

### `openhands.sdk.context.skills`

**Modules:**

- [**exceptions**](#openhands.sdk.context.skills.exceptions) –
- [**skill**](#openhands.sdk.context.skills.skill) –
- [**trigger**](#openhands.sdk.context.skills.trigger) – Trigger types for skills.
- [**types**](#openhands.sdk.context.skills.types) –

**Classes:**

- [**BaseTrigger**](#openhands.sdk.context.skills.BaseTrigger) – Base class for all trigger types.
- [**KeywordTrigger**](#openhands.sdk.context.skills.KeywordTrigger) – Trigger for keyword-based skills.
- [**Skill**](#openhands.sdk.context.skills.Skill) – A skill provides specialized knowledge or functionality.
- [**SkillKnowledge**](#openhands.sdk.context.skills.SkillKnowledge) – Represents knowledge from a triggered skill.
- [**SkillValidationError**](#openhands.sdk.context.skills.SkillValidationError) – Raised when there's a validation error in skill metadata.
- [**TaskTrigger**](#openhands.sdk.context.skills.TaskTrigger) – Trigger for task-specific skills.

**Functions:**

- [**load_skills_from_dir**](#openhands.sdk.context.skills.load_skills_from_dir) – Load all skills from the given directory.

#### `openhands.sdk.context.skills.BaseTrigger`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>, <code>[ABC](#abc.ABC)</code>

Base class for all trigger types.

#### `openhands.sdk.context.skills.KeywordTrigger`

Bases: <code>[BaseTrigger](#openhands.sdk.context.skills.trigger.BaseTrigger)</code>

Trigger for keyword-based skills.

These skills are activated when specific keywords appear in the user's query.

**Attributes:**

- [**keywords**](#openhands.sdk.context.skills.KeywordTrigger.keywords) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.context.skills.KeywordTrigger.type) (<code>[Literal](#typing.Literal)['keyword']</code>) –

##### `openhands.sdk.context.skills.KeywordTrigger.keywords`

```python
keywords: list[str]
```

##### `openhands.sdk.context.skills.KeywordTrigger.type`

```python
type: Literal['keyword'] = 'keyword'
```

#### `openhands.sdk.context.skills.Skill`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

A skill provides specialized knowledge or functionality.

Skills use triggers to determine when they should be activated:

- None: Always active, for repository-specific guidelines
- KeywordTrigger: Activated when keywords appear in user messages
- TaskTrigger: Activated for specific tasks, may require user input

**Functions:**

- [**extract_variables**](#openhands.sdk.context.skills.Skill.extract_variables) – Extract variables from the content.
- [**load**](#openhands.sdk.context.skills.Skill.load) – Load a skill from a markdown file with frontmatter.
- [**match_trigger**](#openhands.sdk.context.skills.Skill.match_trigger) – Match a trigger in the message.
- [**requires_user_input**](#openhands.sdk.context.skills.Skill.requires_user_input) – Check if this skill requires user input.

**Attributes:**

- [**PATH_TO_THIRD_PARTY_SKILL_NAME**](#openhands.sdk.context.skills.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME) (<code>[dict](#dict)\[[str](#str), [str](#str)\]</code>) –
- [**content**](#openhands.sdk.context.skills.Skill.content) (<code>[str](#str)</code>) –
- [**inputs**](#openhands.sdk.context.skills.Skill.inputs) (<code>[list](#list)\[[InputMetadata](#openhands.sdk.context.skills.types.InputMetadata)\]</code>) –
- [**mcp_tools**](#openhands.sdk.context.skills.Skill.mcp_tools) (<code>[dict](#dict) | None</code>) –
- [**name**](#openhands.sdk.context.skills.Skill.name) (<code>[str](#str)</code>) –
- [**source**](#openhands.sdk.context.skills.Skill.source) (<code>[str](#str) | None</code>) –
- [**trigger**](#openhands.sdk.context.skills.Skill.trigger) (<code>[TriggerType](#openhands.sdk.context.skills.skill.TriggerType) | None</code>) –

##### `openhands.sdk.context.skills.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME`

```python
PATH_TO_THIRD_PARTY_SKILL_NAME: dict[str, str] = {'.cursorrules': 'cursorrules', 'agents.md': 'agents', 'agent.md': 'agents'}
```

##### `openhands.sdk.context.skills.Skill.content`

```python
content: str
```

##### `openhands.sdk.context.skills.Skill.extract_variables`

```python
extract_variables(content)
```

Extract variables from the content.

Variables are in the format ${variable_name}.

##### `openhands.sdk.context.skills.Skill.inputs`

```python
inputs: list[InputMetadata] = Field(default_factory=list, description='Input metadata for the skill (task skills only)')
```

##### `openhands.sdk.context.skills.Skill.load`

```python
load(path, skill_dir=None, file_content=None)
```

Load a skill from a markdown file with frontmatter.

The agent's name is derived from its path relative to the skill_dir.

##### `openhands.sdk.context.skills.Skill.match_trigger`

```python
match_trigger(message)
```

Match a trigger in the message.

Returns the first trigger that matches the message, or None if no match.
Only applies to KeywordTrigger and TaskTrigger types.

##### `openhands.sdk.context.skills.Skill.mcp_tools`

```python
mcp_tools: dict | None = Field(default=None, description='MCP tools configuration for the skill (repo skills only). It should conform to the MCPConfig schema: https://gofastmcp.com/clients/client#configuration-format')
```

##### `openhands.sdk.context.skills.Skill.name`

```python
name: str
```

##### `openhands.sdk.context.skills.Skill.requires_user_input`

```python
requires_user_input()
```

Check if this skill requires user input.

Returns True if the content contains variables in the format ${variable_name}.

##### `openhands.sdk.context.skills.Skill.source`

```python
source: str | None = Field(default=None, description='The source path or identifier of the skill. When it is None, it is treated as a programmatically defined skill.')
```

##### `openhands.sdk.context.skills.Skill.trigger`

```python
trigger: TriggerType | None
```

#### `openhands.sdk.context.skills.SkillKnowledge`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Represents knowledge from a triggered skill.

**Attributes:**

- [**content**](#openhands.sdk.context.skills.SkillKnowledge.content) (<code>[str](#str)</code>) –
- [**name**](#openhands.sdk.context.skills.SkillKnowledge.name) (<code>[str](#str)</code>) –
- [**trigger**](#openhands.sdk.context.skills.SkillKnowledge.trigger) (<code>[str](#str)</code>) –

##### `openhands.sdk.context.skills.SkillKnowledge.content`

```python
content: str = Field(description='The actual content/knowledge from the skill')
```

##### `openhands.sdk.context.skills.SkillKnowledge.name`

```python
name: str = Field(description='The name of the skill that was triggered')
```

##### `openhands.sdk.context.skills.SkillKnowledge.trigger`

```python
trigger: str = Field(description='The word that triggered this skill')
```

#### `openhands.sdk.context.skills.SkillValidationError`

```python
SkillValidationError(message='Skill validation failed')
```

Bases: <code>[SkillError](#openhands.sdk.context.skills.exceptions.SkillError)</code>

Raised when there's a validation error in skill metadata.

#### `openhands.sdk.context.skills.TaskTrigger`

Bases: <code>[BaseTrigger](#openhands.sdk.context.skills.trigger.BaseTrigger)</code>

Trigger for task-specific skills.

These skills are activated for specific task types and can modify prompts.

**Attributes:**

- [**triggers**](#openhands.sdk.context.skills.TaskTrigger.triggers) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.context.skills.TaskTrigger.type) (<code>[Literal](#typing.Literal)['task']</code>) –

##### `openhands.sdk.context.skills.TaskTrigger.triggers`

```python
triggers: list[str]
```

##### `openhands.sdk.context.skills.TaskTrigger.type`

```python
type: Literal['task'] = 'task'
```

#### `openhands.sdk.context.skills.exceptions`

**Classes:**

- [**SkillError**](#openhands.sdk.context.skills.exceptions.SkillError) – Base exception for all skill errors.
- [**SkillValidationError**](#openhands.sdk.context.skills.exceptions.SkillValidationError) – Raised when there's a validation error in skill metadata.

##### `openhands.sdk.context.skills.exceptions.SkillError`

Bases: <code>[Exception](#Exception)</code>

Base exception for all skill errors.

##### `openhands.sdk.context.skills.exceptions.SkillValidationError`

```python
SkillValidationError(message='Skill validation failed')
```

Bases: <code>[SkillError](#openhands.sdk.context.skills.exceptions.SkillError)</code>

Raised when there's a validation error in skill metadata.

#### `openhands.sdk.context.skills.load_skills_from_dir`

```python
load_skills_from_dir(skill_dir)
```

Load all skills from the given directory.

Note, legacy repo instructions will not be loaded here.

**Parameters:**

- **skill_dir** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the skills directory (e.g. .openhands/skills)

**Returns:**

- <code>[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]</code> – Tuple of (repo_skills, knowledge_skills) dictionaries.
- <code>[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]</code> – repo_skills have trigger=None, knowledge_skills have KeywordTrigger
- <code>[tuple](#tuple)\[[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\], [dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]\]</code> – or TaskTrigger.

#### `openhands.sdk.context.skills.skill`

**Classes:**

- [**Skill**](#openhands.sdk.context.skills.skill.Skill) – A skill provides specialized knowledge or functionality.

**Functions:**

- [**load_skills_from_dir**](#openhands.sdk.context.skills.skill.load_skills_from_dir) – Load all skills from the given directory.

**Attributes:**

- [**TriggerType**](#openhands.sdk.context.skills.skill.TriggerType) –
- [**logger**](#openhands.sdk.context.skills.skill.logger) –

##### `openhands.sdk.context.skills.skill.Skill`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

A skill provides specialized knowledge or functionality.

Skills use triggers to determine when they should be activated:

- None: Always active, for repository-specific guidelines
- KeywordTrigger: Activated when keywords appear in user messages
- TaskTrigger: Activated for specific tasks, may require user input

**Functions:**

- [**extract_variables**](#openhands.sdk.context.skills.skill.Skill.extract_variables) – Extract variables from the content.
- [**load**](#openhands.sdk.context.skills.skill.Skill.load) – Load a skill from a markdown file with frontmatter.
- [**match_trigger**](#openhands.sdk.context.skills.skill.Skill.match_trigger) – Match a trigger in the message.
- [**requires_user_input**](#openhands.sdk.context.skills.skill.Skill.requires_user_input) – Check if this skill requires user input.

**Attributes:**

- [**PATH_TO_THIRD_PARTY_SKILL_NAME**](#openhands.sdk.context.skills.skill.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME) (<code>[dict](#dict)\[[str](#str), [str](#str)\]</code>) –
- [**content**](#openhands.sdk.context.skills.skill.Skill.content) (<code>[str](#str)</code>) –
- [**inputs**](#openhands.sdk.context.skills.skill.Skill.inputs) (<code>[list](#list)\[[InputMetadata](#openhands.sdk.context.skills.types.InputMetadata)\]</code>) –
- [**mcp_tools**](#openhands.sdk.context.skills.skill.Skill.mcp_tools) (<code>[dict](#dict) | None</code>) –
- [**name**](#openhands.sdk.context.skills.skill.Skill.name) (<code>[str](#str)</code>) –
- [**source**](#openhands.sdk.context.skills.skill.Skill.source) (<code>[str](#str) | None</code>) –
- [**trigger**](#openhands.sdk.context.skills.skill.Skill.trigger) (<code>[TriggerType](#openhands.sdk.context.skills.skill.TriggerType) | None</code>) –

###### `openhands.sdk.context.skills.skill.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME`

```python
PATH_TO_THIRD_PARTY_SKILL_NAME: dict[str, str] = {'.cursorrules': 'cursorrules', 'agents.md': 'agents', 'agent.md': 'agents'}
```

###### `openhands.sdk.context.skills.skill.Skill.content`

```python
content: str
```

###### `openhands.sdk.context.skills.skill.Skill.extract_variables`

```python
extract_variables(content)
```

Extract variables from the content.

Variables are in the format ${variable_name}.

###### `openhands.sdk.context.skills.skill.Skill.inputs`

```python
inputs: list[InputMetadata] = Field(default_factory=list, description='Input metadata for the skill (task skills only)')
```

###### `openhands.sdk.context.skills.skill.Skill.load`

```python
load(path, skill_dir=None, file_content=None)
```

Load a skill from a markdown file with frontmatter.

The agent's name is derived from its path relative to the skill_dir.

###### `openhands.sdk.context.skills.skill.Skill.match_trigger`

```python
match_trigger(message)
```

Match a trigger in the message.

Returns the first trigger that matches the message, or None if no match.
Only applies to KeywordTrigger and TaskTrigger types.

###### `openhands.sdk.context.skills.skill.Skill.mcp_tools`

```python
mcp_tools: dict | None = Field(default=None, description='MCP tools configuration for the skill (repo skills only). It should conform to the MCPConfig schema: https://gofastmcp.com/clients/client#configuration-format')
```

###### `openhands.sdk.context.skills.skill.Skill.name`

```python
name: str
```

###### `openhands.sdk.context.skills.skill.Skill.requires_user_input`

```python
requires_user_input()
```

Check if this skill requires user input.

Returns True if the content contains variables in the format ${variable_name}.

###### `openhands.sdk.context.skills.skill.Skill.source`

```python
source: str | None = Field(default=None, description='The source path or identifier of the skill. When it is None, it is treated as a programmatically defined skill.')
```

###### `openhands.sdk.context.skills.skill.Skill.trigger`

```python
trigger: TriggerType | None
```

##### `openhands.sdk.context.skills.skill.TriggerType`

```python
TriggerType = Annotated[KeywordTrigger | TaskTrigger, Field(discriminator='type')]
```

##### `openhands.sdk.context.skills.skill.load_skills_from_dir`

```python
load_skills_from_dir(skill_dir)
```

Load all skills from the given directory.

Note, legacy repo instructions will not be loaded here.

**Parameters:**

- **skill_dir** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the skills directory (e.g. .openhands/skills)

**Returns:**

- <code>[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]</code> – Tuple of (repo_skills, knowledge_skills) dictionaries.
- <code>[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]</code> – repo_skills have trigger=None, knowledge_skills have KeywordTrigger
- <code>[tuple](#tuple)\[[dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\], [dict](#dict)\[[str](#str), [Skill](#openhands.sdk.context.skills.skill.Skill)\]\]</code> – or TaskTrigger.

##### `openhands.sdk.context.skills.skill.logger`

```python
logger = get_logger(__name__)
```

#### `openhands.sdk.context.skills.trigger`

Trigger types for skills.

This module defines different trigger types that determine when a skill
should be activated.

**Classes:**

- [**BaseTrigger**](#openhands.sdk.context.skills.trigger.BaseTrigger) – Base class for all trigger types.
- [**KeywordTrigger**](#openhands.sdk.context.skills.trigger.KeywordTrigger) – Trigger for keyword-based skills.
- [**TaskTrigger**](#openhands.sdk.context.skills.trigger.TaskTrigger) – Trigger for task-specific skills.

##### `openhands.sdk.context.skills.trigger.BaseTrigger`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>, <code>[ABC](#abc.ABC)</code>

Base class for all trigger types.

##### `openhands.sdk.context.skills.trigger.KeywordTrigger`

Bases: <code>[BaseTrigger](#openhands.sdk.context.skills.trigger.BaseTrigger)</code>

Trigger for keyword-based skills.

These skills are activated when specific keywords appear in the user's query.

**Attributes:**

- [**keywords**](#openhands.sdk.context.skills.trigger.KeywordTrigger.keywords) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.context.skills.trigger.KeywordTrigger.type) (<code>[Literal](#typing.Literal)['keyword']</code>) –

###### `openhands.sdk.context.skills.trigger.KeywordTrigger.keywords`

```python
keywords: list[str]
```

###### `openhands.sdk.context.skills.trigger.KeywordTrigger.type`

```python
type: Literal['keyword'] = 'keyword'
```

##### `openhands.sdk.context.skills.trigger.TaskTrigger`

Bases: <code>[BaseTrigger](#openhands.sdk.context.skills.trigger.BaseTrigger)</code>

Trigger for task-specific skills.

These skills are activated for specific task types and can modify prompts.

**Attributes:**

- [**triggers**](#openhands.sdk.context.skills.trigger.TaskTrigger.triggers) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.context.skills.trigger.TaskTrigger.type) (<code>[Literal](#typing.Literal)['task']</code>) –

###### `openhands.sdk.context.skills.trigger.TaskTrigger.triggers`

```python
triggers: list[str]
```

###### `openhands.sdk.context.skills.trigger.TaskTrigger.type`

```python
type: Literal['task'] = 'task'
```

#### `openhands.sdk.context.skills.types`

**Classes:**

- [**InputMetadata**](#openhands.sdk.context.skills.types.InputMetadata) – Metadata for task skill inputs.
- [**SkillContentResponse**](#openhands.sdk.context.skills.types.SkillContentResponse) – Response model for individual skill content endpoint.
- [**SkillKnowledge**](#openhands.sdk.context.skills.types.SkillKnowledge) – Represents knowledge from a triggered skill.
- [**SkillResponse**](#openhands.sdk.context.skills.types.SkillResponse) – Response model for skills endpoint.

##### `openhands.sdk.context.skills.types.InputMetadata`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Metadata for task skill inputs.

**Attributes:**

- [**description**](#openhands.sdk.context.skills.types.InputMetadata.description) (<code>[str](#str)</code>) –
- [**name**](#openhands.sdk.context.skills.types.InputMetadata.name) (<code>[str](#str)</code>) –

###### `openhands.sdk.context.skills.types.InputMetadata.description`

```python
description: str = Field(description='Description of the input parameter')
```

###### `openhands.sdk.context.skills.types.InputMetadata.name`

```python
name: str = Field(description='Name of the input parameter')
```

##### `openhands.sdk.context.skills.types.SkillContentResponse`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Response model for individual skill content endpoint.

**Attributes:**

- [**content**](#openhands.sdk.context.skills.types.SkillContentResponse.content) (<code>[str](#str)</code>) –
- [**git_provider**](#openhands.sdk.context.skills.types.SkillContentResponse.git_provider) (<code>[str](#str) | None</code>) –
- [**path**](#openhands.sdk.context.skills.types.SkillContentResponse.path) (<code>[str](#str)</code>) –
- [**triggers**](#openhands.sdk.context.skills.types.SkillContentResponse.triggers) (<code>[list](#list)\[[str](#str)\]</code>) –

###### `openhands.sdk.context.skills.types.SkillContentResponse.content`

```python
content: str = Field(description='The full content of the skill')
```

###### `openhands.sdk.context.skills.types.SkillContentResponse.git_provider`

```python
git_provider: str | None = Field(None, description='Git provider if the skill is sourced from a Git repository')
```

###### `openhands.sdk.context.skills.types.SkillContentResponse.path`

```python
path: str = Field(description='The path or identifier of the skill')
```

###### `openhands.sdk.context.skills.types.SkillContentResponse.triggers`

```python
triggers: list[str] = Field(description='List of triggers associated with the skill')
```

##### `openhands.sdk.context.skills.types.SkillKnowledge`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Represents knowledge from a triggered skill.

**Attributes:**

- [**content**](#openhands.sdk.context.skills.types.SkillKnowledge.content) (<code>[str](#str)</code>) –
- [**name**](#openhands.sdk.context.skills.types.SkillKnowledge.name) (<code>[str](#str)</code>) –
- [**trigger**](#openhands.sdk.context.skills.types.SkillKnowledge.trigger) (<code>[str](#str)</code>) –

###### `openhands.sdk.context.skills.types.SkillKnowledge.content`

```python
content: str = Field(description='The actual content/knowledge from the skill')
```

###### `openhands.sdk.context.skills.types.SkillKnowledge.name`

```python
name: str = Field(description='The name of the skill that was triggered')
```

###### `openhands.sdk.context.skills.types.SkillKnowledge.trigger`

```python
trigger: str = Field(description='The word that triggered this skill')
```

##### `openhands.sdk.context.skills.types.SkillResponse`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Response model for skills endpoint.

Note: This model only includes basic metadata that can be determined
without parsing skill content. Use the separate content API
to get detailed skill information.

**Attributes:**

- [**created_at**](#openhands.sdk.context.skills.types.SkillResponse.created_at) (<code>[datetime](#datetime.datetime)</code>) –
- [**name**](#openhands.sdk.context.skills.types.SkillResponse.name) (<code>[str](#str)</code>) –
- [**path**](#openhands.sdk.context.skills.types.SkillResponse.path) (<code>[str](#str)</code>) –

###### `openhands.sdk.context.skills.types.SkillResponse.created_at`

```python
created_at: datetime = Field(default_factory=(lambda: datetime.now(UTC)), description='Timestamp when the skill was created')
```

###### `openhands.sdk.context.skills.types.SkillResponse.name`

```python
name: str = Field(description='The name of the skill')
```

###### `openhands.sdk.context.skills.types.SkillResponse.path`

```python
path: str = Field(description='The path or identifier of the skill')
```

### `openhands.sdk.context.view`

**Classes:**

- [**View**](#openhands.sdk.context.view.View) – Linearly ordered view of events.

**Attributes:**

- [**logger**](#openhands.sdk.context.view.logger) –

#### `openhands.sdk.context.view.View`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Linearly ordered view of events.

Produced by a condenser to indicate the included events are ready to process as LLM
input. Also contains fields with information from the condensation process to aid
in deciding whether further condensation is needed.

**Functions:**

- [**filter_unmatched_tool_calls**](#openhands.sdk.context.view.View.filter_unmatched_tool_calls) – Filter out unmatched tool call events.
- [**from_events**](#openhands.sdk.context.view.View.from_events) – Create a view from a list of events, respecting the semantics of any

**Attributes:**

- [**condensations**](#openhands.sdk.context.view.View.condensations) (<code>[list](#list)\[[Condensation](#openhands.sdk.event.Condensation)\]</code>) – A list of condensations that were processed to produce the view.
- [**events**](#openhands.sdk.context.view.View.events) (<code>[list](#list)\[[LLMConvertibleEvent](#openhands.sdk.event.LLMConvertibleEvent)\]</code>) –
- [**most_recent_condensation**](#openhands.sdk.context.view.View.most_recent_condensation) (<code>[Condensation](#openhands.sdk.event.Condensation) | None</code>) – Return the most recent condensation, or None if no condensations exist.
- [**summary_event**](#openhands.sdk.context.view.View.summary_event) (<code>[CondensationSummaryEvent](#openhands.sdk.event.CondensationSummaryEvent) | None</code>) – Return the summary event, or None if no summary exists.
- [**summary_event_index**](#openhands.sdk.context.view.View.summary_event_index) (<code>[int](#int) | None</code>) – Return the index of the summary event, or None if no summary exists.
- [**unhandled_condensation_request**](#openhands.sdk.context.view.View.unhandled_condensation_request) (<code>[bool](#bool)</code>) – Whether there is an unhandled condensation request in the view.

##### `openhands.sdk.context.view.View.condensations`

```python
condensations: list[Condensation] = []
```

A list of condensations that were processed to produce the view.

##### `openhands.sdk.context.view.View.events`

```python
events: list[LLMConvertibleEvent]
```

##### `openhands.sdk.context.view.View.filter_unmatched_tool_calls`

```python
filter_unmatched_tool_calls(events)
```

Filter out unmatched tool call events.

Removes ActionEvents and ObservationEvents that have tool_call_ids
but don't have matching pairs.

##### `openhands.sdk.context.view.View.from_events`

```python
from_events(events)
```

Create a view from a list of events, respecting the semantics of any
condensation events.

##### `openhands.sdk.context.view.View.most_recent_condensation`

```python
most_recent_condensation: Condensation | None
```

Return the most recent condensation, or None if no condensations exist.

##### `openhands.sdk.context.view.View.summary_event`

```python
summary_event: CondensationSummaryEvent | None
```

Return the summary event, or None if no summary exists.

##### `openhands.sdk.context.view.View.summary_event_index`

```python
summary_event_index: int | None
```

Return the index of the summary event, or None if no summary exists.

##### `openhands.sdk.context.view.View.unhandled_condensation_request`

```python
unhandled_condensation_request: bool = False
```

Whether there is an unhandled condensation request in the view.

#### `openhands.sdk.context.view.logger`

```python
logger = getLogger(__name__)
```
