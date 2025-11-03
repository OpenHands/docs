---
title: openhands.sdk.workspace.remote.base
description: API reference for openhands.sdk.workspace.remote.base
---

# openhands.sdk.workspace.remote.base module

<a id="module-openhands.sdk.workspace.remote.base"></a>

### class openhands.sdk.workspace.remote.base.RemoteWorkspace(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['RemoteWorkspace'] = 'RemoteWorkspace', working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str), host: [str](https://docs.python.org/3/library/stdtypes.html#str), api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`RemoteWorkspaceMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin), [`BaseWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)

Remote workspace implementation that connects to an OpenHands agent server.

RemoteWorkspace provides access to a sandboxed environment running on a remote
OpenHands agent server. This is the recommended approach for production deployments
as it provides better isolation and security.

### Example

```pycon
>>> workspace = RemoteWorkspace(
...     host="https://agent-server.example.com",
...     working_dir="/workspace"
... )
>>> with workspace:
...     result = workspace.execute_command("ls -la")
...     content = workspace.read_file("README.md")
```

#### property client : Client

#### execute_command(command: [str](https://docs.python.org/3/library/stdtypes.html#str), cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None, timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult)

Execute a bash command on the remote system.

This method starts a bash command via the remote agent server API,
then polls for the output until the command completes.

Parameters:
  * command – The bash command to execute
  * cwd – Working directory (optional)
  * timeout – Timeout in seconds
Returns:
  Result with stdout, stderr, exit_code, and other metadata
- **Return type:**
  [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.CommandResult)

#### file_upload(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

Parameters:
  * source_path – Path to the local source file
  * destination_path – Path where the file should be uploaded on remote system
Returns:
  Result with success status and metadata
- **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)

#### file_download(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

Parameters:
  * source_path – Path to the source file on remote system
  * destination_path – Path where the file should be saved locally
Returns:
  Result with success status and metadata
- **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)

#### git_changes(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]

Get the git changes for the repository at the path given.

Parameters:
  path – Path to the git repository
Returns:
  List of changes
- **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]
Raises:
  [Exception](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting changes failed

#### git_diff(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → GitDiff

Get the git diff for the file at the path given.

Parameters:
  path – Path to the file
Returns:
  Git diff
- **Return type:**
  GitDiff
Raises:
  [Exception](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting diff failed

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['RemoteWorkspace']

#### host : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### api_key : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### working_dir : [str](https://docs.python.org/3/library/stdtypes.html#str)
