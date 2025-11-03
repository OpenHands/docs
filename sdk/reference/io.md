## `openhands.sdk.io`

**Modules:**

- [**base**](#openhands.sdk.io.base) –
- [**local**](#openhands.sdk.io.local) –
- [**memory**](#openhands.sdk.io.memory) –

**Classes:**

- [**FileStore**](#openhands.sdk.io.FileStore) – Abstract base class for file storage operations.
- [**InMemoryFileStore**](#openhands.sdk.io.InMemoryFileStore) –
- [**LocalFileStore**](#openhands.sdk.io.LocalFileStore) –

### `openhands.sdk.io.FileStore`

Bases: <code>[ABC](#abc.ABC)</code>

Abstract base class for file storage operations.

This class defines the interface for file storage backends that can
handle basic file operations like reading, writing, listing, and deleting files.

**Functions:**

- [**delete**](#openhands.sdk.io.FileStore.delete) – Delete the file or directory at the specified path.
- [**list**](#openhands.sdk.io.FileStore.list) – List all files and directories at the specified path.
- [**read**](#openhands.sdk.io.FileStore.read) – Read and return the contents of a file as a string.
- [**write**](#openhands.sdk.io.FileStore.write) – Write contents to a file at the specified path.

#### `openhands.sdk.io.FileStore.delete`

```python
delete(path)
```

Delete the file or directory at the specified path.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The file or directory path to delete.

#### `openhands.sdk.io.FileStore.list`

```python
list(path)
```

List all files and directories at the specified path.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The directory path to list contents from.

**Returns:**

- <code>[list](#openhands.sdk.io.base.FileStore.list)\[[str](#str)\]</code> – A list of file and directory names in the specified path.

#### `openhands.sdk.io.FileStore.read`

```python
read(path)
```

Read and return the contents of a file as a string.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The file path to read from.

**Returns:**

- <code>[str](#str)</code> – The file contents as a string.

#### `openhands.sdk.io.FileStore.write`

```python
write(path, contents)
```

Write contents to a file at the specified path.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The file path where contents should be written.
- **contents** (<code>[str](#str) | [bytes](#bytes)</code>) – The data to write, either as string or bytes.

### `openhands.sdk.io.InMemoryFileStore`

```python
InMemoryFileStore(files=None)
```

Bases: <code>[FileStore](#openhands.sdk.io.base.FileStore)</code>

**Functions:**

- [**delete**](#openhands.sdk.io.InMemoryFileStore.delete) –
- [**list**](#openhands.sdk.io.InMemoryFileStore.list) –
- [**read**](#openhands.sdk.io.InMemoryFileStore.read) –
- [**write**](#openhands.sdk.io.InMemoryFileStore.write) –

**Attributes:**

- [**files**](#openhands.sdk.io.InMemoryFileStore.files) (<code>[dict](#dict)\[[str](#str), [str](#str)\]</code>) –

#### `openhands.sdk.io.InMemoryFileStore.delete`

```python
delete(path)
```

#### `openhands.sdk.io.InMemoryFileStore.files`

```python
files: dict[str, str] = {}
```

#### `openhands.sdk.io.InMemoryFileStore.list`

```python
list(path)
```

#### `openhands.sdk.io.InMemoryFileStore.read`

```python
read(path)
```

#### `openhands.sdk.io.InMemoryFileStore.write`

```python
write(path, contents)
```

### `openhands.sdk.io.LocalFileStore`

```python
LocalFileStore(root)
```

Bases: <code>[FileStore](#openhands.sdk.io.base.FileStore)</code>

**Functions:**

- [**delete**](#openhands.sdk.io.LocalFileStore.delete) –
- [**get_full_path**](#openhands.sdk.io.LocalFileStore.get_full_path) –
- [**list**](#openhands.sdk.io.LocalFileStore.list) –
- [**read**](#openhands.sdk.io.LocalFileStore.read) –
- [**write**](#openhands.sdk.io.LocalFileStore.write) –

**Attributes:**

- [**root**](#openhands.sdk.io.LocalFileStore.root) (<code>[str](#str)</code>) –

#### `openhands.sdk.io.LocalFileStore.delete`

```python
delete(path)
```

#### `openhands.sdk.io.LocalFileStore.get_full_path`

```python
get_full_path(path)
```

#### `openhands.sdk.io.LocalFileStore.list`

```python
list(path)
```

#### `openhands.sdk.io.LocalFileStore.read`

```python
read(path)
```

#### `openhands.sdk.io.LocalFileStore.root`

```python
root: str = root
```

#### `openhands.sdk.io.LocalFileStore.write`

```python
write(path, contents)
```

### `openhands.sdk.io.base`

**Classes:**

- [**FileStore**](#openhands.sdk.io.base.FileStore) – Abstract base class for file storage operations.

#### `openhands.sdk.io.base.FileStore`

Bases: <code>[ABC](#abc.ABC)</code>

Abstract base class for file storage operations.

This class defines the interface for file storage backends that can
handle basic file operations like reading, writing, listing, and deleting files.

**Functions:**

- [**delete**](#openhands.sdk.io.base.FileStore.delete) – Delete the file or directory at the specified path.
- [**list**](#openhands.sdk.io.base.FileStore.list) – List all files and directories at the specified path.
- [**read**](#openhands.sdk.io.base.FileStore.read) – Read and return the contents of a file as a string.
- [**write**](#openhands.sdk.io.base.FileStore.write) – Write contents to a file at the specified path.

##### `openhands.sdk.io.base.FileStore.delete`

```python
delete(path)
```

Delete the file or directory at the specified path.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The file or directory path to delete.

##### `openhands.sdk.io.base.FileStore.list`

```python
list(path)
```

List all files and directories at the specified path.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The directory path to list contents from.

**Returns:**

- <code>[list](#openhands.sdk.io.base.FileStore.list)\[[str](#str)\]</code> – A list of file and directory names in the specified path.

##### `openhands.sdk.io.base.FileStore.read`

```python
read(path)
```

Read and return the contents of a file as a string.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The file path to read from.

**Returns:**

- <code>[str](#str)</code> – The file contents as a string.

##### `openhands.sdk.io.base.FileStore.write`

```python
write(path, contents)
```

Write contents to a file at the specified path.

**Parameters:**

- **path** (<code>[str](#str)</code>) – The file path where contents should be written.
- **contents** (<code>[str](#str) | [bytes](#bytes)</code>) – The data to write, either as string or bytes.

### `openhands.sdk.io.local`

**Classes:**

- [**LocalFileStore**](#openhands.sdk.io.local.LocalFileStore) –

**Attributes:**

- [**logger**](#openhands.sdk.io.local.logger) –

#### `openhands.sdk.io.local.LocalFileStore`

```python
LocalFileStore(root)
```

Bases: <code>[FileStore](#openhands.sdk.io.base.FileStore)</code>

**Functions:**

- [**delete**](#openhands.sdk.io.local.LocalFileStore.delete) –
- [**get_full_path**](#openhands.sdk.io.local.LocalFileStore.get_full_path) –
- [**list**](#openhands.sdk.io.local.LocalFileStore.list) –
- [**read**](#openhands.sdk.io.local.LocalFileStore.read) –
- [**write**](#openhands.sdk.io.local.LocalFileStore.write) –

**Attributes:**

- [**root**](#openhands.sdk.io.local.LocalFileStore.root) (<code>[str](#str)</code>) –

##### `openhands.sdk.io.local.LocalFileStore.delete`

```python
delete(path)
```

##### `openhands.sdk.io.local.LocalFileStore.get_full_path`

```python
get_full_path(path)
```

##### `openhands.sdk.io.local.LocalFileStore.list`

```python
list(path)
```

##### `openhands.sdk.io.local.LocalFileStore.read`

```python
read(path)
```

##### `openhands.sdk.io.local.LocalFileStore.root`

```python
root: str = root
```

##### `openhands.sdk.io.local.LocalFileStore.write`

```python
write(path, contents)
```

#### `openhands.sdk.io.local.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.io.memory`

**Classes:**

- [**InMemoryFileStore**](#openhands.sdk.io.memory.InMemoryFileStore) –

**Attributes:**

- [**logger**](#openhands.sdk.io.memory.logger) –

#### `openhands.sdk.io.memory.InMemoryFileStore`

```python
InMemoryFileStore(files=None)
```

Bases: <code>[FileStore](#openhands.sdk.io.base.FileStore)</code>

**Functions:**

- [**delete**](#openhands.sdk.io.memory.InMemoryFileStore.delete) –
- [**list**](#openhands.sdk.io.memory.InMemoryFileStore.list) –
- [**read**](#openhands.sdk.io.memory.InMemoryFileStore.read) –
- [**write**](#openhands.sdk.io.memory.InMemoryFileStore.write) –

**Attributes:**

- [**files**](#openhands.sdk.io.memory.InMemoryFileStore.files) (<code>[dict](#dict)\[[str](#str), [str](#str)\]</code>) –

##### `openhands.sdk.io.memory.InMemoryFileStore.delete`

```python
delete(path)
```

##### `openhands.sdk.io.memory.InMemoryFileStore.files`

```python
files: dict[str, str] = {}
```

##### `openhands.sdk.io.memory.InMemoryFileStore.list`

```python
list(path)
```

##### `openhands.sdk.io.memory.InMemoryFileStore.read`

```python
read(path)
```

##### `openhands.sdk.io.memory.InMemoryFileStore.write`

```python
write(path, contents)
```

#### `openhands.sdk.io.memory.logger`

```python
logger = get_logger(__name__)
```
