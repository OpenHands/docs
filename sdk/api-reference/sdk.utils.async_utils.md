---
title: openhands.sdk.utils.async_utils
description: API reference for openhands.sdk.utils.async_utils
---

# openhands.sdk.utils.async_utils module

<a id="module-openhands.sdk.utils.async_utils"></a>

Async utilities for OpenHands SDK.

This module provides utilities for working with async callbacks in the context
of synchronous conversation handling.

### class openhands.sdk.utils.async_utils.AsyncCallbackWrapper(async_callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [Coroutine](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine)[[Any](https://docs.python.org/3/library/typing.html#typing.Any), [Any](https://docs.python.org/3/library/typing.html#typing.Any), [None](https://docs.python.org/3/library/constants.html#None)]], loop: AbstractEventLoop)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Wrapper that executes async callbacks in a different thread’s event loop.

This class implements the ConversationCallbackType interface (synchronous)
but internally executes an async callback in an event loop running in a
different thread. This allows async callbacks to be used in synchronous
conversation contexts.

#### \_\_init_\_(async_callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [Coroutine](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine)[[Any](https://docs.python.org/3/library/typing.html#typing.Any), [Any](https://docs.python.org/3/library/typing.html#typing.Any), [None](https://docs.python.org/3/library/constants.html#None)]], loop: AbstractEventLoop)

#### async_callback : [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [Coroutine](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine)[[Any](https://docs.python.org/3/library/typing.html#typing.Any), [Any](https://docs.python.org/3/library/typing.html#typing.Any), [None](https://docs.python.org/3/library/constants.html#None)]]

#### loop : AbstractEventLoop
