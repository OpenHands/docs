---
title: openhands.sdk.workspace.base
description: API reference for openhands.sdk.workspace.base
---

# openhands.sdk.workspace.base module

<a id="module-openhands.sdk.workspace.base"></a>

### class openhands.sdk.workspace.base.BaseWorkspace(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LocalWorkspace', 'RemoteWorkspace'] = 'LocalWorkspace', working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for workspace implementations.

Workspaces provide a sandboxed environment where agents can execute commands,
read/write files, and perform other operations. All workspace implementations
support the context manager protocol for safe resource management.

### Example

```pycon
>>> with workspace:
...     result = workspace.execute_command("echo 'hello'")
...     content = workspace.read_file("example.txt")
```

#### working_dir : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### \_\_enter_\_() → [BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)

Enter the workspace context.

Returns:
  Self for use in with statements

#### \_\_exit_\_(exc_type: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_val: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_tb: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Exit the workspace context and cleanup resources.

Default implementation performs no cleanup. Subclasses should override
to add cleanup logic (e.g., stopping containers, closing connections).

Parameters:
  * exc_type – Exception type if an exception occurred
  * exc_val – Exception value if an exception occurred
  * exc_tb – Exception traceback if an exception occurred

#### abstractmethod execute_command(command: [str](https://docs.python.org/3/library/stdtypes.html#str), cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None, timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult)

Execute a bash command on the system.

Parameters:
  * command – The bash command to execute
  * cwd – Working directory for the command (optional)
  * timeout – Timeout in seconds (defaults to 30.0)
Returns:
  Result containing stdout, stderr, exit_code, and other
  : metadata
- **Return type:**
  [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.CommandResult)
Raises:
  [Exception](https://docs.python.org/3/library/exceptions.html#Exception) – If command execution fails

#### abstractmethod file_upload(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Upload a file to the system.

Parameters:
  * source_path – Path to the source file
  * destination_path – Path where the file should be uploaded
Returns:
  Result containing success status and metadata
- **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)
Raises:
  [Exception](https://docs.python.org/3/library/exceptions.html#Exception) – If file upload fails

#### abstractmethod file_download(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Download a file from the system.

Parameters:
  * source_path – Path to the source file on the system
  * destination_path – Path where the file should be downloaded
Returns:
  Result containing success status and metadata
- **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)
Raises:
  [Exception](https://docs.python.org/3/library/exceptions.html#Exception) – If file download fails

#### abstractmethod git_changes(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]

Get the git changes for the repository at the path given.

Parameters:
  path – Path to the git repository
Returns:
  List of changes
- **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[GitChange]
Raises:
  [Exception](https://docs.python.org/3/library/exceptions.html#Exception) – If path is not a git repository or getting changes failed

#### abstractmethod git_diff(path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → GitDiff

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

#### kind : [str](https://docs.python.org/3/library/stdtypes.html#str)
