---
title: openhands.sdk.workspace.remote.async_remote_workspace
description: API reference for openhands.sdk.workspace.remote.async_remote_workspace
---

# openhands.sdk.workspace.remote.async_remote_workspace module

<a id="module-openhands.sdk.workspace.remote.async_remote_workspace"></a>

### *class* openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace(, host: [str](https://docs.python.org/3/library/stdtypes.html#str), api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`RemoteWorkspaceMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin)

Async Remote Workspace Implementation.

#### *property* client *: AsyncClient*

#### *async* execute_command(command: [str](https://docs.python.org/3/library/stdtypes.html#str), cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None, timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult)

Execute a bash command on the remote system.

This method starts a bash command via the remote agent server API,
then polls for the output until the command completes.

* **Parameters:**
  * **command** – The bash command to execute
  * **cwd** – Working directory (optional)
  * **timeout** – Timeout in seconds
* **Returns:**
  Result with stdout, stderr, exit_code, and other metadata
* **Return type:**
  [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.CommandResult)

#### *async* file_upload(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

* **Parameters:**
  * **source_path** – Path to the local source file
  * **destination_path** – Path where the file should be uploaded on remote system
* **Returns:**
  Result with success status and metadata
* **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)

#### *async* file_download(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

* **Parameters:**
  * **source_path** – Path to the source file on remote system
  * **destination_path** – Path where the file should be saved locally
* **Returns:**
  Result with success status and metadata
* **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)

#### *async* git_changes(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]

Get the git changes for the repository at the path given.

* **Parameters:**
  **path** – Path to the git repository
* **Returns:**
  List of changes
* **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting changes failed

#### *async* git_diff(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → GitDiff

Get the git diff for the file at the path given.

* **Parameters:**
  **path** – Path to the file
* **Returns:**
  Git diff
* **Return type:**
  GitDiff
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting diff failed

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.
