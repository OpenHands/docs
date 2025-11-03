---
title: openhands.sdk.io.base
description: API reference for openhands.sdk.io.base
---

# openhands.sdk.io.base module

<a id="module-openhands.sdk.io.base"></a>

### *class* openhands.sdk.io.base.FileStore

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for file storage operations.

This class defines the interface for file storage backends that can
handle basic file operations like reading, writing, listing, and deleting files.

#### *abstractmethod* write(path: [str](https://docs.python.org/3/library/stdtypes.html#str), contents: [str](https://docs.python.org/3/library/stdtypes.html#str) | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) → [None](https://docs.python.org/3/library/constants.html#None)

Write contents to a file at the specified path.

**Parameters:**
  - **path** – The file path where contents should be written.
  - **contents** – The data to write, either as string or bytes.

#### *abstractmethod* read(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Read and return the contents of a file as a string.

**Parameters:**
  **path** – The file path to read from.
**Returns:**
  The file contents as a string.

#### *abstractmethod* list(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

List all files and directories at the specified path.

**Parameters:**
  **path** – The directory path to list contents from.
**Returns:**
  A list of file and directory names in the specified path.

#### *abstractmethod* delete(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

Delete the file or directory at the specified path.

**Parameters:**
  **path** – The file or directory path to delete.
