---
title: openhands.sdk.conversation.secret_registry
description: API reference for openhands.sdk.conversation.secret_registry
---

# openhands.sdk.conversation.secret_registry module

<a id="module-openhands.sdk.conversation.secret_registry"></a>

Secrets manager for handling sensitive data in conversations.

### class openhands.sdk.conversation.secret_registry.SecretRegistry(secret_sources: dict[str, ~openhands.sdk.conversation.secret_source.SecretSource] = `<factory>`)

Bases: [`OpenHandsModel`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel)

Manages secrets and injects them into bash commands when needed.

The secret registry stores a mapping of secret keys to SecretSources
that retrieve the actual secret values. When a bash command is about to be
executed, it scans the command for any secret keys and injects the corresponding
environment variables.

Secret sources will redact / encrypt their sensitive values as appropriate when
serializing, depending on the content of the context. If a context is present
and contains a ‘cipher’ object, this is used for encryption. If it contains a
boolean ‘expose_secrets’ flag set to True, secrets are dunped in plain text.
Otherwise secrets are redacted.

Additionally, it tracks the latest exported values to enable consistent masking
even when callable secrets fail on subsequent calls.

#### secret_sources : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]

#### update_secrets(secrets: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)]) → [None](https://docs.python.org/3/library/constants.html#None)

Add or update secrets in the manager.

Parameters:
  secrets – Dictionary mapping secret keys to either string values
  or callable functions that return string values

#### find_secrets_in_text(text: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [set](https://docs.python.org/3/library/stdtypes.html#set)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Find all secret keys mentioned in the given text.

Parameters:
  text – The text to search for secret keys
Returns:
  Set of secret keys found in the text

#### get_secrets_as_env_vars(command: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]

Get secrets that should be exported as environment variables for a command.

Parameters:
  command – The bash command to check for secret references
Returns:
  Dictionary of environment variables to export (key -> value)

#### mask_secrets_in_output(text: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Mask secret values in the given text.

This method uses both the current exported values and attempts to get
fresh values from callables to ensure comprehensive masking.

Parameters:
  text – The text to mask secrets in
Returns:
  Text with secret values replaced by ``<secret-hidden>``

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.
