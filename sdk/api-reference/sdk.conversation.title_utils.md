---
title: openhands.sdk.conversation.title_utils
description: API reference for openhands.sdk.conversation.title_utils
---

# openhands.sdk.conversation.title_utils module

<a id="module-openhands.sdk.conversation.title_utils"></a>

Utility functions for generating conversation titles.

### openhands.sdk.conversation.title_utils.extract_first_user_message(events: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)]) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

Extract the first user message from conversation events.

Parameters:
  events – List of conversation events.
Returns:
  The first user message text, or None if no user message is found.

### openhands.sdk.conversation.title_utils.generate_title_with_llm(message: [str](https://docs.python.org/3/library/stdtypes.html#str), llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM), max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

Generate a conversation title using LLM.

Parameters:
  * message – The first user message to generate title from.
  * llm – The LLM to use for title generation.
  * max_length – Maximum length of the generated title.
Returns:
  Generated title, or None if LLM fails or returns empty response.

### openhands.sdk.conversation.title_utils.generate_fallback_title(message: [str](https://docs.python.org/3/library/stdtypes.html#str), max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a fallback title by truncating the first user message.

Parameters:
  * message – The first user message.
  * max_length – Maximum length of the title.
Returns:
  A truncated title.

### openhands.sdk.conversation.title_utils.generate_conversation_title(events: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_length: [int](https://docs.python.org/3/library/functions.html#int) = 50) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Generate a title for a conversation based on the first user message.

This is the main utility function that orchestrates the title generation process:
1. Extract the first user message from events
2. Try to generate title using LLM
3. Fall back to simple truncation if LLM fails

Parameters:
  * events – List of conversation events.
  * llm – Optional LLM to use for title generation.
  * max_length – Maximum length of the generated title.
Returns:
  A generated title for the conversation.
Raises:
  [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If no user messages are found in the conversation events.
