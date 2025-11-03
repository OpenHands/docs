---
title: openhands.sdk.workspace
description: API reference for openhands.sdk.workspace
---

# openhands.sdk.workspace package

<a id="module-openhands.sdk.workspace"></a>

### *class* openhands.sdk.workspace.BaseWorkspace

**Parameters:**

- `kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LocalWorkspace', 'RemoteWorkspace'] = 'LocalWorkspace'`
- `working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str)`


Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base mixin for workspace.

All workspace implementations support the context manager protocol,
allowing safe resource management:

> with workspace:
> : workspace.execute_command(“echo ‘hello’”)

#### \_\_enter_\_() → [BaseWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)

Enter the workspace context.

* **Returns:**
  Self for use in with statements

#### \_\_exit_\_

**Parameters:**

- `exc_type: [Any](https://docs.python.org/3/library/typing.html#typing.Any)`
- `exc_val: [Any](https://docs.python.org/3/library/typing.html#typing.Any)`
- `exc_tb: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None`


Exit the workspace context and cleanup resources.

Default implementation performs no cleanup. Subclasses should override
to add cleanup logic (e.g., stopping containers, closing connections).

* **Parameters:**
  * **exc_type** – Exception type if an exception occurred
  * **exc_val** – Exception value if an exception occurred
  * **exc_tb** – Exception traceback if an exception occurred

#### *abstractmethod* execute_command

**Parameters:**

- `command: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult`


Execute a bash command on the system.

* **Parameters:**
  * **command** – The bash command to execute
  * **cwd** – Working directory for the command (optional)
  * **timeout** – Timeout in seconds (defaults to 30.0)
* **Returns:**
  Result containing stdout, stderr, exit_code, and other
  : metadata
* **Return type:**
  [CommandResult](#openhands.sdk.workspace.CommandResult)
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If command execution fails

#### *abstractmethod* file_download

**Parameters:**

- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult`


Download a file from the system.

* **Parameters:**
  * **source_path** – Path to the source file on the system
  * **destination_path** – Path where the file should be downloaded
* **Returns:**
  Result containing success status and metadata
* **Return type:**
  [FileOperationResult](#openhands.sdk.workspace.FileOperationResult)
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If file download fails

#### *abstractmethod* file_upload

**Parameters:**

- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult`


Upload a file to the system.

* **Parameters:**
  * **source_path** – Path to the source file
  * **destination_path** – Path where the file should be uploaded
* **Returns:**
  Result containing success status and metadata
* **Return type:**
  [FileOperationResult](#openhands.sdk.workspace.FileOperationResult)
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If file upload fails

#### *abstractmethod* git_changes

**Parameters:**

- `path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [list](https://docs.python.org/3/library/stdtypes.html#list`


Get the git changes for the repository at the path given.

* **Parameters:**
  **path** – Path to the git repository
* **Returns:**
  List of changes
* **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting changes failed

#### *abstractmethod* git_diff(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → GitDiff

Get the git diff for the file at the path given.

* **Parameters:**
  **path** – Path to the file
* **Returns:**
  Git diff
* **Return type:**
  GitDiff
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting diff failed

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### working_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.workspace.CommandResult

**Parameters:**

- `command: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `exit_code: [int](https://docs.python.org/3/library/functions.html#int)`
- `stdout: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `stderr: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `timeout_occurred: [bool](https://docs.python.org/3/library/functions.html#bool)`


Bases: `BaseModel`

Result of executing a command in the workspace.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### command *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### exit_code *: [int](https://docs.python.org/3/library/functions.html#int)*

#### stdout *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### stderr *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### timeout_occurred *: [bool](https://docs.python.org/3/library/functions.html#bool)*

### *class* openhands.sdk.workspace.FileOperationResult

**Parameters:**

- `success: [bool](https://docs.python.org/3/library/functions.html#bool)`
- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `file_size: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `error: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None`


Bases: `BaseModel`

Result of a file upload or download operation.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### success *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### source_path *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### destination_path *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### file_size *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

#### error *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

### *class* openhands.sdk.workspace.LocalWorkspace

**Parameters:**

- `kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LocalWorkspace'] = 'LocalWorkspace'`
- `working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str)`


Bases: [`BaseWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)

Mixin providing local workspace operations.

#### execute_command

**Parameters:**

- `command: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult`


Execute a bash command locally.

Uses the shared shell execution utility to run commands with proper
timeout handling, output streaming, and error management.

* **Parameters:**
  * **command** – The bash command to execute
  * **cwd** – Working directory (optional)
  * **timeout** – Timeout in seconds
* **Returns:**
  Result with stdout, stderr, exit_code, command, and
  : timeout_occurred
* **Return type:**
  [CommandResult](#openhands.sdk.workspace.CommandResult)

#### file_download

**Parameters:**

- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult`


Download (copy) a file locally.

For local systems, file download is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

* **Parameters:**
  * **source_path** – Path to the source file
  * **destination_path** – Path where the file should be copied
* **Returns:**
  Result with success status and file information
* **Return type:**
  [FileOperationResult](#openhands.sdk.workspace.FileOperationResult)

#### file_upload

**Parameters:**

- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult`


Upload (copy) a file locally.

For local systems, file upload is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

* **Parameters:**
  * **source_path** – Path to the source file
  * **destination_path** – Path where the file should be copied
* **Returns:**
  Result with success status and file information
* **Return type:**
  [FileOperationResult](#openhands.sdk.workspace.FileOperationResult)

#### git_changes

**Parameters:**

- `path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [list](https://docs.python.org/3/library/stdtypes.html#list`


Get the git changes for the repository at the path given.

* **Parameters:**
  **path** – Path to the git repository
* **Returns:**
  List of changes
* **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting changes failed

#### git_diff(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → GitDiff

Get the git diff for the file at the path given.

* **Parameters:**
  **path** – Path to the file
* **Returns:**
  Git diff
* **Return type:**
  GitDiff
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting diff failed

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LocalWorkspace']*

### *class* openhands.sdk.workspace.RemoteWorkspace

**Parameters:**

- `kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['RemoteWorkspace'] = 'RemoteWorkspace'`
- `working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `host: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None`


Bases: [`RemoteWorkspaceMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin), [`BaseWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)

Remote Workspace Implementation.

#### *property* client *: Client*

#### execute_command

**Parameters:**

- `command: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult`


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
  [CommandResult](#openhands.sdk.workspace.CommandResult)

#### file_download

**Parameters:**

- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult`


Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

* **Parameters:**
  * **source_path** – Path to the source file on remote system
  * **destination_path** – Path where the file should be saved locally
* **Returns:**
  Result with success status and metadata
* **Return type:**
  [FileOperationResult](#openhands.sdk.workspace.FileOperationResult)

#### file_upload

**Parameters:**

- `source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)`
- `destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult`


Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

* **Parameters:**
  * **source_path** – Path to the local source file
  * **destination_path** – Path where the file should be uploaded on remote system
* **Returns:**
  Result with success status and metadata
* **Return type:**
  [FileOperationResult](#openhands.sdk.workspace.FileOperationResult)

#### git_changes

**Parameters:**

- `path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [list](https://docs.python.org/3/library/stdtypes.html#list`


Get the git changes for the repository at the path given.

* **Parameters:**
  **path** – Path to the git repository
* **Returns:**
  List of changes
* **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting changes failed

#### git_diff(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → GitDiff

Get the git diff for the file at the path given.

* **Parameters:**
  **path** – Path to the file
* **Returns:**
  Git diff
* **Return type:**
  GitDiff
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting diff failed

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['RemoteWorkspace']*

### *class* openhands.sdk.workspace.Workspace(, working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'workspace/project')

### *class* openhands.sdk.workspace.Workspace

**Parameters:**

- `host: [str](https://docs.python.org/3/library/stdtypes.html#str)`
- `working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'workspace/project'`
- `api_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None`


Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Factory entrypoint that returns a LocalWorkspace or RemoteWorkspace.

Usage:
: - Workspace(working_dir=…) -> LocalWorkspace
  - Workspace(working_dir=…, host=”[http://](http://)…”) -> RemoteWorkspace

## Subpackages

* [openhands.sdk.workspace.remote package](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md)
  * [`RemoteWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace)
    * [`RemoteWorkspace.client`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.client)
    * [`RemoteWorkspace.execute_command()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.execute_command)
    * [`RemoteWorkspace.file_download()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.file_download)
    * [`RemoteWorkspace.file_upload()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.file_upload)
    * [`RemoteWorkspace.git_changes()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.git_changes)
    * [`RemoteWorkspace.git_diff()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.git_diff)
    * [`RemoteWorkspace.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.model_config)
    * [`RemoteWorkspace.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.model_post_init)
    * [`RemoteWorkspace.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.kind)
    * [`RemoteWorkspace.host`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.host)
    * [`RemoteWorkspace.api_key`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.api_key)
    * [`RemoteWorkspace.working_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#openhands.sdk.workspace.remote.RemoteWorkspace.working_dir)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.md#submodules)
    * [openhands.sdk.workspace.remote.async_remote_workspace module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md)
      * [`AsyncRemoteWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.async_remote_workspace.md#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace)
    * [openhands.sdk.workspace.remote.base module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md)
      * [`RemoteWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace)
    * [openhands.sdk.workspace.remote.remote_workspace_mixin module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md)
      * [`RemoteWorkspaceMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.remote_workspace_mixin.md#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin)

## Submodules

* [openhands.sdk.workspace.base module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md)
  * [`BaseWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)
    * [`BaseWorkspace.working_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.working_dir)
    * [`BaseWorkspace.__enter__()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.__enter__)
    * [`BaseWorkspace.__exit__()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.__exit__)
    * [`BaseWorkspace.execute_command()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.execute_command)
    * [`BaseWorkspace.file_upload()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.file_upload)
    * [`BaseWorkspace.file_download()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.file_download)
    * [`BaseWorkspace.git_changes()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.git_changes)
    * [`BaseWorkspace.git_diff()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.git_diff)
    * [`BaseWorkspace.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.model_config)
    * [`BaseWorkspace.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace.kind)
* [openhands.sdk.workspace.local module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md)
  * [`LocalWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace)
    * [`LocalWorkspace.execute_command()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.execute_command)
    * [`LocalWorkspace.file_upload()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.file_upload)
    * [`LocalWorkspace.file_download()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.file_download)
    * [`LocalWorkspace.git_changes()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.git_changes)
    * [`LocalWorkspace.git_diff()`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.git_diff)
    * [`LocalWorkspace.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.model_config)
    * [`LocalWorkspace.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.kind)
    * [`LocalWorkspace.working_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace.working_dir)
* [openhands.sdk.workspace.models module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md)
  * [`CommandResult`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult)
    * [`CommandResult.command`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult.command)
    * [`CommandResult.exit_code`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult.exit_code)
    * [`CommandResult.stdout`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult.stdout)
    * [`CommandResult.stderr`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult.stderr)
    * [`CommandResult.timeout_occurred`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult.timeout_occurred)
    * [`CommandResult.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult.model_config)
  * [`FileOperationResult`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)
    * [`FileOperationResult.success`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult.success)
    * [`FileOperationResult.source_path`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult.source_path)
    * [`FileOperationResult.destination_path`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult.destination_path)
    * [`FileOperationResult.file_size`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult.file_size)
    * [`FileOperationResult.error`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult.error)
    * [`FileOperationResult.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult.model_config)
* [openhands.sdk.workspace.workspace module](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.workspace.md)
  * [`Workspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.workspace.md#openhands.sdk.workspace.workspace.Workspace)
