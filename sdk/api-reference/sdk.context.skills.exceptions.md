---
title: openhands.sdk.context.skills.exceptions
description: API reference for openhands.sdk.context.skills.exceptions
---

# openhands.sdk.context.skills.exceptions module

<a id="module-openhands.sdk.context.skills.exceptions"></a>

### *exception* openhands.sdk.context.skills.exceptions.SkillError

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

Base exception for all skill errors.

### *exception* openhands.sdk.context.skills.exceptions.SkillValidationError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Skill validation failed')

Bases: [`SkillError`](#openhands.sdk.context.skills.exceptions.SkillError)

Raised when there’s a validation error in skill metadata.

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Skill validation failed') → [None](https://docs.python.org/3/library/constants.html#None)
