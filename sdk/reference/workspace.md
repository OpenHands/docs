## `openhands.sdk.workspace`

**Modules:**

- [**base**](#openhands.sdk.workspace.base) –
- [**local**](#openhands.sdk.workspace.local) –
- [**models**](#openhands.sdk.workspace.models) – Pydantic models for workspace operation results.
- [**remote**](#openhands.sdk.workspace.remote) – Remote workspace implementations.
- [**workspace**](#openhands.sdk.workspace.workspace) –

**Classes:**

- [**BaseWorkspace**](#openhands.sdk.workspace.BaseWorkspace) – Abstract base mixin for workspace.
- [**CommandResult**](#openhands.sdk.workspace.CommandResult) – Result of executing a command in the workspace.
- [**FileOperationResult**](#openhands.sdk.workspace.FileOperationResult) – Result of a file upload or download operation.
- [**LocalWorkspace**](#openhands.sdk.workspace.LocalWorkspace) – Mixin providing local workspace operations.
- [**RemoteWorkspace**](#openhands.sdk.workspace.RemoteWorkspace) – Remote Workspace Implementation.
- [**Workspace**](#openhands.sdk.workspace.Workspace) – Factory entrypoint that returns a LocalWorkspace or RemoteWorkspace.

### `openhands.sdk.workspace.BaseWorkspace`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Abstract base mixin for workspace.

All workspace implementations support the context manager protocol,
allowing safe resource management:

```
with workspace:
    workspace.execute_command("echo 'hello'")
```

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.BaseWorkspace.execute_command) – Execute a bash command on the system.
- [**file_download**](#openhands.sdk.workspace.BaseWorkspace.file_download) – Download a file from the system.
- [**file_upload**](#openhands.sdk.workspace.BaseWorkspace.file_upload) – Upload a file to the system.
- [**get_serializable_type**](#openhands.sdk.workspace.BaseWorkspace.get_serializable_type) – Custom method to get the union of all currently loaded
- [**git_changes**](#openhands.sdk.workspace.BaseWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.BaseWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_dump_json**](#openhands.sdk.workspace.BaseWorkspace.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.workspace.BaseWorkspace.model_json_schema) –
- [**model_post_init**](#openhands.sdk.workspace.BaseWorkspace.model_post_init) –
- [**model_rebuild**](#openhands.sdk.workspace.BaseWorkspace.model_rebuild) –
- [**model_validate**](#openhands.sdk.workspace.BaseWorkspace.model_validate) –
- [**model_validate_json**](#openhands.sdk.workspace.BaseWorkspace.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.workspace.BaseWorkspace.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.workspace.BaseWorkspace.kind) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.BaseWorkspace.working_dir) (<code>[str](#str)</code>) –

#### `openhands.sdk.workspace.BaseWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command on the system.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory for the command (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds (defaults to 30.0)

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result containing stdout, stderr, exit_code, and other
  metadata

**Raises:**

- <code>[Exception](#Exception)</code> – If command execution fails

#### `openhands.sdk.workspace.BaseWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download a file from the system.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file on the system
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be downloaded

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result containing success status and metadata

**Raises:**

- <code>[Exception](#Exception)</code> – If file download fails

#### `openhands.sdk.workspace.BaseWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload a file to the system.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be uploaded

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result containing success status and metadata

**Raises:**

- <code>[Exception](#Exception)</code> – If file upload fails

#### `openhands.sdk.workspace.BaseWorkspace.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.workspace.BaseWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

#### `openhands.sdk.workspace.BaseWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

#### `openhands.sdk.workspace.BaseWorkspace.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.workspace.BaseWorkspace.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.workspace.BaseWorkspace.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.workspace.BaseWorkspace.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.workspace.BaseWorkspace.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.workspace.BaseWorkspace.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.workspace.BaseWorkspace.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.workspace.BaseWorkspace.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.workspace.BaseWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

### `openhands.sdk.workspace.CommandResult`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Result of executing a command in the workspace.

**Attributes:**

- [**command**](#openhands.sdk.workspace.CommandResult.command) (<code>[str](#str)</code>) –
- [**exit_code**](#openhands.sdk.workspace.CommandResult.exit_code) (<code>[int](#int)</code>) –
- [**stderr**](#openhands.sdk.workspace.CommandResult.stderr) (<code>[str](#str)</code>) –
- [**stdout**](#openhands.sdk.workspace.CommandResult.stdout) (<code>[str](#str)</code>) –
- [**timeout_occurred**](#openhands.sdk.workspace.CommandResult.timeout_occurred) (<code>[bool](#bool)</code>) –

#### `openhands.sdk.workspace.CommandResult.command`

```python
command: str = Field(description='The command that was executed')
```

#### `openhands.sdk.workspace.CommandResult.exit_code`

```python
exit_code: int = Field(description='Exit code of the command')
```

#### `openhands.sdk.workspace.CommandResult.stderr`

```python
stderr: str = Field(description='Standard error from the command')
```

#### `openhands.sdk.workspace.CommandResult.stdout`

```python
stdout: str = Field(description='Standard output from the command')
```

#### `openhands.sdk.workspace.CommandResult.timeout_occurred`

```python
timeout_occurred: bool = Field(description='Whether the command timed out during execution')
```

### `openhands.sdk.workspace.FileOperationResult`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Result of a file upload or download operation.

**Attributes:**

- [**destination_path**](#openhands.sdk.workspace.FileOperationResult.destination_path) (<code>[str](#str)</code>) –
- [**error**](#openhands.sdk.workspace.FileOperationResult.error) (<code>[str](#str) | None</code>) –
- [**file_size**](#openhands.sdk.workspace.FileOperationResult.file_size) (<code>[int](#int) | None</code>) –
- [**source_path**](#openhands.sdk.workspace.FileOperationResult.source_path) (<code>[str](#str)</code>) –
- [**success**](#openhands.sdk.workspace.FileOperationResult.success) (<code>[bool](#bool)</code>) –

#### `openhands.sdk.workspace.FileOperationResult.destination_path`

```python
destination_path: str = Field(description='Path to the destination file')
```

#### `openhands.sdk.workspace.FileOperationResult.error`

```python
error: str | None = Field(default=None, description='Error message (if operation failed)')
```

#### `openhands.sdk.workspace.FileOperationResult.file_size`

```python
file_size: int | None = Field(default=None, description='Size of the file in bytes (if successful)')
```

#### `openhands.sdk.workspace.FileOperationResult.source_path`

```python
source_path: str = Field(description='Path to the source file')
```

#### `openhands.sdk.workspace.FileOperationResult.success`

```python
success: bool = Field(description='Whether the operation was successful')
```

### `openhands.sdk.workspace.LocalWorkspace`

Bases: <code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>

Mixin providing local workspace operations.

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.LocalWorkspace.execute_command) – Execute a bash command locally.
- [**file_download**](#openhands.sdk.workspace.LocalWorkspace.file_download) – Download (copy) a file locally.
- [**file_upload**](#openhands.sdk.workspace.LocalWorkspace.file_upload) – Upload (copy) a file locally.
- [**get_serializable_type**](#openhands.sdk.workspace.LocalWorkspace.get_serializable_type) – Custom method to get the union of all currently loaded
- [**git_changes**](#openhands.sdk.workspace.LocalWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.LocalWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_dump_json**](#openhands.sdk.workspace.LocalWorkspace.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.workspace.LocalWorkspace.model_json_schema) –
- [**model_post_init**](#openhands.sdk.workspace.LocalWorkspace.model_post_init) –
- [**model_rebuild**](#openhands.sdk.workspace.LocalWorkspace.model_rebuild) –
- [**model_validate**](#openhands.sdk.workspace.LocalWorkspace.model_validate) –
- [**model_validate_json**](#openhands.sdk.workspace.LocalWorkspace.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.workspace.LocalWorkspace.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.workspace.LocalWorkspace.kind) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.LocalWorkspace.working_dir) (<code>[str](#str)</code>) –

#### `openhands.sdk.workspace.LocalWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command locally.

Uses the shared shell execution utility to run commands with proper
timeout handling, output streaming, and error management.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result with stdout, stderr, exit_code, command, and
  timeout_occurred

#### `openhands.sdk.workspace.LocalWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download (copy) a file locally.

For local systems, file download is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be copied

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and file information

#### `openhands.sdk.workspace.LocalWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload (copy) a file locally.

For local systems, file upload is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be copied

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and file information

#### `openhands.sdk.workspace.LocalWorkspace.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.workspace.LocalWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

#### `openhands.sdk.workspace.LocalWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

#### `openhands.sdk.workspace.LocalWorkspace.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.workspace.LocalWorkspace.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.workspace.LocalWorkspace.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.workspace.LocalWorkspace.model_post_init`

```python
model_post_init(_context)
```

#### `openhands.sdk.workspace.LocalWorkspace.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.workspace.LocalWorkspace.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.workspace.LocalWorkspace.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.workspace.LocalWorkspace.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.workspace.LocalWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

### `openhands.sdk.workspace.RemoteWorkspace`

Bases: <code>[RemoteWorkspaceMixin](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin)</code>, <code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>

Remote Workspace Implementation.

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.RemoteWorkspace.execute_command) – Execute a bash command on the remote system.
- [**file_download**](#openhands.sdk.workspace.RemoteWorkspace.file_download) – Download a file from the remote system.
- [**file_upload**](#openhands.sdk.workspace.RemoteWorkspace.file_upload) – Upload a file to the remote system.
- [**get_serializable_type**](#openhands.sdk.workspace.RemoteWorkspace.get_serializable_type) – Custom method to get the union of all currently loaded
- [**git_changes**](#openhands.sdk.workspace.RemoteWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.RemoteWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_dump_json**](#openhands.sdk.workspace.RemoteWorkspace.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.workspace.RemoteWorkspace.model_json_schema) –
- [**model_post_init**](#openhands.sdk.workspace.RemoteWorkspace.model_post_init) –
- [**model_rebuild**](#openhands.sdk.workspace.RemoteWorkspace.model_rebuild) –
- [**model_validate**](#openhands.sdk.workspace.RemoteWorkspace.model_validate) –
- [**model_validate_json**](#openhands.sdk.workspace.RemoteWorkspace.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.workspace.RemoteWorkspace.resolve_kind) –

**Attributes:**

- [**api_key**](#openhands.sdk.workspace.RemoteWorkspace.api_key) (<code>[str](#str) | None</code>) –
- [**client**](#openhands.sdk.workspace.RemoteWorkspace.client) (<code>[Client](#httpx.Client)</code>) –
- [**host**](#openhands.sdk.workspace.RemoteWorkspace.host) (<code>[str](#str)</code>) –
- [**kind**](#openhands.sdk.workspace.RemoteWorkspace.kind) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.RemoteWorkspace.working_dir) (<code>[str](#str)</code>) –

#### `openhands.sdk.workspace.RemoteWorkspace.api_key`

```python
api_key: str | None = Field(default=None, description='API key for authenticating with the remote host.')
```

#### `openhands.sdk.workspace.RemoteWorkspace.client`

```python
client: httpx.Client
```

#### `openhands.sdk.workspace.RemoteWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command on the remote system.

This method starts a bash command via the remote agent server API,
then polls for the output until the command completes.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result with stdout, stderr, exit_code, and other metadata

#### `openhands.sdk.workspace.RemoteWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file on remote system
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be saved locally

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

#### `openhands.sdk.workspace.RemoteWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the local source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be uploaded on remote system

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

#### `openhands.sdk.workspace.RemoteWorkspace.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

#### `openhands.sdk.workspace.RemoteWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

#### `openhands.sdk.workspace.RemoteWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

#### `openhands.sdk.workspace.RemoteWorkspace.host`

```python
host: str = Field(description='The remote host URL for the workspace.')
```

#### `openhands.sdk.workspace.RemoteWorkspace.kind`

```python
kind: str = Field(default='')
```

#### `openhands.sdk.workspace.RemoteWorkspace.model_dump_json`

```python
model_dump_json(**kwargs)
```

#### `openhands.sdk.workspace.RemoteWorkspace.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

#### `openhands.sdk.workspace.RemoteWorkspace.model_post_init`

```python
model_post_init(context)
```

#### `openhands.sdk.workspace.RemoteWorkspace.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

#### `openhands.sdk.workspace.RemoteWorkspace.model_validate`

```python
model_validate(obj, **kwargs)
```

#### `openhands.sdk.workspace.RemoteWorkspace.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

#### `openhands.sdk.workspace.RemoteWorkspace.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.workspace.RemoteWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

### `openhands.sdk.workspace.Workspace`

Factory entrypoint that returns a LocalWorkspace or RemoteWorkspace.

<details class="usage" open markdown="1">
<summary>Usage</summary>

- Workspace(working_dir=...) -> LocalWorkspace
- Workspace(working_dir=..., host="http://...") -> RemoteWorkspace

</details>

### `openhands.sdk.workspace.base`

**Classes:**

- [**BaseWorkspace**](#openhands.sdk.workspace.base.BaseWorkspace) – Abstract base mixin for workspace.

**Attributes:**

- [**logger**](#openhands.sdk.workspace.base.logger) –

#### `openhands.sdk.workspace.base.BaseWorkspace`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Abstract base mixin for workspace.

All workspace implementations support the context manager protocol,
allowing safe resource management:

```
with workspace:
    workspace.execute_command("echo 'hello'")
```

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.base.BaseWorkspace.execute_command) – Execute a bash command on the system.
- [**file_download**](#openhands.sdk.workspace.base.BaseWorkspace.file_download) – Download a file from the system.
- [**file_upload**](#openhands.sdk.workspace.base.BaseWorkspace.file_upload) – Upload a file to the system.
- [**get_serializable_type**](#openhands.sdk.workspace.base.BaseWorkspace.get_serializable_type) – Custom method to get the union of all currently loaded
- [**git_changes**](#openhands.sdk.workspace.base.BaseWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.base.BaseWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_dump_json**](#openhands.sdk.workspace.base.BaseWorkspace.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.workspace.base.BaseWorkspace.model_json_schema) –
- [**model_post_init**](#openhands.sdk.workspace.base.BaseWorkspace.model_post_init) –
- [**model_rebuild**](#openhands.sdk.workspace.base.BaseWorkspace.model_rebuild) –
- [**model_validate**](#openhands.sdk.workspace.base.BaseWorkspace.model_validate) –
- [**model_validate_json**](#openhands.sdk.workspace.base.BaseWorkspace.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.workspace.base.BaseWorkspace.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.workspace.base.BaseWorkspace.kind) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.base.BaseWorkspace.working_dir) (<code>[str](#str)</code>) –

##### `openhands.sdk.workspace.base.BaseWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command on the system.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory for the command (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds (defaults to 30.0)

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result containing stdout, stderr, exit_code, and other
  metadata

**Raises:**

- <code>[Exception](#Exception)</code> – If command execution fails

##### `openhands.sdk.workspace.base.BaseWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download a file from the system.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file on the system
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be downloaded

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result containing success status and metadata

**Raises:**

- <code>[Exception](#Exception)</code> – If file download fails

##### `openhands.sdk.workspace.base.BaseWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload a file to the system.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be uploaded

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result containing success status and metadata

**Raises:**

- <code>[Exception](#Exception)</code> – If file upload fails

##### `openhands.sdk.workspace.base.BaseWorkspace.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.workspace.base.BaseWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

##### `openhands.sdk.workspace.base.BaseWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

##### `openhands.sdk.workspace.base.BaseWorkspace.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.workspace.base.BaseWorkspace.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.workspace.base.BaseWorkspace.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.workspace.base.BaseWorkspace.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.workspace.base.BaseWorkspace.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.workspace.base.BaseWorkspace.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.workspace.base.BaseWorkspace.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.workspace.base.BaseWorkspace.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.workspace.base.BaseWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

#### `openhands.sdk.workspace.base.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.workspace.local`

**Classes:**

- [**LocalWorkspace**](#openhands.sdk.workspace.local.LocalWorkspace) – Mixin providing local workspace operations.

**Attributes:**

- [**logger**](#openhands.sdk.workspace.local.logger) –

#### `openhands.sdk.workspace.local.LocalWorkspace`

Bases: <code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>

Mixin providing local workspace operations.

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.local.LocalWorkspace.execute_command) – Execute a bash command locally.
- [**file_download**](#openhands.sdk.workspace.local.LocalWorkspace.file_download) – Download (copy) a file locally.
- [**file_upload**](#openhands.sdk.workspace.local.LocalWorkspace.file_upload) – Upload (copy) a file locally.
- [**get_serializable_type**](#openhands.sdk.workspace.local.LocalWorkspace.get_serializable_type) – Custom method to get the union of all currently loaded
- [**git_changes**](#openhands.sdk.workspace.local.LocalWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.local.LocalWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_dump_json**](#openhands.sdk.workspace.local.LocalWorkspace.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.workspace.local.LocalWorkspace.model_json_schema) –
- [**model_post_init**](#openhands.sdk.workspace.local.LocalWorkspace.model_post_init) –
- [**model_rebuild**](#openhands.sdk.workspace.local.LocalWorkspace.model_rebuild) –
- [**model_validate**](#openhands.sdk.workspace.local.LocalWorkspace.model_validate) –
- [**model_validate_json**](#openhands.sdk.workspace.local.LocalWorkspace.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.workspace.local.LocalWorkspace.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.workspace.local.LocalWorkspace.kind) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.local.LocalWorkspace.working_dir) (<code>[str](#str)</code>) –

##### `openhands.sdk.workspace.local.LocalWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command locally.

Uses the shared shell execution utility to run commands with proper
timeout handling, output streaming, and error management.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result with stdout, stderr, exit_code, command, and
  timeout_occurred

##### `openhands.sdk.workspace.local.LocalWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download (copy) a file locally.

For local systems, file download is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be copied

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and file information

##### `openhands.sdk.workspace.local.LocalWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload (copy) a file locally.

For local systems, file upload is implemented as a file copy operation
using shutil.copy2 to preserve metadata.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be copied

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and file information

##### `openhands.sdk.workspace.local.LocalWorkspace.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.workspace.local.LocalWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

##### `openhands.sdk.workspace.local.LocalWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

##### `openhands.sdk.workspace.local.LocalWorkspace.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.workspace.local.LocalWorkspace.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.workspace.local.LocalWorkspace.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.workspace.local.LocalWorkspace.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.workspace.local.LocalWorkspace.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.workspace.local.LocalWorkspace.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.workspace.local.LocalWorkspace.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.workspace.local.LocalWorkspace.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.workspace.local.LocalWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

#### `openhands.sdk.workspace.local.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.workspace.models`

Pydantic models for workspace operation results.

**Classes:**

- [**CommandResult**](#openhands.sdk.workspace.models.CommandResult) – Result of executing a command in the workspace.
- [**FileOperationResult**](#openhands.sdk.workspace.models.FileOperationResult) – Result of a file upload or download operation.

#### `openhands.sdk.workspace.models.CommandResult`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Result of executing a command in the workspace.

**Attributes:**

- [**command**](#openhands.sdk.workspace.models.CommandResult.command) (<code>[str](#str)</code>) –
- [**exit_code**](#openhands.sdk.workspace.models.CommandResult.exit_code) (<code>[int](#int)</code>) –
- [**stderr**](#openhands.sdk.workspace.models.CommandResult.stderr) (<code>[str](#str)</code>) –
- [**stdout**](#openhands.sdk.workspace.models.CommandResult.stdout) (<code>[str](#str)</code>) –
- [**timeout_occurred**](#openhands.sdk.workspace.models.CommandResult.timeout_occurred) (<code>[bool](#bool)</code>) –

##### `openhands.sdk.workspace.models.CommandResult.command`

```python
command: str = Field(description='The command that was executed')
```

##### `openhands.sdk.workspace.models.CommandResult.exit_code`

```python
exit_code: int = Field(description='Exit code of the command')
```

##### `openhands.sdk.workspace.models.CommandResult.stderr`

```python
stderr: str = Field(description='Standard error from the command')
```

##### `openhands.sdk.workspace.models.CommandResult.stdout`

```python
stdout: str = Field(description='Standard output from the command')
```

##### `openhands.sdk.workspace.models.CommandResult.timeout_occurred`

```python
timeout_occurred: bool = Field(description='Whether the command timed out during execution')
```

#### `openhands.sdk.workspace.models.FileOperationResult`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Result of a file upload or download operation.

**Attributes:**

- [**destination_path**](#openhands.sdk.workspace.models.FileOperationResult.destination_path) (<code>[str](#str)</code>) –
- [**error**](#openhands.sdk.workspace.models.FileOperationResult.error) (<code>[str](#str) | None</code>) –
- [**file_size**](#openhands.sdk.workspace.models.FileOperationResult.file_size) (<code>[int](#int) | None</code>) –
- [**source_path**](#openhands.sdk.workspace.models.FileOperationResult.source_path) (<code>[str](#str)</code>) –
- [**success**](#openhands.sdk.workspace.models.FileOperationResult.success) (<code>[bool](#bool)</code>) –

##### `openhands.sdk.workspace.models.FileOperationResult.destination_path`

```python
destination_path: str = Field(description='Path to the destination file')
```

##### `openhands.sdk.workspace.models.FileOperationResult.error`

```python
error: str | None = Field(default=None, description='Error message (if operation failed)')
```

##### `openhands.sdk.workspace.models.FileOperationResult.file_size`

```python
file_size: int | None = Field(default=None, description='Size of the file in bytes (if successful)')
```

##### `openhands.sdk.workspace.models.FileOperationResult.source_path`

```python
source_path: str = Field(description='Path to the source file')
```

##### `openhands.sdk.workspace.models.FileOperationResult.success`

```python
success: bool = Field(description='Whether the operation was successful')
```

### `openhands.sdk.workspace.remote`

Remote workspace implementations.

**Modules:**

- [**async_remote_workspace**](#openhands.sdk.workspace.remote.async_remote_workspace) –
- [**base**](#openhands.sdk.workspace.remote.base) –
- [**remote_workspace_mixin**](#openhands.sdk.workspace.remote.remote_workspace_mixin) –

**Classes:**

- [**RemoteWorkspace**](#openhands.sdk.workspace.remote.RemoteWorkspace) – Remote Workspace Implementation.

#### `openhands.sdk.workspace.remote.RemoteWorkspace`

Bases: <code>[RemoteWorkspaceMixin](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin)</code>, <code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>

Remote Workspace Implementation.

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.remote.RemoteWorkspace.execute_command) – Execute a bash command on the remote system.
- [**file_download**](#openhands.sdk.workspace.remote.RemoteWorkspace.file_download) – Download a file from the remote system.
- [**file_upload**](#openhands.sdk.workspace.remote.RemoteWorkspace.file_upload) – Upload a file to the remote system.
- [**get_serializable_type**](#openhands.sdk.workspace.remote.RemoteWorkspace.get_serializable_type) – Custom method to get the union of all currently loaded
- [**git_changes**](#openhands.sdk.workspace.remote.RemoteWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.remote.RemoteWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_dump_json**](#openhands.sdk.workspace.remote.RemoteWorkspace.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.workspace.remote.RemoteWorkspace.model_json_schema) –
- [**model_post_init**](#openhands.sdk.workspace.remote.RemoteWorkspace.model_post_init) –
- [**model_rebuild**](#openhands.sdk.workspace.remote.RemoteWorkspace.model_rebuild) –
- [**model_validate**](#openhands.sdk.workspace.remote.RemoteWorkspace.model_validate) –
- [**model_validate_json**](#openhands.sdk.workspace.remote.RemoteWorkspace.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.workspace.remote.RemoteWorkspace.resolve_kind) –

**Attributes:**

- [**api_key**](#openhands.sdk.workspace.remote.RemoteWorkspace.api_key) (<code>[str](#str) | None</code>) –
- [**client**](#openhands.sdk.workspace.remote.RemoteWorkspace.client) (<code>[Client](#httpx.Client)</code>) –
- [**host**](#openhands.sdk.workspace.remote.RemoteWorkspace.host) (<code>[str](#str)</code>) –
- [**kind**](#openhands.sdk.workspace.remote.RemoteWorkspace.kind) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.remote.RemoteWorkspace.working_dir) (<code>[str](#str)</code>) –

##### `openhands.sdk.workspace.remote.RemoteWorkspace.api_key`

```python
api_key: str | None = Field(default=None, description='API key for authenticating with the remote host.')
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.client`

```python
client: httpx.Client
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command on the remote system.

This method starts a bash command via the remote agent server API,
then polls for the output until the command completes.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result with stdout, stderr, exit_code, and other metadata

##### `openhands.sdk.workspace.remote.RemoteWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file on remote system
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be saved locally

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

##### `openhands.sdk.workspace.remote.RemoteWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the local source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be uploaded on remote system

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

##### `openhands.sdk.workspace.remote.RemoteWorkspace.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.workspace.remote.RemoteWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

##### `openhands.sdk.workspace.remote.RemoteWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

##### `openhands.sdk.workspace.remote.RemoteWorkspace.host`

```python
host: str = Field(description='The remote host URL for the workspace.')
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.model_post_init`

```python
model_post_init(context)
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.workspace.remote.RemoteWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

#### `openhands.sdk.workspace.remote.async_remote_workspace`

**Classes:**

- [**AsyncRemoteWorkspace**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace) – Async Remote Workspace Implementation.

##### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace`

Bases: <code>[RemoteWorkspaceMixin](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin)</code>

Async Remote Workspace Implementation.

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.execute_command) – Execute a bash command on the remote system.
- [**file_download**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.file_download) – Download a file from the remote system.
- [**file_upload**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.file_upload) – Upload a file to the remote system.
- [**git_changes**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_post_init**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.model_post_init) –

**Attributes:**

- [**api_key**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.api_key) (<code>[str](#str) | None</code>) –
- [**client**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.client) (<code>[AsyncClient](#httpx.AsyncClient)</code>) –
- [**host**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.host) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.working_dir) (<code>[str](#str)</code>) –

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.api_key`

```python
api_key: str | None = Field(default=None, description='API key for authenticating with the remote host.')
```

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.client`

```python
client: httpx.AsyncClient
```

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command on the remote system.

This method starts a bash command via the remote agent server API,
then polls for the output until the command completes.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result with stdout, stderr, exit_code, and other metadata

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file on remote system
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be saved locally

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the local source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be uploaded on remote system

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.host`

```python
host: str = Field(description='The remote host URL for the workspace.')
```

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.model_post_init`

```python
model_post_init(context)
```

###### `openhands.sdk.workspace.remote.async_remote_workspace.AsyncRemoteWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

#### `openhands.sdk.workspace.remote.base`

**Classes:**

- [**RemoteWorkspace**](#openhands.sdk.workspace.remote.base.RemoteWorkspace) – Remote Workspace Implementation.

##### `openhands.sdk.workspace.remote.base.RemoteWorkspace`

Bases: <code>[RemoteWorkspaceMixin](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin)</code>, <code>[BaseWorkspace](#openhands.sdk.workspace.base.BaseWorkspace)</code>

Remote Workspace Implementation.

**Functions:**

- [**execute_command**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.execute_command) – Execute a bash command on the remote system.
- [**file_download**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.file_download) – Download a file from the remote system.
- [**file_upload**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.file_upload) – Upload a file to the remote system.
- [**get_serializable_type**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.get_serializable_type) – Custom method to get the union of all currently loaded
- [**git_changes**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.git_changes) – Get the git changes for the repository at the path given.
- [**git_diff**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.git_diff) – Get the git diff for the file at the path given.
- [**model_dump_json**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_json_schema) –
- [**model_post_init**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_post_init) –
- [**model_rebuild**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_rebuild) –
- [**model_validate**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_validate) –
- [**model_validate_json**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.resolve_kind) –

**Attributes:**

- [**api_key**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.api_key) (<code>[str](#str) | None</code>) –
- [**client**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.client) (<code>[Client](#httpx.Client)</code>) –
- [**host**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.host) (<code>[str](#str)</code>) –
- [**kind**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.kind) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.remote.base.RemoteWorkspace.working_dir) (<code>[str](#str)</code>) –

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.api_key`

```python
api_key: str | None = Field(default=None, description='API key for authenticating with the remote host.')
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.client`

```python
client: httpx.Client
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.execute_command`

```python
execute_command(command, cwd=None, timeout=30.0)
```

Execute a bash command on the remote system.

This method starts a bash command via the remote agent server API,
then polls for the output until the command completes.

**Parameters:**

- **command** (<code>[str](#str)</code>) – The bash command to execute
- **cwd** (<code>[str](#str) | [Path](#pathlib.Path) | None</code>) – Working directory (optional)
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds

**Returns:**

- **CommandResult** (<code>[CommandResult](#openhands.sdk.workspace.models.CommandResult)</code>) – Result with stdout, stderr, exit_code, and other metadata

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.file_download`

```python
file_download(source_path, destination_path)
```

Download a file from the remote system.

Requests the file from the remote system via HTTP API and saves it locally.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the source file on remote system
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be saved locally

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.file_upload`

```python
file_upload(source_path, destination_path)
```

Upload a file to the remote system.

Reads the local file and sends it to the remote system via HTTP API.

**Parameters:**

- **source_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the local source file
- **destination_path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path where the file should be uploaded on remote system

**Returns:**

- **FileOperationResult** (<code>[FileOperationResult](#openhands.sdk.workspace.models.FileOperationResult)</code>) – Result with success status and metadata

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.git_changes`

```python
git_changes(path)
```

Get the git changes for the repository at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the git repository

**Returns:**

- <code>[list](#list)\[[GitChange](#openhands.sdk.git.models.GitChange)\]</code> – list\[GitChange\]: List of changes

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting changes failed

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.git_diff`

```python
git_diff(path)
```

Get the git diff for the file at the path given.

**Parameters:**

- **path** (<code>[str](#str) | [Path](#pathlib.Path)</code>) – Path to the file

**Returns:**

- **GitDiff** (<code>[GitDiff](#openhands.sdk.git.models.GitDiff)</code>) – Git diff

**Raises:**

- <code>[Exception](#Exception)</code> – If path is not a git repository or getting diff failed

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.host`

```python
host: str = Field(description='The remote host URL for the workspace.')
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.kind`

```python
kind: str = Field(default='')
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.model_dump_json`

```python
model_dump_json(**kwargs)
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.model_post_init`

```python
model_post_init(context)
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.model_validate`

```python
model_validate(obj, **kwargs)
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.resolve_kind`

```python
resolve_kind(kind)
```

###### `openhands.sdk.workspace.remote.base.RemoteWorkspace.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

#### `openhands.sdk.workspace.remote.remote_workspace_mixin`

**Classes:**

- [**RemoteWorkspaceMixin**](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin) – Mixin providing remote workspace operations.

##### `openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Mixin providing remote workspace operations.
This allows the same code to be used for sync and async.

**Functions:**

- [**model_post_init**](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.model_post_init) –

**Attributes:**

- [**api_key**](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.api_key) (<code>[str](#str) | None</code>) –
- [**host**](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.host) (<code>[str](#str)</code>) –
- [**working_dir**](#openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.working_dir) (<code>[str](#str)</code>) –

###### `openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.api_key`

```python
api_key: str | None = Field(default=None, description='API key for authenticating with the remote host.')
```

###### `openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.host`

```python
host: str = Field(description='The remote host URL for the workspace.')
```

###### `openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.model_post_init`

```python
model_post_init(context)
```

###### `openhands.sdk.workspace.remote.remote_workspace_mixin.RemoteWorkspaceMixin.working_dir`

```python
working_dir: str = Field(description='The working directory for agent operations and tool execution.')
```

### `openhands.sdk.workspace.workspace`

**Classes:**

- [**Workspace**](#openhands.sdk.workspace.workspace.Workspace) – Factory entrypoint that returns a LocalWorkspace or RemoteWorkspace.

**Attributes:**

- [**logger**](#openhands.sdk.workspace.workspace.logger) –

#### `openhands.sdk.workspace.workspace.Workspace`

Factory entrypoint that returns a LocalWorkspace or RemoteWorkspace.

<details class="usage" open markdown="1">
<summary>Usage</summary>

- Workspace(working_dir=...) -> LocalWorkspace
- Workspace(working_dir=..., host="http://...") -> RemoteWorkspace

</details>

#### `openhands.sdk.workspace.workspace.logger`

```python
logger = get_logger(__name__)
```
