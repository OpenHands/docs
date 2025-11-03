---
title: openhands.sdk.conversation.events_list_base
description: API reference for openhands.sdk.conversation.events_list_base
---

# openhands.sdk.conversation.events_list_base module

<a id="module-openhands.sdk.conversation.events_list_base"></a>

### *class* openhands.sdk.conversation.events_list_base.EventsListBase

Bases: [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[`Event`](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for event lists that can be appended to.

This provides a common interface for both local EventLog and remote
RemoteEventsList implementations, avoiding circular imports in protocols.

#### *abstractmethod* append(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Add a new event to the list.
