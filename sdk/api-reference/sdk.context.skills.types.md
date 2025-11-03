---
title: openhands.sdk.context.skills.types
description: API reference for openhands.sdk.context.skills.types
---

# openhands.sdk.context.skills.types module

<a id="module-openhands.sdk.context.skills.types"></a>

### *class* openhands.sdk.context.skills.types.InputMetadata(, name: [str](https://docs.python.org/3/library/stdtypes.html#str), description: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Metadata for task skill inputs.

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### description *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.context.skills.types.SkillKnowledge(, name: [str](https://docs.python.org/3/library/stdtypes.html#str), trigger: [str](https://docs.python.org/3/library/stdtypes.html#str), content: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Represents knowledge from a triggered skill.

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### trigger *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.context.skills.types.SkillResponse(\*, name: str, path: str, created_at: ~datetime.datetime = <factory>)

Bases: `BaseModel`

Response model for skills endpoint.

Note: This model only includes basic metadata that can be determined
without parsing skill content. Use the separate content API
to get detailed skill information.

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### path *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### created_at *: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)*

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.context.skills.types.SkillContentResponse(, content: [str](https://docs.python.org/3/library/stdtypes.html#str), path: [str](https://docs.python.org/3/library/stdtypes.html#str), triggers: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)], git_provider: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: `BaseModel`

Response model for individual skill content endpoint.

#### content *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### path *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### triggers *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### git_provider *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
