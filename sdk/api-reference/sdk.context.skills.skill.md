---
title: openhands.sdk.context.skills.skill
description: API reference for openhands.sdk.context.skills.skill
---

# openhands.sdk.context.skills.skill module

<a id="module-openhands.sdk.context.skills.skill"></a>

### *class* openhands.sdk.context.skills.skill.Skill(\*, name: str, content: str, trigger: ~typing.Annotated[~openhands.sdk.context.skills.trigger.KeywordTrigger | ~openhands.sdk.context.skills.trigger.TaskTrigger, FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None, source: str | None = None, mcp_tools: dict | None = None, inputs: list[~openhands.sdk.context.skills.types.InputMetadata] = `<factory>`)

Bases: `BaseModel`

A skill provides specialized knowledge or functionality.

Skills use triggers to determine when they should be activated:
- None: Always active, for repository-specific guidelines
- KeywordTrigger: Activated when keywords appear in user messages
- TaskTrigger: Activated for specific tasks, may require user input

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### trigger *: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[KeywordTrigger](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.KeywordTrigger) | [TaskTrigger](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.trigger.md#openhands.sdk.context.skills.trigger.TaskTrigger), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | [None](https://docs.python.org/3/library/constants.html#None)*

#### source *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### mcp_tools *: [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [None](https://docs.python.org/3/library/constants.html#None)*

#### inputs *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[InputMetadata](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.types.md#openhands.sdk.context.skills.types.InputMetadata)]*

#### PATH_TO_THIRD_PARTY_SKILL_NAME  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]]*  = \{'.cursorrules': 'cursorrules', 'agent.md': 'agents', 'agents.md': 'agents'\}*

#### *classmethod* load(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), skill_dir: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None, file_content: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [Skill](#openhands.sdk.context.skills.skill.Skill)

Load a skill from a markdown file with frontmatter.

The agent’s name is derived from its path relative to the skill_dir.

#### match_trigger(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

Match a trigger in the message.

Returns the first trigger that matches the message, or None if no match.
Only applies to KeywordTrigger and TaskTrigger types.

#### extract_variables(content: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Extract variables from the content.

Variables are in the format ${variable_name}.

#### requires_user_input() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if this skill requires user input.

Returns True if the content contains variables in the format ${variable_name}.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### openhands.sdk.context.skills.skill.load_skills_from_dir(skill_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Skill](#openhands.sdk.context.skills.skill.Skill)], [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Skill](#openhands.sdk.context.skills.skill.Skill)]]

Load all skills from the given directory.

Note, legacy repo instructions will not be loaded here.

* **Parameters:**
  **skill_dir** – Path to the skills directory (e.g. .openhands/skills)
* **Returns:**
  Tuple of (repo_skills, knowledge_skills) dictionaries.
  repo_skills have trigger=None, knowledge_skills have KeywordTrigger
  or TaskTrigger.
