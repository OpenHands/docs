---
title: openhands.sdk.utils.pydantic_secrets
description: API reference for openhands.sdk.utils.pydantic_secrets
---

# openhands.sdk.utils.pydantic_secrets module

<a id="module-openhands.sdk.utils.pydantic_secrets"></a>

### openhands.sdk.utils.pydantic_secrets.serialize_secret(v: SecretStr | [None](https://docs.python.org/3/library/constants.html#None), info)

Serialize secret fields with encryption or redaction.

- If a cipher is provided in context, encrypts the secret value
- If expose_secrets flag is True in context, exposes the actual value
- Otherwise, lets Pydantic handle default masking (redaction)
- This prevents accidental secret disclosure

### openhands.sdk.utils.pydantic_secrets.validate_secret(v: SecretStr | [None](https://docs.python.org/3/library/constants.html#None), info)

Deserialize secret fields, handling encryption and empty values.

- Empty secrets are converted to None
- If a cipher is provided in context, attempts to decrypt the value
- If decryption fails, the cipher returns None and a warning is logged
- This gracefully handles conversations encrypted with different keys or were redacted
