---
title: openhands.sdk.tool.spec
description: API reference for openhands.sdk.tool.spec
---

# openhands.sdk.tool.spec module

<a id="module-openhands.sdk.tool.spec"></a>

### *class* openhands.sdk.tool.spec.Tool(\*, name: str, params: dict[str, ~typing.Any] = `<factory>`)

Bases: `BaseModel`

Defines a tool to be initialized for the agent.

This is only used in agent-sdk for type schema for server use.

#### name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### params : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

#### classmethod validate_name(v: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Validate that name is not empty.

#### classmethod validate_params(v: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [None](https://docs.python.org/3/library/constants.html#None)) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Convert None params to empty dict.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
