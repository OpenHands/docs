---
title: openhands.sdk.utils.async_executor
description: API reference for openhands.sdk.utils.async_executor
---

# openhands.sdk.utils.async_executor module

<a id="module-openhands.sdk.utils.async_executor"></a>

Reusable async-to-sync execution utility.

### *class* openhands.sdk.utils.async_executor.AsyncExecutor

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Manages a background event loop for executing async code from sync contexts.

This provides a robust async-to-sync bridge with proper resource management,
timeout support, and thread safety.

#### \_\_init_\_()

#### run_async

**Parameters:**

- `awaitable_or_fn: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [Any](https://docs.python.org/3/library/typing.html#typing.Any)`
- `\*args`
- `timeout: [float](https://docs.python.org/3/library/functions.html#float) = 300.0`
- `\*\*kwargs) → [Any](https://docs.python.org/3/library/typing.html#typing.Any`


Run a coroutine or async function on the background loop from sync code.

* **Parameters:**
  * **awaitable_or_fn** – Coroutine or async function to execute
  * **\*args** – Arguments to pass to the function
  * **timeout** – Timeout in seconds (default: 300)
  * **\*\*kwargs** – Keyword arguments to pass to the function
* **Returns:**
  The result of the async operation
* **Raises:**
  * [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError) – If awaitable_or_fn is not a coroutine or async function
  * [**asyncio.TimeoutError**](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.TimeoutError) – If the operation times out

#### close()

Close the async executor and cleanup resources.

#### \_\_del_\_()

Cleanup on deletion.
