---
title: openhands.sdk.context.skills
description: API reference for openhands.sdk.context.skills
---

# openhands.sdk.context.skills package

<a id="module-openhands.sdk.context.skills"></a>

### *class* openhands.sdk.context.skills.Skill

**Parameters:**

- `\*`
- `name: str`
- `content: str`
- `trigger: ~typing.Annotated[~openhands.sdk.context.skills.trigger.KeywordTrigger | ~openhands.sdk.context.skills.trigger.TaskTrigger, FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None`
- `source: str | None = None`
- `mcp_tools: dict | None = None`
- `inputs: list[~openhands.sdk.context.skills.types.InputMetadata] = `<factory>``


Bases: `BaseModel`

A skill provides specialized knowledge or functionality.

Skills use triggers to determine when they should be activated:
- None: Always active, for repository-specific guidelines
- KeywordTrigger: Activated when keywords appear in user messages
- TaskTrigger: Activated for specific tasks, may require user input

#### PATH_TO_THIRD_PARTY_SKILL_NAME  : [ClassVar]

**Parameters:**

- `https://docs.python.org/3/library/typing.html#typing.ClassVar)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str`


#### extract_variables

**Parameters:**

- `content: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str`


Extract variables from the content.

Variables are in the format ${variable_name}.

#### *classmethod* load

**Parameters:**

- `path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)`
- `skill_dir: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `file_content: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill`


Load a skill from a markdown file with frontmatter.

The agent’s name is derived from its path relative to the skill_dir.

#### match_trigger

**Parameters:**

- `message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None`


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

#### trigger *: [Annotated]

**Parameters:**

- `https://docs.python.org/3/library/typing.html#typing.Annotated)[[KeywordTrigger](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger) | [TaskTrigger](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger)`
- `FieldInfo(annotation=NoneType, required=True, discriminator='type')] | [None](https://docs.python.org/3/library/constants.html#None`


#### source *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### mcp_tools *: [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [None](https://docs.python.org/3/library/constants.html#None)*

#### inputs *: [list]

**Parameters:**

- `https://docs.python.org/3/library/stdtypes.html#list)[[InputMetadata](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata`


### *class* openhands.sdk.context.skills.BaseTrigger

Bases: `BaseModel`, [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for all trigger types.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.context.skills.KeywordTrigger

**Parameters:**

- `type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['keyword'] = 'keyword'`
- `keywords: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`


Bases: [`BaseTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.BaseTrigger)

Trigger for keyword-based skills.

These skills are activated when specific keywords appear in the user’s query.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### type *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['keyword']*

#### keywords *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* openhands.sdk.context.skills.TaskTrigger

**Parameters:**

- `type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['task'] = 'task'`
- `triggers: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`


Bases: [`BaseTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.BaseTrigger)

Trigger for task-specific skills.

These skills are activated for specific task types and can modify prompts.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### type *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['task']*

#### triggers *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* openhands.sdk.context.skills.SkillKnowledge

**Parameters:**

- `name: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `trigger: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `content: [str](https://docs.python.org/3/library/stdtypes.html#str)`


Bases: `BaseModel`

Represents knowledge from a triggered skill.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### trigger *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### openhands.sdk.context.skills.load_skills_from_dir(skill_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)], [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)]]

Load all skills from the given directory.

Note, legacy repo instructions will not be loaded here.

* **Parameters:**
  **skill_dir** – Path to the skills directory (e.g. .openhands/skills)
* **Returns:**
  Tuple of (repo_skills, knowledge_skills) dictionaries.
  repo_skills have trigger=None, knowledge_skills have KeywordTrigger
  or TaskTrigger.

### *exception* openhands.sdk.context.skills.SkillValidationError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Skill validation failed')

Bases: [`SkillError`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md#openhands.sdk.context.skills.exceptions.SkillError)

Raised when there’s a validation error in skill metadata.

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Skill validation failed') → [None](https://docs.python.org/3/library/constants.html#None)

## Submodules

* [openhands.sdk.context.skills.exceptions module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md)
  * [`SkillError`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md#openhands.sdk.context.skills.exceptions.SkillError)
  * [`SkillValidationError`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md#openhands.sdk.context.skills.exceptions.SkillValidationError)
    * [`SkillValidationError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.exceptions.md#openhands.sdk.context.skills.exceptions.SkillValidationError.__init__)
* [openhands.sdk.context.skills.skill module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md)
  * [`Skill`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)
    * [`Skill.name`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.name)
    * [`Skill.content`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.content)
    * [`Skill.trigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.trigger)
    * [`Skill.source`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.source)
    * [`Skill.mcp_tools`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.mcp_tools)
    * [`Skill.inputs`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.inputs)
    * [`Skill.PATH_TO_THIRD_PARTY_SKILL_NAME`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.PATH_TO_THIRD_PARTY_SKILL_NAME)
    * [`Skill.load()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.load)
    * [`Skill.match_trigger()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.match_trigger)
    * [`Skill.extract_variables()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.extract_variables)
    * [`Skill.requires_user_input()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.requires_user_input)
    * [`Skill.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill.model_config)
  * [`load_skills_from_dir()`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.load_skills_from_dir)
* [openhands.sdk.context.skills.trigger module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md)
  * [`BaseTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.BaseTrigger)
    * [`BaseTrigger.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.BaseTrigger.model_config)
  * [`KeywordTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger)
    * [`KeywordTrigger.type`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger.type)
    * [`KeywordTrigger.keywords`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger.keywords)
    * [`KeywordTrigger.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger.model_config)
  * [`TaskTrigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger)
    * [`TaskTrigger.type`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger.type)
    * [`TaskTrigger.triggers`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger.triggers)
    * [`TaskTrigger.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger.model_config)
* [openhands.sdk.context.skills.types module](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md)
  * [`InputMetadata`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata)
    * [`InputMetadata.name`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata.name)
    * [`InputMetadata.description`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata.description)
    * [`InputMetadata.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata.model_config)
  * [`SkillKnowledge`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillKnowledge)
    * [`SkillKnowledge.name`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillKnowledge.name)
    * [`SkillKnowledge.trigger`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillKnowledge.trigger)
    * [`SkillKnowledge.content`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillKnowledge.content)
    * [`SkillKnowledge.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillKnowledge.model_config)
  * [`SkillResponse`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillResponse)
    * [`SkillResponse.name`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillResponse.name)
    * [`SkillResponse.path`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillResponse.path)
    * [`SkillResponse.created_at`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillResponse.created_at)
    * [`SkillResponse.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillResponse.model_config)
  * [`SkillContentResponse`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillContentResponse)
    * [`SkillContentResponse.content`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillContentResponse.content)
    * [`SkillContentResponse.path`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillContentResponse.path)
    * [`SkillContentResponse.triggers`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillContentResponse.triggers)
    * [`SkillContentResponse.git_provider`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillContentResponse.git_provider)
    * [`SkillContentResponse.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.SkillContentResponse.model_config)
