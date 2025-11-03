---
title: openhands.sdk.workspace.models
description: API reference for openhands.sdk.workspace.models
---

# openhands.sdk.workspace.models module

<a id="module-openhands.sdk.workspace.models"></a>

Pydantic models for workspace operation results.

### *class* openhands.sdk.workspace.models.CommandResult

**Parameters:**

- `command: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `exit_code: [int](https://docs.python.org/3/library/functions.html#int)`
- `stdout: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `stderr: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `timeout_occurred: [bool](https://docs.python.org/3/library/functions.html#bool)`


Bases: `BaseModel`

Result of executing a command in the workspace.

#### command *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### exit_code *: [int](https://docs.python.org/3/library/functions.html#int)*

#### stdout *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### stderr *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### timeout_occurred *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.workspace.models.FileOperationResult

**Parameters:**

- `success: [bool](https://docs.python.org/3/library/functions.html#bool)`
- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `file_size: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `error: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None`


Bases: `BaseModel`

Result of a file upload or download operation.

#### success *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### source_path *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### destination_path *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### file_size *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

#### error *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
