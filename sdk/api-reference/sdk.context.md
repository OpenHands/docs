---
title: openhands.sdk.context
description: API reference for openhands.sdk.context
---

# openhands.sdk.context package

<a id="module-openhands.sdk.context"></a>

### *class* openhands.sdk.context.AgentContext(\*, skills: list[~openhands.sdk.context.skills.skill.Skill] = `<factory>`, system_message_suffix: str | None = None, user_message_suffix: str | None = None)

Bases: `BaseModel`

Central structure for managing prompt extension.

AgentContext unifies all the contextual inputs that shape how the system
extends and interprets user prompts. It combines both static environment
details and dynamic, user-activated extensions from skills.

Specifically, it provides:
- **Repository context / Repo Skills**: Information about the active codebase,

> branches, and repo-specific instructions contributed by repo skills.
- **Runtime context**: Current execution environment (hosts, working
  directory, secrets, date, etc.).
- **Conversation instructions**: Optional task- or channel-specific rules
  that constrain or guide the agent’s behavior across the session.
- **Knowledge Skills**: Extensible components that can be triggered by user input
  to inject knowledge or domain-specific guidance.

Together, these elements make AgentContext the primary container responsible
for assembling, formatting, and injecting all prompt-relevant context into
LLM interactions.

#### get_system_message_suffix() → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

Get the system message with repo skill content and custom suffix.

Custom suffix can typically includes:
- Repository information (repo name, branch name, PR number, etc.)
- Runtime information (e.g., available hosts, current date)
- Conversation instructions (e.g., user preferences, task details)
- Repository-specific instructions (collected from repo skills)

#### get_user_message_suffix(user_message: [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message), skip_skill_names: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent), [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]] | [None](https://docs.python.org/3/library/constants.html#None)

Augment the user’s message with knowledge recalled from skills.

This works by:
- Extracting the text content of the user message
- Matching skill triggers against the query
- Returning formatted knowledge and triggered skill names if relevant skills were triggered

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)]*

#### system_message_suffix *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### user_message_suffix *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

### *class* openhands.sdk.context.Skill(\*, name: str, content: str, trigger: ~typing.Annotated[~openhands.sdk.context.skills.trigger.KeywordTrigger | ~openhands.sdk.context.skills.trigger.TaskTrigger, FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None, source: str | None = None, mcp_tools: dict | None = None, inputs: list[~openhands.sdk.context.skills.types.InputMetadata] = `<factory>`)

Bases: `BaseModel`

A skill provides specialized knowledge or functionality.

Skills use triggers to determine when they should be activated:
- None: Always active, for repository-specific guidelines
- KeywordTrigger: Activated when keywords appear in user messages
- TaskTrigger: Activated for specific tasks, may require user input

#### PATH_TO_THIRD_PARTY_SKILL_NAME  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]]*  = \{'.cursorrules': 'cursorrules', 'agent.md': 'agents', 'agents.md': 'agents'\}*

#### extract_variables(content: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Extract variables from the content.

Variables are in the format ${variable_name}.

#### *classmethod* load(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), skill_dir: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None, file_content: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)

Load a skill from a markdown file with frontmatter.

The agent’s name is derived from its path relative to the skill_dir.

#### match_trigger(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

Match a trigger in the message.

Returns the first trigger that matches the message, or None if no match.
Only applies to KeywordTrigger and TaskTrigger types.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### requires_user_input() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if this skill requires user input.

Returns True if the content contains variables in the format ${variable_name}.

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### trigger *: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[KeywordTrigger](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger) | [TaskTrigger](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | [None](https://docs.python.org/3/library/constants.html#None)*

#### source *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### mcp_tools *: [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [None](https://docs.python.org/3/library/constants.html#None)*

#### inputs *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[InputMetadata](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata)]*

### *class* openhands.sdk.context.BaseTrigger

Bases: `BaseModel`, [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for all trigger types.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.context.KeywordTrigger(, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['keyword'] = 'keyword', keywords: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)])

Bases: [`BaseTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.BaseTrigger)

Trigger for keyword-based skills.

These skills are activated when specific keywords appear in the user’s query.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### type *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['keyword']*

#### keywords *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* openhands.sdk.context.TaskTrigger(, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['task'] = 'task', triggers: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)])

Bases: [`BaseTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.BaseTrigger)

Trigger for task-specific skills.

These skills are activated for specific task types and can modify prompts.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### type *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['task']*

#### triggers *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* openhands.sdk.context.SkillKnowledge(, name: [str](https://docs.python.org/3/library/stdtypes.html#str), trigger: [str](https://docs.python.org/3/library/stdtypes.html#str), content: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Represents knowledge from a triggered skill.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### trigger *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### openhands.sdk.context.load_skills_from_dir(skill_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)], [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)]]

Load all skills from the given directory.

Note, legacy repo instructions will not be loaded here.

* **Parameters:**
  **skill_dir** – Path to the skills directory (e.g. .openhands/skills)
* **Returns:**
  Tuple of (repo_skills, knowledge_skills) dictionaries.
  repo_skills have trigger=None, knowledge_skills have KeywordTrigger
  or TaskTrigger.

### openhands.sdk.context.render_template(prompt_dir: [str](https://docs.python.org/3/library/stdtypes.html#str), template_name: [str](https://docs.python.org/3/library/stdtypes.html#str), \*\*ctx) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Render a Jinja2 template.

* **Parameters:**
  * **prompt_dir** – The base directory for relative template paths.
  * **template_name** – The template filename. Can be either:
    - A relative filename (e.g., “system_prompt.j2”) loaded from prompt_dir
    - An absolute path (e.g., “/path/to/custom_prompt.j2”)
  * **\*\*ctx** – Template context variables.
* **Returns:**
  Rendered template string.
* **Raises:**
  [**FileNotFoundError**](https://docs.python.org/3/library/exceptions.html#FileNotFoundError) – If the template file cannot be found.

### *exception* openhands.sdk.context.SkillValidationError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Skill validation failed')

Bases: [`SkillError`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md#openhands.sdk.context.skills.exceptions.SkillError)

Raised when there’s a validation error in skill metadata.

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Skill validation failed') → [None](https://docs.python.org/3/library/constants.html#None)

## Subpackages

* [openhands.sdk.context.condenser package](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md)
  * [`CondenserBase`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.CondenserBase)
    * [`CondenserBase.condense()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.CondenserBase.condense)
    * [`CondenserBase.handles_condensation_requests()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.CondenserBase.handles_condensation_requests)
    * [`CondenserBase.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.CondenserBase.model_config)
  * [`RollingCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.RollingCondenser)
    * [`RollingCondenser.condense()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.RollingCondenser.condense)
    * [`RollingCondenser.get_condensation()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.RollingCondenser.get_condensation)
    * [`RollingCondenser.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.RollingCondenser.model_config)
    * [`RollingCondenser.should_condense()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.RollingCondenser.should_condense)
  * [`NoOpCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.NoOpCondenser)
    * [`NoOpCondenser.condense()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.NoOpCondenser.condense)
    * [`NoOpCondenser.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.NoOpCondenser.model_config)
    * [`NoOpCondenser.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.NoOpCondenser.kind)
  * [`PipelineCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.PipelineCondenser)
    * [`PipelineCondenser.condense()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.PipelineCondenser.condense)
    * [`PipelineCondenser.handles_condensation_requests()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.PipelineCondenser.handles_condensation_requests)
    * [`PipelineCondenser.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.PipelineCondenser.model_config)
    * [`PipelineCondenser.condensers`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.PipelineCondenser.condensers)
    * [`PipelineCondenser.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.PipelineCondenser.kind)
  * [`LLMSummarizingCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser)
    * [`LLMSummarizingCondenser.get_condensation()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.get_condensation)
    * [`LLMSummarizingCondenser.handles_condensation_requests()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.handles_condensation_requests)
    * [`LLMSummarizingCondenser.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.model_config)
    * [`LLMSummarizingCondenser.should_condense()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.should_condense)
    * [`LLMSummarizingCondenser.validate_keep_first_vs_max_size()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.validate_keep_first_vs_max_size)
    * [`LLMSummarizingCondenser.llm`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.llm)
    * [`LLMSummarizingCondenser.max_size`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.max_size)
    * [`LLMSummarizingCondenser.keep_first`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.keep_first)
    * [`LLMSummarizingCondenser.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.LLMSummarizingCondenser.kind)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#submodules)
    * [openhands.sdk.context.condenser.base module](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md)
      * [`CondenserBase`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.CondenserBase)
      * [`PipelinableCondenserBase`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.PipelinableCondenserBase)
      * [`RollingCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.RollingCondenser)
    * [openhands.sdk.context.condenser.llm_summarizing_condenser module](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.llm_summarizing_condenser.md)
      * [`LLMSummarizingCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.llm_summarizing_condenser.md#openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser)
    * [openhands.sdk.context.condenser.no_op_condenser module](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.no_op_condenser.md)
      * [`NoOpCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.no_op_condenser.md#openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser)
    * [openhands.sdk.context.condenser.pipeline_condenser module](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.pipeline_condenser.md)
      * [`PipelineCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.pipeline_condenser.md#openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser)
* [openhands.sdk.context.prompts package](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.md)
  * [`render_template()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.md#openhands.sdk.context.prompts.render_template)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.md#submodules)
    * [openhands.sdk.context.prompts.prompt module](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.prompt.md)
      * [`refine()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.prompt.md#openhands.sdk.context.prompts.prompt.refine)
      * [`render_template()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.prompts.prompt.md#openhands.sdk.context.prompts.prompt.render_template)
* [openhands.sdk.context.skills package](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md)
  * [`Skill`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill)
    * [`Skill.PATH_TO_THIRD_PARTY_SKILL_NAME`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME)
    * [`Skill.extract_variables()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.extract_variables)
    * [`Skill.load()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.load)
    * [`Skill.match_trigger()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.match_trigger)
    * [`Skill.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.model_config)
    * [`Skill.requires_user_input()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.requires_user_input)
    * [`Skill.name`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.name)
    * [`Skill.content`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.content)
    * [`Skill.trigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.trigger)
    * [`Skill.source`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.source)
    * [`Skill.mcp_tools`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.mcp_tools)
    * [`Skill.inputs`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.Skill.inputs)
  * [`BaseTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.BaseTrigger)
    * [`BaseTrigger.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.BaseTrigger.model_config)
  * [`KeywordTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.KeywordTrigger)
    * [`KeywordTrigger.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.KeywordTrigger.model_config)
    * [`KeywordTrigger.type`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.KeywordTrigger.type)
    * [`KeywordTrigger.keywords`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.KeywordTrigger.keywords)
  * [`TaskTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.TaskTrigger)
    * [`TaskTrigger.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.TaskTrigger.model_config)
    * [`TaskTrigger.type`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.TaskTrigger.type)
    * [`TaskTrigger.triggers`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.TaskTrigger.triggers)
  * [`SkillKnowledge`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.SkillKnowledge)
    * [`SkillKnowledge.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.SkillKnowledge.model_config)
    * [`SkillKnowledge.name`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.SkillKnowledge.name)
    * [`SkillKnowledge.trigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.SkillKnowledge.trigger)
    * [`SkillKnowledge.content`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.SkillKnowledge.content)
  * [`load_skills_from_dir()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.load_skills_from_dir)
  * [`SkillValidationError`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.SkillValidationError)
    * [`SkillValidationError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#openhands.sdk.context.skills.SkillValidationError.__init__)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.md#submodules)
    * [openhands.sdk.context.skills.exceptions module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md)
      * [`SkillError`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md#openhands.sdk.context.skills.exceptions.SkillError)
      * [`SkillValidationError`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md#openhands.sdk.context.skills.exceptions.SkillValidationError)
    * [openhands.sdk.context.skills.skill module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md)
      * [`Skill`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)
      * [`load_skills_from_dir()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.load_skills_from_dir)
    * [openhands.sdk.context.skills.trigger module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md)
      * [`BaseTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.BaseTrigger)
      * [`KeywordTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger)
      * [`TaskTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger)
    * [openhands.sdk.context.skills.types module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md)
      * [`InputMetadata`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata)
      * [`SkillKnowledge`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillKnowledge)
      * [`SkillResponse`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillResponse)
      * [`SkillContentResponse`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillContentResponse)

## Submodules

* [openhands.sdk.context.agent_context module](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md)
  * [`AgentContext`](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext)
    * [`AgentContext.skills`](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext.skills)
    * [`AgentContext.system_message_suffix`](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext.system_message_suffix)
    * [`AgentContext.user_message_suffix`](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext.user_message_suffix)
    * [`AgentContext.get_system_message_suffix()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext.get_system_message_suffix)
    * [`AgentContext.get_user_message_suffix()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext.get_user_message_suffix)
    * [`AgentContext.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext.model_config)
* [openhands.sdk.context.view module](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md)
  * [`View`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View)
    * [`View.events`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.events)
    * [`View.unhandled_condensation_request`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.unhandled_condensation_request)
    * [`View.condensations`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.condensations)
    * [`View.most_recent_condensation`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.most_recent_condensation)
    * [`View.summary_event_index`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.summary_event_index)
    * [`View.summary_event`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.summary_event)
    * [`View.filter_unmatched_tool_calls()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.filter_unmatched_tool_calls)
    * [`View.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.model_config)
    * [`View.from_events()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View.from_events)
