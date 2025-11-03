---
title: openhands.sdk.utils.cipher
description: API reference for openhands.sdk.utils.cipher
---

# openhands.sdk.utils.cipher module

<a id="module-openhands.sdk.utils.cipher"></a>

Cipher utility for preventing accidental secret disclosure in serialized data

SECURITY WARNINGS:
- The secret key is a string for ease of use but should contain at least 256

> bits of entropy

### *class* openhands.sdk.utils.cipher.Cipher(secret_key: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Simple encryption utility for preventing accidental secret disclosure.

#### \_\_init_\_(secret_key: [str](https://docs.python.org/3/library/stdtypes.html#str))

#### encrypt(secret: SecretStr | [None](https://docs.python.org/3/library/constants.html#None)) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### decrypt(secret: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)) → SecretStr | [None](https://docs.python.org/3/library/constants.html#None)

Decrypt a secret value, returning None if decryption fails.

This handles cases where existing conversations were serialized with different
encryption keys or contain invalid encrypted data. A warning is logged when
decryption fails and a None is returned. This mimics the case where
no cipher was defined so secrets where redacted.
