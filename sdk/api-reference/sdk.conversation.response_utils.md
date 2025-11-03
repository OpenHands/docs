---
title: openhands.sdk.conversation.response_utils
description: API reference for openhands.sdk.conversation.response_utils
---

# openhands.sdk.conversation.response_utils module

<a id="module-openhands.sdk.conversation.response_utils"></a>

Utility functions for extracting agent responses from conversation events.

### openhands.sdk.conversation.response_utils.get_agent_final_response(events: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)]) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Extract the final response from the agent.

An agent can end a conversation in two ways:
1. By calling the finish tool
2. By returning a text message with no tool calls

Parameters:
  events – List of conversation events to search through.
Returns:
  The final response message from the agent, or empty string if not found.
