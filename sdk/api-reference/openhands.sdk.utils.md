---
title: openhands.sdk.utils
description: API reference for openhands.sdk.utils
---

# openhands.sdk.utils module

Utility functions for the OpenHands SDK.

### maybe_truncate

Truncate the middle of content if it exceeds the specified length.

Keeps the head and tail of the content to preserve context at both ends.

* Parameters:
  * content – The text content to potentially truncate
  * truncate_after – Maximum length before truncation. If None, no truncation occurs
  * truncate_notice – Notice to insert in the middle when content is truncated
* Returns:
  Original content if under limit, or truncated content with head and tail
  preserved
