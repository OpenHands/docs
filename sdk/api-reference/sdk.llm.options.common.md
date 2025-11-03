---
title: openhands.sdk.llm.options.common
description: API reference for openhands.sdk.llm.options.common
---

# openhands.sdk.llm.options.common module

<a id="module-openhands.sdk.llm.options.common"></a>

### openhands.sdk.llm.options.common.apply_defaults_if_absent(user_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)], defaults: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Return a new dict with defaults applied when keys are absent.

- Pure and deterministic; does not mutate inputs
- Only applies defaults when the key is missing and default is not None
- Does not alter user-provided values
