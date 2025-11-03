---
title: openhands.sdk.conversation.fifo_lock
description: API reference for openhands.sdk.conversation.fifo_lock
---

# openhands.sdk.conversation.fifo_lock module

<a id="module-openhands.sdk.conversation.fifo_lock"></a>

FIFO Lock implementation that guarantees first-in-first-out access ordering.

This provides fair lock access where threads acquire the lock in the exact order
they requested it, preventing starvation that can occur with standard RLock.

### *class* openhands.sdk.conversation.fifo_lock.FIFOLock

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A reentrant lock that guarantees FIFO (first-in-first-out) access ordering.

Unlike Python’s standard RLock, this lock ensures that threads acquire
the lock in the exact order they requested it, providing fairness and
preventing lock starvation.

Features:
- Reentrant: Same thread can acquire multiple times
- FIFO ordering: Threads get lock in request order
- Context manager support: Use with ‘with’ statement
- Thread-safe: Safe for concurrent access

#### \_\_init_\_() → [None](https://docs.python.org/3/library/constants.html#None)

#### acquire(blocking: [bool](https://docs.python.org/3/library/functions.html#bool) = True, timeout: [float](https://docs.python.org/3/library/functions.html#float) = -1) → [bool](https://docs.python.org/3/library/functions.html#bool)

Acquire the lock.

* **Parameters:**
  * **blocking** – If True, block until lock is acquired. If False, return
    immediately.
  * **timeout** – Maximum time to wait for lock (ignored if blocking=False).
    -1 means wait indefinitely.
* **Returns:**
  True if lock was acquired, False otherwise.

#### release() → [None](https://docs.python.org/3/library/constants.html#None)

Release the lock.

* **Raises:**
  [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) – If the current thread doesn’t own the lock.

#### \_\_enter_\_() → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

Context manager entry.

#### \_\_exit_\_(exc_type: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_val: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_tb: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Context manager exit.

#### locked() → [bool](https://docs.python.org/3/library/functions.html#bool)

Return True if the lock is currently held by any thread.

#### owned() → [bool](https://docs.python.org/3/library/functions.html#bool)

Return True if the lock is currently held by the calling thread.
