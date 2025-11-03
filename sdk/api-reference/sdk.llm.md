---
title: openhands.sdk.llm
description: API reference for openhands.sdk.llm
---

# openhands.sdk.llm package

<a id="module-openhands.sdk.llm"></a>

### class openhands.sdk.llm.LLMResponse(, message: [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message), metrics: [MetricsSnapshot](#openhands.sdk.llm.MetricsSnapshot), raw_response: ModelResponse | ResponsesAPIResponse)

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
  [openhands.sdk.llm.utils.metrics.MetricsSnapshot](#openhands.sdk.llm.MetricsSnapshot)

#### raw_response

The original LiteLLM response (ModelResponse or
ResponsesAPIResponse) for internal use

- **Type:**
  litellm.types.utils.ModelResponse | litellm.types.llms.openai.ResponsesAPIResponse

#### property id : [str](https://docs.python.org/3/library/stdtypes.html#str)

Get the response ID from the underlying LLM response.

This property provides a clean interface to access the response ID,
supporting both completion mode (ModelResponse) and response API modes
(ResponsesAPIResponse).

Returns:
  The response ID from the LLM response

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'arbitrary_types_allowed': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### message : [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

#### metrics : [MetricsSnapshot](#openhands.sdk.llm.MetricsSnapshot)

#### raw_response : ModelResponse | ResponsesAPIResponse

### class openhands.sdk.llm.LLM(model: str = 'claude-sonnet-4-20250514', api_key: ~pydantic.types.SecretStr | None = None, base_url: str | None = None, api_version: str | None = None, aws_access_key_id: ~pydantic.types.SecretStr | None = None, aws_secret_access_key: ~pydantic.types.SecretStr | None = None, aws_region_name: str | None = None, openrouter_site_url: str = 'https://docs.all-hands.dev/', openrouter_app_name: str = 'OpenHands', num_retries: typing.Annotated[int, annotated_types.Ge(ge=0)] = 5, retry_multiplier: typing.Annotated[float, annotated_types.Ge(ge=0)] = 8.0, retry_min_wait: typing.Annotated[int, annotated_types.Ge(ge=0)] = 8, retry_max_wait: typing.Annotated[int, annotated_types.Ge(ge=0)] = 64, timeout: typing.Annotated[int | None, annotated_types.Ge(ge=0)] = None, max_message_chars: typing.Annotated[int, annotated_types.Ge(ge=1)] = 30000, temperature: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = 0.0, top_p: typing.Annotated[float | None, annotated_types.Ge(ge=0), annotated_types.Le(le=1)] = 1.0, top_k: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, custom_llm_provider: str | None = None, max_input_tokens: typing.Annotated[int | None, annotated_types.Ge(ge=1)] = None, max_output_tokens: typing.Annotated[int | None, annotated_types.Ge(ge=1)] = None, input_cost_per_token: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, output_cost_per_token: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, ollama_base_url: str | None = None, drop_params: bool = True, modify_params: bool = True, disable_vision: bool | None = None, disable_stop_word: bool | None = False, caching_prompt: bool = True, log_completions: bool = False, log_completions_folder: str = 'logs/completions', custom_tokenizer: str | None = None, native_tool_calling: bool = True, reasoning_effort: typing.Literal['low', 'medium', 'high', 'none'] | None = None, enable_encrypted_reasoning: bool = False, extended_thinking_budget: int | None = 200000, seed: int | None = None, safety_settings: list[dict[str, str]] | None = None, usage_id: str = 'default', metadata: dict[str, typing.Any] = `<factory>`, retry_listener: typing.Annotated[~collections.abc.Callable[[int, int], None] | None, ~pydantic.json_schema.SkipJsonSchema()] = None, OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key'))

Bases: `BaseModel`, `RetryMixin`, `NonNativeToolCallingMixin`

Language model interface for OpenHands agents.

The LLM class provides a unified interface for interacting with various
language models through the litellm library. It handles model configuration,
API authentication,
retry logic, and tool calling capabilities.

### Example

```pycon
>>> from openhands.sdk import LLM
>>> from pydantic import SecretStr
>>> llm = LLM(
...     model="claude-sonnet-4-20250514",
...     api_key=SecretStr("your-api-key"),
...     usage_id="my-agent"
... )
>>> # Use with agent or conversation
```

#### completion(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](#openhands.sdk.llm.Message)], tools: Sequence[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.ToolBase)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \_return_metrics: [bool](https://docs.python.org/3/library/functions.html#bool) = False, add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, **kwargs) → [LLMResponse](#openhands.sdk.llm.LLMResponse)

Generate a completion from the language model.

This is the method for getting responses from the model via Completion API.
It handles message formatting, tool calling, and response processing.

Returns:
  LLMResponse containing the model’s response and metadata.
Raises:
  [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If streaming is requested (not supported).

### Example

```pycon
>>> from openhands.sdk.llm import Message, TextContent
>>> messages = [Message(role="user", content=[TextContent(text="Hello")])]
>>> response = llm.completion(messages)
>>> print(response.content)
```

#### format_messages_for_llm(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)]

Formats Message objects for LLM consumption.

#### format_messages_for_responses(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None), [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]]]

Prepare (instructions, input[]) for the OpenAI Responses API.

- Skips prompt caching flags and string serializer concerns
- Uses Message.to_responses_value to get either instructions (system)

> or input items (others)
- Concatenates system instructions into a single instructions string

#### get_token_count(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [int](https://docs.python.org/3/library/functions.html#int)

#### is_caching_prompt_active() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if prompt caching is supported and enabled for current model.

Returns:
  True if prompt caching is supported and enabled for the given
  : model.
- **Return type:**
  boolean

#### classmethod load_from_env(prefix: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM_') → [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)

#### classmethod load_from_json(json_path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)

#### property metrics : [Metrics](#openhands.sdk.llm.Metrics)

Get usage metrics for this LLM instance.

Returns:
  Metrics object containing token usage, costs, and other statistics.

### Example

```pycon
>>> cost = llm.metrics.accumulated_cost
>>> print(f"Total cost: ${cost}")
```

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'extra': 'forbid'\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### property model_info : [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [None](https://docs.python.org/3/library/constants.html#None)

Returns the model info dictionary.

#### model_post_init(context: Any,)  → [None](https://docs.python.org/3/library/constants.html#None)

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:
  * self – The BaseModel instance.
  * context – The context.

#### resolve_diff_from_deserialized(persisted: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)) → [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)

Resolve differences between a deserialized LLM and the current instance.

This is due to fields like api_key being serialized to “

```
\*\*
```

```
\*\*
```

” in dumps,
and we want to ensure that when loading from a file, we still use the
runtime-provided api_key in the self instance.

Return a new LLM instance equivalent to persisted but with
explicitly whitelisted fields (e.g. api_key) taken from self.

#### responses(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](#openhands.sdk.llm.Message)], tools: Sequence[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.ToolBase)] | [None](https://docs.python.org/3/library/constants.html#None) = None, include: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None, store: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None, \_return_metrics: [bool](https://docs.python.org/3/library/functions.html#bool) = False, add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, **kwargs) → [LLMResponse](#openhands.sdk.llm.LLMResponse)

Alternative invocation path using OpenAI Responses API via LiteLLM.

Maps Message[] -> (instructions, input[]) and returns LLMResponse.
Non-stream only for v1.

#### restore_metrics(metrics: [Metrics](#openhands.sdk.llm.Metrics)) → [None](https://docs.python.org/3/library/constants.html#None)

#### property service_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### uses_responses_api() → [bool](https://docs.python.org/3/library/functions.html#bool)

Whether this model uses the OpenAI Responses API path.

#### vision_is_active() → [bool](https://docs.python.org/3/library/functions.html#bool)

#### model : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### api_key : SecretStr | [None](https://docs.python.org/3/library/constants.html#None)

#### base_url : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### api_version : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### aws_access_key_id : SecretStr | [None](https://docs.python.org/3/library/constants.html#None)

#### aws_secret_access_key : SecretStr | [None](https://docs.python.org/3/library/constants.html#None)

#### aws_region_name : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### openrouter_site_url : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### openrouter_app_name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### num_retries : [int](https://docs.python.org/3/library/functions.html#int)

#### retry_multiplier : [float](https://docs.python.org/3/library/functions.html#float)

#### retry_min_wait : [int](https://docs.python.org/3/library/functions.html#int)

#### retry_max_wait : [int](https://docs.python.org/3/library/functions.html#int)

#### timeout : [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)

#### max_message_chars : [int](https://docs.python.org/3/library/functions.html#int)

#### temperature : [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)

#### top_p : [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)

#### top_k : [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)

#### custom_llm_provider : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### max_input_tokens : [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)

#### max_output_tokens : [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)

#### input_cost_per_token : [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)

#### output_cost_per_token : [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)

#### ollama_base_url : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### drop_params : [bool](https://docs.python.org/3/library/functions.html#bool)

#### modify_params : [bool](https://docs.python.org/3/library/functions.html#bool)

#### disable_vision : [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None)

#### disable_stop_word : [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None)

#### caching_prompt : [bool](https://docs.python.org/3/library/functions.html#bool)

#### log_completions : [bool](https://docs.python.org/3/library/functions.html#bool)

#### log_completions_folder : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### custom_tokenizer : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### native_tool_calling : [bool](https://docs.python.org/3/library/functions.html#bool)

#### reasoning_effort : Literal['low', 'medium', 'high', 'none'] | [None](https://docs.python.org/3/library/constants.html#None)

#### enable_encrypted_reasoning : [bool](https://docs.python.org/3/library/functions.html#bool)

#### extended_thinking_budget : [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)

#### seed : [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)

#### safety_settings : [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]] | [None](https://docs.python.org/3/library/constants.html#None)

#### usage_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### metadata : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any]

#### retry_listener : SkipJsonSchema[Callable[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None)]

#### OVERRIDE_ON_SERIALIZE : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...]

### class openhands.sdk.llm.LLMRegistry(retry_listener: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A minimal LLM registry for managing LLM instances by usage ID.

This registry provides a simple way to manage multiple LLM instances,
avoiding the need to recreate LLMs with the same configuration.

#### \_\_init_\_(retry_listener: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

Initialize the LLM registry.

Parameters:
  retry_listener – Optional callback for retry events.

#### add(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)) → [None](https://docs.python.org/3/library/constants.html#None)

Add an LLM instance to the registry.

Parameters:
  llm – The LLM instance to register.
Raises:
  [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If llm.usage_id already exists in the registry.

#### get(usage_id: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)

Get an LLM instance from the registry.

Parameters:
  usage_id – Unique identifier for the LLM usage slot.
Returns:
  The LLM instance.
Raises:
  [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError) – If usage_id is not found in the registry.

#### list_services() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Deprecated alias for [`list_usage_ids()`](#openhands.sdk.llm.LLMRegistry.list_usage_ids).

#### list_usage_ids() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

List all registered usage IDs.

#### notify(event: [RegistryEvent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.RegistryEvent)) → [None](https://docs.python.org/3/library/constants.html#None)

Notify subscribers of registry events.

Parameters:
  event – The registry event to notify about.

#### property service_to_llm : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)]

#### subscribe(callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[RegistryEvent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.RegistryEvent)], [None](https://docs.python.org/3/library/constants.html#None)]) → [None](https://docs.python.org/3/library/constants.html#None)

Subscribe to registry events.

Parameters:
  callback – Function to call when LLMs are created or updated.

#### property usage_to_llm : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)]

Access the internal usage-ID-to-LLM mapping.

#### registry_id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### retry_listener : [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None)

### class openhands.sdk.llm.RouterLLM(model: str = 'claude-sonnet-4-20250514', api_key: ~pydantic.types.SecretStr | None = None, base_url: str | None = None, api_version: str | None = None, aws_access_key_id: ~pydantic.types.SecretStr | None = None, aws_secret_access_key: ~pydantic.types.SecretStr | None = None, aws_region_name: str | None = None, openrouter_site_url: str = 'https://docs.all-hands.dev/', openrouter_app_name: str = 'OpenHands', num_retries: typing.Annotated[int, annotated_types.Ge(ge=0)] = 5, retry_multiplier: typing.Annotated[float, annotated_types.Ge(ge=0)] = 8.0, retry_min_wait: typing.Annotated[int, annotated_types.Ge(ge=0)] = 8, retry_max_wait: typing.Annotated[int, annotated_types.Ge(ge=0)] = 64, timeout: typing.Annotated[int | None, annotated_types.Ge(ge=0)] = None, max_message_chars: typing.Annotated[int, annotated_types.Ge(ge=1)] = 30000, temperature: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = 0.0, top_p: typing.Annotated[float | None, annotated_types.Ge(ge=0), annotated_types.Le(le=1)] = 1.0, top_k: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, custom_llm_provider: str | None = None, max_input_tokens: typing.Annotated[int | None, annotated_types.Ge(ge=1)] = None, max_output_tokens: typing.Annotated[int | None, annotated_types.Ge(ge=1)] = None, input_cost_per_token: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, output_cost_per_token: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, ollama_base_url: str | None = None, drop_params: bool = True, modify_params: bool = True, disable_vision: bool | None = None, disable_stop_word: bool | None = False, caching_prompt: bool = True, log_completions: bool = False, log_completions_folder: str = 'logs/completions', custom_tokenizer: str | None = None, native_tool_calling: bool = True, reasoning_effort: typing.Literal['low', 'medium', 'high', 'none'] | None = None, enable_encrypted_reasoning: bool = False, extended_thinking_budget: int | None = 200000, seed: int | None = None, safety_settings: list[dict[str, str]] | None = None, usage_id: str = 'default', metadata: dict[str, typing.Any] = `<factory>`, retry_listener: typing.Annotated[~collections.abc.Callable[[int, int], None] | None, ~pydantic.json_schema.SkipJsonSchema()] = None, OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key'), router_name: str = 'base_router', llms_for_routing: dict[str, openhands.sdk.llm.llm.LLM] = `<factory>`, active_llm: openhands.sdk.llm.llm.LLM | None = None)

Bases: [`LLM`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)

Base class for multiple LLM acting as a unified LLM.
This class provides a foundation for implementing model routing by
inheriting from LLM, allowing routers to work with multiple underlying
LLM models while presenting a unified LLM interface to consumers.
Key features:
- Works with multiple LLMs configured via llms_for_routing
- Delegates all other operations/properties to the selected LLM
- Provides routing interface through select_llm() method

#### \_\_getattr_\_(name)

Delegate other attributes/methods to the active LLM.

#### \_\_str_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str)

String representation of the router.

#### completion(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)], tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase)] | [None](https://docs.python.org/3/library/constants.html#None) = None, return_metrics: [bool](https://docs.python.org/3/library/functions.html#bool) = False, add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, **kwargs) → [LLMResponse](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse)

This method intercepts completion calls and routes them to the appropriate
underlying LLM based on the routing logic implemented in select_llm().

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'extra': 'forbid'\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: Any,)  → [None](https://docs.python.org/3/library/constants.html#None)

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

Parameters:
  * self – The BaseModel instance.
  * context – The context.

#### abstractmethod select_llm(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Select which LLM to use based on messages and events.

This method implements the core routing logic for the RouterLLM.
Subclasses should analyze the provided messages to determine which
LLM from llms_for_routing is most appropriate for handling the request.

Parameters:
  messages – List of messages in the conversation that can be used
  to inform the routing decision.
Returns:
  The key/name of the LLM to use from llms_for_routing dictionary.

#### classmethod set_placeholder_model(data)

Guarantee model exists before LLM base validation runs.

#### classmethod validate_llms_not_empty(v)

#### router_name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### llms_for_routing : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)]

#### active_llm : [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None)

### class openhands.sdk.llm.RegistryEvent(, llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM))

Bases: `BaseModel`

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'arbitrary_types_allowed': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### llm : [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)

### class openhands.sdk.llm.Message(role: typing.Literal['user', 'system', 'assistant', 'tool'], content: ~collections.abc.Sequence[openhands.sdk.llm.message.TextContent | openhands.sdk.llm.message.ImageContent] = `<factory>`, cache_enabled: bool = False, vision_enabled: bool = False, function_calling_enabled: bool = False, tool_calls: list[openhands.sdk.llm.message.MessageToolCall] | None = None, tool_call_id: str | None = None, name: str | None = None, force_string_serializer: bool = False, reasoning_content: str | None = None, thinking_blocks: ~collections.abc.Sequence[openhands.sdk.llm.message.ThinkingBlock | openhands.sdk.llm.message.RedactedThinkingBlock] = `<factory>`, responses_reasoning_item: openhands.sdk.llm.message.ReasoningItemModel | None = None)

Bases: `BaseModel`

#### property contains_image : [bool](https://docs.python.org/3/library/functions.html#bool)

#### classmethod from_llm_chat_message(message: Message) → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

Convert a LiteLLMMessage (Chat Completions) to our Message class.

Provider-agnostic mapping for reasoning:
- Prefer message.reasoning_content if present (LiteLLM normalized field)
- Extract thinking_blocks from content array (Anthropic-specific)

#### classmethod from_llm_responses_output(output: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)

Convert OpenAI Responses API output items into a single assistant Message.

Policy (non-stream):
- Collect assistant text by concatenating output_text parts from message items
- Normalize function_call items to MessageToolCall list

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_chat_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Serialize message for OpenAI Chat Completions.

Chooses the appropriate content serializer and then injects threading keys:
- Assistant tool call turn: role == “assistant” and self.tool_calls
- Tool result turn: role == “tool” and self.tool_call_id (with name)

#### to_responses_dict(, vision_enabled: [bool](https://docs.python.org/3/library/functions.html#bool)) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]]

Serialize message for OpenAI Responses (input parameter).

Produces a list of “input” items for the Responses API:
- system: returns [], system content is expected in ‘instructions’
- user: one ‘message’ item with content parts -> input_text / input_image
(when vision enabled)
- assistant: emits prior assistant content as input_text,
and function_call items for tool_calls
- tool: emits function_call_output items (one per TextContent)
with matching call_id

#### to_responses_value(, vision_enabled: [bool](https://docs.python.org/3/library/functions.html#bool)) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]]

Return serialized form.

Either an instructions string (for system) or input items (for other roles).

#### role : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['user', 'system', 'assistant', 'tool']

#### content : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]

#### cache_enabled : [bool](https://docs.python.org/3/library/functions.html#bool)

#### vision_enabled : [bool](https://docs.python.org/3/library/functions.html#bool)

#### function_calling_enabled : [bool](https://docs.python.org/3/library/functions.html#bool)

#### tool_calls : [list](https://docs.python.org/3/library/stdtypes.html#list)[[MessageToolCall](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall)] | [None](https://docs.python.org/3/library/constants.html#None)

#### tool_call_id : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### name : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### force_string_serializer : [bool](https://docs.python.org/3/library/functions.html#bool)

#### reasoning_content : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### thinking_blocks : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)]

#### responses_reasoning_item : [ReasoningItemModel](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel) | [None](https://docs.python.org/3/library/constants.html#None)

### class openhands.sdk.llm.MessageToolCall(, id: [str](https://docs.python.org/3/library/stdtypes.html#str), name: [str](https://docs.python.org/3/library/stdtypes.html#str), arguments: [str](https://docs.python.org/3/library/stdtypes.html#str), origin: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['completion', 'responses'])

Bases: `BaseModel`

Transport-agnostic tool call representation.

One canonical id is used for linking across actions/observations and
for Responses function_call_output call_id.

#### classmethod from_chat_tool_call(tool_call: ChatCompletionMessageToolCall) → [MessageToolCall](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall)

Create a MessageToolCall from a Chat Completions tool call.

#### classmethod from_responses_function_call(item: ResponseFunctionToolCall | OutputFunctionToolCall) → [MessageToolCall](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall)

Create a MessageToolCall from a typed OpenAI Responses function_call item.

Note: OpenAI Responses function_call.arguments is already a JSON string.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_chat_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Serialize to OpenAI Chat Completions tool_calls format.

#### to_responses_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Serialize to OpenAI Responses ‘function_call’ input item format.

#### id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### arguments : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### origin : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['completion', 'responses']

### class openhands.sdk.llm.TextContent(, cache_prompt: [bool](https://docs.python.org/3/library/functions.html#bool) = False, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['text'] = 'text', text: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`BaseContent`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.BaseContent)

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'populate_by_name': True, 'validate_by_alias': True, 'validate_by_name': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_dict() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]]]

Convert to LLM API format.

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['text']

#### text : [str](https://docs.python.org/3/library/stdtypes.html#str)

### class openhands.sdk.llm.ImageContent(, cache_prompt: [bool](https://docs.python.org/3/library/functions.html#bool) = False, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['image'] = 'image', image_urls: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)])

Bases: [`BaseContent`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.BaseContent)

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_dict() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]]]

Convert to LLM API format.

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['image']

#### image_urls : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

### class openhands.sdk.llm.ThinkingBlock(, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['thinking'] = 'thinking', thinking: [str](https://docs.python.org/3/library/stdtypes.html#str), signature: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Anthropic thinking block for extended thinking feature.

This represents the raw thinking blocks returned by Anthropic models
when extended thinking is enabled. These blocks must be preserved
and passed back to the API for tool use scenarios.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['thinking']

#### thinking : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### signature : [str](https://docs.python.org/3/library/stdtypes.html#str)

### class openhands.sdk.llm.RedactedThinkingBlock(, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['redacted_thinking'] = 'redacted_thinking', data: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Redacted thinking block for previous responses without extended thinking.

This is used as a placeholder for assistant messages that were generated
before extended thinking was enabled.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['redacted_thinking']

#### data : [str](https://docs.python.org/3/library/stdtypes.html#str)

### class openhands.sdk.llm.ReasoningItemModel(id: str | None = None, summary: list[str] = `<factory>`, content: list[str] | None = None, encrypted_content: str | None = None, status: str | None = None)

Bases: `BaseModel`

OpenAI Responses reasoning item (non-stream, subset we consume).

Do not log or render encrypted_content.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### id : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### summary : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

#### content : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)

#### encrypted_content : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### status : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

### openhands.sdk.llm.content_to_str(contents: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent) | [ImageContent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Convert a list of TextContent and ImageContent to a list of strings.

This is primarily used for display purposes.

### class openhands.sdk.llm.Metrics(model_name: str = 'default', accumulated_cost: typing.Annotated[float, annotated_types.Ge(ge=0)] = 0.0, max_budget_per_task: float | None = None, accumulated_token_usage: openhands.sdk.llm.utils.metrics.TokenUsage | None = None, costs: list[openhands.sdk.llm.utils.metrics.Cost] = `<factory>`, response_latencies: list[openhands.sdk.llm.utils.metrics.ResponseLatency] = `<factory>`, token_usages: list[openhands.sdk.llm.utils.metrics.TokenUsage] = `<factory>`)

Bases: [`MetricsSnapshot`](#openhands.sdk.llm.MetricsSnapshot)

Metrics class can record various metrics during running and evaluation.
We track:

> - accumulated_cost and costs
> - max_budget_per_task (budget limit)
> - A list of ResponseLatency
> - A list of TokenUsage (one per call).

#### add_cost(value: [float](https://docs.python.org/3/library/functions.html#float)) → [None](https://docs.python.org/3/library/constants.html#None)

#### add_response_latency(value: [float](https://docs.python.org/3/library/functions.html#float), response_id: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [None](https://docs.python.org/3/library/constants.html#None)

#### add_token_usage(prompt_tokens: [int](https://docs.python.org/3/library/functions.html#int), completion_tokens: [int](https://docs.python.org/3/library/functions.html#int), cache_read_tokens: [int](https://docs.python.org/3/library/functions.html#int), cache_write_tokens: [int](https://docs.python.org/3/library/functions.html#int), context_window: [int](https://docs.python.org/3/library/functions.html#int), response_id: [str](https://docs.python.org/3/library/stdtypes.html#str), reasoning_tokens: [int](https://docs.python.org/3/library/functions.html#int) = 0) → [None](https://docs.python.org/3/library/constants.html#None)

Add a single usage record.

#### deep_copy() → [Metrics](#openhands.sdk.llm.Metrics)

Create a deep copy of the Metrics object.

#### diff(baseline: [Metrics](#openhands.sdk.llm.Metrics)) → [Metrics](#openhands.sdk.llm.Metrics)

Calculate the difference between current metrics and a baseline.

This is useful for tracking metrics for specific operations like delegates.

Parameters:
  baseline – A metrics object representing the baseline state
Returns:
  A new Metrics object containing only the differences since the baseline

#### get() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)

Return the metrics in a dictionary.

#### get_snapshot() → [MetricsSnapshot](#openhands.sdk.llm.MetricsSnapshot)

Get a snapshot of the current metrics without the detailed lists.

#### initialize_accumulated_token_usage() → [Metrics](#openhands.sdk.llm.Metrics)

#### log() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Log the metrics.

#### merge(other: [Metrics](#openhands.sdk.llm.Metrics)) → [None](https://docs.python.org/3/library/constants.html#None)

Merge ‘other’ metrics into this one.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### classmethod validate_accumulated_cost(v: [float](https://docs.python.org/3/library/functions.html#float)) → [float](https://docs.python.org/3/library/functions.html#float)

#### costs : [list](https://docs.python.org/3/library/stdtypes.html#list)[Cost]

#### response_latencies : [list](https://docs.python.org/3/library/stdtypes.html#list)[ResponseLatency]

#### token_usages : [list](https://docs.python.org/3/library/stdtypes.html#list)[TokenUsage]

### class openhands.sdk.llm.MetricsSnapshot(, model_name: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'default', accumulated_cost: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[float](https://docs.python.org/3/library/functions.html#float), Ge(ge=0)] = 0.0, max_budget_per_task: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None) = None, accumulated_token_usage: TokenUsage | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: `BaseModel`

A snapshot of metrics at a point in time.

Does not include lists of individual costs, latencies, or token usages.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### accumulated_cost : [float](https://docs.python.org/3/library/functions.html#float)

#### max_budget_per_task : [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)

#### accumulated_token_usage : TokenUsage | [None](https://docs.python.org/3/library/constants.html#None)

### openhands.sdk.llm.get_unverified_models(aws_region_name: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, aws_access_key_id: SecretStr | [None](https://docs.python.org/3/library/constants.html#None) = None, aws_secret_access_key: SecretStr | [None](https://docs.python.org/3/library/constants.html#None) = None) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]]

Organize a mapping of unverified model identifiers by provider.

## Subpackages

* [openhands.sdk.llm.exceptions package](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md)
  * [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMError)
    * [`LLMError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMError.__init__)
    * [`LLMError.message`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMError.message)
  * [`LLMMalformedActionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMMalformedActionError)
    * [`LLMMalformedActionError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMMalformedActionError.__init__)
  * [`LLMNoActionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMNoActionError)
    * [`LLMNoActionError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMNoActionError.__init__)
  * [`LLMResponseError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMResponseError)
    * [`LLMResponseError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMResponseError.__init__)
  * [`FunctionCallConversionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.FunctionCallConversionError)
    * [`FunctionCallConversionError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.FunctionCallConversionError.__init__)
  * [`FunctionCallValidationError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.FunctionCallValidationError)
    * [`FunctionCallValidationError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.FunctionCallValidationError.__init__)
  * [`FunctionCallNotExistsError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.FunctionCallNotExistsError)
    * [`FunctionCallNotExistsError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.FunctionCallNotExistsError.__init__)
  * [`LLMNoResponseError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMNoResponseError)
    * [`LLMNoResponseError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMNoResponseError.__init__)
  * [`LLMContextWindowExceedError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMContextWindowExceedError)
    * [`LLMContextWindowExceedError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMContextWindowExceedError.__init__)
  * [`LLMAuthenticationError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMAuthenticationError)
    * [`LLMAuthenticationError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMAuthenticationError.__init__)
  * [`LLMRateLimitError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMRateLimitError)
    * [`LLMRateLimitError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMRateLimitError.__init__)
  * [`LLMTimeoutError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMTimeoutError)
    * [`LLMTimeoutError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMTimeoutError.__init__)
  * [`LLMServiceUnavailableError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMServiceUnavailableError)
    * [`LLMServiceUnavailableError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMServiceUnavailableError.__init__)
  * [`LLMBadRequestError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMBadRequestError)
    * [`LLMBadRequestError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.LLMBadRequestError.__init__)
  * [`UserCancelledError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.UserCancelledError)
    * [`UserCancelledError.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.UserCancelledError.__init__)
  * [`OperationCancelled`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.OperationCancelled)
    * [`OperationCancelled.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.OperationCancelled.__init__)
  * [`is_context_window_exceeded()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.is_context_window_exceeded)
  * [`looks_like_auth_error()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.looks_like_auth_error)
  * [`map_provider_exception()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#openhands.sdk.llm.exceptions.map_provider_exception)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.md#submodules)
    * [openhands.sdk.llm.exceptions.classifier module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.classifier.md)
      * [`is_context_window_exceeded()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.classifier.md#openhands.sdk.llm.exceptions.classifier.is_context_window_exceeded)
      * [`looks_like_auth_error()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.classifier.md#openhands.sdk.llm.exceptions.classifier.looks_like_auth_error)
    * [openhands.sdk.llm.exceptions.mapping module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.mapping.md)
      * [`map_provider_exception()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.mapping.md#openhands.sdk.llm.exceptions.mapping.map_provider_exception)
    * [openhands.sdk.llm.exceptions.types module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md)
      * [`LLMError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMError)
      * [`LLMMalformedActionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMMalformedActionError)
      * [`LLMNoActionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMNoActionError)
      * [`LLMResponseError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMResponseError)
      * [`FunctionCallConversionError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallConversionError)
      * [`FunctionCallValidationError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallValidationError)
      * [`FunctionCallNotExistsError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.FunctionCallNotExistsError)
      * [`LLMNoResponseError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMNoResponseError)
      * [`LLMContextWindowExceedError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMContextWindowExceedError)
      * [`LLMAuthenticationError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMAuthenticationError)
      * [`LLMRateLimitError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMRateLimitError)
      * [`LLMTimeoutError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMTimeoutError)
      * [`LLMServiceUnavailableError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMServiceUnavailableError)
      * [`LLMBadRequestError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.LLMBadRequestError)
      * [`UserCancelledError`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.UserCancelledError)
      * [`OperationCancelled`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.exceptions.types.md#openhands.sdk.llm.exceptions.types.OperationCancelled)
* [openhands.sdk.llm.options package](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.md)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.md#submodules)
    * [openhands.sdk.llm.options.chat_options module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.chat_options.md)
      * [`select_chat_options()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.chat_options.md#openhands.sdk.llm.options.chat_options.select_chat_options)
    * [openhands.sdk.llm.options.common module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.common.md)
      * [`apply_defaults_if_absent()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.common.md#openhands.sdk.llm.options.common.apply_defaults_if_absent)
    * [openhands.sdk.llm.options.responses_options module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.responses_options.md)
      * [`select_responses_options()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.options.responses_options.md#openhands.sdk.llm.options.responses_options.select_responses_options)
* [openhands.sdk.llm.router package](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md)
  * [`RouterLLM`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM)
    * [`RouterLLM.__getattr__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.__getattr__)
    * [`RouterLLM.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.__str__)
    * [`RouterLLM.completion()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.completion)
    * [`RouterLLM.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.model_config)
    * [`RouterLLM.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.model_post_init)
    * [`RouterLLM.select_llm()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.select_llm)
    * [`RouterLLM.set_placeholder_model()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.set_placeholder_model)
    * [`RouterLLM.validate_llms_not_empty()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.validate_llms_not_empty)
    * [`RouterLLM.router_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.router_name)
    * [`RouterLLM.llms_for_routing`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.llms_for_routing)
    * [`RouterLLM.active_llm`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.active_llm)
    * [`RouterLLM.model`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.model)
    * [`RouterLLM.api_key`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.api_key)
    * [`RouterLLM.base_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.base_url)
    * [`RouterLLM.api_version`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.api_version)
    * [`RouterLLM.aws_access_key_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.aws_access_key_id)
    * [`RouterLLM.aws_secret_access_key`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.aws_secret_access_key)
    * [`RouterLLM.aws_region_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.aws_region_name)
    * [`RouterLLM.openrouter_site_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.openrouter_site_url)
    * [`RouterLLM.openrouter_app_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.openrouter_app_name)
    * [`RouterLLM.num_retries`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.num_retries)
    * [`RouterLLM.retry_multiplier`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.retry_multiplier)
    * [`RouterLLM.retry_min_wait`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.retry_min_wait)
    * [`RouterLLM.retry_max_wait`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.retry_max_wait)
    * [`RouterLLM.timeout`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.timeout)
    * [`RouterLLM.max_message_chars`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.max_message_chars)
    * [`RouterLLM.temperature`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.temperature)
    * [`RouterLLM.top_p`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.top_p)
    * [`RouterLLM.top_k`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.top_k)
    * [`RouterLLM.custom_llm_provider`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.custom_llm_provider)
    * [`RouterLLM.max_input_tokens`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.max_input_tokens)
    * [`RouterLLM.max_output_tokens`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.max_output_tokens)
    * [`RouterLLM.input_cost_per_token`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.input_cost_per_token)
    * [`RouterLLM.output_cost_per_token`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.output_cost_per_token)
    * [`RouterLLM.ollama_base_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.ollama_base_url)
    * [`RouterLLM.drop_params`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.drop_params)
    * [`RouterLLM.modify_params`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.modify_params)
    * [`RouterLLM.disable_vision`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.disable_vision)
    * [`RouterLLM.disable_stop_word`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.disable_stop_word)
    * [`RouterLLM.caching_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.caching_prompt)
    * [`RouterLLM.log_completions`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.log_completions)
    * [`RouterLLM.log_completions_folder`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.log_completions_folder)
    * [`RouterLLM.custom_tokenizer`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.custom_tokenizer)
    * [`RouterLLM.native_tool_calling`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.native_tool_calling)
    * [`RouterLLM.reasoning_effort`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.reasoning_effort)
    * [`RouterLLM.enable_encrypted_reasoning`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.enable_encrypted_reasoning)
    * [`RouterLLM.extended_thinking_budget`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.extended_thinking_budget)
    * [`RouterLLM.seed`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.seed)
    * [`RouterLLM.safety_settings`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.safety_settings)
    * [`RouterLLM.usage_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.usage_id)
    * [`RouterLLM.metadata`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.metadata)
    * [`RouterLLM.retry_listener`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.retry_listener)
    * [`RouterLLM.OVERRIDE_ON_SERIALIZE`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RouterLLM.OVERRIDE_ON_SERIALIZE)
  * [`RandomRouter`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RandomRouter)
    * [`RandomRouter.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RandomRouter.model_config)
    * [`RandomRouter.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RandomRouter.model_post_init)
    * [`RandomRouter.select_llm()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RandomRouter.select_llm)
    * [`RandomRouter.router_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.RandomRouter.router_name)
  * [`MultimodalRouter`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.MultimodalRouter)
    * [`MultimodalRouter.PRIMARY_MODEL_KEY`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.MultimodalRouter.PRIMARY_MODEL_KEY)
    * [`MultimodalRouter.SECONDARY_MODEL_KEY`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.MultimodalRouter.SECONDARY_MODEL_KEY)
    * [`MultimodalRouter.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.MultimodalRouter.model_config)
    * [`MultimodalRouter.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.MultimodalRouter.model_post_init)
    * [`MultimodalRouter.select_llm()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.MultimodalRouter.select_llm)
    * [`MultimodalRouter.router_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#openhands.sdk.llm.router.MultimodalRouter.router_name)
  * [Submodules](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.md#submodules)
    * [openhands.sdk.llm.router.base module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md)
      * [`RouterLLM`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM)

## Submodules

* [openhands.sdk.llm.llm module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md)
  * [`LLM`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)
    * [`LLM.model`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.model)
    * [`LLM.api_key`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.api_key)
    * [`LLM.base_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.base_url)
    * [`LLM.api_version`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.api_version)
    * [`LLM.aws_access_key_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.aws_access_key_id)
    * [`LLM.aws_secret_access_key`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.aws_secret_access_key)
    * [`LLM.aws_region_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.aws_region_name)
    * [`LLM.openrouter_site_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.openrouter_site_url)
    * [`LLM.openrouter_app_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.openrouter_app_name)
    * [`LLM.num_retries`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.num_retries)
    * [`LLM.retry_multiplier`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.retry_multiplier)
    * [`LLM.retry_min_wait`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.retry_min_wait)
    * [`LLM.retry_max_wait`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.retry_max_wait)
    * [`LLM.timeout`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.timeout)
    * [`LLM.max_message_chars`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.max_message_chars)
    * [`LLM.temperature`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.temperature)
    * [`LLM.top_p`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.top_p)
    * [`LLM.top_k`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.top_k)
    * [`LLM.custom_llm_provider`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.custom_llm_provider)
    * [`LLM.max_input_tokens`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.max_input_tokens)
    * [`LLM.max_output_tokens`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.max_output_tokens)
    * [`LLM.input_cost_per_token`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.input_cost_per_token)
    * [`LLM.output_cost_per_token`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.output_cost_per_token)
    * [`LLM.ollama_base_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.ollama_base_url)
    * [`LLM.drop_params`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.drop_params)
    * [`LLM.modify_params`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.modify_params)
    * [`LLM.disable_vision`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.disable_vision)
    * [`LLM.disable_stop_word`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.disable_stop_word)
    * [`LLM.caching_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.caching_prompt)
    * [`LLM.log_completions`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.log_completions)
    * [`LLM.log_completions_folder`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.log_completions_folder)
    * [`LLM.custom_tokenizer`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.custom_tokenizer)
    * [`LLM.native_tool_calling`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.native_tool_calling)
    * [`LLM.reasoning_effort`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.reasoning_effort)
    * [`LLM.enable_encrypted_reasoning`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.enable_encrypted_reasoning)
    * [`LLM.extended_thinking_budget`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.extended_thinking_budget)
    * [`LLM.seed`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.seed)
    * [`LLM.safety_settings`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.safety_settings)
    * [`LLM.usage_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.usage_id)
    * [`LLM.metadata`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.metadata)
    * [`LLM.retry_listener`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.retry_listener)
    * [`LLM.OVERRIDE_ON_SERIALIZE`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.OVERRIDE_ON_SERIALIZE)
    * [`LLM.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.model_config)
    * [`LLM.service_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.service_id)
    * [`LLM.metrics`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.metrics)
    * [`LLM.restore_metrics()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.restore_metrics)
    * [`LLM.completion()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.completion)
    * [`LLM.responses()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.responses)
    * [`LLM.vision_is_active()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.vision_is_active)
    * [`LLM.is_caching_prompt_active()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.is_caching_prompt_active)
    * [`LLM.uses_responses_api()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.uses_responses_api)
    * [`LLM.model_info`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.model_info)
    * [`LLM.format_messages_for_llm()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.format_messages_for_llm)
    * [`LLM.format_messages_for_responses()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.format_messages_for_responses)
    * [`LLM.get_token_count()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.get_token_count)
    * [`LLM.load_from_json()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.load_from_json)
    * [`LLM.load_from_env()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.load_from_env)
    * [`LLM.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.model_post_init)
    * [`LLM.resolve_diff_from_deserialized()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM.resolve_diff_from_deserialized)
* [openhands.sdk.llm.llm_registry module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md)
  * [`RegistryEvent`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.RegistryEvent)
    * [`RegistryEvent.llm`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.RegistryEvent.llm)
    * [`RegistryEvent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.RegistryEvent.model_config)
  * [`LLMRegistry`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry)
    * [`LLMRegistry.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.__init__)
    * [`LLMRegistry.registry_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.registry_id)
    * [`LLMRegistry.retry_listener`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.retry_listener)
    * [`LLMRegistry.subscriber`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.subscriber)
    * [`LLMRegistry.subscribe()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.subscribe)
    * [`LLMRegistry.notify()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.notify)
    * [`LLMRegistry.usage_to_llm`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.usage_to_llm)
    * [`LLMRegistry.service_to_llm`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.service_to_llm)
    * [`LLMRegistry.add()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.add)
    * [`LLMRegistry.get()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.get)
    * [`LLMRegistry.list_usage_ids()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.list_usage_ids)
    * [`LLMRegistry.list_services()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.LLMRegistry.list_services)
* [openhands.sdk.llm.llm_response module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md)
  * [`LLMResponse`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse)
    * [`LLMResponse.message`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse.message)
    * [`LLMResponse.metrics`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse.metrics)
    * [`LLMResponse.raw_response`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse.raw_response)
    * [`LLMResponse.message`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#id0)
    * [`LLMResponse.metrics`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#id1)
    * [`LLMResponse.raw_response`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#id2)
    * [`LLMResponse.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse.model_config)
    * [`LLMResponse.id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse.id)
* [openhands.sdk.llm.message module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md)
  * [`MessageToolCall`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall)
    * [`MessageToolCall.id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.id)
    * [`MessageToolCall.name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.name)
    * [`MessageToolCall.arguments`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.arguments)
    * [`MessageToolCall.origin`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.origin)
    * [`MessageToolCall.from_chat_tool_call()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.from_chat_tool_call)
    * [`MessageToolCall.from_responses_function_call()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.from_responses_function_call)
    * [`MessageToolCall.to_chat_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.to_chat_dict)
    * [`MessageToolCall.to_responses_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.to_responses_dict)
    * [`MessageToolCall.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.MessageToolCall.model_config)
  * [`ThinkingBlock`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock)
    * [`ThinkingBlock.type`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock.type)
    * [`ThinkingBlock.thinking`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock.thinking)
    * [`ThinkingBlock.signature`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock.signature)
    * [`ThinkingBlock.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ThinkingBlock.model_config)
  * [`RedactedThinkingBlock`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock)
    * [`RedactedThinkingBlock.type`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock.type)
    * [`RedactedThinkingBlock.data`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock.data)
    * [`RedactedThinkingBlock.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.RedactedThinkingBlock.model_config)
  * [`ReasoningItemModel`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel)
    * [`ReasoningItemModel.id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel.id)
    * [`ReasoningItemModel.summary`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel.summary)
    * [`ReasoningItemModel.content`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel.content)
    * [`ReasoningItemModel.encrypted_content`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel.encrypted_content)
    * [`ReasoningItemModel.status`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel.status)
    * [`ReasoningItemModel.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ReasoningItemModel.model_config)
  * [`BaseContent`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.BaseContent)
    * [`BaseContent.cache_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.BaseContent.cache_prompt)
    * [`BaseContent.to_llm_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.BaseContent.to_llm_dict)
    * [`BaseContent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.BaseContent.model_config)
  * [`TextContent`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent)
    * [`TextContent.type`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent.type)
    * [`TextContent.text`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent.text)
    * [`TextContent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent.model_config)
    * [`TextContent.to_llm_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent.to_llm_dict)
    * [`TextContent.cache_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.TextContent.cache_prompt)
  * [`ImageContent`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent)
    * [`ImageContent.type`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent.type)
    * [`ImageContent.image_urls`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent.image_urls)
    * [`ImageContent.to_llm_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent.to_llm_dict)
    * [`ImageContent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent.model_config)
    * [`ImageContent.cache_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.ImageContent.cache_prompt)
  * [`Message`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)
    * [`Message.role`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.role)
    * [`Message.content`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.content)
    * [`Message.cache_enabled`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.cache_enabled)
    * [`Message.vision_enabled`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.vision_enabled)
    * [`Message.function_calling_enabled`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.function_calling_enabled)
    * [`Message.tool_calls`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.tool_calls)
    * [`Message.tool_call_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.tool_call_id)
    * [`Message.name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.name)
    * [`Message.force_string_serializer`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.force_string_serializer)
    * [`Message.reasoning_content`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.reasoning_content)
    * [`Message.thinking_blocks`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.thinking_blocks)
    * [`Message.responses_reasoning_item`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.responses_reasoning_item)
    * [`Message.contains_image`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.contains_image)
    * [`Message.to_chat_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.to_chat_dict)
    * [`Message.to_responses_value()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.to_responses_value)
    * [`Message.to_responses_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.to_responses_dict)
    * [`Message.from_llm_chat_message()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.from_llm_chat_message)
    * [`Message.from_llm_responses_output()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.from_llm_responses_output)
    * [`Message.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message.model_config)
  * [`content_to_str()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.content_to_str)
