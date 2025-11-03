---
title: openhands.sdk.conversation.secret_source
description: API reference for openhands.sdk.conversation.secret_source
---

# openhands.sdk.conversation.secret_source module

<a id="module-openhands.sdk.conversation.secret_source"></a>

### class openhands.sdk.conversation.secret_source.SecretSource(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LookupSecret', 'StaticSecret'] = 'LookupSecret', description: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Source for a named secret which may be obtained dynamically

#### description : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### abstractmethod get_value() → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

Get the value of a secret in plain text

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### class openhands.sdk.conversation.secret_source.StaticSecret(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['StaticSecret'] = 'StaticSecret', description: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, value: SecretStr)

Bases: [`SecretSource`](#openhands.sdk.conversation.secret_source.SecretSource)

A secret stored locally

#### value : SecretStr

#### get_value()

Get the value of a secret in plain text

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['StaticSecret']

### class openhands.sdk.conversation.secret_source.LookupSecret(kind: ~typing.Literal['LookupSecret'] = 'LookupSecret', description: str | None = None, url: str, headers: dict[str, str] = `<factory>`)

Bases: [`SecretSource`](#openhands.sdk.conversation.secret_source.SecretSource)

A secret looked up from some external url

#### url : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### headers : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]

#### get_value()

Get the value of a secret in plain text

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LookupSecret']
