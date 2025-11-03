---
title: openhands.sdk.context.agent_context
description: API reference for openhands.sdk.context.agent_context
---

# openhands.sdk.context.agent_context module

<a id="module-openhands.sdk.context.agent_context"></a>

### *class* openhands.sdk.context.agent_context.AgentContext(\*, skills: list[~openhands.sdk.context.skills.skill.Skill] = `<factory>`, system_message_suffix: str | None = None, user_message_suffix: str | None = None)

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

#### skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Skill](https://github.com/OpenHands/software-agent-sdk/sdk.context.skills.skill.md#openhands.sdk.context.skills.skill.Skill)]*

#### system_message_suffix *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### user_message_suffix *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

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
