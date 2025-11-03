---
title: openhands.sdk.workspace.local
description: API reference for openhands.sdk.workspace.local
---

# openhands.sdk.workspace.local module

<a id="module-openhands.sdk.workspace.local"></a>

### *class* openhands.sdk.workspace.local.LocalWorkspace(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LocalWorkspace'] = 'LocalWorkspace', working_dir: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`BaseWorkspace`](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)

Mixin providing local workspace operations.

#### execute_command(command: [str](https://docs.python.org/3/library/stdtypes.html#str), cwd: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) | [None](https://docs.python.org/3/library/constants.html#None) = None, timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.CommandResult)

Execute a bash command locally.

Uses the shared shell execution utility to run commands with proper
timeout handling, output streaming, and error management.

Parameters:
  * command – The bash command to execute
  * cwd – Working directory (optional)
  * timeout – Timeout in seconds
Returns:
  Result with stdout, stderr, exit_code, command, and
  : timeout_occurred
- **Return type:**
  [CommandResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.CommandResult)

#### file_upload(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Upload (copy) a file locally.

For local systems, file upload is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

Parameters:
  * source_path – Path to the source file
  * destination_path – Path where the file should be copied
Returns:
  Result with success status and file information
- **Return type:**
  [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.md#openhands.sdk.workspace.FileOperationResult)

#### file_download(source_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path), destination_path: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) → [FileOperationResult](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.models.md#openhands.sdk.workspace.models.FileOperationResult)

Download (copy) a file locally.

For local systems, file download is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

Parameters:
  * source_path – Path to the source file
  * destination_path – Path where the file should be copied
Returns:
  Result with success status and file information
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

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LocalWorkspace']

#### working_dir : [str](https://docs.python.org/3/library/stdtypes.html#str)
