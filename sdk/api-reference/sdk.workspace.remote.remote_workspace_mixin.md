---
title: openhands.sdk.workspace.remote.remote_workspace_mixin
description: API reference for openhands.sdk.workspace.remote.remote_workspace_mixin
---

# openhands.sdk.workspace.remote.remote_workspace_mixin module

<a id="module-openhands.sdk.workspace.remote.remote_workspace_mixin"></a>

### *class* openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin(, host: [str](https://docs.python.org/3/library/stdtypes.html#str), api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Mixin providing remote workspace operations.
This allows the same code to be used for sync and async.

#### host *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### api_key *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### working_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### model_post_init(context: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
