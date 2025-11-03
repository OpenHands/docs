---
title: openhands.sdk.llm.exceptions
description: API reference for openhands.sdk.llm.exceptions
---

# openhands.sdk.llm.exceptions package

<a id="module-openhands.sdk.llm.exceptions"></a>

### *exception* openhands.sdk.llm.exceptions.LLMError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

#### message : [str](https://docs.python.org/3/library/stdtypes.html#str)

### *exception* openhands.sdk.llm.exceptions.LLMMalformedActionError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Malformed response')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Malformed response') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMNoActionError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Agent must return an action')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Agent must return an action') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMResponseError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Failed to retrieve action from LLM response')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Failed to retrieve action from LLM response') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.FunctionCallConversionError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.FunctionCallValidationError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.FunctionCallNotExistsError(message: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMNoResponseError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM did not return a response. This is only seen in Gemini models so far.')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM did not return a response. This is only seen in Gemini models so far.') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMContextWindowExceedError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Conversation history longer than LLM context window limit. Consider enabling a condenser or shortening inputs.')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Conversation history longer than LLM context window limit. Consider enabling a condenser or shortening inputs.') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMAuthenticationError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Invalid or missing API credentials')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Invalid or missing API credentials') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMRateLimitError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Rate limit exceeded')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Rate limit exceeded') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMTimeoutError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM request timed out')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM request timed out') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMServiceUnavailableError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM service unavailable')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM service unavailable') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.LLMBadRequestError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Bad request to LLM provider')

Bases: [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Bad request to LLM provider') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.UserCancelledError(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User cancelled the request')

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'User cancelled the request') → [None](https://docs.python.org/3/library/constants.html#None)

### *exception* openhands.sdk.llm.exceptions.OperationCancelled(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Operation was cancelled')

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

#### \_\_init_\_(message: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'Operation was cancelled') → [None](https://docs.python.org/3/library/constants.html#None)

### openhands.sdk.llm.exceptions.is_context_window_exceeded(exception: [Exception](https://docs.python.org/3/library/exceptions.html#Exception)) → [bool](https://docs.python.org/3/library/functions.html#bool)

### openhands.sdk.llm.exceptions.looks_like_auth_error(exception: [Exception](https://docs.python.org/3/library/exceptions.html#Exception)) → [bool](https://docs.python.org/3/library/functions.html#bool)

### openhands.sdk.llm.exceptions.map_provider_exception(exception: [Exception](https://docs.python.org/3/library/exceptions.html#Exception)) → [Exception](https://docs.python.org/3/library/exceptions.html#Exception)

Map provider/LiteLLM exceptions to SDK-typed exceptions.

Returns original exception if no mapping applies.

## Submodules

* [openhands.sdk.llm.exceptions.classifier module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.classifier.md)
  * [`is_context_window_exceeded()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.classifier.md#openhands.sdk.llm.exceptions.classifier.is_context_window_exceeded)
  * [`looks_like_auth_error()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.classifier.md#openhands.sdk.llm.exceptions.classifier.looks_like_auth_error)
* [openhands.sdk.llm.exceptions.mapping module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.mapping.md)
  * [`map_provider_exception()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.mapping.md#openhands.sdk.llm.exceptions.mapping.map_provider_exception)
* [openhands.sdk.llm.exceptions.types module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md)
  * [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)
    * [`LLMError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError.__init__)
    * [`LLMError.message`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError.message)
  * [`LLMMalformedActionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMMalformedActionError)
    * [`LLMMalformedActionError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMMalformedActionError.__init__)
  * [`LLMNoActionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMNoActionError)
    * [`LLMNoActionError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMNoActionError.__init__)
  * [`LLMResponseError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMResponseError)
    * [`LLMResponseError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMResponseError.__init__)
  * [`FunctionCallConversionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallConversionError)
    * [`FunctionCallConversionError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallConversionError.__init__)
  * [`FunctionCallValidationError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallValidationError)
    * [`FunctionCallValidationError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallValidationError.__init__)
  * [`FunctionCallNotExistsError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallNotExistsError)
    * [`FunctionCallNotExistsError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallNotExistsError.__init__)
  * [`LLMNoResponseError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMNoResponseError)
    * [`LLMNoResponseError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMNoResponseError.__init__)
  * [`LLMContextWindowExceedError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMContextWindowExceedError)
    * [`LLMContextWindowExceedError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMContextWindowExceedError.__init__)
  * [`LLMAuthenticationError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMAuthenticationError)
    * [`LLMAuthenticationError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMAuthenticationError.__init__)
  * [`LLMRateLimitError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMRateLimitError)
    * [`LLMRateLimitError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMRateLimitError.__init__)
  * [`LLMTimeoutError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMTimeoutError)
    * [`LLMTimeoutError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMTimeoutError.__init__)
  * [`LLMServiceUnavailableError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMServiceUnavailableError)
    * [`LLMServiceUnavailableError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMServiceUnavailableError.__init__)
  * [`LLMBadRequestError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMBadRequestError)
    * [`LLMBadRequestError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMBadRequestError.__init__)
  * [`UserCancelledError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.UserCancelledError)
    * [`UserCancelledError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.UserCancelledError.__init__)
  * [`OperationCancelled`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.OperationCancelled)
    * [`OperationCancelled.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.OperationCancelled.__init__)
