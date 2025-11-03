---
title: openhands.sdk.llm.llm
description: API reference for openhands.sdk.llm.llm
---

# openhands.sdk.llm.llm module

<a id="module-openhands.sdk.llm.llm"></a>

### *class* openhands.sdk.llm.llm.LLM(\*, model: str = 'claude-sonnet-4-20250514', api_key: ~pydantic.types.SecretStr | None = None, base_url: str | None = None, api_version: str | None = None, aws_access_key_id: ~pydantic.types.SecretStr | None = None, aws_secret_access_key: ~pydantic.types.SecretStr | None = None, aws_region_name: str | None = None, openrouter_site_url: str = 'https://docs.all-hands.dev/', openrouter_app_name: str = 'OpenHands', num_retries: typing.Annotated[int, annotated_types.Ge(ge=0)] = 5, retry_multiplier: typing.Annotated[float, annotated_types.Ge(ge=0)] = 8.0, retry_min_wait: typing.Annotated[int, annotated_types.Ge(ge=0)] = 8, retry_max_wait: typing.Annotated[int, annotated_types.Ge(ge=0)] = 64, timeout: typing.Annotated[int | None, annotated_types.Ge(ge=0)] = None, max_message_chars: typing.Annotated[int, annotated_types.Ge(ge=1)] = 30000, temperature: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = 0.0, top_p: typing.Annotated[float | None, annotated_types.Ge(ge=0), annotated_types.Le(le=1)] = 1.0, top_k: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, custom_llm_provider: str | None = None, max_input_tokens: typing.Annotated[int | None, annotated_types.Ge(ge=1)] = None, max_output_tokens: typing.Annotated[int | None, annotated_types.Ge(ge=1)] = None, input_cost_per_token: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, output_cost_per_token: typing.Annotated[float | None, annotated_types.Ge(ge=0)] = None, ollama_base_url: str | None = None, drop_params: bool = True, modify_params: bool = True, disable_vision: bool | None = None, disable_stop_word: bool | None = False, caching_prompt: bool = True, log_completions: bool = False, log_completions_folder: str = 'logs/completions', custom_tokenizer: str | None = None, native_tool_calling: bool = True, reasoning_effort: typing.Literal['low', 'medium', 'high', 'none'] | None = None, enable_encrypted_reasoning: bool = False, extended_thinking_budget: int | None = 200000, seed: int | None = None, safety_settings: list[dict[str, str]] | None = None, usage_id: str = 'default', metadata: dict[str, typing.Any] = `<factory>`, retry_listener: typing.Annotated[~collections.abc.Callable[[int, int], None] | None, ~pydantic.json_schema.SkipJsonSchema()] = None, OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key'))

Bases: `BaseModel`, `RetryMixin`, `NonNativeToolCallingMixin`

Refactored LLM: simple completion(), centralized Telemetry, tiny helpers.

#### model *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### api_key *: SecretStr | [None](https://docs.python.org/3/library/constants.html#None)*

#### base_url *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### api_version *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### aws_access_key_id *: SecretStr | [None](https://docs.python.org/3/library/constants.html#None)*

#### aws_secret_access_key *: SecretStr | [None](https://docs.python.org/3/library/constants.html#None)*

#### aws_region_name *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### openrouter_site_url *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### openrouter_app_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### num_retries *: [int](https://docs.python.org/3/library/functions.html#int)*

#### retry_multiplier *: [float](https://docs.python.org/3/library/functions.html#float)*

#### retry_min_wait *: [int](https://docs.python.org/3/library/functions.html#int)*

#### retry_max_wait *: [int](https://docs.python.org/3/library/functions.html#int)*

#### timeout *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

#### max_message_chars *: [int](https://docs.python.org/3/library/functions.html#int)*

#### temperature *: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)*

#### top_p *: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)*

#### top_k *: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)*

#### custom_llm_provider *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### max_input_tokens *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

#### max_output_tokens *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

#### input_cost_per_token *: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)*

#### output_cost_per_token *: [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)*

#### ollama_base_url *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### drop_params *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### modify_params *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### disable_vision *: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None)*

#### disable_stop_word *: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None)*

#### caching_prompt *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### log_completions *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### log_completions_folder *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### custom_tokenizer *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### native_tool_calling *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### reasoning_effort *: Literal['low', 'medium', 'high', 'none'] | [None](https://docs.python.org/3/library/constants.html#None)*

#### enable_encrypted_reasoning *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### extended_thinking_budget *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

#### seed *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

#### safety_settings *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]] | [None](https://docs.python.org/3/library/constants.html#None)*

#### usage_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### metadata *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any]*

#### retry_listener *: SkipJsonSchema[Callable[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None)]*

#### OVERRIDE_ON_SERIALIZE *: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...]*

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'extra': 'forbid'\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *property* service_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* metrics *: [Metrics](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Metrics)*

#### restore_metrics(metrics: [Metrics](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Metrics)) → [None](https://docs.python.org/3/library/constants.html#None)

#### completion(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Message)], tools: Sequence[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.ToolBase)] | [None](https://docs.python.org/3/library/constants.html#None) = None, \_return_metrics: [bool](https://docs.python.org/3/library/functions.html#bool) = False, add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, \*\*kwargs) → [LLMResponse](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.LLMResponse)

Single entry point for LLM completion.

Normalize → (maybe) mock tools → transport → postprocess.

#### responses(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Message)], tools: Sequence[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.ToolBase)] | [None](https://docs.python.org/3/library/constants.html#None) = None, include: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None) = None, store: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None, \_return_metrics: [bool](https://docs.python.org/3/library/functions.html#bool) = False, add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, \*\*kwargs) → [LLMResponse](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.LLMResponse)

Alternative invocation path using OpenAI Responses API via LiteLLM.

Maps Message[] -> (instructions, input[]) and returns LLMResponse.
Non-stream only for v1.

#### vision_is_active() → [bool](https://docs.python.org/3/library/functions.html#bool)

#### is_caching_prompt_active() → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if prompt caching is supported and enabled for current model.

**Returns:**
  True if prompt caching is supported and enabled for the given
  : model.
- **Return type:**
  boolean

#### uses_responses_api() → [bool](https://docs.python.org/3/library/functions.html#bool)

Whether this model uses the OpenAI Responses API path.

#### *property* model_info *: [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [None](https://docs.python.org/3/library/constants.html#None)*

Returns the model info dictionary.

#### format_messages_for_llm(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)]

Formats Message objects for LLM consumption.

#### format_messages_for_responses(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None), [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]]]

Prepare (instructions, input[]) for the OpenAI Responses API.

- Skips prompt caching flags and string serializer concerns
- Uses Message.to_responses_value to get either instructions (system)

> or input items (others)
- Concatenates system instructions into a single instructions string

#### get_token_count(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [int](https://docs.python.org/3/library/functions.html#int)

#### *classmethod* load_from_json(json_path: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [LLM](#openhands.sdk.llm.llm.LLM)

#### *classmethod* load_from_env(prefix: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'LLM_') → [LLM](#openhands.sdk.llm.llm.LLM)

#### model_post_init(context: Any,)  → [None](https://docs.python.org/3/library/constants.html#None)

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

**Parameters:**
  - **self** – The BaseModel instance.
  - **context** – The context.

#### resolve_diff_from_deserialized(persisted: [LLM](#openhands.sdk.llm.llm.LLM)) → [LLM](#openhands.sdk.llm.llm.LLM)

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
