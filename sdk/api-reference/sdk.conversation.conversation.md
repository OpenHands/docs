---
title: openhands.sdk.conversation.conversation
description: API reference for openhands.sdk.conversation.conversation
---

# openhands.sdk.conversation.conversation module

<a id="module-openhands.sdk.conversation.conversation"></a>

### *class* openhands.sdk.conversation.conversation.Conversation

**Parameters:**

- `agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)`
- `workspace: [str](https://docs.python.org/3/library/stdtypes.html#str) | [LocalWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.local.md#openhands.sdk.workspace.local.LocalWorkspace) = 'workspace/project'`
- `persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500`
- `stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True`
- `visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True`
- `name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `secrets: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None`


### *class* openhands.sdk.conversation.conversation.Conversation

**Parameters:**

- `agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)`
- `workspace: [RemoteWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.remote.base.md#openhands.sdk.workspace.remote.base.RemoteWorkspace)`
- `conversation_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `callbacks: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]] | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `max_iteration_per_run: [int](https://docs.python.org/3/library/functions.html#int) = 500`
- `stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True`
- `visualize: [bool](https://docs.python.org/3/library/functions.html#bool) = True`
- `name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None`
- `secrets: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [SecretSource](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_source.md#openhands.sdk.conversation.secret_source.SecretSource)] | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None`


Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Factory entrypoint that returns a LocalConversation or RemoteConversation.

Usage:
: - Conversation(agent=…) -> LocalConversation
  - Conversation(agent=…, host=”[http://](http://)…”) -> RemoteConversation
