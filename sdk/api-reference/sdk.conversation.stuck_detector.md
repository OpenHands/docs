---
title: openhands.sdk.conversation.stuck_detector
description: API reference for openhands.sdk.conversation.stuck_detector
---

# openhands.sdk.conversation.stuck_detector module

<a id="module-openhands.sdk.conversation.stuck_detector"></a>

### *class* openhands.sdk.conversation.stuck_detector.StuckDetector

**Parameters:**

- `state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)`


Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Detects when an agent is stuck in repetitive or unproductive patterns.

This detector analyzes the conversation history to identify various stuck patterns:
1. Repeating action-observation cycles
2. Repeating action-error cycles
3. Agent monologue (repeated messages without user input)
4. Repeating alternating action-observation patterns
5. Context window errors indicating memory issues

#### \_\_init_\_(state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState))

#### state *: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)*

#### is_stuck() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if the agent is currently stuck.
