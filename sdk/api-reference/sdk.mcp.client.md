---
title: openhands.sdk.mcp.client
description: API reference for openhands.sdk.mcp.client
---

# openhands.sdk.mcp.client module

<a id="module-openhands.sdk.mcp.client"></a>

Minimal sync helpers on top of fastmcp.Client, preserving original behavior.

### *class* openhands.sdk.mcp.client.MCPClient(\*args, \*\*kwargs)

Bases: `Client`

Behaves exactly like fastmcp.Client (same constructor & async API),
but owns a background event loop and offers:

> - call_async_from_sync(awaitable_or_fn, 

>   ```
>   *
>   ```

>   args, timeout=None, 

>   ```
>   **
>   ```

>   kwargs)
> - call_sync_from_async(fn, 

>   ```
>   *
>   ```

>   args, 

>   ```
>   **
>   ```

>   kwargs)  # await this from async code

#### \_\_init_\_(\*args, \*\*kwargs)

#### call_async_from_sync(awaitable_or_fn: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)] | [Any](https://docs.python.org/3/library/typing.html#typing.Any), \*args, timeout: [float](https://docs.python.org/3/library/functions.html#float), \*\*kwargs) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)

Run a coroutine or async function on this client’s loop from sync code.

Usage:
: mcp.call_async_from_sync(async_fn, arg1, kw=…)
  mcp.call_async_from_sync(coro)

#### *async* call_sync_from_async(fn: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)], \*args, \*\*kwargs) → [Any](https://docs.python.org/3/library/typing.html#typing.Any)

Await running a blocking function in the default threadpool from async code.

#### sync_close() → [None](https://docs.python.org/3/library/constants.html#None)

Synchronously close the MCP client and cleanup resources.

This will attempt to call the async close() method if available,
then shutdown the background event loop.

#### \_\_del_\_()

Cleanup on deletion.
