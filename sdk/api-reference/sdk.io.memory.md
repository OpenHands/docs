---
title: openhands.sdk.io.memory
description: API reference for openhands.sdk.io.memory
---

# openhands.sdk.io.memory module

<a id="module-openhands.sdk.io.memory"></a>

### *class* openhands.sdk.io.memory.InMemoryFileStore(files: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`FileStore`](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore)

#### \_\_init_\_(files: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None) → [None](https://docs.python.org/3/library/constants.html#None)

#### files *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### write(path: [str](https://docs.python.org/3/library/stdtypes.html#str), contents: [str](https://docs.python.org/3/library/stdtypes.html#str) | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) → [None](https://docs.python.org/3/library/constants.html#None)

Write contents to a file at the specified path.

* **Parameters:**
  * **path** – The file path where contents should be written.
  * **contents** – The data to write, either as string or bytes.

#### read(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Read and return the contents of a file as a string.

* **Parameters:**
  **path** – The file path to read from.
* **Returns:**
  The file contents as a string.

#### list(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

List all files and directories at the specified path.

* **Parameters:**
  **path** – The directory path to list contents from.
* **Returns:**
  A list of file and directory names in the specified path.

#### delete(path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

Delete the file or directory at the specified path.

* **Parameters:**
  **path** – The file or directory path to delete.
