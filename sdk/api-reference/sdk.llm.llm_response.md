---
title: openhands.sdk.llm.llm_response
description: API reference for openhands.sdk.llm.llm_response
---

# openhands.sdk.llm.llm_response module

<a id="module-openhands.sdk.llm.llm_response"></a>

LLMResponse type for LLM completion responses.

This module provides the LLMResponse type that wraps LLM completion responses
with OpenHands-native types, eliminating the need for consumers to work directly
with LiteLLM types.

### *class* openhands.sdk.llm.llm_response.LLMResponse(, message: [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message), metrics: [MetricsSnapshot](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.MetricsSnapshot), raw_response: ModelResponse | ResponsesAPIResponse)

Bases: `BaseModel`

Result of an LLM completion request.

This type provides a clean interface for LLM completion results, exposing
only OpenHands-native types to consumers while preserving access to the
raw LiteLLM response for internal use.

#### message

The completion message converted to OpenHands Message type

- **Type:**
  [openhands.sdk.llm.message.Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### metrics

Snapshot of metrics from the completion request

- **Type:**
  [openhands.sdk.llm.utils.metrics.MetricsSnapshot](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.MetricsSnapshot)

#### raw_response

The original LiteLLM response (ModelResponse or
ResponsesAPIResponse) for internal use

- **Type:**
  litellm.types.utils.ModelResponse | litellm.types.llms.openai.ResponsesAPIResponse

#### message : [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### metrics : [MetricsSnapshot](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.MetricsSnapshot)

#### raw_response : ModelResponse | ResponsesAPIResponse

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'arbitrary_types_allowed': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### property id : [str](https://docs.python.org/3/library/stdtypes.html#str)

Get the response ID from the underlying LLM response.

This property provides a clean interface to access the response ID,
supporting both completion mode (ModelResponse) and response API modes
(ResponsesAPIResponse).

Returns:
  The response ID from the LLM response
