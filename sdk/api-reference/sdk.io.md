---
title: openhands.sdk.io
description: API reference for openhands.sdk.io
---

# openhands.sdk.io package

<a id="module-openhands.sdk.io"></a>

### *class* openhands.sdk.io.LocalFileStore(root: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`FileStore`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore)

#### \_\_init_\_(root: [str](https://docs.python.org/3/library/stdtypes.html#str))

#### delete(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

Delete the file or directory at the specified path.

Parameters:
  path – The file or directory path to delete.

#### get_full_path(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

#### list(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

List all files and directories at the specified path.

Parameters:
  path – The directory path to list contents from.
Returns:
  A list of file and directory names in the specified path.

#### read(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Read and return the contents of a file as a string.

Parameters:
  path – The file path to read from.
Returns:
  The file contents as a string.

#### write(path: [str](https://docs.python.org/3/library/stdtypes.html#str), contents: [str](https://docs.python.org/3/library/stdtypes.html#str) | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) → [None](https://docs.python.org/3/library/constants.html#None)

Write contents to a file at the specified path.

Parameters:
  * path – The file path where contents should be written.
  * contents – The data to write, either as string or bytes.

#### root : [str](https://docs.python.org/3/library/stdtypes.html#str)

### *class* openhands.sdk.io.FileStore

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for file storage operations.

This class defines the interface for file storage backends that can
handle basic file operations like reading, writing, listing, and deleting files.

#### abstractmethod delete(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

Delete the file or directory at the specified path.

Parameters:
  path – The file or directory path to delete.

#### abstractmethod list(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

List all files and directories at the specified path.

Parameters:
  path – The directory path to list contents from.
Returns:
  A list of file and directory names in the specified path.

#### abstractmethod read(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Read and return the contents of a file as a string.

Parameters:
  path – The file path to read from.
Returns:
  The file contents as a string.

#### abstractmethod write(path: [str](https://docs.python.org/3/library/stdtypes.html#str), contents: [str](https://docs.python.org/3/library/stdtypes.html#str) | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) → [None](https://docs.python.org/3/library/constants.html#None)

Write contents to a file at the specified path.

Parameters:
  * path – The file path where contents should be written.
  * contents – The data to write, either as string or bytes.

### *class* openhands.sdk.io.InMemoryFileStore(files: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`FileStore`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore)

#### \_\_init_\_(files: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → [None](https://docs.python.org/3/library/constants.html#None)

#### delete(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

Delete the file or directory at the specified path.

Parameters:
  path – The file or directory path to delete.

#### list(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

List all files and directories at the specified path.

Parameters:
  path – The directory path to list contents from.
Returns:
  A list of file and directory names in the specified path.

#### read(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Read and return the contents of a file as a string.

Parameters:
  path – The file path to read from.
Returns:
  The file contents as a string.

#### write(path: [str](https://docs.python.org/3/library/stdtypes.html#str), contents: [str](https://docs.python.org/3/library/stdtypes.html#str) | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) → [None](https://docs.python.org/3/library/constants.html#None)

Write contents to a file at the specified path.

Parameters:
  * path – The file path where contents should be written.
  * contents – The data to write, either as string or bytes.

#### files : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]

## Submodules

* [openhands.sdk.io.base module](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md)
  * [`FileStore`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore)
    * [`FileStore.write()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore.write)
    * [`FileStore.read()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore.read)
    * [`FileStore.list()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore.list)
    * [`FileStore.delete()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore.delete)
* [openhands.sdk.io.local module](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md)
  * [`LocalFileStore`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore)
    * [`LocalFileStore.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore.__init__)
    * [`LocalFileStore.root`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore.root)
    * [`LocalFileStore.get_full_path()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore.get_full_path)
    * [`LocalFileStore.write()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore.write)
    * [`LocalFileStore.read()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore.read)
    * [`LocalFileStore.list()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore.list)
    * [`LocalFileStore.delete()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.local.md#openhands.sdk.io.local.LocalFileStore.delete)
* [openhands.sdk.io.memory module](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md)
  * [`InMemoryFileStore`](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md#openhands.sdk.io.memory.InMemoryFileStore)
    * [`InMemoryFileStore.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md#openhands.sdk.io.memory.InMemoryFileStore.__init__)
    * [`InMemoryFileStore.files`](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md#openhands.sdk.io.memory.InMemoryFileStore.files)
    * [`InMemoryFileStore.write()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md#openhands.sdk.io.memory.InMemoryFileStore.write)
    * [`InMemoryFileStore.read()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md#openhands.sdk.io.memory.InMemoryFileStore.read)
    * [`InMemoryFileStore.list()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md#openhands.sdk.io.memory.InMemoryFileStore.list)
    * [`InMemoryFileStore.delete()`](https://github.com/OpenHands/software-agent-sdk/sdk.io.memory.md#openhands.sdk.io.memory.InMemoryFileStore.delete)
