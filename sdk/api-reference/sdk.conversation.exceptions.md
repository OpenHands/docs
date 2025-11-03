---
title: openhands.sdk.conversation.exceptions
description: API reference for openhands.sdk.conversation.exceptions
---

# openhands.sdk.conversation.exceptions module

<a id="module-openhands.sdk.conversation.exceptions"></a>

### *exception* openhands.sdk.conversation.exceptions.ConversationRunError(conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID), original_exception: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException), message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError)

Raised when a conversation run fails.

Carries the conversation_id to make resuming/debugging easier while
preserving the original exception via exception chaining.

#### \_\_init_\_(conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID), original_exception: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException), message: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [None](https://docs.python.org/3/library/constants.html#None)

#### conversation_id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

#### original_exception *: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)*
