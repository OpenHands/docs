---
title: openhands.sdk.workspace.remote
description: API reference for openhands.sdk.workspace.remote
---

# openhands.sdk.workspace.remote package

<a id="module-openhands.sdk.workspace.remote"></a>

Remote workspace implementations.

### *class* openhands.sdk.workspace.remote.RemoteWorkspace(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['RemoteWorkspace'] = 'RemoteWorkspace', working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str), host: [str](https://docs.python.org/3/library/stdtypes.html#str), api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`RemoteWorkspaceMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin), [`BaseWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)

Remote Workspace Implementation.

#### *property* client *: Client*

#### execute_command(command: [str](https://docs.python.org/3/library/stdtypes.html#str), cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None, timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult)

Execute a bash command on the remote system.

This method starts a bash command via the remote agent server API,
then polls for the output until the command completes.

**Parameters:**
  * **command** – The bash command to execute
  * **cwd** – Working directory (optional)
  * **timeout** – Timeout in seconds
**Returns:**
  Result with stdout, stderr, exit_code, and other metadata
* **Return type:**
  [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.CommandResult)

#### file_download(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

**Parameters:**
  * **source_path** – Path to the source file on remote system
  * **destination_path** – Path where the file should be saved locally
**Returns:**
  Result with success status and metadata
* **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)

#### file_upload(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

**Parameters:**
  * **source_path** – Path to the local source file
  * **destination_path** – Path where the file should be uploaded on remote system
**Returns:**
  Result with success status and metadata
* **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)

#### git_changes(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]

Get the git changes for the repository at the path given.

**Parameters:**
  **path** – Path to the git repository
**Returns:**
  List of changes
* **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]
**Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting changes failed

#### git_diff(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → GitDiff

Get the git diff for the file at the path given.

**Parameters:**
  **path** – Path to the file
**Returns:**
  Git diff
* **Return type:**
  GitDiff
**Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting diff failed

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['RemoteWorkspace']*

#### host *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### api_key *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### working_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

## Submodules

* [openhands.sdk.workspace.remote.async_remote_workspace module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md)
  * [`AsyncRemoteWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace)
    * [`AsyncRemoteWorkspace.client`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.client)
    * [`AsyncRemoteWorkspace.execute_command()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.execute_command)
    * [`AsyncRemoteWorkspace.file_upload()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.file_upload)
    * [`AsyncRemoteWorkspace.file_download()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.file_download)
    * [`AsyncRemoteWorkspace.git_changes()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.git_changes)
    * [`AsyncRemoteWorkspace.git_diff()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.git_diff)
    * [`AsyncRemoteWorkspace.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.model_config)
    * [`AsyncRemoteWorkspace.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.model_post_init)
* [openhands.sdk.workspace.remote.base module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md)
  * [`RemoteWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace)
    * [`RemoteWorkspace.client`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.client)
    * [`RemoteWorkspace.execute_command()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.execute_command)
    * [`RemoteWorkspace.file_upload()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.file_upload)
    * [`RemoteWorkspace.file_download()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.file_download)
    * [`RemoteWorkspace.git_changes()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.git_changes)
    * [`RemoteWorkspace.git_diff()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.git_diff)
    * [`RemoteWorkspace.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_config)
    * [`RemoteWorkspace.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_post_init)
    * [`RemoteWorkspace.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.kind)
    * [`RemoteWorkspace.host`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.host)
    * [`RemoteWorkspace.api_key`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.api_key)
    * [`RemoteWorkspace.working_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace.working_dir)
* [openhands.sdk.workspace.remote.remote_workspace_mixin module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md)
  * [`RemoteWorkspaceMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin)
    * [`RemoteWorkspaceMixin.host`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.host)
    * [`RemoteWorkspaceMixin.api_key`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.api_key)
    * [`RemoteWorkspaceMixin.working_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.working_dir)
    * [`RemoteWorkspaceMixin.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.model_post_init)
    * [`RemoteWorkspaceMixin.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.model_config)
