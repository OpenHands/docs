---
title: openhands.sdk.conversation.visualizer
description: API reference for openhands.sdk.conversation.visualizer
---

# openhands.sdk.conversation.visualizer module

<a id="module-openhands.sdk.conversation.visualizer"></a>

### *class* openhands.sdk.conversation.visualizer.ConversationVisualizer(highlight_regex: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None, skip_user_messages: [bool](https://docs.python.org/3/library/functions.html#bool) = False, conversation_stats: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats) | [None](https://docs.python.org/3/library/constants.html#None) = None, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Handles visualization of conversation events with Rich formatting.

Provides Rich-formatted output with panels and complete content display.

#### \_\_init_\_(highlight_regex: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None, skip_user_messages: [bool](https://docs.python.org/3/library/functions.html#bool) = False, conversation_stats: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats) | [None](https://docs.python.org/3/library/constants.html#None) = None, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

Initialize the visualizer.

**Parameters:**
  * **highlight_regex** – Dictionary mapping regex patterns to Rich color styles
    for highlighting keywords in the visualizer.
    For example: {“Reasoning:”: “bold blue”,
    “Thought:”: “bold green”}
  * **skip_user_messages** – If True, skip displaying user messages. Useful for
    scenarios where user input is not relevant to show.
  * **conversation_stats** – ConversationStats object to display metrics information.
  * **name_for_visualization** – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.

#### on_event(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [None](https://docs.python.org/3/library/constants.html#None)

Main event handler that displays events with Rich formatting.

### openhands.sdk.conversation.visualizer.create_default_visualizer(highlight_regex: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None, conversation_stats: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats) | [None](https://docs.python.org/3/library/constants.html#None) = None, name_for_visualization: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, \*\*kwargs) → [ConversationVisualizer](#openhands.sdk.conversation.visualizer.ConversationVisualizer)

Create a default conversation visualizer instance.

**Parameters:**
  * **highlight_regex** – Dictionary mapping regex patterns to Rich color styles
    for highlighting keywords in the visualizer.
    For example: {“Reasoning:”: “bold blue”,
    “Thought:”: “bold green”}
  * **conversation_stats** – ConversationStats object to display metrics information.
  * **name_for_visualization** – Optional name to prefix in panel titles to identify
    which agent/conversation is speaking.
