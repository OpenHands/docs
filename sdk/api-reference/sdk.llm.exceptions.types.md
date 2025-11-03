---
title: openhands.sdk.llm.exceptions.types
description: API reference for openhands.sdk.llm.exceptions.types
---

# openhands.sdk.llm.exceptions.types module

<a id="module-openhands.sdk.llm.exceptions.types"></a>

### *exception* openhands.sdk.llm.exceptions.types.LLMError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

#### message : [str](https://docs.python.org/3/library/stdtypes.html#str)

### *exception* openhands.sdk.llm.exceptions.types.LLMMalformedActionError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Malformed response')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Malformed response') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMNoActionError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Agent must return an action')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Agent must return an action') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMResponseError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Failed to retrieve action from LLM response')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Failed to retrieve action from LLM response') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.FunctionCallConversionError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.FunctionCallValidationError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.FunctionCallNotExistsError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMNoResponseError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM did not return a response. This is only seen in Gemini models so far.')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM did not return a response. This is only seen in Gemini models so far.') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMContextWindowExceedError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Conversation history longer than LLM context window limit. Consider enabling a condenser or shortening inputs.')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Conversation history longer than LLM context window limit. Consider enabling a condenser or shortening inputs.') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMAuthenticationError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Invalid or missing API credentials')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Invalid or missing API credentials') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMRateLimitError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Rate limit exceeded')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Rate limit exceeded') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMTimeoutError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM request timed out')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM request timed out') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMServiceUnavailableError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM service unavailable')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM service unavailable') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.LLMBadRequestError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Bad request to LLM provider')

Bases: [`LLMError`](#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Bad request to LLM provider') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.UserCancelledError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User cancelled the request')

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User cancelled the request') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.types.OperationCancelled(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Operation was cancelled')

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Operation was cancelled') → [None](https://docs.python.org/3/library/constants.html#None)
