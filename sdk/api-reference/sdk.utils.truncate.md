---
title: openhands.sdk.utils.truncate
description: API reference for openhands.sdk.utils.truncate
---

# openhands.sdk.utils.truncate module

<a id="module-openhands.sdk.utils.truncate"></a>

Utility functions for truncating text content.

### openhands.sdk.utils.truncate.maybe_truncate(content: [str](https://docs.python.org/3/library/stdtypes.html#str), truncate_after: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None, truncate_notice: [str](https://docs.python.org/3/library/stdtypes.html#str) = '<response clipped><NOTE>Due to the max output limit, only part of the full response has been shown to you.</NOTE>') → [str](https://docs.python.org/3/library/stdtypes.html#str)

Truncate the middle of content if it exceeds the specified length.

Keeps the head and tail of the content to preserve context at both ends.

* **Parameters:**
  * **content** – The text content to potentially truncate
  * **truncate_after** – Maximum length before truncation. If None, no truncation occurs
  * **truncate_notice** – Notice to insert in the middle when content is truncated
* **Returns:**
  Original content if under limit, or truncated content with head and tail
  preserved
