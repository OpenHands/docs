---
title: openhands.sdk.conversation.event_store
description: API reference for openhands.sdk.conversation.event_store
---

# openhands.sdk.conversation.event_store module

<a id="module-openhands.sdk.conversation.event_store"></a>

### class openhands.sdk.conversation.event_store.EventLog(fs: [FileStore](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore), dir_path: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'events')

Bases: [`EventsListBase`](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.events_list_base.md#openhands.sdk.conversation.events_list_base.EventsListBase)

#### \_\_init_\_(fs: [FileStore](https://github.com/OpenHands/software-agent-sdk/sdk.io.base.md#openhands.sdk.io.base.FileStore), dir_path: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'events') → [None](https://docs.python.org/3/library/constants.html#None)

#### get_index(event_id: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [int](https://docs.python.org/3/library/functions.html#int)

Return the integer index for a given event_id.

#### get_id(idx: [int](https://docs.python.org/3/library/functions.html#int)) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Return the event_id for a given index.

#### append(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Add a new event to the list.
