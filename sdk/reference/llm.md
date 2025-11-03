## `openhands.sdk.llm`

**Modules:**

- [**exceptions**](#openhands.sdk.llm.exceptions) –
- [**llm**](#openhands.sdk.llm.llm) –
- [**llm_registry**](#openhands.sdk.llm.llm_registry) –
- [**llm_response**](#openhands.sdk.llm.llm_response) – LLMResponse type for LLM completion responses.
- [**message**](#openhands.sdk.llm.message) –
- [**options**](#openhands.sdk.llm.options) –
- [**router**](#openhands.sdk.llm.router) –

**Classes:**

- [**ImageContent**](#openhands.sdk.llm.ImageContent) –
- [**LLM**](#openhands.sdk.llm.LLM) – Refactored LLM: simple `completion()`, centralized Telemetry, tiny helpers.
- [**LLMRegistry**](#openhands.sdk.llm.LLMRegistry) – A minimal LLM registry for managing LLM instances by usage ID.
- [**LLMResponse**](#openhands.sdk.llm.LLMResponse) – Result of an LLM completion request.
- [**Message**](#openhands.sdk.llm.Message) –
- [**MessageToolCall**](#openhands.sdk.llm.MessageToolCall) – Transport-agnostic tool call representation.
- [**ReasoningItemModel**](#openhands.sdk.llm.ReasoningItemModel) – OpenAI Responses reasoning item (non-stream, subset we consume).
- [**RedactedThinkingBlock**](#openhands.sdk.llm.RedactedThinkingBlock) – Redacted thinking block for previous responses without extended thinking.
- [**RegistryEvent**](#openhands.sdk.llm.RegistryEvent) –
- [**RouterLLM**](#openhands.sdk.llm.RouterLLM) – Base class for multiple LLM acting as a unified LLM.
- [**TextContent**](#openhands.sdk.llm.TextContent) –
- [**ThinkingBlock**](#openhands.sdk.llm.ThinkingBlock) – Anthropic thinking block for extended thinking feature.

**Functions:**

- [**content_to_str**](#openhands.sdk.llm.content_to_str) – Convert a list of TextContent and ImageContent to a list of strings.

### `openhands.sdk.llm.ImageContent`

Bases: <code>[BaseContent](#openhands.sdk.llm.message.BaseContent)</code>

**Functions:**

- [**to_llm_dict**](#openhands.sdk.llm.ImageContent.to_llm_dict) – Convert to LLM API format.

**Attributes:**

- [**cache_prompt**](#openhands.sdk.llm.ImageContent.cache_prompt) (<code>[bool](#bool)</code>) –
- [**image_urls**](#openhands.sdk.llm.ImageContent.image_urls) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.llm.ImageContent.type) (<code>[Literal](#typing.Literal)['image']</code>) –

#### `openhands.sdk.llm.ImageContent.cache_prompt`

```python
cache_prompt: bool = False
```

#### `openhands.sdk.llm.ImageContent.image_urls`

```python
image_urls: list[str]
```

#### `openhands.sdk.llm.ImageContent.to_llm_dict`

```python
to_llm_dict()
```

Convert to LLM API format.

#### `openhands.sdk.llm.ImageContent.type`

```python
type: Literal['image'] = 'image'
```

### `openhands.sdk.llm.LLM`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>, <code>[RetryMixin](#openhands.sdk.llm.utils.retry_mixin.RetryMixin)</code>, <code>[NonNativeToolCallingMixin](#openhands.sdk.llm.mixins.non_native_fc.NonNativeToolCallingMixin)</code>

Refactored LLM: simple `completion()`, centralized Telemetry, tiny helpers.

**Functions:**

- [**completion**](#openhands.sdk.llm.LLM.completion) – Single entry point for LLM completion.
- [**format_messages_for_llm**](#openhands.sdk.llm.LLM.format_messages_for_llm) – Formats Message objects for LLM consumption.
- [**format_messages_for_responses**](#openhands.sdk.llm.LLM.format_messages_for_responses) – Prepare (instructions, input[]) for the OpenAI Responses API.
- [**get_token_count**](#openhands.sdk.llm.LLM.get_token_count) –
- [**is_caching_prompt_active**](#openhands.sdk.llm.LLM.is_caching_prompt_active) – Check if prompt caching is supported and enabled for current model.
- [**is_context_window_exceeded_exception**](#openhands.sdk.llm.LLM.is_context_window_exceeded_exception) – Check if the exception indicates a context window exceeded error.
- [**load_from_env**](#openhands.sdk.llm.LLM.load_from_env) –
- [**load_from_json**](#openhands.sdk.llm.LLM.load_from_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.llm.LLM.resolve_diff_from_deserialized) – Resolve differences between a deserialized LLM and the current instance.
- [**responses**](#openhands.sdk.llm.LLM.responses) – Alternative invocation path using OpenAI Responses API via LiteLLM.
- [**restore_metrics**](#openhands.sdk.llm.LLM.restore_metrics) –
- [**uses_responses_api**](#openhands.sdk.llm.LLM.uses_responses_api) – Whether this model uses the OpenAI Responses API path.
- [**vision_is_active**](#openhands.sdk.llm.LLM.vision_is_active) –

**Attributes:**

- [**OVERRIDE_ON_SERIALIZE**](#openhands.sdk.llm.LLM.OVERRIDE_ON_SERIALIZE) (<code>[tuple](#tuple)\[[str](#str), ...\]</code>) –
- [**api_key**](#openhands.sdk.llm.LLM.api_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**api_version**](#openhands.sdk.llm.LLM.api_version) (<code>[str](#str) | None</code>) –
- [**aws_access_key_id**](#openhands.sdk.llm.LLM.aws_access_key_id) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**aws_region_name**](#openhands.sdk.llm.LLM.aws_region_name) (<code>[str](#str) | None</code>) –
- [**aws_secret_access_key**](#openhands.sdk.llm.LLM.aws_secret_access_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**base_url**](#openhands.sdk.llm.LLM.base_url) (<code>[str](#str) | None</code>) –
- [**caching_prompt**](#openhands.sdk.llm.LLM.caching_prompt) (<code>[bool](#bool)</code>) –
- [**custom_llm_provider**](#openhands.sdk.llm.LLM.custom_llm_provider) (<code>[str](#str) | None</code>) –
- [**custom_tokenizer**](#openhands.sdk.llm.LLM.custom_tokenizer) (<code>[str](#str) | None</code>) –
- [**disable_stop_word**](#openhands.sdk.llm.LLM.disable_stop_word) (<code>[bool](#bool) | None</code>) –
- [**disable_vision**](#openhands.sdk.llm.LLM.disable_vision) (<code>[bool](#bool) | None</code>) –
- [**drop_params**](#openhands.sdk.llm.LLM.drop_params) (<code>[bool](#bool)</code>) –
- [**enable_encrypted_reasoning**](#openhands.sdk.llm.LLM.enable_encrypted_reasoning) (<code>[bool](#bool)</code>) –
- [**extended_thinking_budget**](#openhands.sdk.llm.LLM.extended_thinking_budget) (<code>[int](#int) | None</code>) –
- [**input_cost_per_token**](#openhands.sdk.llm.LLM.input_cost_per_token) (<code>[float](#float) | None</code>) –
- [**log_completions**](#openhands.sdk.llm.LLM.log_completions) (<code>[bool](#bool)</code>) –
- [**log_completions_folder**](#openhands.sdk.llm.LLM.log_completions_folder) (<code>[str](#str)</code>) –
- [**max_input_tokens**](#openhands.sdk.llm.LLM.max_input_tokens) (<code>[int](#int) | None</code>) –
- [**max_message_chars**](#openhands.sdk.llm.LLM.max_message_chars) (<code>[int](#int)</code>) –
- [**max_output_tokens**](#openhands.sdk.llm.LLM.max_output_tokens) (<code>[int](#int) | None</code>) –
- [**metadata**](#openhands.sdk.llm.LLM.metadata) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**metrics**](#openhands.sdk.llm.LLM.metrics) (<code>[Metrics](#openhands.sdk.llm.utils.metrics.Metrics)</code>) –
- [**model**](#openhands.sdk.llm.LLM.model) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.llm.LLM.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**model_info**](#openhands.sdk.llm.LLM.model_info) (<code>[dict](#dict) | None</code>) – Returns the model info dictionary.
- [**modify_params**](#openhands.sdk.llm.LLM.modify_params) (<code>[bool](#bool)</code>) –
- [**native_tool_calling**](#openhands.sdk.llm.LLM.native_tool_calling) (<code>[bool](#bool)</code>) –
- [**num_retries**](#openhands.sdk.llm.LLM.num_retries) (<code>[int](#int)</code>) –
- [**ollama_base_url**](#openhands.sdk.llm.LLM.ollama_base_url) (<code>[str](#str) | None</code>) –
- [**openrouter_app_name**](#openhands.sdk.llm.LLM.openrouter_app_name) (<code>[str](#str)</code>) –
- [**openrouter_site_url**](#openhands.sdk.llm.LLM.openrouter_site_url) (<code>[str](#str)</code>) –
- [**output_cost_per_token**](#openhands.sdk.llm.LLM.output_cost_per_token) (<code>[float](#float) | None</code>) –
- [**reasoning_effort**](#openhands.sdk.llm.LLM.reasoning_effort) (<code>[Literal](#typing.Literal)['low', 'medium', 'high', 'none'] | None</code>) –
- [**retry_listener**](#openhands.sdk.llm.LLM.retry_listener) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None\]</code>) –
- [**retry_max_wait**](#openhands.sdk.llm.LLM.retry_max_wait) (<code>[int](#int)</code>) –
- [**retry_min_wait**](#openhands.sdk.llm.LLM.retry_min_wait) (<code>[int](#int)</code>) –
- [**retry_multiplier**](#openhands.sdk.llm.LLM.retry_multiplier) (<code>[float](#float)</code>) –
- [**safety_settings**](#openhands.sdk.llm.LLM.safety_settings) (<code>[list](#list)\[[dict](#dict)\[[str](#str), [str](#str)\]\] | None</code>) –
- [**seed**](#openhands.sdk.llm.LLM.seed) (<code>[int](#int) | None</code>) –
- [**service_id**](#openhands.sdk.llm.LLM.service_id) (<code>[str](#str)</code>) –
- [**temperature**](#openhands.sdk.llm.LLM.temperature) (<code>[float](#float) | None</code>) –
- [**timeout**](#openhands.sdk.llm.LLM.timeout) (<code>[int](#int) | None</code>) –
- [**top_k**](#openhands.sdk.llm.LLM.top_k) (<code>[float](#float) | None</code>) –
- [**top_p**](#openhands.sdk.llm.LLM.top_p) (<code>[float](#float) | None</code>) –
- [**usage_id**](#openhands.sdk.llm.LLM.usage_id) (<code>[str](#str)</code>) –

#### `openhands.sdk.llm.LLM.OVERRIDE_ON_SERIALIZE`

```python
OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key')
```

#### `openhands.sdk.llm.LLM.api_key`

```python
api_key: SecretStr | None = Field(default=None, description='API key.')
```

#### `openhands.sdk.llm.LLM.api_version`

```python
api_version: str | None = Field(default=None, description='API version (e.g., Azure).')
```

#### `openhands.sdk.llm.LLM.aws_access_key_id`

```python
aws_access_key_id: SecretStr | None = Field(default=None)
```

#### `openhands.sdk.llm.LLM.aws_region_name`

```python
aws_region_name: str | None = Field(default=None)
```

#### `openhands.sdk.llm.LLM.aws_secret_access_key`

```python
aws_secret_access_key: SecretStr | None = Field(default=None)
```

#### `openhands.sdk.llm.LLM.base_url`

```python
base_url: str | None = Field(default=None, description='Custom base URL.')
```

#### `openhands.sdk.llm.LLM.caching_prompt`

```python
caching_prompt: bool = Field(default=True, description='Enable caching of prompts.')
```

#### `openhands.sdk.llm.LLM.completion`

```python
completion(messages, tools=None, _return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

Single entry point for LLM completion.

Normalize → (maybe) mock tools → transport → postprocess.

#### `openhands.sdk.llm.LLM.custom_llm_provider`

```python
custom_llm_provider: str | None = Field(default=None)
```

#### `openhands.sdk.llm.LLM.custom_tokenizer`

```python
custom_tokenizer: str | None = Field(default=None, description='A custom tokenizer to use for token counting.')
```

#### `openhands.sdk.llm.LLM.disable_stop_word`

```python
disable_stop_word: bool | None = Field(default=False, description='Disable using of stop word.')
```

#### `openhands.sdk.llm.LLM.disable_vision`

```python
disable_vision: bool | None = Field(default=None, description='If model is vision capable, this option allows to disable image processing (useful for cost reduction).')
```

#### `openhands.sdk.llm.LLM.drop_params`

```python
drop_params: bool = Field(default=True)
```

#### `openhands.sdk.llm.LLM.enable_encrypted_reasoning`

```python
enable_encrypted_reasoning: bool = Field(default=False, description="If True, ask for ['reasoning.encrypted_content'] in Responses API include.")
```

#### `openhands.sdk.llm.LLM.extended_thinking_budget`

```python
extended_thinking_budget: int | None = Field(default=200000, description='The budget tokens for extended thinking, supported by Anthropic models.')
```

#### `openhands.sdk.llm.LLM.format_messages_for_llm`

```python
format_messages_for_llm(messages)
```

Formats Message objects for LLM consumption.

#### `openhands.sdk.llm.LLM.format_messages_for_responses`

```python
format_messages_for_responses(messages)
```

Prepare (instructions, input[]) for the OpenAI Responses API.

- Skips prompt caching flags and string serializer concerns
- Uses Message.to_responses_value to get either instructions (system)
  or input items (others)
- Concatenates system instructions into a single instructions string

#### `openhands.sdk.llm.LLM.get_token_count`

```python
get_token_count(messages)
```

#### `openhands.sdk.llm.LLM.input_cost_per_token`

```python
input_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per input token. This will available in logs for user.')
```

#### `openhands.sdk.llm.LLM.is_caching_prompt_active`

```python
is_caching_prompt_active()
```

Check if prompt caching is supported and enabled for current model.

**Returns:**

- **boolean** (<code>[bool](#bool)</code>) – True if prompt caching is supported and enabled for the given
  model.

#### `openhands.sdk.llm.LLM.is_context_window_exceeded_exception`

```python
is_context_window_exceeded_exception(exception)
```

Check if the exception indicates a context window exceeded error.

Context window exceeded errors vary by provider, and LiteLLM does not do a
consistent job of identifying and wrapping them.

#### `openhands.sdk.llm.LLM.load_from_env`

```python
load_from_env(prefix='LLM_')
```

#### `openhands.sdk.llm.LLM.load_from_json`

```python
load_from_json(json_path)
```

#### `openhands.sdk.llm.LLM.log_completions`

```python
log_completions: bool = Field(default=False, description='Enable logging of completions.')
```

#### `openhands.sdk.llm.LLM.log_completions_folder`

```python
log_completions_folder: str = Field(default=(os.path.join(ENV_LOG_DIR, 'completions')), description='The folder to log LLM completions to. Required if log_completions is True.')
```

#### `openhands.sdk.llm.LLM.max_input_tokens`

```python
max_input_tokens: int | None = Field(default=None, ge=1, description='The maximum number of input tokens. Note that this is currently unused, and the value at runtime is actually the total tokens in OpenAI (e.g. 128,000 tokens for GPT-4).')
```

#### `openhands.sdk.llm.LLM.max_message_chars`

```python
max_message_chars: int = Field(default=30000, ge=1, description='Approx max chars in each event/content sent to the LLM.')
```

#### `openhands.sdk.llm.LLM.max_output_tokens`

```python
max_output_tokens: int | None = Field(default=None, ge=1, description='The maximum number of output tokens. This is sent to the LLM.')
```

#### `openhands.sdk.llm.LLM.metadata`

```python
metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata for the LLM instance. Example structure: {'trace_version': '1.0.0', 'tags': ['model:gpt-4', 'agent:my-agent'], 'session_id': 'session-123', 'trace_user_id': 'user-456'}")
```

#### `openhands.sdk.llm.LLM.metrics`

```python
metrics: Metrics
```

#### `openhands.sdk.llm.LLM.model`

```python
model: str = Field(default='claude-sonnet-4-20250514', description='Model name.')
```

#### `openhands.sdk.llm.LLM.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', arbitrary_types_allowed=True)
```

#### `openhands.sdk.llm.LLM.model_info`

```python
model_info: dict | None
```

Returns the model info dictionary.

#### `openhands.sdk.llm.LLM.modify_params`

```python
modify_params: bool = Field(default=True, description='Modify params allows litellm to do transformations like adding a default message, when a message is empty.')
```

#### `openhands.sdk.llm.LLM.native_tool_calling`

```python
native_tool_calling: bool = Field(default=True, description='Whether to use native tool calling.')
```

#### `openhands.sdk.llm.LLM.num_retries`

```python
num_retries: int = Field(default=5, ge=0)
```

#### `openhands.sdk.llm.LLM.ollama_base_url`

```python
ollama_base_url: str | None = Field(default=None)
```

#### `openhands.sdk.llm.LLM.openrouter_app_name`

```python
openrouter_app_name: str = Field(default='OpenHands')
```

#### `openhands.sdk.llm.LLM.openrouter_site_url`

```python
openrouter_site_url: str = Field(default='https://docs.all-hands.dev/')
```

#### `openhands.sdk.llm.LLM.output_cost_per_token`

```python
output_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per output token. This will available in logs for user.')
```

#### `openhands.sdk.llm.LLM.reasoning_effort`

```python
reasoning_effort: Literal['low', 'medium', 'high', 'none'] | None = Field(default=None, description="The effort to put into reasoning. This is a string that can be one of 'low', 'medium', 'high', or 'none'. Can apply to all reasoning models.")
```

#### `openhands.sdk.llm.LLM.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Resolve differences between a deserialized LLM and the current instance.

This is due to fields like api_key being serialized to "\*\*\*\*" in dumps,
and we want to ensure that when loading from a file, we still use the
runtime-provided api_key in the self instance.

Return a new LLM instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key) taken from `self`.

#### `openhands.sdk.llm.LLM.responses`

```python
responses(messages, tools=None, include=None, store=None, _return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

Alternative invocation path using OpenAI Responses API via LiteLLM.

Maps Message[] -> (instructions, input[]) and returns LLMResponse.
Non-stream only for v1.

#### `openhands.sdk.llm.LLM.restore_metrics`

```python
restore_metrics(metrics)
```

#### `openhands.sdk.llm.LLM.retry_listener`

```python
retry_listener: SkipJsonSchema[Callable[[int, int], None] | None] = Field(default=None, exclude=True)
```

#### `openhands.sdk.llm.LLM.retry_max_wait`

```python
retry_max_wait: int = Field(default=64, ge=0)
```

#### `openhands.sdk.llm.LLM.retry_min_wait`

```python
retry_min_wait: int = Field(default=8, ge=0)
```

#### `openhands.sdk.llm.LLM.retry_multiplier`

```python
retry_multiplier: float = Field(default=8.0, ge=0)
```

#### `openhands.sdk.llm.LLM.safety_settings`

```python
safety_settings: list[dict[str, str]] | None = Field(default=None, description='Safety settings for models that support them (like Mistral AI and Gemini)')
```

#### `openhands.sdk.llm.LLM.seed`

```python
seed: int | None = Field(default=None, description='The seed to use for random number generation.')
```

#### `openhands.sdk.llm.LLM.service_id`

```python
service_id: str
```

#### `openhands.sdk.llm.LLM.temperature`

```python
temperature: float | None = Field(default=0.0, ge=0)
```

#### `openhands.sdk.llm.LLM.timeout`

```python
timeout: int | None = Field(default=None, ge=0, description='HTTP timeout (s).')
```

#### `openhands.sdk.llm.LLM.top_k`

```python
top_k: float | None = Field(default=None, ge=0)
```

#### `openhands.sdk.llm.LLM.top_p`

```python
top_p: float | None = Field(default=1.0, ge=0, le=1)
```

#### `openhands.sdk.llm.LLM.usage_id`

```python
usage_id: str = Field(default='default', validation_alias=(AliasChoices('usage_id', 'service_id')), serialization_alias='usage_id', description='Unique usage identifier for the LLM. Used for registry lookups, telemetry, and spend tracking.')
```

#### `openhands.sdk.llm.LLM.uses_responses_api`

```python
uses_responses_api()
```

Whether this model uses the OpenAI Responses API path.

#### `openhands.sdk.llm.LLM.vision_is_active`

```python
vision_is_active()
```

### `openhands.sdk.llm.LLMRegistry`

```python
LLMRegistry(retry_listener=None)
```

A minimal LLM registry for managing LLM instances by usage ID.

This registry provides a simple way to manage multiple LLM instances,
avoiding the need to recreate LLMs with the same configuration.

**Functions:**

- [**add**](#openhands.sdk.llm.LLMRegistry.add) – Add an LLM instance to the registry.
- [**get**](#openhands.sdk.llm.LLMRegistry.get) – Get an LLM instance from the registry.
- [**list_services**](#openhands.sdk.llm.LLMRegistry.list_services) – Deprecated alias for :meth:`list_usage_ids`.
- [**list_usage_ids**](#openhands.sdk.llm.LLMRegistry.list_usage_ids) – List all registered usage IDs.
- [**notify**](#openhands.sdk.llm.LLMRegistry.notify) – Notify subscribers of registry events.
- [**subscribe**](#openhands.sdk.llm.LLMRegistry.subscribe) – Subscribe to registry events.

**Attributes:**

- [**registry_id**](#openhands.sdk.llm.LLMRegistry.registry_id) (<code>[str](#str)</code>) –
- [**retry_listener**](#openhands.sdk.llm.LLMRegistry.retry_listener) (<code>[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None</code>) –
- [**service_to_llm**](#openhands.sdk.llm.LLMRegistry.service_to_llm) (<code>[dict](#dict)\[[str](#str), [LLM](#openhands.sdk.llm.llm.LLM)\]</code>) –
- [**subscriber**](#openhands.sdk.llm.LLMRegistry.subscriber) (<code>[Callable](#collections.abc.Callable)\[\[[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)\], None\] | None</code>) –
- [**usage_to_llm**](#openhands.sdk.llm.LLMRegistry.usage_to_llm) (<code>[dict](#dict)\[[str](#str), [LLM](#openhands.sdk.llm.llm.LLM)\]</code>) – Access the internal usage-ID-to-LLM mapping.

**Parameters:**

- **retry_listener** (<code>[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None</code>) – Optional callback for retry events.

#### `openhands.sdk.llm.LLMRegistry.add`

```python
add(llm)
```

Add an LLM instance to the registry.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.llm.LLM)</code>) – The LLM instance to register.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If llm.usage_id already exists in the registry.

#### `openhands.sdk.llm.LLMRegistry.get`

```python
get(usage_id)
```

Get an LLM instance from the registry.

**Parameters:**

- **usage_id** (<code>[str](#str)</code>) – Unique identifier for the LLM usage slot.

**Returns:**

- <code>[LLM](#openhands.sdk.llm.llm.LLM)</code> – The LLM instance.

**Raises:**

- <code>[KeyError](#KeyError)</code> – If usage_id is not found in the registry.

#### `openhands.sdk.llm.LLMRegistry.list_services`

```python
list_services()
```

Deprecated alias for :meth:`list_usage_ids`.

#### `openhands.sdk.llm.LLMRegistry.list_usage_ids`

```python
list_usage_ids()
```

List all registered usage IDs.

#### `openhands.sdk.llm.LLMRegistry.notify`

```python
notify(event)
```

Notify subscribers of registry events.

**Parameters:**

- **event** (<code>[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)</code>) – The registry event to notify about.

#### `openhands.sdk.llm.LLMRegistry.registry_id`

```python
registry_id: str = str(uuid4())
```

#### `openhands.sdk.llm.LLMRegistry.retry_listener`

```python
retry_listener: Callable[[int, int], None] | None = retry_listener
```

#### `openhands.sdk.llm.LLMRegistry.service_to_llm`

```python
service_to_llm: dict[str, LLM]
```

#### `openhands.sdk.llm.LLMRegistry.subscribe`

```python
subscribe(callback)
```

Subscribe to registry events.

**Parameters:**

- **callback** (<code>[Callable](#collections.abc.Callable)\[\[[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)\], None\]</code>) – Function to call when LLMs are created or updated.

#### `openhands.sdk.llm.LLMRegistry.subscriber`

```python
subscriber: Callable[[RegistryEvent], None] | None = None
```

#### `openhands.sdk.llm.LLMRegistry.usage_to_llm`

```python
usage_to_llm: dict[str, LLM]
```

Access the internal usage-ID-to-LLM mapping.

### `openhands.sdk.llm.LLMResponse`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Result of an LLM completion request.

This type provides a clean interface for LLM completion results, exposing
only OpenHands-native types to consumers while preserving access to the
raw LiteLLM response for internal use.

**Attributes:**

- [**message**](#openhands.sdk.llm.LLMResponse.message) (<code>[Message](#openhands.sdk.llm.message.Message)</code>) – The completion message converted to OpenHands Message type
- [**metrics**](#openhands.sdk.llm.LLMResponse.metrics) (<code>[MetricsSnapshot](#openhands.sdk.llm.utils.metrics.MetricsSnapshot)</code>) – Snapshot of metrics from the completion request
- [**raw_response**](#openhands.sdk.llm.LLMResponse.raw_response) (<code>[ModelResponse](#litellm.types.utils.ModelResponse) | [ResponsesAPIResponse](#litellm.ResponsesAPIResponse)</code>) – The original LiteLLM response (ModelResponse or
  ResponsesAPIResponse) for internal use

#### `openhands.sdk.llm.LLMResponse.id`

```python
id: str
```

Get the response ID from the underlying LLM response.

This property provides a clean interface to access the response ID,
supporting both completion mode (ModelResponse) and response API modes
(ResponsesAPIResponse).

**Returns:**

- <code>[str](#str)</code> – The response ID from the LLM response

#### `openhands.sdk.llm.LLMResponse.message`

```python
message: Message
```

#### `openhands.sdk.llm.LLMResponse.metrics`

```python
metrics: MetricsSnapshot
```

#### `openhands.sdk.llm.LLMResponse.model_config`

```python
model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
```

#### `openhands.sdk.llm.LLMResponse.raw_response`

```python
raw_response: ModelResponse | ResponsesAPIResponse
```

### `openhands.sdk.llm.Message`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

**Functions:**

- [**from_llm_chat_message**](#openhands.sdk.llm.Message.from_llm_chat_message) – Convert a LiteLLMMessage (Chat Completions) to our Message class.
- [**from_llm_responses_output**](#openhands.sdk.llm.Message.from_llm_responses_output) – Convert OpenAI Responses API output items into a single assistant Message.
- [**to_chat_dict**](#openhands.sdk.llm.Message.to_chat_dict) – Serialize message for OpenAI Chat Completions.
- [**to_responses_dict**](#openhands.sdk.llm.Message.to_responses_dict) – Serialize message for OpenAI Responses (input parameter).
- [**to_responses_value**](#openhands.sdk.llm.Message.to_responses_value) – Return serialized form.

**Attributes:**

- [**cache_enabled**](#openhands.sdk.llm.Message.cache_enabled) (<code>[bool](#bool)</code>) –
- [**contains_image**](#openhands.sdk.llm.Message.contains_image) (<code>[bool](#bool)</code>) –
- [**content**](#openhands.sdk.llm.Message.content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)\]</code>) –
- [**force_string_serializer**](#openhands.sdk.llm.Message.force_string_serializer) (<code>[bool](#bool)</code>) –
- [**function_calling_enabled**](#openhands.sdk.llm.Message.function_calling_enabled) (<code>[bool](#bool)</code>) –
- [**name**](#openhands.sdk.llm.Message.name) (<code>[str](#str) | None</code>) –
- [**reasoning_content**](#openhands.sdk.llm.Message.reasoning_content) (<code>[str](#str) | None</code>) –
- [**responses_reasoning_item**](#openhands.sdk.llm.Message.responses_reasoning_item) (<code>[ReasoningItemModel](#openhands.sdk.llm.message.ReasoningItemModel) | None</code>) –
- [**role**](#openhands.sdk.llm.Message.role) (<code>[Literal](#typing.Literal)['user', 'system', 'assistant', 'tool']</code>) –
- [**thinking_blocks**](#openhands.sdk.llm.Message.thinking_blocks) (<code>[Sequence](#collections.abc.Sequence)\[[ThinkingBlock](#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](#openhands.sdk.llm.message.RedactedThinkingBlock)\]</code>) –
- [**tool_call_id**](#openhands.sdk.llm.Message.tool_call_id) (<code>[str](#str) | None</code>) –
- [**tool_calls**](#openhands.sdk.llm.Message.tool_calls) (<code>[list](#list)\[[MessageToolCall](#openhands.sdk.llm.message.MessageToolCall)\] | None</code>) –
- [**vision_enabled**](#openhands.sdk.llm.Message.vision_enabled) (<code>[bool](#bool)</code>) –

#### `openhands.sdk.llm.Message.cache_enabled`

```python
cache_enabled: bool = False
```

#### `openhands.sdk.llm.Message.contains_image`

```python
contains_image: bool
```

#### `openhands.sdk.llm.Message.content`

```python
content: Sequence[TextContent | ImageContent] = Field(default_factory=list)
```

#### `openhands.sdk.llm.Message.force_string_serializer`

```python
force_string_serializer: bool = False
```

#### `openhands.sdk.llm.Message.from_llm_chat_message`

```python
from_llm_chat_message(message)
```

Convert a LiteLLMMessage (Chat Completions) to our Message class.

Provider-agnostic mapping for reasoning:

- Prefer `message.reasoning_content` if present (LiteLLM normalized field)
- Extract `thinking_blocks` from content array (Anthropic-specific)

#### `openhands.sdk.llm.Message.from_llm_responses_output`

```python
from_llm_responses_output(output)
```

Convert OpenAI Responses API output items into a single assistant Message.

Policy (non-stream):

- Collect assistant text by concatenating output_text parts from message items
- Normalize function_call items to MessageToolCall list

#### `openhands.sdk.llm.Message.function_calling_enabled`

```python
function_calling_enabled: bool = False
```

#### `openhands.sdk.llm.Message.name`

```python
name: str | None = None
```

#### `openhands.sdk.llm.Message.reasoning_content`

```python
reasoning_content: str | None = Field(default=None, description='Intermediate reasoning/thinking content from reasoning models')
```

#### `openhands.sdk.llm.Message.responses_reasoning_item`

```python
responses_reasoning_item: ReasoningItemModel | None = Field(default=None, description='OpenAI Responses reasoning item from model output')
```

#### `openhands.sdk.llm.Message.role`

```python
role: Literal['user', 'system', 'assistant', 'tool']
```

#### `openhands.sdk.llm.Message.thinking_blocks`

```python
thinking_blocks: Sequence[ThinkingBlock | RedactedThinkingBlock] = Field(default_factory=list, description='Raw Anthropic thinking blocks for extended thinking feature')
```

#### `openhands.sdk.llm.Message.to_chat_dict`

```python
to_chat_dict()
```

Serialize message for OpenAI Chat Completions.

Chooses the appropriate content serializer and then injects threading keys:

- Assistant tool call turn: role == "assistant" and self.tool_calls
- Tool result turn: role == "tool" and self.tool_call_id (with name)

#### `openhands.sdk.llm.Message.to_responses_dict`

```python
to_responses_dict(*, vision_enabled)
```

Serialize message for OpenAI Responses (input parameter).

Produces a list of "input" items for the Responses API:

- system: returns [], system content is expected in 'instructions'
- user: one 'message' item with content parts -> input_text / input_image
  (when vision enabled)
- assistant: emits prior assistant content as input_text,
  and function_call items for tool_calls
- tool: emits function_call_output items (one per TextContent)
  with matching call_id

#### `openhands.sdk.llm.Message.to_responses_value`

```python
to_responses_value(*, vision_enabled)
```

Return serialized form.

Either an instructions string (for system) or input items (for other roles).

#### `openhands.sdk.llm.Message.tool_call_id`

```python
tool_call_id: str | None = None
```

#### `openhands.sdk.llm.Message.tool_calls`

```python
tool_calls: list[MessageToolCall] | None = None
```

#### `openhands.sdk.llm.Message.vision_enabled`

```python
vision_enabled: bool = False
```

### `openhands.sdk.llm.MessageToolCall`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Transport-agnostic tool call representation.

One canonical id is used for linking across actions/observations and
for Responses function_call_output call_id.

**Functions:**

- [**from_chat_tool_call**](#openhands.sdk.llm.MessageToolCall.from_chat_tool_call) – Create a MessageToolCall from a Chat Completions tool call.
- [**from_responses_function_call**](#openhands.sdk.llm.MessageToolCall.from_responses_function_call) – Create a MessageToolCall from a typed OpenAI Responses function_call item.
- [**to_chat_dict**](#openhands.sdk.llm.MessageToolCall.to_chat_dict) – Serialize to OpenAI Chat Completions tool_calls format.
- [**to_responses_dict**](#openhands.sdk.llm.MessageToolCall.to_responses_dict) – Serialize to OpenAI Responses 'function_call' input item format.

**Attributes:**

- [**arguments**](#openhands.sdk.llm.MessageToolCall.arguments) (<code>[str](#str)</code>) –
- [**id**](#openhands.sdk.llm.MessageToolCall.id) (<code>[str](#str)</code>) –
- [**name**](#openhands.sdk.llm.MessageToolCall.name) (<code>[str](#str)</code>) –
- [**origin**](#openhands.sdk.llm.MessageToolCall.origin) (<code>[Literal](#typing.Literal)['completion', 'responses']</code>) –

#### `openhands.sdk.llm.MessageToolCall.arguments`

```python
arguments: str = Field(..., description='JSON string of arguments')
```

#### `openhands.sdk.llm.MessageToolCall.from_chat_tool_call`

```python
from_chat_tool_call(tool_call)
```

Create a MessageToolCall from a Chat Completions tool call.

#### `openhands.sdk.llm.MessageToolCall.from_responses_function_call`

```python
from_responses_function_call(item)
```

Create a MessageToolCall from a typed OpenAI Responses function_call item.

Note: OpenAI Responses function_call.arguments is already a JSON string.

#### `openhands.sdk.llm.MessageToolCall.id`

```python
id: str = Field(..., description='Canonical tool call id')
```

#### `openhands.sdk.llm.MessageToolCall.name`

```python
name: str = Field(..., description='Tool/function name')
```

#### `openhands.sdk.llm.MessageToolCall.origin`

```python
origin: Literal['completion', 'responses'] = Field(..., description='Originating API family')
```

#### `openhands.sdk.llm.MessageToolCall.to_chat_dict`

```python
to_chat_dict()
```

Serialize to OpenAI Chat Completions tool_calls format.

#### `openhands.sdk.llm.MessageToolCall.to_responses_dict`

```python
to_responses_dict()
```

Serialize to OpenAI Responses 'function_call' input item format.

### `openhands.sdk.llm.ReasoningItemModel`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

OpenAI Responses reasoning item (non-stream, subset we consume).

Do not log or render encrypted_content.

**Attributes:**

- [**content**](#openhands.sdk.llm.ReasoningItemModel.content) (<code>[list](#list)\[[str](#str)\] | None</code>) –
- [**encrypted_content**](#openhands.sdk.llm.ReasoningItemModel.encrypted_content) (<code>[str](#str) | None</code>) –
- [**id**](#openhands.sdk.llm.ReasoningItemModel.id) (<code>[str](#str) | None</code>) –
- [**status**](#openhands.sdk.llm.ReasoningItemModel.status) (<code>[str](#str) | None</code>) –
- [**summary**](#openhands.sdk.llm.ReasoningItemModel.summary) (<code>[list](#list)\[[str](#str)\]</code>) –

#### `openhands.sdk.llm.ReasoningItemModel.content`

```python
content: list[str] | None = Field(default=None)
```

#### `openhands.sdk.llm.ReasoningItemModel.encrypted_content`

```python
encrypted_content: str | None = Field(default=None)
```

#### `openhands.sdk.llm.ReasoningItemModel.id`

```python
id: str | None = Field(default=None)
```

#### `openhands.sdk.llm.ReasoningItemModel.status`

```python
status: str | None = Field(default=None)
```

#### `openhands.sdk.llm.ReasoningItemModel.summary`

```python
summary: list[str] = Field(default_factory=list)
```

### `openhands.sdk.llm.RedactedThinkingBlock`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Redacted thinking block for previous responses without extended thinking.

This is used as a placeholder for assistant messages that were generated
before extended thinking was enabled.

**Attributes:**

- [**data**](#openhands.sdk.llm.RedactedThinkingBlock.data) (<code>[str](#str)</code>) –
- [**type**](#openhands.sdk.llm.RedactedThinkingBlock.type) (<code>[Literal](#typing.Literal)['redacted_thinking']</code>) –

#### `openhands.sdk.llm.RedactedThinkingBlock.data`

```python
data: str = Field(..., description='The redacted thinking content')
```

#### `openhands.sdk.llm.RedactedThinkingBlock.type`

```python
type: Literal['redacted_thinking'] = 'redacted_thinking'
```

### `openhands.sdk.llm.RegistryEvent`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

**Attributes:**

- [**llm**](#openhands.sdk.llm.RegistryEvent.llm) (<code>[LLM](#openhands.sdk.llm.llm.LLM)</code>) –
- [**model_config**](#openhands.sdk.llm.RegistryEvent.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –

#### `openhands.sdk.llm.RegistryEvent.llm`

```python
llm: LLM
```

#### `openhands.sdk.llm.RegistryEvent.model_config`

```python
model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
```

### `openhands.sdk.llm.RouterLLM`

Bases: <code>[LLM](#openhands.sdk.llm.llm.LLM)</code>

Base class for multiple LLM acting as a unified LLM.
This class provides a foundation for implementing model routing by
inheriting from LLM, allowing routers to work with multiple underlying
LLM models while presenting a unified LLM interface to consumers.
Key features:

- Works with multiple LLMs configured via llms_for_routing
- Delegates all other operations/properties to the selected LLM
- Provides routing interface through select_llm() method

**Functions:**

- [**completion**](#openhands.sdk.llm.RouterLLM.completion) – This method intercepts completion calls and routes them to the appropriate
- [**format_messages_for_llm**](#openhands.sdk.llm.RouterLLM.format_messages_for_llm) – Formats Message objects for LLM consumption.
- [**format_messages_for_responses**](#openhands.sdk.llm.RouterLLM.format_messages_for_responses) – Prepare (instructions, input[]) for the OpenAI Responses API.
- [**get_token_count**](#openhands.sdk.llm.RouterLLM.get_token_count) –
- [**is_caching_prompt_active**](#openhands.sdk.llm.RouterLLM.is_caching_prompt_active) – Check if prompt caching is supported and enabled for current model.
- [**is_context_window_exceeded_exception**](#openhands.sdk.llm.RouterLLM.is_context_window_exceeded_exception) – Check if the exception indicates a context window exceeded error.
- [**load_from_env**](#openhands.sdk.llm.RouterLLM.load_from_env) –
- [**load_from_json**](#openhands.sdk.llm.RouterLLM.load_from_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.llm.RouterLLM.resolve_diff_from_deserialized) – Resolve differences between a deserialized LLM and the current instance.
- [**responses**](#openhands.sdk.llm.RouterLLM.responses) – Alternative invocation path using OpenAI Responses API via LiteLLM.
- [**restore_metrics**](#openhands.sdk.llm.RouterLLM.restore_metrics) –
- [**select_llm**](#openhands.sdk.llm.RouterLLM.select_llm) – Select which LLM to use based on messages and events.
- [**set_placeholder_model**](#openhands.sdk.llm.RouterLLM.set_placeholder_model) – Guarantee `model` exists before LLM base validation runs.
- [**uses_responses_api**](#openhands.sdk.llm.RouterLLM.uses_responses_api) – Whether this model uses the OpenAI Responses API path.
- [**validate_llms_not_empty**](#openhands.sdk.llm.RouterLLM.validate_llms_not_empty) –
- [**vision_is_active**](#openhands.sdk.llm.RouterLLM.vision_is_active) –

**Attributes:**

- [**OVERRIDE_ON_SERIALIZE**](#openhands.sdk.llm.RouterLLM.OVERRIDE_ON_SERIALIZE) (<code>[tuple](#tuple)\[[str](#str), ...\]</code>) –
- [**active_llm**](#openhands.sdk.llm.RouterLLM.active_llm) (<code>[LLM](#openhands.sdk.llm.llm.LLM) | None</code>) –
- [**api_key**](#openhands.sdk.llm.RouterLLM.api_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**api_version**](#openhands.sdk.llm.RouterLLM.api_version) (<code>[str](#str) | None</code>) –
- [**aws_access_key_id**](#openhands.sdk.llm.RouterLLM.aws_access_key_id) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**aws_region_name**](#openhands.sdk.llm.RouterLLM.aws_region_name) (<code>[str](#str) | None</code>) –
- [**aws_secret_access_key**](#openhands.sdk.llm.RouterLLM.aws_secret_access_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**base_url**](#openhands.sdk.llm.RouterLLM.base_url) (<code>[str](#str) | None</code>) –
- [**caching_prompt**](#openhands.sdk.llm.RouterLLM.caching_prompt) (<code>[bool](#bool)</code>) –
- [**custom_llm_provider**](#openhands.sdk.llm.RouterLLM.custom_llm_provider) (<code>[str](#str) | None</code>) –
- [**custom_tokenizer**](#openhands.sdk.llm.RouterLLM.custom_tokenizer) (<code>[str](#str) | None</code>) –
- [**disable_stop_word**](#openhands.sdk.llm.RouterLLM.disable_stop_word) (<code>[bool](#bool) | None</code>) –
- [**disable_vision**](#openhands.sdk.llm.RouterLLM.disable_vision) (<code>[bool](#bool) | None</code>) –
- [**drop_params**](#openhands.sdk.llm.RouterLLM.drop_params) (<code>[bool](#bool)</code>) –
- [**enable_encrypted_reasoning**](#openhands.sdk.llm.RouterLLM.enable_encrypted_reasoning) (<code>[bool](#bool)</code>) –
- [**extended_thinking_budget**](#openhands.sdk.llm.RouterLLM.extended_thinking_budget) (<code>[int](#int) | None</code>) –
- [**input_cost_per_token**](#openhands.sdk.llm.RouterLLM.input_cost_per_token) (<code>[float](#float) | None</code>) –
- [**llms_for_routing**](#openhands.sdk.llm.RouterLLM.llms_for_routing) (<code>[dict](#dict)\[[str](#str), [LLM](#openhands.sdk.llm.llm.LLM)\]</code>) –
- [**log_completions**](#openhands.sdk.llm.RouterLLM.log_completions) (<code>[bool](#bool)</code>) –
- [**log_completions_folder**](#openhands.sdk.llm.RouterLLM.log_completions_folder) (<code>[str](#str)</code>) –
- [**max_input_tokens**](#openhands.sdk.llm.RouterLLM.max_input_tokens) (<code>[int](#int) | None</code>) –
- [**max_message_chars**](#openhands.sdk.llm.RouterLLM.max_message_chars) (<code>[int](#int)</code>) –
- [**max_output_tokens**](#openhands.sdk.llm.RouterLLM.max_output_tokens) (<code>[int](#int) | None</code>) –
- [**metadata**](#openhands.sdk.llm.RouterLLM.metadata) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**metrics**](#openhands.sdk.llm.RouterLLM.metrics) (<code>[Metrics](#openhands.sdk.llm.utils.metrics.Metrics)</code>) –
- [**model**](#openhands.sdk.llm.RouterLLM.model) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.llm.RouterLLM.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**model_info**](#openhands.sdk.llm.RouterLLM.model_info) (<code>[dict](#dict) | None</code>) – Returns the model info dictionary.
- [**modify_params**](#openhands.sdk.llm.RouterLLM.modify_params) (<code>[bool](#bool)</code>) –
- [**native_tool_calling**](#openhands.sdk.llm.RouterLLM.native_tool_calling) (<code>[bool](#bool)</code>) –
- [**num_retries**](#openhands.sdk.llm.RouterLLM.num_retries) (<code>[int](#int)</code>) –
- [**ollama_base_url**](#openhands.sdk.llm.RouterLLM.ollama_base_url) (<code>[str](#str) | None</code>) –
- [**openrouter_app_name**](#openhands.sdk.llm.RouterLLM.openrouter_app_name) (<code>[str](#str)</code>) –
- [**openrouter_site_url**](#openhands.sdk.llm.RouterLLM.openrouter_site_url) (<code>[str](#str)</code>) –
- [**output_cost_per_token**](#openhands.sdk.llm.RouterLLM.output_cost_per_token) (<code>[float](#float) | None</code>) –
- [**reasoning_effort**](#openhands.sdk.llm.RouterLLM.reasoning_effort) (<code>[Literal](#typing.Literal)['low', 'medium', 'high', 'none'] | None</code>) –
- [**retry_listener**](#openhands.sdk.llm.RouterLLM.retry_listener) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None\]</code>) –
- [**retry_max_wait**](#openhands.sdk.llm.RouterLLM.retry_max_wait) (<code>[int](#int)</code>) –
- [**retry_min_wait**](#openhands.sdk.llm.RouterLLM.retry_min_wait) (<code>[int](#int)</code>) –
- [**retry_multiplier**](#openhands.sdk.llm.RouterLLM.retry_multiplier) (<code>[float](#float)</code>) –
- [**router_name**](#openhands.sdk.llm.RouterLLM.router_name) (<code>[str](#str)</code>) –
- [**safety_settings**](#openhands.sdk.llm.RouterLLM.safety_settings) (<code>[list](#list)\[[dict](#dict)\[[str](#str), [str](#str)\]\] | None</code>) –
- [**seed**](#openhands.sdk.llm.RouterLLM.seed) (<code>[int](#int) | None</code>) –
- [**service_id**](#openhands.sdk.llm.RouterLLM.service_id) (<code>[str](#str)</code>) –
- [**temperature**](#openhands.sdk.llm.RouterLLM.temperature) (<code>[float](#float) | None</code>) –
- [**timeout**](#openhands.sdk.llm.RouterLLM.timeout) (<code>[int](#int) | None</code>) –
- [**top_k**](#openhands.sdk.llm.RouterLLM.top_k) (<code>[float](#float) | None</code>) –
- [**top_p**](#openhands.sdk.llm.RouterLLM.top_p) (<code>[float](#float) | None</code>) –
- [**usage_id**](#openhands.sdk.llm.RouterLLM.usage_id) (<code>[str](#str)</code>) –

#### `openhands.sdk.llm.RouterLLM.OVERRIDE_ON_SERIALIZE`

```python
OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key')
```

#### `openhands.sdk.llm.RouterLLM.active_llm`

```python
active_llm: LLM | None = Field(default=None, description='Currently selected LLM instance')
```

#### `openhands.sdk.llm.RouterLLM.api_key`

```python
api_key: SecretStr | None = Field(default=None, description='API key.')
```

#### `openhands.sdk.llm.RouterLLM.api_version`

```python
api_version: str | None = Field(default=None, description='API version (e.g., Azure).')
```

#### `openhands.sdk.llm.RouterLLM.aws_access_key_id`

```python
aws_access_key_id: SecretStr | None = Field(default=None)
```

#### `openhands.sdk.llm.RouterLLM.aws_region_name`

```python
aws_region_name: str | None = Field(default=None)
```

#### `openhands.sdk.llm.RouterLLM.aws_secret_access_key`

```python
aws_secret_access_key: SecretStr | None = Field(default=None)
```

#### `openhands.sdk.llm.RouterLLM.base_url`

```python
base_url: str | None = Field(default=None, description='Custom base URL.')
```

#### `openhands.sdk.llm.RouterLLM.caching_prompt`

```python
caching_prompt: bool = Field(default=True, description='Enable caching of prompts.')
```

#### `openhands.sdk.llm.RouterLLM.completion`

```python
completion(messages, tools=None, return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

This method intercepts completion calls and routes them to the appropriate
underlying LLM based on the routing logic implemented in select_llm().

#### `openhands.sdk.llm.RouterLLM.custom_llm_provider`

```python
custom_llm_provider: str | None = Field(default=None)
```

#### `openhands.sdk.llm.RouterLLM.custom_tokenizer`

```python
custom_tokenizer: str | None = Field(default=None, description='A custom tokenizer to use for token counting.')
```

#### `openhands.sdk.llm.RouterLLM.disable_stop_word`

```python
disable_stop_word: bool | None = Field(default=False, description='Disable using of stop word.')
```

#### `openhands.sdk.llm.RouterLLM.disable_vision`

```python
disable_vision: bool | None = Field(default=None, description='If model is vision capable, this option allows to disable image processing (useful for cost reduction).')
```

#### `openhands.sdk.llm.RouterLLM.drop_params`

```python
drop_params: bool = Field(default=True)
```

#### `openhands.sdk.llm.RouterLLM.enable_encrypted_reasoning`

```python
enable_encrypted_reasoning: bool = Field(default=False, description="If True, ask for ['reasoning.encrypted_content'] in Responses API include.")
```

#### `openhands.sdk.llm.RouterLLM.extended_thinking_budget`

```python
extended_thinking_budget: int | None = Field(default=200000, description='The budget tokens for extended thinking, supported by Anthropic models.')
```

#### `openhands.sdk.llm.RouterLLM.format_messages_for_llm`

```python
format_messages_for_llm(messages)
```

Formats Message objects for LLM consumption.

#### `openhands.sdk.llm.RouterLLM.format_messages_for_responses`

```python
format_messages_for_responses(messages)
```

Prepare (instructions, input[]) for the OpenAI Responses API.

- Skips prompt caching flags and string serializer concerns
- Uses Message.to_responses_value to get either instructions (system)
  or input items (others)
- Concatenates system instructions into a single instructions string

#### `openhands.sdk.llm.RouterLLM.get_token_count`

```python
get_token_count(messages)
```

#### `openhands.sdk.llm.RouterLLM.input_cost_per_token`

```python
input_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per input token. This will available in logs for user.')
```

#### `openhands.sdk.llm.RouterLLM.is_caching_prompt_active`

```python
is_caching_prompt_active()
```

Check if prompt caching is supported and enabled for current model.

**Returns:**

- **boolean** (<code>[bool](#bool)</code>) – True if prompt caching is supported and enabled for the given
  model.

#### `openhands.sdk.llm.RouterLLM.is_context_window_exceeded_exception`

```python
is_context_window_exceeded_exception(exception)
```

Check if the exception indicates a context window exceeded error.

Context window exceeded errors vary by provider, and LiteLLM does not do a
consistent job of identifying and wrapping them.

#### `openhands.sdk.llm.RouterLLM.llms_for_routing`

```python
llms_for_routing: dict[str, LLM] = Field(default_factory=dict)
```

#### `openhands.sdk.llm.RouterLLM.load_from_env`

```python
load_from_env(prefix='LLM_')
```

#### `openhands.sdk.llm.RouterLLM.load_from_json`

```python
load_from_json(json_path)
```

#### `openhands.sdk.llm.RouterLLM.log_completions`

```python
log_completions: bool = Field(default=False, description='Enable logging of completions.')
```

#### `openhands.sdk.llm.RouterLLM.log_completions_folder`

```python
log_completions_folder: str = Field(default=(os.path.join(ENV_LOG_DIR, 'completions')), description='The folder to log LLM completions to. Required if log_completions is True.')
```

#### `openhands.sdk.llm.RouterLLM.max_input_tokens`

```python
max_input_tokens: int | None = Field(default=None, ge=1, description='The maximum number of input tokens. Note that this is currently unused, and the value at runtime is actually the total tokens in OpenAI (e.g. 128,000 tokens for GPT-4).')
```

#### `openhands.sdk.llm.RouterLLM.max_message_chars`

```python
max_message_chars: int = Field(default=30000, ge=1, description='Approx max chars in each event/content sent to the LLM.')
```

#### `openhands.sdk.llm.RouterLLM.max_output_tokens`

```python
max_output_tokens: int | None = Field(default=None, ge=1, description='The maximum number of output tokens. This is sent to the LLM.')
```

#### `openhands.sdk.llm.RouterLLM.metadata`

```python
metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata for the LLM instance. Example structure: {'trace_version': '1.0.0', 'tags': ['model:gpt-4', 'agent:my-agent'], 'session_id': 'session-123', 'trace_user_id': 'user-456'}")
```

#### `openhands.sdk.llm.RouterLLM.metrics`

```python
metrics: Metrics
```

#### `openhands.sdk.llm.RouterLLM.model`

```python
model: str = Field(default='claude-sonnet-4-20250514', description='Model name.')
```

#### `openhands.sdk.llm.RouterLLM.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', arbitrary_types_allowed=True)
```

#### `openhands.sdk.llm.RouterLLM.model_info`

```python
model_info: dict | None
```

Returns the model info dictionary.

#### `openhands.sdk.llm.RouterLLM.modify_params`

```python
modify_params: bool = Field(default=True, description='Modify params allows litellm to do transformations like adding a default message, when a message is empty.')
```

#### `openhands.sdk.llm.RouterLLM.native_tool_calling`

```python
native_tool_calling: bool = Field(default=True, description='Whether to use native tool calling.')
```

#### `openhands.sdk.llm.RouterLLM.num_retries`

```python
num_retries: int = Field(default=5, ge=0)
```

#### `openhands.sdk.llm.RouterLLM.ollama_base_url`

```python
ollama_base_url: str | None = Field(default=None)
```

#### `openhands.sdk.llm.RouterLLM.openrouter_app_name`

```python
openrouter_app_name: str = Field(default='OpenHands')
```

#### `openhands.sdk.llm.RouterLLM.openrouter_site_url`

```python
openrouter_site_url: str = Field(default='https://docs.all-hands.dev/')
```

#### `openhands.sdk.llm.RouterLLM.output_cost_per_token`

```python
output_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per output token. This will available in logs for user.')
```

#### `openhands.sdk.llm.RouterLLM.reasoning_effort`

```python
reasoning_effort: Literal['low', 'medium', 'high', 'none'] | None = Field(default=None, description="The effort to put into reasoning. This is a string that can be one of 'low', 'medium', 'high', or 'none'. Can apply to all reasoning models.")
```

#### `openhands.sdk.llm.RouterLLM.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Resolve differences between a deserialized LLM and the current instance.

This is due to fields like api_key being serialized to "\*\*\*\*" in dumps,
and we want to ensure that when loading from a file, we still use the
runtime-provided api_key in the self instance.

Return a new LLM instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key) taken from `self`.

#### `openhands.sdk.llm.RouterLLM.responses`

```python
responses(messages, tools=None, include=None, store=None, _return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

Alternative invocation path using OpenAI Responses API via LiteLLM.

Maps Message[] -> (instructions, input[]) and returns LLMResponse.
Non-stream only for v1.

#### `openhands.sdk.llm.RouterLLM.restore_metrics`

```python
restore_metrics(metrics)
```

#### `openhands.sdk.llm.RouterLLM.retry_listener`

```python
retry_listener: SkipJsonSchema[Callable[[int, int], None] | None] = Field(default=None, exclude=True)
```

#### `openhands.sdk.llm.RouterLLM.retry_max_wait`

```python
retry_max_wait: int = Field(default=64, ge=0)
```

#### `openhands.sdk.llm.RouterLLM.retry_min_wait`

```python
retry_min_wait: int = Field(default=8, ge=0)
```

#### `openhands.sdk.llm.RouterLLM.retry_multiplier`

```python
retry_multiplier: float = Field(default=8.0, ge=0)
```

#### `openhands.sdk.llm.RouterLLM.router_name`

```python
router_name: str = Field(default='base_router', description='Name of the router')
```

#### `openhands.sdk.llm.RouterLLM.safety_settings`

```python
safety_settings: list[dict[str, str]] | None = Field(default=None, description='Safety settings for models that support them (like Mistral AI and Gemini)')
```

#### `openhands.sdk.llm.RouterLLM.seed`

```python
seed: int | None = Field(default=None, description='The seed to use for random number generation.')
```

#### `openhands.sdk.llm.RouterLLM.select_llm`

```python
select_llm(messages)
```

Select which LLM to use based on messages and events.

This method implements the core routing logic for the RouterLLM.
Subclasses should analyze the provided messages to determine which
LLM from llms_for_routing is most appropriate for handling the request.

**Parameters:**

- **messages** (<code>[list](#list)\[[Message](#openhands.sdk.llm.message.Message)\]</code>) – List of messages in the conversation that can be used
  to inform the routing decision.

**Returns:**

- <code>[str](#str)</code> – The key/name of the LLM to use from llms_for_routing dictionary.

#### `openhands.sdk.llm.RouterLLM.service_id`

```python
service_id: str
```

#### `openhands.sdk.llm.RouterLLM.set_placeholder_model`

```python
set_placeholder_model(data)
```

Guarantee `model` exists before LLM base validation runs.

#### `openhands.sdk.llm.RouterLLM.temperature`

```python
temperature: float | None = Field(default=0.0, ge=0)
```

#### `openhands.sdk.llm.RouterLLM.timeout`

```python
timeout: int | None = Field(default=None, ge=0, description='HTTP timeout (s).')
```

#### `openhands.sdk.llm.RouterLLM.top_k`

```python
top_k: float | None = Field(default=None, ge=0)
```

#### `openhands.sdk.llm.RouterLLM.top_p`

```python
top_p: float | None = Field(default=1.0, ge=0, le=1)
```

#### `openhands.sdk.llm.RouterLLM.usage_id`

```python
usage_id: str = Field(default='default', validation_alias=(AliasChoices('usage_id', 'service_id')), serialization_alias='usage_id', description='Unique usage identifier for the LLM. Used for registry lookups, telemetry, and spend tracking.')
```

#### `openhands.sdk.llm.RouterLLM.uses_responses_api`

```python
uses_responses_api()
```

Whether this model uses the OpenAI Responses API path.

#### `openhands.sdk.llm.RouterLLM.validate_llms_not_empty`

```python
validate_llms_not_empty(v)
```

#### `openhands.sdk.llm.RouterLLM.vision_is_active`

```python
vision_is_active()
```

### `openhands.sdk.llm.TextContent`

Bases: <code>[BaseContent](#openhands.sdk.llm.message.BaseContent)</code>

**Functions:**

- [**to_llm_dict**](#openhands.sdk.llm.TextContent.to_llm_dict) – Convert to LLM API format.

**Attributes:**

- [**cache_prompt**](#openhands.sdk.llm.TextContent.cache_prompt) (<code>[bool](#bool)</code>) –
- [**model_config**](#openhands.sdk.llm.TextContent.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**text**](#openhands.sdk.llm.TextContent.text) (<code>[str](#str)</code>) –
- [**type**](#openhands.sdk.llm.TextContent.type) (<code>[Literal](#typing.Literal)['text']</code>) –

#### `openhands.sdk.llm.TextContent.cache_prompt`

```python
cache_prompt: bool = False
```

#### `openhands.sdk.llm.TextContent.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', populate_by_name=True)
```

#### `openhands.sdk.llm.TextContent.text`

```python
text: str
```

#### `openhands.sdk.llm.TextContent.to_llm_dict`

```python
to_llm_dict()
```

Convert to LLM API format.

#### `openhands.sdk.llm.TextContent.type`

```python
type: Literal['text'] = 'text'
```

### `openhands.sdk.llm.ThinkingBlock`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Anthropic thinking block for extended thinking feature.

This represents the raw thinking blocks returned by Anthropic models
when extended thinking is enabled. These blocks must be preserved
and passed back to the API for tool use scenarios.

**Attributes:**

- [**signature**](#openhands.sdk.llm.ThinkingBlock.signature) (<code>[str](#str)</code>) –
- [**thinking**](#openhands.sdk.llm.ThinkingBlock.thinking) (<code>[str](#str)</code>) –
- [**type**](#openhands.sdk.llm.ThinkingBlock.type) (<code>[Literal](#typing.Literal)['thinking']</code>) –

#### `openhands.sdk.llm.ThinkingBlock.signature`

```python
signature: str = Field(..., description='Cryptographic signature for the thinking block')
```

#### `openhands.sdk.llm.ThinkingBlock.thinking`

```python
thinking: str = Field(..., description='The thinking content')
```

#### `openhands.sdk.llm.ThinkingBlock.type`

```python
type: Literal['thinking'] = 'thinking'
```

### `openhands.sdk.llm.content_to_str`

```python
content_to_str(contents)
```

Convert a list of TextContent and ImageContent to a list of strings.

This is primarily used for display purposes.

### `openhands.sdk.llm.exceptions`

**Classes:**

- [**FunctionCallConversionError**](#openhands.sdk.llm.exceptions.FunctionCallConversionError) – Exception raised when FunctionCallingConverter failed to convert a non-function
- [**FunctionCallNotExistsError**](#openhands.sdk.llm.exceptions.FunctionCallNotExistsError) – Exception raised when an LLM call a tool that is not registered.
- [**FunctionCallValidationError**](#openhands.sdk.llm.exceptions.FunctionCallValidationError) – Exception raised when FunctionCallingConverter failed to validate a function
- [**LLMContextWindowExceedError**](#openhands.sdk.llm.exceptions.LLMContextWindowExceedError) –
- [**LLMError**](#openhands.sdk.llm.exceptions.LLMError) – Base class for all LLM-related exceptions.
- [**LLMMalformedActionError**](#openhands.sdk.llm.exceptions.LLMMalformedActionError) – Exception raised when the LLM response is malformed or does not conform to the expected format.
- [**LLMNoActionError**](#openhands.sdk.llm.exceptions.LLMNoActionError) – Exception raised when the LLM response does not include an action.
- [**LLMNoResponseError**](#openhands.sdk.llm.exceptions.LLMNoResponseError) – Exception raised when the LLM does not return a response, typically seen in
- [**LLMResponseError**](#openhands.sdk.llm.exceptions.LLMResponseError) – Exception raised when the LLM response does not include an action or the action is not of the expected type.
- [**OperationCancelled**](#openhands.sdk.llm.exceptions.OperationCancelled) – Exception raised when an operation is cancelled (e.g. by a keyboard interrupt).
- [**UserCancelledError**](#openhands.sdk.llm.exceptions.UserCancelledError) –

#### `openhands.sdk.llm.exceptions.FunctionCallConversionError`

```python
FunctionCallConversionError(message)
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

Exception raised when FunctionCallingConverter failed to convert a non-function
call message to a function call message.

This typically happens when there's a malformed message (e.g., missing
\<function=...> tags). But not due to LLM output.

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.FunctionCallConversionError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.FunctionCallConversionError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.FunctionCallNotExistsError`

```python
FunctionCallNotExistsError(message)
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

Exception raised when an LLM call a tool that is not registered.

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.FunctionCallNotExistsError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.FunctionCallNotExistsError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.FunctionCallValidationError`

```python
FunctionCallValidationError(message)
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

Exception raised when FunctionCallingConverter failed to validate a function
call message.

This typically happens when the LLM outputs unrecognized function call /
parameter names / values.

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.FunctionCallValidationError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.FunctionCallValidationError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.LLMContextWindowExceedError`

```python
LLMContextWindowExceedError(message='Conversation history longer than LLM context window limit. Consider turning on enable_history_truncation config to avoid this error')
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.LLMContextWindowExceedError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.LLMContextWindowExceedError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.LLMError`

```python
LLMError(message)
```

Bases: <code>[Exception](#Exception)</code>

Base class for all LLM-related exceptions.

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.LLMError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.LLMError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.LLMMalformedActionError`

```python
LLMMalformedActionError(message='Malformed response')
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

Exception raised when the LLM response is malformed or does not conform to the expected format.

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.LLMMalformedActionError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.LLMMalformedActionError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.LLMNoActionError`

```python
LLMNoActionError(message='Agent must return an action')
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

Exception raised when the LLM response does not include an action.

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.LLMNoActionError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.LLMNoActionError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.LLMNoResponseError`

```python
LLMNoResponseError(message='LLM did not return a response. This is only seen in Gemini models so far.')
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

Exception raised when the LLM does not return a response, typically seen in
Gemini models.

This exception should be retried
Typically, after retry with a non-zero temperature, the LLM will return a response

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.LLMNoResponseError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.LLMNoResponseError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.LLMResponseError`

```python
LLMResponseError(message='Failed to retrieve action from LLM response')
```

Bases: <code>[LLMError](#openhands.sdk.llm.exceptions.LLMError)</code>

Exception raised when the LLM response does not include an action or the action is not of the expected type.

**Attributes:**

- [**message**](#openhands.sdk.llm.exceptions.LLMResponseError.message) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.exceptions.LLMResponseError.message`

```python
message: str = message
```

#### `openhands.sdk.llm.exceptions.OperationCancelled`

```python
OperationCancelled(message='Operation was cancelled')
```

Bases: <code>[Exception](#Exception)</code>

Exception raised when an operation is cancelled (e.g. by a keyboard interrupt).

#### `openhands.sdk.llm.exceptions.UserCancelledError`

```python
UserCancelledError(message='User cancelled the request')
```

Bases: <code>[Exception](#Exception)</code>

### `openhands.sdk.llm.llm`

**Classes:**

- [**LLM**](#openhands.sdk.llm.llm.LLM) – Refactored LLM: simple `completion()`, centralized Telemetry, tiny helpers.

#### `openhands.sdk.llm.llm.LLM`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>, <code>[RetryMixin](#openhands.sdk.llm.utils.retry_mixin.RetryMixin)</code>, <code>[NonNativeToolCallingMixin](#openhands.sdk.llm.mixins.non_native_fc.NonNativeToolCallingMixin)</code>

Refactored LLM: simple `completion()`, centralized Telemetry, tiny helpers.

**Functions:**

- [**completion**](#openhands.sdk.llm.llm.LLM.completion) – Single entry point for LLM completion.
- [**format_messages_for_llm**](#openhands.sdk.llm.llm.LLM.format_messages_for_llm) – Formats Message objects for LLM consumption.
- [**format_messages_for_responses**](#openhands.sdk.llm.llm.LLM.format_messages_for_responses) – Prepare (instructions, input[]) for the OpenAI Responses API.
- [**get_token_count**](#openhands.sdk.llm.llm.LLM.get_token_count) –
- [**is_caching_prompt_active**](#openhands.sdk.llm.llm.LLM.is_caching_prompt_active) – Check if prompt caching is supported and enabled for current model.
- [**is_context_window_exceeded_exception**](#openhands.sdk.llm.llm.LLM.is_context_window_exceeded_exception) – Check if the exception indicates a context window exceeded error.
- [**load_from_env**](#openhands.sdk.llm.llm.LLM.load_from_env) –
- [**load_from_json**](#openhands.sdk.llm.llm.LLM.load_from_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.llm.llm.LLM.resolve_diff_from_deserialized) – Resolve differences between a deserialized LLM and the current instance.
- [**responses**](#openhands.sdk.llm.llm.LLM.responses) – Alternative invocation path using OpenAI Responses API via LiteLLM.
- [**restore_metrics**](#openhands.sdk.llm.llm.LLM.restore_metrics) –
- [**uses_responses_api**](#openhands.sdk.llm.llm.LLM.uses_responses_api) – Whether this model uses the OpenAI Responses API path.
- [**vision_is_active**](#openhands.sdk.llm.llm.LLM.vision_is_active) –

**Attributes:**

- [**OVERRIDE_ON_SERIALIZE**](#openhands.sdk.llm.llm.LLM.OVERRIDE_ON_SERIALIZE) (<code>[tuple](#tuple)\[[str](#str), ...\]</code>) –
- [**api_key**](#openhands.sdk.llm.llm.LLM.api_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**api_version**](#openhands.sdk.llm.llm.LLM.api_version) (<code>[str](#str) | None</code>) –
- [**aws_access_key_id**](#openhands.sdk.llm.llm.LLM.aws_access_key_id) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**aws_region_name**](#openhands.sdk.llm.llm.LLM.aws_region_name) (<code>[str](#str) | None</code>) –
- [**aws_secret_access_key**](#openhands.sdk.llm.llm.LLM.aws_secret_access_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**base_url**](#openhands.sdk.llm.llm.LLM.base_url) (<code>[str](#str) | None</code>) –
- [**caching_prompt**](#openhands.sdk.llm.llm.LLM.caching_prompt) (<code>[bool](#bool)</code>) –
- [**custom_llm_provider**](#openhands.sdk.llm.llm.LLM.custom_llm_provider) (<code>[str](#str) | None</code>) –
- [**custom_tokenizer**](#openhands.sdk.llm.llm.LLM.custom_tokenizer) (<code>[str](#str) | None</code>) –
- [**disable_stop_word**](#openhands.sdk.llm.llm.LLM.disable_stop_word) (<code>[bool](#bool) | None</code>) –
- [**disable_vision**](#openhands.sdk.llm.llm.LLM.disable_vision) (<code>[bool](#bool) | None</code>) –
- [**drop_params**](#openhands.sdk.llm.llm.LLM.drop_params) (<code>[bool](#bool)</code>) –
- [**enable_encrypted_reasoning**](#openhands.sdk.llm.llm.LLM.enable_encrypted_reasoning) (<code>[bool](#bool)</code>) –
- [**extended_thinking_budget**](#openhands.sdk.llm.llm.LLM.extended_thinking_budget) (<code>[int](#int) | None</code>) –
- [**input_cost_per_token**](#openhands.sdk.llm.llm.LLM.input_cost_per_token) (<code>[float](#float) | None</code>) –
- [**log_completions**](#openhands.sdk.llm.llm.LLM.log_completions) (<code>[bool](#bool)</code>) –
- [**log_completions_folder**](#openhands.sdk.llm.llm.LLM.log_completions_folder) (<code>[str](#str)</code>) –
- [**max_input_tokens**](#openhands.sdk.llm.llm.LLM.max_input_tokens) (<code>[int](#int) | None</code>) –
- [**max_message_chars**](#openhands.sdk.llm.llm.LLM.max_message_chars) (<code>[int](#int)</code>) –
- [**max_output_tokens**](#openhands.sdk.llm.llm.LLM.max_output_tokens) (<code>[int](#int) | None</code>) –
- [**metadata**](#openhands.sdk.llm.llm.LLM.metadata) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**metrics**](#openhands.sdk.llm.llm.LLM.metrics) (<code>[Metrics](#openhands.sdk.llm.utils.metrics.Metrics)</code>) –
- [**model**](#openhands.sdk.llm.llm.LLM.model) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.llm.llm.LLM.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**model_info**](#openhands.sdk.llm.llm.LLM.model_info) (<code>[dict](#dict) | None</code>) – Returns the model info dictionary.
- [**modify_params**](#openhands.sdk.llm.llm.LLM.modify_params) (<code>[bool](#bool)</code>) –
- [**native_tool_calling**](#openhands.sdk.llm.llm.LLM.native_tool_calling) (<code>[bool](#bool)</code>) –
- [**num_retries**](#openhands.sdk.llm.llm.LLM.num_retries) (<code>[int](#int)</code>) –
- [**ollama_base_url**](#openhands.sdk.llm.llm.LLM.ollama_base_url) (<code>[str](#str) | None</code>) –
- [**openrouter_app_name**](#openhands.sdk.llm.llm.LLM.openrouter_app_name) (<code>[str](#str)</code>) –
- [**openrouter_site_url**](#openhands.sdk.llm.llm.LLM.openrouter_site_url) (<code>[str](#str)</code>) –
- [**output_cost_per_token**](#openhands.sdk.llm.llm.LLM.output_cost_per_token) (<code>[float](#float) | None</code>) –
- [**reasoning_effort**](#openhands.sdk.llm.llm.LLM.reasoning_effort) (<code>[Literal](#typing.Literal)['low', 'medium', 'high', 'none'] | None</code>) –
- [**retry_listener**](#openhands.sdk.llm.llm.LLM.retry_listener) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None\]</code>) –
- [**retry_max_wait**](#openhands.sdk.llm.llm.LLM.retry_max_wait) (<code>[int](#int)</code>) –
- [**retry_min_wait**](#openhands.sdk.llm.llm.LLM.retry_min_wait) (<code>[int](#int)</code>) –
- [**retry_multiplier**](#openhands.sdk.llm.llm.LLM.retry_multiplier) (<code>[float](#float)</code>) –
- [**safety_settings**](#openhands.sdk.llm.llm.LLM.safety_settings) (<code>[list](#list)\[[dict](#dict)\[[str](#str), [str](#str)\]\] | None</code>) –
- [**seed**](#openhands.sdk.llm.llm.LLM.seed) (<code>[int](#int) | None</code>) –
- [**service_id**](#openhands.sdk.llm.llm.LLM.service_id) (<code>[str](#str)</code>) –
- [**temperature**](#openhands.sdk.llm.llm.LLM.temperature) (<code>[float](#float) | None</code>) –
- [**timeout**](#openhands.sdk.llm.llm.LLM.timeout) (<code>[int](#int) | None</code>) –
- [**top_k**](#openhands.sdk.llm.llm.LLM.top_k) (<code>[float](#float) | None</code>) –
- [**top_p**](#openhands.sdk.llm.llm.LLM.top_p) (<code>[float](#float) | None</code>) –
- [**usage_id**](#openhands.sdk.llm.llm.LLM.usage_id) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.llm.LLM.OVERRIDE_ON_SERIALIZE`

```python
OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key')
```

##### `openhands.sdk.llm.llm.LLM.api_key`

```python
api_key: SecretStr | None = Field(default=None, description='API key.')
```

##### `openhands.sdk.llm.llm.LLM.api_version`

```python
api_version: str | None = Field(default=None, description='API version (e.g., Azure).')
```

##### `openhands.sdk.llm.llm.LLM.aws_access_key_id`

```python
aws_access_key_id: SecretStr | None = Field(default=None)
```

##### `openhands.sdk.llm.llm.LLM.aws_region_name`

```python
aws_region_name: str | None = Field(default=None)
```

##### `openhands.sdk.llm.llm.LLM.aws_secret_access_key`

```python
aws_secret_access_key: SecretStr | None = Field(default=None)
```

##### `openhands.sdk.llm.llm.LLM.base_url`

```python
base_url: str | None = Field(default=None, description='Custom base URL.')
```

##### `openhands.sdk.llm.llm.LLM.caching_prompt`

```python
caching_prompt: bool = Field(default=True, description='Enable caching of prompts.')
```

##### `openhands.sdk.llm.llm.LLM.completion`

```python
completion(messages, tools=None, _return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

Single entry point for LLM completion.

Normalize → (maybe) mock tools → transport → postprocess.

##### `openhands.sdk.llm.llm.LLM.custom_llm_provider`

```python
custom_llm_provider: str | None = Field(default=None)
```

##### `openhands.sdk.llm.llm.LLM.custom_tokenizer`

```python
custom_tokenizer: str | None = Field(default=None, description='A custom tokenizer to use for token counting.')
```

##### `openhands.sdk.llm.llm.LLM.disable_stop_word`

```python
disable_stop_word: bool | None = Field(default=False, description='Disable using of stop word.')
```

##### `openhands.sdk.llm.llm.LLM.disable_vision`

```python
disable_vision: bool | None = Field(default=None, description='If model is vision capable, this option allows to disable image processing (useful for cost reduction).')
```

##### `openhands.sdk.llm.llm.LLM.drop_params`

```python
drop_params: bool = Field(default=True)
```

##### `openhands.sdk.llm.llm.LLM.enable_encrypted_reasoning`

```python
enable_encrypted_reasoning: bool = Field(default=False, description="If True, ask for ['reasoning.encrypted_content'] in Responses API include.")
```

##### `openhands.sdk.llm.llm.LLM.extended_thinking_budget`

```python
extended_thinking_budget: int | None = Field(default=200000, description='The budget tokens for extended thinking, supported by Anthropic models.')
```

##### `openhands.sdk.llm.llm.LLM.format_messages_for_llm`

```python
format_messages_for_llm(messages)
```

Formats Message objects for LLM consumption.

##### `openhands.sdk.llm.llm.LLM.format_messages_for_responses`

```python
format_messages_for_responses(messages)
```

Prepare (instructions, input[]) for the OpenAI Responses API.

- Skips prompt caching flags and string serializer concerns
- Uses Message.to_responses_value to get either instructions (system)
  or input items (others)
- Concatenates system instructions into a single instructions string

##### `openhands.sdk.llm.llm.LLM.get_token_count`

```python
get_token_count(messages)
```

##### `openhands.sdk.llm.llm.LLM.input_cost_per_token`

```python
input_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per input token. This will available in logs for user.')
```

##### `openhands.sdk.llm.llm.LLM.is_caching_prompt_active`

```python
is_caching_prompt_active()
```

Check if prompt caching is supported and enabled for current model.

**Returns:**

- **boolean** (<code>[bool](#bool)</code>) – True if prompt caching is supported and enabled for the given
  model.

##### `openhands.sdk.llm.llm.LLM.is_context_window_exceeded_exception`

```python
is_context_window_exceeded_exception(exception)
```

Check if the exception indicates a context window exceeded error.

Context window exceeded errors vary by provider, and LiteLLM does not do a
consistent job of identifying and wrapping them.

##### `openhands.sdk.llm.llm.LLM.load_from_env`

```python
load_from_env(prefix='LLM_')
```

##### `openhands.sdk.llm.llm.LLM.load_from_json`

```python
load_from_json(json_path)
```

##### `openhands.sdk.llm.llm.LLM.log_completions`

```python
log_completions: bool = Field(default=False, description='Enable logging of completions.')
```

##### `openhands.sdk.llm.llm.LLM.log_completions_folder`

```python
log_completions_folder: str = Field(default=(os.path.join(ENV_LOG_DIR, 'completions')), description='The folder to log LLM completions to. Required if log_completions is True.')
```

##### `openhands.sdk.llm.llm.LLM.max_input_tokens`

```python
max_input_tokens: int | None = Field(default=None, ge=1, description='The maximum number of input tokens. Note that this is currently unused, and the value at runtime is actually the total tokens in OpenAI (e.g. 128,000 tokens for GPT-4).')
```

##### `openhands.sdk.llm.llm.LLM.max_message_chars`

```python
max_message_chars: int = Field(default=30000, ge=1, description='Approx max chars in each event/content sent to the LLM.')
```

##### `openhands.sdk.llm.llm.LLM.max_output_tokens`

```python
max_output_tokens: int | None = Field(default=None, ge=1, description='The maximum number of output tokens. This is sent to the LLM.')
```

##### `openhands.sdk.llm.llm.LLM.metadata`

```python
metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata for the LLM instance. Example structure: {'trace_version': '1.0.0', 'tags': ['model:gpt-4', 'agent:my-agent'], 'session_id': 'session-123', 'trace_user_id': 'user-456'}")
```

##### `openhands.sdk.llm.llm.LLM.metrics`

```python
metrics: Metrics
```

##### `openhands.sdk.llm.llm.LLM.model`

```python
model: str = Field(default='claude-sonnet-4-20250514', description='Model name.')
```

##### `openhands.sdk.llm.llm.LLM.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', arbitrary_types_allowed=True)
```

##### `openhands.sdk.llm.llm.LLM.model_info`

```python
model_info: dict | None
```

Returns the model info dictionary.

##### `openhands.sdk.llm.llm.LLM.modify_params`

```python
modify_params: bool = Field(default=True, description='Modify params allows litellm to do transformations like adding a default message, when a message is empty.')
```

##### `openhands.sdk.llm.llm.LLM.native_tool_calling`

```python
native_tool_calling: bool = Field(default=True, description='Whether to use native tool calling.')
```

##### `openhands.sdk.llm.llm.LLM.num_retries`

```python
num_retries: int = Field(default=5, ge=0)
```

##### `openhands.sdk.llm.llm.LLM.ollama_base_url`

```python
ollama_base_url: str | None = Field(default=None)
```

##### `openhands.sdk.llm.llm.LLM.openrouter_app_name`

```python
openrouter_app_name: str = Field(default='OpenHands')
```

##### `openhands.sdk.llm.llm.LLM.openrouter_site_url`

```python
openrouter_site_url: str = Field(default='https://docs.all-hands.dev/')
```

##### `openhands.sdk.llm.llm.LLM.output_cost_per_token`

```python
output_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per output token. This will available in logs for user.')
```

##### `openhands.sdk.llm.llm.LLM.reasoning_effort`

```python
reasoning_effort: Literal['low', 'medium', 'high', 'none'] | None = Field(default=None, description="The effort to put into reasoning. This is a string that can be one of 'low', 'medium', 'high', or 'none'. Can apply to all reasoning models.")
```

##### `openhands.sdk.llm.llm.LLM.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Resolve differences between a deserialized LLM and the current instance.

This is due to fields like api_key being serialized to "\*\*\*\*" in dumps,
and we want to ensure that when loading from a file, we still use the
runtime-provided api_key in the self instance.

Return a new LLM instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key) taken from `self`.

##### `openhands.sdk.llm.llm.LLM.responses`

```python
responses(messages, tools=None, include=None, store=None, _return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

Alternative invocation path using OpenAI Responses API via LiteLLM.

Maps Message[] -> (instructions, input[]) and returns LLMResponse.
Non-stream only for v1.

##### `openhands.sdk.llm.llm.LLM.restore_metrics`

```python
restore_metrics(metrics)
```

##### `openhands.sdk.llm.llm.LLM.retry_listener`

```python
retry_listener: SkipJsonSchema[Callable[[int, int], None] | None] = Field(default=None, exclude=True)
```

##### `openhands.sdk.llm.llm.LLM.retry_max_wait`

```python
retry_max_wait: int = Field(default=64, ge=0)
```

##### `openhands.sdk.llm.llm.LLM.retry_min_wait`

```python
retry_min_wait: int = Field(default=8, ge=0)
```

##### `openhands.sdk.llm.llm.LLM.retry_multiplier`

```python
retry_multiplier: float = Field(default=8.0, ge=0)
```

##### `openhands.sdk.llm.llm.LLM.safety_settings`

```python
safety_settings: list[dict[str, str]] | None = Field(default=None, description='Safety settings for models that support them (like Mistral AI and Gemini)')
```

##### `openhands.sdk.llm.llm.LLM.seed`

```python
seed: int | None = Field(default=None, description='The seed to use for random number generation.')
```

##### `openhands.sdk.llm.llm.LLM.service_id`

```python
service_id: str
```

##### `openhands.sdk.llm.llm.LLM.temperature`

```python
temperature: float | None = Field(default=0.0, ge=0)
```

##### `openhands.sdk.llm.llm.LLM.timeout`

```python
timeout: int | None = Field(default=None, ge=0, description='HTTP timeout (s).')
```

##### `openhands.sdk.llm.llm.LLM.top_k`

```python
top_k: float | None = Field(default=None, ge=0)
```

##### `openhands.sdk.llm.llm.LLM.top_p`

```python
top_p: float | None = Field(default=1.0, ge=0, le=1)
```

##### `openhands.sdk.llm.llm.LLM.usage_id`

```python
usage_id: str = Field(default='default', validation_alias=(AliasChoices('usage_id', 'service_id')), serialization_alias='usage_id', description='Unique usage identifier for the LLM. Used for registry lookups, telemetry, and spend tracking.')
```

##### `openhands.sdk.llm.llm.LLM.uses_responses_api`

```python
uses_responses_api()
```

Whether this model uses the OpenAI Responses API path.

##### `openhands.sdk.llm.llm.LLM.vision_is_active`

```python
vision_is_active()
```

### `openhands.sdk.llm.llm_registry`

**Classes:**

- [**LLMRegistry**](#openhands.sdk.llm.llm_registry.LLMRegistry) – A minimal LLM registry for managing LLM instances by usage ID.
- [**RegistryEvent**](#openhands.sdk.llm.llm_registry.RegistryEvent) –

**Attributes:**

- [**LIST_SERVICES_DEPRECATION_MSG**](#openhands.sdk.llm.llm_registry.LIST_SERVICES_DEPRECATION_MSG) –
- [**SERVICE_TO_LLM_DEPRECATION_MSG**](#openhands.sdk.llm.llm_registry.SERVICE_TO_LLM_DEPRECATION_MSG) –
- [**logger**](#openhands.sdk.llm.llm_registry.logger) –

#### `openhands.sdk.llm.llm_registry.LIST_SERVICES_DEPRECATION_MSG`

```python
LIST_SERVICES_DEPRECATION_MSG = 'LLMRegistry.list_services is deprecated and will be removed in a future release; use list_usage_ids instead.'
```

#### `openhands.sdk.llm.llm_registry.LLMRegistry`

```python
LLMRegistry(retry_listener=None)
```

A minimal LLM registry for managing LLM instances by usage ID.

This registry provides a simple way to manage multiple LLM instances,
avoiding the need to recreate LLMs with the same configuration.

**Functions:**

- [**add**](#openhands.sdk.llm.llm_registry.LLMRegistry.add) – Add an LLM instance to the registry.
- [**get**](#openhands.sdk.llm.llm_registry.LLMRegistry.get) – Get an LLM instance from the registry.
- [**list_services**](#openhands.sdk.llm.llm_registry.LLMRegistry.list_services) – Deprecated alias for :meth:`list_usage_ids`.
- [**list_usage_ids**](#openhands.sdk.llm.llm_registry.LLMRegistry.list_usage_ids) – List all registered usage IDs.
- [**notify**](#openhands.sdk.llm.llm_registry.LLMRegistry.notify) – Notify subscribers of registry events.
- [**subscribe**](#openhands.sdk.llm.llm_registry.LLMRegistry.subscribe) – Subscribe to registry events.

**Attributes:**

- [**registry_id**](#openhands.sdk.llm.llm_registry.LLMRegistry.registry_id) (<code>[str](#str)</code>) –
- [**retry_listener**](#openhands.sdk.llm.llm_registry.LLMRegistry.retry_listener) (<code>[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None</code>) –
- [**service_to_llm**](#openhands.sdk.llm.llm_registry.LLMRegistry.service_to_llm) (<code>[dict](#dict)\[[str](#str), [LLM](#openhands.sdk.llm.llm.LLM)\]</code>) –
- [**subscriber**](#openhands.sdk.llm.llm_registry.LLMRegistry.subscriber) (<code>[Callable](#collections.abc.Callable)\[\[[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)\], None\] | None</code>) –
- [**usage_to_llm**](#openhands.sdk.llm.llm_registry.LLMRegistry.usage_to_llm) (<code>[dict](#dict)\[[str](#str), [LLM](#openhands.sdk.llm.llm.LLM)\]</code>) – Access the internal usage-ID-to-LLM mapping.

**Parameters:**

- **retry_listener** (<code>[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None</code>) – Optional callback for retry events.

##### `openhands.sdk.llm.llm_registry.LLMRegistry.add`

```python
add(llm)
```

Add an LLM instance to the registry.

**Parameters:**

- **llm** (<code>[LLM](#openhands.sdk.llm.llm.LLM)</code>) – The LLM instance to register.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If llm.usage_id already exists in the registry.

##### `openhands.sdk.llm.llm_registry.LLMRegistry.get`

```python
get(usage_id)
```

Get an LLM instance from the registry.

**Parameters:**

- **usage_id** (<code>[str](#str)</code>) – Unique identifier for the LLM usage slot.

**Returns:**

- <code>[LLM](#openhands.sdk.llm.llm.LLM)</code> – The LLM instance.

**Raises:**

- <code>[KeyError](#KeyError)</code> – If usage_id is not found in the registry.

##### `openhands.sdk.llm.llm_registry.LLMRegistry.list_services`

```python
list_services()
```

Deprecated alias for :meth:`list_usage_ids`.

##### `openhands.sdk.llm.llm_registry.LLMRegistry.list_usage_ids`

```python
list_usage_ids()
```

List all registered usage IDs.

##### `openhands.sdk.llm.llm_registry.LLMRegistry.notify`

```python
notify(event)
```

Notify subscribers of registry events.

**Parameters:**

- **event** (<code>[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)</code>) – The registry event to notify about.

##### `openhands.sdk.llm.llm_registry.LLMRegistry.registry_id`

```python
registry_id: str = str(uuid4())
```

##### `openhands.sdk.llm.llm_registry.LLMRegistry.retry_listener`

```python
retry_listener: Callable[[int, int], None] | None = retry_listener
```

##### `openhands.sdk.llm.llm_registry.LLMRegistry.service_to_llm`

```python
service_to_llm: dict[str, LLM]
```

##### `openhands.sdk.llm.llm_registry.LLMRegistry.subscribe`

```python
subscribe(callback)
```

Subscribe to registry events.

**Parameters:**

- **callback** (<code>[Callable](#collections.abc.Callable)\[\[[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)\], None\]</code>) – Function to call when LLMs are created or updated.

##### `openhands.sdk.llm.llm_registry.LLMRegistry.subscriber`

```python
subscriber: Callable[[RegistryEvent], None] | None = None
```

##### `openhands.sdk.llm.llm_registry.LLMRegistry.usage_to_llm`

```python
usage_to_llm: dict[str, LLM]
```

Access the internal usage-ID-to-LLM mapping.

#### `openhands.sdk.llm.llm_registry.RegistryEvent`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

**Attributes:**

- [**llm**](#openhands.sdk.llm.llm_registry.RegistryEvent.llm) (<code>[LLM](#openhands.sdk.llm.llm.LLM)</code>) –
- [**model_config**](#openhands.sdk.llm.llm_registry.RegistryEvent.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –

##### `openhands.sdk.llm.llm_registry.RegistryEvent.llm`

```python
llm: LLM
```

##### `openhands.sdk.llm.llm_registry.RegistryEvent.model_config`

```python
model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
```

#### `openhands.sdk.llm.llm_registry.SERVICE_TO_LLM_DEPRECATION_MSG`

```python
SERVICE_TO_LLM_DEPRECATION_MSG = 'LLMRegistry.service_to_llm is deprecated and will be removed in a future release; use usage_to_llm instead.'
```

#### `openhands.sdk.llm.llm_registry.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.llm.llm_response`

LLMResponse type for LLM completion responses.

This module provides the LLMResponse type that wraps LLM completion responses
with OpenHands-native types, eliminating the need for consumers to work directly
with LiteLLM types.

**Classes:**

- [**LLMResponse**](#openhands.sdk.llm.llm_response.LLMResponse) – Result of an LLM completion request.

#### `openhands.sdk.llm.llm_response.LLMResponse`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Result of an LLM completion request.

This type provides a clean interface for LLM completion results, exposing
only OpenHands-native types to consumers while preserving access to the
raw LiteLLM response for internal use.

**Attributes:**

- [**message**](#openhands.sdk.llm.llm_response.LLMResponse.message) (<code>[Message](#openhands.sdk.llm.message.Message)</code>) – The completion message converted to OpenHands Message type
- [**metrics**](#openhands.sdk.llm.llm_response.LLMResponse.metrics) (<code>[MetricsSnapshot](#openhands.sdk.llm.utils.metrics.MetricsSnapshot)</code>) – Snapshot of metrics from the completion request
- [**raw_response**](#openhands.sdk.llm.llm_response.LLMResponse.raw_response) (<code>[ModelResponse](#litellm.types.utils.ModelResponse) | [ResponsesAPIResponse](#litellm.ResponsesAPIResponse)</code>) – The original LiteLLM response (ModelResponse or
  ResponsesAPIResponse) for internal use

##### `openhands.sdk.llm.llm_response.LLMResponse.id`

```python
id: str
```

Get the response ID from the underlying LLM response.

This property provides a clean interface to access the response ID,
supporting both completion mode (ModelResponse) and response API modes
(ResponsesAPIResponse).

**Returns:**

- <code>[str](#str)</code> – The response ID from the LLM response

##### `openhands.sdk.llm.llm_response.LLMResponse.message`

```python
message: Message
```

##### `openhands.sdk.llm.llm_response.LLMResponse.metrics`

```python
metrics: MetricsSnapshot
```

##### `openhands.sdk.llm.llm_response.LLMResponse.model_config`

```python
model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
```

##### `openhands.sdk.llm.llm_response.LLMResponse.raw_response`

```python
raw_response: ModelResponse | ResponsesAPIResponse
```

### `openhands.sdk.llm.message`

**Classes:**

- [**BaseContent**](#openhands.sdk.llm.message.BaseContent) –
- [**ImageContent**](#openhands.sdk.llm.message.ImageContent) –
- [**Message**](#openhands.sdk.llm.message.Message) –
- [**MessageToolCall**](#openhands.sdk.llm.message.MessageToolCall) – Transport-agnostic tool call representation.
- [**ReasoningItemModel**](#openhands.sdk.llm.message.ReasoningItemModel) – OpenAI Responses reasoning item (non-stream, subset we consume).
- [**RedactedThinkingBlock**](#openhands.sdk.llm.message.RedactedThinkingBlock) – Redacted thinking block for previous responses without extended thinking.
- [**TextContent**](#openhands.sdk.llm.message.TextContent) –
- [**ThinkingBlock**](#openhands.sdk.llm.message.ThinkingBlock) – Anthropic thinking block for extended thinking feature.

**Functions:**

- [**content_to_str**](#openhands.sdk.llm.message.content_to_str) – Convert a list of TextContent and ImageContent to a list of strings.

**Attributes:**

- [**logger**](#openhands.sdk.llm.message.logger) –

#### `openhands.sdk.llm.message.BaseContent`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

**Functions:**

- [**to_llm_dict**](#openhands.sdk.llm.message.BaseContent.to_llm_dict) – Convert to LLM API format. Always returns a list of dictionaries.

**Attributes:**

- [**cache_prompt**](#openhands.sdk.llm.message.BaseContent.cache_prompt) (<code>[bool](#bool)</code>) –

##### `openhands.sdk.llm.message.BaseContent.cache_prompt`

```python
cache_prompt: bool = False
```

##### `openhands.sdk.llm.message.BaseContent.to_llm_dict`

```python
to_llm_dict()
```

Convert to LLM API format. Always returns a list of dictionaries.

Subclasses should implement this method to return a list of dictionaries,
even if they only have a single item.

#### `openhands.sdk.llm.message.ImageContent`

Bases: <code>[BaseContent](#openhands.sdk.llm.message.BaseContent)</code>

**Functions:**

- [**to_llm_dict**](#openhands.sdk.llm.message.ImageContent.to_llm_dict) – Convert to LLM API format.

**Attributes:**

- [**cache_prompt**](#openhands.sdk.llm.message.ImageContent.cache_prompt) (<code>[bool](#bool)</code>) –
- [**image_urls**](#openhands.sdk.llm.message.ImageContent.image_urls) (<code>[list](#list)\[[str](#str)\]</code>) –
- [**type**](#openhands.sdk.llm.message.ImageContent.type) (<code>[Literal](#typing.Literal)['image']</code>) –

##### `openhands.sdk.llm.message.ImageContent.cache_prompt`

```python
cache_prompt: bool = False
```

##### `openhands.sdk.llm.message.ImageContent.image_urls`

```python
image_urls: list[str]
```

##### `openhands.sdk.llm.message.ImageContent.to_llm_dict`

```python
to_llm_dict()
```

Convert to LLM API format.

##### `openhands.sdk.llm.message.ImageContent.type`

```python
type: Literal['image'] = 'image'
```

#### `openhands.sdk.llm.message.Message`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

**Functions:**

- [**from_llm_chat_message**](#openhands.sdk.llm.message.Message.from_llm_chat_message) – Convert a LiteLLMMessage (Chat Completions) to our Message class.
- [**from_llm_responses_output**](#openhands.sdk.llm.message.Message.from_llm_responses_output) – Convert OpenAI Responses API output items into a single assistant Message.
- [**to_chat_dict**](#openhands.sdk.llm.message.Message.to_chat_dict) – Serialize message for OpenAI Chat Completions.
- [**to_responses_dict**](#openhands.sdk.llm.message.Message.to_responses_dict) – Serialize message for OpenAI Responses (input parameter).
- [**to_responses_value**](#openhands.sdk.llm.message.Message.to_responses_value) – Return serialized form.

**Attributes:**

- [**cache_enabled**](#openhands.sdk.llm.message.Message.cache_enabled) (<code>[bool](#bool)</code>) –
- [**contains_image**](#openhands.sdk.llm.message.Message.contains_image) (<code>[bool](#bool)</code>) –
- [**content**](#openhands.sdk.llm.message.Message.content) (<code>[Sequence](#collections.abc.Sequence)\[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)\]</code>) –
- [**force_string_serializer**](#openhands.sdk.llm.message.Message.force_string_serializer) (<code>[bool](#bool)</code>) –
- [**function_calling_enabled**](#openhands.sdk.llm.message.Message.function_calling_enabled) (<code>[bool](#bool)</code>) –
- [**name**](#openhands.sdk.llm.message.Message.name) (<code>[str](#str) | None</code>) –
- [**reasoning_content**](#openhands.sdk.llm.message.Message.reasoning_content) (<code>[str](#str) | None</code>) –
- [**responses_reasoning_item**](#openhands.sdk.llm.message.Message.responses_reasoning_item) (<code>[ReasoningItemModel](#openhands.sdk.llm.message.ReasoningItemModel) | None</code>) –
- [**role**](#openhands.sdk.llm.message.Message.role) (<code>[Literal](#typing.Literal)['user', 'system', 'assistant', 'tool']</code>) –
- [**thinking_blocks**](#openhands.sdk.llm.message.Message.thinking_blocks) (<code>[Sequence](#collections.abc.Sequence)\[[ThinkingBlock](#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](#openhands.sdk.llm.message.RedactedThinkingBlock)\]</code>) –
- [**tool_call_id**](#openhands.sdk.llm.message.Message.tool_call_id) (<code>[str](#str) | None</code>) –
- [**tool_calls**](#openhands.sdk.llm.message.Message.tool_calls) (<code>[list](#list)\[[MessageToolCall](#openhands.sdk.llm.message.MessageToolCall)\] | None</code>) –
- [**vision_enabled**](#openhands.sdk.llm.message.Message.vision_enabled) (<code>[bool](#bool)</code>) –

##### `openhands.sdk.llm.message.Message.cache_enabled`

```python
cache_enabled: bool = False
```

##### `openhands.sdk.llm.message.Message.contains_image`

```python
contains_image: bool
```

##### `openhands.sdk.llm.message.Message.content`

```python
content: Sequence[TextContent | ImageContent] = Field(default_factory=list)
```

##### `openhands.sdk.llm.message.Message.force_string_serializer`

```python
force_string_serializer: bool = False
```

##### `openhands.sdk.llm.message.Message.from_llm_chat_message`

```python
from_llm_chat_message(message)
```

Convert a LiteLLMMessage (Chat Completions) to our Message class.

Provider-agnostic mapping for reasoning:

- Prefer `message.reasoning_content` if present (LiteLLM normalized field)
- Extract `thinking_blocks` from content array (Anthropic-specific)

##### `openhands.sdk.llm.message.Message.from_llm_responses_output`

```python
from_llm_responses_output(output)
```

Convert OpenAI Responses API output items into a single assistant Message.

Policy (non-stream):

- Collect assistant text by concatenating output_text parts from message items
- Normalize function_call items to MessageToolCall list

##### `openhands.sdk.llm.message.Message.function_calling_enabled`

```python
function_calling_enabled: bool = False
```

##### `openhands.sdk.llm.message.Message.name`

```python
name: str | None = None
```

##### `openhands.sdk.llm.message.Message.reasoning_content`

```python
reasoning_content: str | None = Field(default=None, description='Intermediate reasoning/thinking content from reasoning models')
```

##### `openhands.sdk.llm.message.Message.responses_reasoning_item`

```python
responses_reasoning_item: ReasoningItemModel | None = Field(default=None, description='OpenAI Responses reasoning item from model output')
```

##### `openhands.sdk.llm.message.Message.role`

```python
role: Literal['user', 'system', 'assistant', 'tool']
```

##### `openhands.sdk.llm.message.Message.thinking_blocks`

```python
thinking_blocks: Sequence[ThinkingBlock | RedactedThinkingBlock] = Field(default_factory=list, description='Raw Anthropic thinking blocks for extended thinking feature')
```

##### `openhands.sdk.llm.message.Message.to_chat_dict`

```python
to_chat_dict()
```

Serialize message for OpenAI Chat Completions.

Chooses the appropriate content serializer and then injects threading keys:

- Assistant tool call turn: role == "assistant" and self.tool_calls
- Tool result turn: role == "tool" and self.tool_call_id (with name)

##### `openhands.sdk.llm.message.Message.to_responses_dict`

```python
to_responses_dict(*, vision_enabled)
```

Serialize message for OpenAI Responses (input parameter).

Produces a list of "input" items for the Responses API:

- system: returns [], system content is expected in 'instructions'
- user: one 'message' item with content parts -> input_text / input_image
  (when vision enabled)
- assistant: emits prior assistant content as input_text,
  and function_call items for tool_calls
- tool: emits function_call_output items (one per TextContent)
  with matching call_id

##### `openhands.sdk.llm.message.Message.to_responses_value`

```python
to_responses_value(*, vision_enabled)
```

Return serialized form.

Either an instructions string (for system) or input items (for other roles).

##### `openhands.sdk.llm.message.Message.tool_call_id`

```python
tool_call_id: str | None = None
```

##### `openhands.sdk.llm.message.Message.tool_calls`

```python
tool_calls: list[MessageToolCall] | None = None
```

##### `openhands.sdk.llm.message.Message.vision_enabled`

```python
vision_enabled: bool = False
```

#### `openhands.sdk.llm.message.MessageToolCall`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Transport-agnostic tool call representation.

One canonical id is used for linking across actions/observations and
for Responses function_call_output call_id.

**Functions:**

- [**from_chat_tool_call**](#openhands.sdk.llm.message.MessageToolCall.from_chat_tool_call) – Create a MessageToolCall from a Chat Completions tool call.
- [**from_responses_function_call**](#openhands.sdk.llm.message.MessageToolCall.from_responses_function_call) – Create a MessageToolCall from a typed OpenAI Responses function_call item.
- [**to_chat_dict**](#openhands.sdk.llm.message.MessageToolCall.to_chat_dict) – Serialize to OpenAI Chat Completions tool_calls format.
- [**to_responses_dict**](#openhands.sdk.llm.message.MessageToolCall.to_responses_dict) – Serialize to OpenAI Responses 'function_call' input item format.

**Attributes:**

- [**arguments**](#openhands.sdk.llm.message.MessageToolCall.arguments) (<code>[str](#str)</code>) –
- [**id**](#openhands.sdk.llm.message.MessageToolCall.id) (<code>[str](#str)</code>) –
- [**name**](#openhands.sdk.llm.message.MessageToolCall.name) (<code>[str](#str)</code>) –
- [**origin**](#openhands.sdk.llm.message.MessageToolCall.origin) (<code>[Literal](#typing.Literal)['completion', 'responses']</code>) –

##### `openhands.sdk.llm.message.MessageToolCall.arguments`

```python
arguments: str = Field(..., description='JSON string of arguments')
```

##### `openhands.sdk.llm.message.MessageToolCall.from_chat_tool_call`

```python
from_chat_tool_call(tool_call)
```

Create a MessageToolCall from a Chat Completions tool call.

##### `openhands.sdk.llm.message.MessageToolCall.from_responses_function_call`

```python
from_responses_function_call(item)
```

Create a MessageToolCall from a typed OpenAI Responses function_call item.

Note: OpenAI Responses function_call.arguments is already a JSON string.

##### `openhands.sdk.llm.message.MessageToolCall.id`

```python
id: str = Field(..., description='Canonical tool call id')
```

##### `openhands.sdk.llm.message.MessageToolCall.name`

```python
name: str = Field(..., description='Tool/function name')
```

##### `openhands.sdk.llm.message.MessageToolCall.origin`

```python
origin: Literal['completion', 'responses'] = Field(..., description='Originating API family')
```

##### `openhands.sdk.llm.message.MessageToolCall.to_chat_dict`

```python
to_chat_dict()
```

Serialize to OpenAI Chat Completions tool_calls format.

##### `openhands.sdk.llm.message.MessageToolCall.to_responses_dict`

```python
to_responses_dict()
```

Serialize to OpenAI Responses 'function_call' input item format.

#### `openhands.sdk.llm.message.ReasoningItemModel`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

OpenAI Responses reasoning item (non-stream, subset we consume).

Do not log or render encrypted_content.

**Attributes:**

- [**content**](#openhands.sdk.llm.message.ReasoningItemModel.content) (<code>[list](#list)\[[str](#str)\] | None</code>) –
- [**encrypted_content**](#openhands.sdk.llm.message.ReasoningItemModel.encrypted_content) (<code>[str](#str) | None</code>) –
- [**id**](#openhands.sdk.llm.message.ReasoningItemModel.id) (<code>[str](#str) | None</code>) –
- [**status**](#openhands.sdk.llm.message.ReasoningItemModel.status) (<code>[str](#str) | None</code>) –
- [**summary**](#openhands.sdk.llm.message.ReasoningItemModel.summary) (<code>[list](#list)\[[str](#str)\]</code>) –

##### `openhands.sdk.llm.message.ReasoningItemModel.content`

```python
content: list[str] | None = Field(default=None)
```

##### `openhands.sdk.llm.message.ReasoningItemModel.encrypted_content`

```python
encrypted_content: str | None = Field(default=None)
```

##### `openhands.sdk.llm.message.ReasoningItemModel.id`

```python
id: str | None = Field(default=None)
```

##### `openhands.sdk.llm.message.ReasoningItemModel.status`

```python
status: str | None = Field(default=None)
```

##### `openhands.sdk.llm.message.ReasoningItemModel.summary`

```python
summary: list[str] = Field(default_factory=list)
```

#### `openhands.sdk.llm.message.RedactedThinkingBlock`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Redacted thinking block for previous responses without extended thinking.

This is used as a placeholder for assistant messages that were generated
before extended thinking was enabled.

**Attributes:**

- [**data**](#openhands.sdk.llm.message.RedactedThinkingBlock.data) (<code>[str](#str)</code>) –
- [**type**](#openhands.sdk.llm.message.RedactedThinkingBlock.type) (<code>[Literal](#typing.Literal)['redacted_thinking']</code>) –

##### `openhands.sdk.llm.message.RedactedThinkingBlock.data`

```python
data: str = Field(..., description='The redacted thinking content')
```

##### `openhands.sdk.llm.message.RedactedThinkingBlock.type`

```python
type: Literal['redacted_thinking'] = 'redacted_thinking'
```

#### `openhands.sdk.llm.message.TextContent`

Bases: <code>[BaseContent](#openhands.sdk.llm.message.BaseContent)</code>

**Functions:**

- [**to_llm_dict**](#openhands.sdk.llm.message.TextContent.to_llm_dict) – Convert to LLM API format.

**Attributes:**

- [**cache_prompt**](#openhands.sdk.llm.message.TextContent.cache_prompt) (<code>[bool](#bool)</code>) –
- [**model_config**](#openhands.sdk.llm.message.TextContent.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**text**](#openhands.sdk.llm.message.TextContent.text) (<code>[str](#str)</code>) –
- [**type**](#openhands.sdk.llm.message.TextContent.type) (<code>[Literal](#typing.Literal)['text']</code>) –

##### `openhands.sdk.llm.message.TextContent.cache_prompt`

```python
cache_prompt: bool = False
```

##### `openhands.sdk.llm.message.TextContent.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', populate_by_name=True)
```

##### `openhands.sdk.llm.message.TextContent.text`

```python
text: str
```

##### `openhands.sdk.llm.message.TextContent.to_llm_dict`

```python
to_llm_dict()
```

Convert to LLM API format.

##### `openhands.sdk.llm.message.TextContent.type`

```python
type: Literal['text'] = 'text'
```

#### `openhands.sdk.llm.message.ThinkingBlock`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Anthropic thinking block for extended thinking feature.

This represents the raw thinking blocks returned by Anthropic models
when extended thinking is enabled. These blocks must be preserved
and passed back to the API for tool use scenarios.

**Attributes:**

- [**signature**](#openhands.sdk.llm.message.ThinkingBlock.signature) (<code>[str](#str)</code>) –
- [**thinking**](#openhands.sdk.llm.message.ThinkingBlock.thinking) (<code>[str](#str)</code>) –
- [**type**](#openhands.sdk.llm.message.ThinkingBlock.type) (<code>[Literal](#typing.Literal)['thinking']</code>) –

##### `openhands.sdk.llm.message.ThinkingBlock.signature`

```python
signature: str = Field(..., description='Cryptographic signature for the thinking block')
```

##### `openhands.sdk.llm.message.ThinkingBlock.thinking`

```python
thinking: str = Field(..., description='The thinking content')
```

##### `openhands.sdk.llm.message.ThinkingBlock.type`

```python
type: Literal['thinking'] = 'thinking'
```

#### `openhands.sdk.llm.message.content_to_str`

```python
content_to_str(contents)
```

Convert a list of TextContent and ImageContent to a list of strings.

This is primarily used for display purposes.

#### `openhands.sdk.llm.message.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.llm.options`

**Modules:**

- [**chat_options**](#openhands.sdk.llm.options.chat_options) –
- [**common**](#openhands.sdk.llm.options.common) –
- [**responses_options**](#openhands.sdk.llm.options.responses_options) –

#### `openhands.sdk.llm.options.chat_options`

**Functions:**

- [**select_chat_options**](#openhands.sdk.llm.options.chat_options.select_chat_options) – Behavior-preserving extraction of \_normalize_call_kwargs.

##### `openhands.sdk.llm.options.chat_options.select_chat_options`

```python
select_chat_options(llm, user_kwargs, has_tools)
```

Behavior-preserving extraction of \_normalize_call_kwargs.

This keeps the exact provider-aware mappings and precedence.

#### `openhands.sdk.llm.options.common`

**Functions:**

- [**apply_defaults_if_absent**](#openhands.sdk.llm.options.common.apply_defaults_if_absent) – Return a new dict with defaults applied when keys are absent.

##### `openhands.sdk.llm.options.common.apply_defaults_if_absent`

```python
apply_defaults_if_absent(user_kwargs, defaults)
```

Return a new dict with defaults applied when keys are absent.

- Pure and deterministic; does not mutate inputs
- Only applies defaults when the key is missing and default is not None
- Does not alter user-provided values

#### `openhands.sdk.llm.options.responses_options`

**Functions:**

- [**select_responses_options**](#openhands.sdk.llm.options.responses_options.select_responses_options) – Behavior-preserving extraction of \_normalize_responses_kwargs.

##### `openhands.sdk.llm.options.responses_options.select_responses_options`

```python
select_responses_options(llm, user_kwargs, *, include, store)
```

Behavior-preserving extraction of \_normalize_responses_kwargs.

### `openhands.sdk.llm.router`

**Modules:**

- [**base**](#openhands.sdk.llm.router.base) –

**Classes:**

- [**RouterLLM**](#openhands.sdk.llm.router.RouterLLM) – Base class for multiple LLM acting as a unified LLM.

#### `openhands.sdk.llm.router.RouterLLM`

Bases: <code>[LLM](#openhands.sdk.llm.llm.LLM)</code>

Base class for multiple LLM acting as a unified LLM.
This class provides a foundation for implementing model routing by
inheriting from LLM, allowing routers to work with multiple underlying
LLM models while presenting a unified LLM interface to consumers.
Key features:

- Works with multiple LLMs configured via llms_for_routing
- Delegates all other operations/properties to the selected LLM
- Provides routing interface through select_llm() method

**Functions:**

- [**completion**](#openhands.sdk.llm.router.RouterLLM.completion) – This method intercepts completion calls and routes them to the appropriate
- [**format_messages_for_llm**](#openhands.sdk.llm.router.RouterLLM.format_messages_for_llm) – Formats Message objects for LLM consumption.
- [**format_messages_for_responses**](#openhands.sdk.llm.router.RouterLLM.format_messages_for_responses) – Prepare (instructions, input[]) for the OpenAI Responses API.
- [**get_token_count**](#openhands.sdk.llm.router.RouterLLM.get_token_count) –
- [**is_caching_prompt_active**](#openhands.sdk.llm.router.RouterLLM.is_caching_prompt_active) – Check if prompt caching is supported and enabled for current model.
- [**is_context_window_exceeded_exception**](#openhands.sdk.llm.router.RouterLLM.is_context_window_exceeded_exception) – Check if the exception indicates a context window exceeded error.
- [**load_from_env**](#openhands.sdk.llm.router.RouterLLM.load_from_env) –
- [**load_from_json**](#openhands.sdk.llm.router.RouterLLM.load_from_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.llm.router.RouterLLM.resolve_diff_from_deserialized) – Resolve differences between a deserialized LLM and the current instance.
- [**responses**](#openhands.sdk.llm.router.RouterLLM.responses) – Alternative invocation path using OpenAI Responses API via LiteLLM.
- [**restore_metrics**](#openhands.sdk.llm.router.RouterLLM.restore_metrics) –
- [**select_llm**](#openhands.sdk.llm.router.RouterLLM.select_llm) – Select which LLM to use based on messages and events.
- [**set_placeholder_model**](#openhands.sdk.llm.router.RouterLLM.set_placeholder_model) – Guarantee `model` exists before LLM base validation runs.
- [**uses_responses_api**](#openhands.sdk.llm.router.RouterLLM.uses_responses_api) – Whether this model uses the OpenAI Responses API path.
- [**validate_llms_not_empty**](#openhands.sdk.llm.router.RouterLLM.validate_llms_not_empty) –
- [**vision_is_active**](#openhands.sdk.llm.router.RouterLLM.vision_is_active) –

**Attributes:**

- [**OVERRIDE_ON_SERIALIZE**](#openhands.sdk.llm.router.RouterLLM.OVERRIDE_ON_SERIALIZE) (<code>[tuple](#tuple)\[[str](#str), ...\]</code>) –
- [**active_llm**](#openhands.sdk.llm.router.RouterLLM.active_llm) (<code>[LLM](#openhands.sdk.llm.llm.LLM) | None</code>) –
- [**api_key**](#openhands.sdk.llm.router.RouterLLM.api_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**api_version**](#openhands.sdk.llm.router.RouterLLM.api_version) (<code>[str](#str) | None</code>) –
- [**aws_access_key_id**](#openhands.sdk.llm.router.RouterLLM.aws_access_key_id) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**aws_region_name**](#openhands.sdk.llm.router.RouterLLM.aws_region_name) (<code>[str](#str) | None</code>) –
- [**aws_secret_access_key**](#openhands.sdk.llm.router.RouterLLM.aws_secret_access_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**base_url**](#openhands.sdk.llm.router.RouterLLM.base_url) (<code>[str](#str) | None</code>) –
- [**caching_prompt**](#openhands.sdk.llm.router.RouterLLM.caching_prompt) (<code>[bool](#bool)</code>) –
- [**custom_llm_provider**](#openhands.sdk.llm.router.RouterLLM.custom_llm_provider) (<code>[str](#str) | None</code>) –
- [**custom_tokenizer**](#openhands.sdk.llm.router.RouterLLM.custom_tokenizer) (<code>[str](#str) | None</code>) –
- [**disable_stop_word**](#openhands.sdk.llm.router.RouterLLM.disable_stop_word) (<code>[bool](#bool) | None</code>) –
- [**disable_vision**](#openhands.sdk.llm.router.RouterLLM.disable_vision) (<code>[bool](#bool) | None</code>) –
- [**drop_params**](#openhands.sdk.llm.router.RouterLLM.drop_params) (<code>[bool](#bool)</code>) –
- [**enable_encrypted_reasoning**](#openhands.sdk.llm.router.RouterLLM.enable_encrypted_reasoning) (<code>[bool](#bool)</code>) –
- [**extended_thinking_budget**](#openhands.sdk.llm.router.RouterLLM.extended_thinking_budget) (<code>[int](#int) | None</code>) –
- [**input_cost_per_token**](#openhands.sdk.llm.router.RouterLLM.input_cost_per_token) (<code>[float](#float) | None</code>) –
- [**llms_for_routing**](#openhands.sdk.llm.router.RouterLLM.llms_for_routing) (<code>[dict](#dict)\[[str](#str), [LLM](#openhands.sdk.llm.llm.LLM)\]</code>) –
- [**log_completions**](#openhands.sdk.llm.router.RouterLLM.log_completions) (<code>[bool](#bool)</code>) –
- [**log_completions_folder**](#openhands.sdk.llm.router.RouterLLM.log_completions_folder) (<code>[str](#str)</code>) –
- [**max_input_tokens**](#openhands.sdk.llm.router.RouterLLM.max_input_tokens) (<code>[int](#int) | None</code>) –
- [**max_message_chars**](#openhands.sdk.llm.router.RouterLLM.max_message_chars) (<code>[int](#int)</code>) –
- [**max_output_tokens**](#openhands.sdk.llm.router.RouterLLM.max_output_tokens) (<code>[int](#int) | None</code>) –
- [**metadata**](#openhands.sdk.llm.router.RouterLLM.metadata) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**metrics**](#openhands.sdk.llm.router.RouterLLM.metrics) (<code>[Metrics](#openhands.sdk.llm.utils.metrics.Metrics)</code>) –
- [**model**](#openhands.sdk.llm.router.RouterLLM.model) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.llm.router.RouterLLM.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**model_info**](#openhands.sdk.llm.router.RouterLLM.model_info) (<code>[dict](#dict) | None</code>) – Returns the model info dictionary.
- [**modify_params**](#openhands.sdk.llm.router.RouterLLM.modify_params) (<code>[bool](#bool)</code>) –
- [**native_tool_calling**](#openhands.sdk.llm.router.RouterLLM.native_tool_calling) (<code>[bool](#bool)</code>) –
- [**num_retries**](#openhands.sdk.llm.router.RouterLLM.num_retries) (<code>[int](#int)</code>) –
- [**ollama_base_url**](#openhands.sdk.llm.router.RouterLLM.ollama_base_url) (<code>[str](#str) | None</code>) –
- [**openrouter_app_name**](#openhands.sdk.llm.router.RouterLLM.openrouter_app_name) (<code>[str](#str)</code>) –
- [**openrouter_site_url**](#openhands.sdk.llm.router.RouterLLM.openrouter_site_url) (<code>[str](#str)</code>) –
- [**output_cost_per_token**](#openhands.sdk.llm.router.RouterLLM.output_cost_per_token) (<code>[float](#float) | None</code>) –
- [**reasoning_effort**](#openhands.sdk.llm.router.RouterLLM.reasoning_effort) (<code>[Literal](#typing.Literal)['low', 'medium', 'high', 'none'] | None</code>) –
- [**retry_listener**](#openhands.sdk.llm.router.RouterLLM.retry_listener) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None\]</code>) –
- [**retry_max_wait**](#openhands.sdk.llm.router.RouterLLM.retry_max_wait) (<code>[int](#int)</code>) –
- [**retry_min_wait**](#openhands.sdk.llm.router.RouterLLM.retry_min_wait) (<code>[int](#int)</code>) –
- [**retry_multiplier**](#openhands.sdk.llm.router.RouterLLM.retry_multiplier) (<code>[float](#float)</code>) –
- [**router_name**](#openhands.sdk.llm.router.RouterLLM.router_name) (<code>[str](#str)</code>) –
- [**safety_settings**](#openhands.sdk.llm.router.RouterLLM.safety_settings) (<code>[list](#list)\[[dict](#dict)\[[str](#str), [str](#str)\]\] | None</code>) –
- [**seed**](#openhands.sdk.llm.router.RouterLLM.seed) (<code>[int](#int) | None</code>) –
- [**service_id**](#openhands.sdk.llm.router.RouterLLM.service_id) (<code>[str](#str)</code>) –
- [**temperature**](#openhands.sdk.llm.router.RouterLLM.temperature) (<code>[float](#float) | None</code>) –
- [**timeout**](#openhands.sdk.llm.router.RouterLLM.timeout) (<code>[int](#int) | None</code>) –
- [**top_k**](#openhands.sdk.llm.router.RouterLLM.top_k) (<code>[float](#float) | None</code>) –
- [**top_p**](#openhands.sdk.llm.router.RouterLLM.top_p) (<code>[float](#float) | None</code>) –
- [**usage_id**](#openhands.sdk.llm.router.RouterLLM.usage_id) (<code>[str](#str)</code>) –

##### `openhands.sdk.llm.router.RouterLLM.OVERRIDE_ON_SERIALIZE`

```python
OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key')
```

##### `openhands.sdk.llm.router.RouterLLM.active_llm`

```python
active_llm: LLM | None = Field(default=None, description='Currently selected LLM instance')
```

##### `openhands.sdk.llm.router.RouterLLM.api_key`

```python
api_key: SecretStr | None = Field(default=None, description='API key.')
```

##### `openhands.sdk.llm.router.RouterLLM.api_version`

```python
api_version: str | None = Field(default=None, description='API version (e.g., Azure).')
```

##### `openhands.sdk.llm.router.RouterLLM.aws_access_key_id`

```python
aws_access_key_id: SecretStr | None = Field(default=None)
```

##### `openhands.sdk.llm.router.RouterLLM.aws_region_name`

```python
aws_region_name: str | None = Field(default=None)
```

##### `openhands.sdk.llm.router.RouterLLM.aws_secret_access_key`

```python
aws_secret_access_key: SecretStr | None = Field(default=None)
```

##### `openhands.sdk.llm.router.RouterLLM.base_url`

```python
base_url: str | None = Field(default=None, description='Custom base URL.')
```

##### `openhands.sdk.llm.router.RouterLLM.caching_prompt`

```python
caching_prompt: bool = Field(default=True, description='Enable caching of prompts.')
```

##### `openhands.sdk.llm.router.RouterLLM.completion`

```python
completion(messages, tools=None, return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

This method intercepts completion calls and routes them to the appropriate
underlying LLM based on the routing logic implemented in select_llm().

##### `openhands.sdk.llm.router.RouterLLM.custom_llm_provider`

```python
custom_llm_provider: str | None = Field(default=None)
```

##### `openhands.sdk.llm.router.RouterLLM.custom_tokenizer`

```python
custom_tokenizer: str | None = Field(default=None, description='A custom tokenizer to use for token counting.')
```

##### `openhands.sdk.llm.router.RouterLLM.disable_stop_word`

```python
disable_stop_word: bool | None = Field(default=False, description='Disable using of stop word.')
```

##### `openhands.sdk.llm.router.RouterLLM.disable_vision`

```python
disable_vision: bool | None = Field(default=None, description='If model is vision capable, this option allows to disable image processing (useful for cost reduction).')
```

##### `openhands.sdk.llm.router.RouterLLM.drop_params`

```python
drop_params: bool = Field(default=True)
```

##### `openhands.sdk.llm.router.RouterLLM.enable_encrypted_reasoning`

```python
enable_encrypted_reasoning: bool = Field(default=False, description="If True, ask for ['reasoning.encrypted_content'] in Responses API include.")
```

##### `openhands.sdk.llm.router.RouterLLM.extended_thinking_budget`

```python
extended_thinking_budget: int | None = Field(default=200000, description='The budget tokens for extended thinking, supported by Anthropic models.')
```

##### `openhands.sdk.llm.router.RouterLLM.format_messages_for_llm`

```python
format_messages_for_llm(messages)
```

Formats Message objects for LLM consumption.

##### `openhands.sdk.llm.router.RouterLLM.format_messages_for_responses`

```python
format_messages_for_responses(messages)
```

Prepare (instructions, input[]) for the OpenAI Responses API.

- Skips prompt caching flags and string serializer concerns
- Uses Message.to_responses_value to get either instructions (system)
  or input items (others)
- Concatenates system instructions into a single instructions string

##### `openhands.sdk.llm.router.RouterLLM.get_token_count`

```python
get_token_count(messages)
```

##### `openhands.sdk.llm.router.RouterLLM.input_cost_per_token`

```python
input_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per input token. This will available in logs for user.')
```

##### `openhands.sdk.llm.router.RouterLLM.is_caching_prompt_active`

```python
is_caching_prompt_active()
```

Check if prompt caching is supported and enabled for current model.

**Returns:**

- **boolean** (<code>[bool](#bool)</code>) – True if prompt caching is supported and enabled for the given
  model.

##### `openhands.sdk.llm.router.RouterLLM.is_context_window_exceeded_exception`

```python
is_context_window_exceeded_exception(exception)
```

Check if the exception indicates a context window exceeded error.

Context window exceeded errors vary by provider, and LiteLLM does not do a
consistent job of identifying and wrapping them.

##### `openhands.sdk.llm.router.RouterLLM.llms_for_routing`

```python
llms_for_routing: dict[str, LLM] = Field(default_factory=dict)
```

##### `openhands.sdk.llm.router.RouterLLM.load_from_env`

```python
load_from_env(prefix='LLM_')
```

##### `openhands.sdk.llm.router.RouterLLM.load_from_json`

```python
load_from_json(json_path)
```

##### `openhands.sdk.llm.router.RouterLLM.log_completions`

```python
log_completions: bool = Field(default=False, description='Enable logging of completions.')
```

##### `openhands.sdk.llm.router.RouterLLM.log_completions_folder`

```python
log_completions_folder: str = Field(default=(os.path.join(ENV_LOG_DIR, 'completions')), description='The folder to log LLM completions to. Required if log_completions is True.')
```

##### `openhands.sdk.llm.router.RouterLLM.max_input_tokens`

```python
max_input_tokens: int | None = Field(default=None, ge=1, description='The maximum number of input tokens. Note that this is currently unused, and the value at runtime is actually the total tokens in OpenAI (e.g. 128,000 tokens for GPT-4).')
```

##### `openhands.sdk.llm.router.RouterLLM.max_message_chars`

```python
max_message_chars: int = Field(default=30000, ge=1, description='Approx max chars in each event/content sent to the LLM.')
```

##### `openhands.sdk.llm.router.RouterLLM.max_output_tokens`

```python
max_output_tokens: int | None = Field(default=None, ge=1, description='The maximum number of output tokens. This is sent to the LLM.')
```

##### `openhands.sdk.llm.router.RouterLLM.metadata`

```python
metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata for the LLM instance. Example structure: {'trace_version': '1.0.0', 'tags': ['model:gpt-4', 'agent:my-agent'], 'session_id': 'session-123', 'trace_user_id': 'user-456'}")
```

##### `openhands.sdk.llm.router.RouterLLM.metrics`

```python
metrics: Metrics
```

##### `openhands.sdk.llm.router.RouterLLM.model`

```python
model: str = Field(default='claude-sonnet-4-20250514', description='Model name.')
```

##### `openhands.sdk.llm.router.RouterLLM.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', arbitrary_types_allowed=True)
```

##### `openhands.sdk.llm.router.RouterLLM.model_info`

```python
model_info: dict | None
```

Returns the model info dictionary.

##### `openhands.sdk.llm.router.RouterLLM.modify_params`

```python
modify_params: bool = Field(default=True, description='Modify params allows litellm to do transformations like adding a default message, when a message is empty.')
```

##### `openhands.sdk.llm.router.RouterLLM.native_tool_calling`

```python
native_tool_calling: bool = Field(default=True, description='Whether to use native tool calling.')
```

##### `openhands.sdk.llm.router.RouterLLM.num_retries`

```python
num_retries: int = Field(default=5, ge=0)
```

##### `openhands.sdk.llm.router.RouterLLM.ollama_base_url`

```python
ollama_base_url: str | None = Field(default=None)
```

##### `openhands.sdk.llm.router.RouterLLM.openrouter_app_name`

```python
openrouter_app_name: str = Field(default='OpenHands')
```

##### `openhands.sdk.llm.router.RouterLLM.openrouter_site_url`

```python
openrouter_site_url: str = Field(default='https://docs.all-hands.dev/')
```

##### `openhands.sdk.llm.router.RouterLLM.output_cost_per_token`

```python
output_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per output token. This will available in logs for user.')
```

##### `openhands.sdk.llm.router.RouterLLM.reasoning_effort`

```python
reasoning_effort: Literal['low', 'medium', 'high', 'none'] | None = Field(default=None, description="The effort to put into reasoning. This is a string that can be one of 'low', 'medium', 'high', or 'none'. Can apply to all reasoning models.")
```

##### `openhands.sdk.llm.router.RouterLLM.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Resolve differences between a deserialized LLM and the current instance.

This is due to fields like api_key being serialized to "\*\*\*\*" in dumps,
and we want to ensure that when loading from a file, we still use the
runtime-provided api_key in the self instance.

Return a new LLM instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key) taken from `self`.

##### `openhands.sdk.llm.router.RouterLLM.responses`

```python
responses(messages, tools=None, include=None, store=None, _return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

Alternative invocation path using OpenAI Responses API via LiteLLM.

Maps Message[] -> (instructions, input[]) and returns LLMResponse.
Non-stream only for v1.

##### `openhands.sdk.llm.router.RouterLLM.restore_metrics`

```python
restore_metrics(metrics)
```

##### `openhands.sdk.llm.router.RouterLLM.retry_listener`

```python
retry_listener: SkipJsonSchema[Callable[[int, int], None] | None] = Field(default=None, exclude=True)
```

##### `openhands.sdk.llm.router.RouterLLM.retry_max_wait`

```python
retry_max_wait: int = Field(default=64, ge=0)
```

##### `openhands.sdk.llm.router.RouterLLM.retry_min_wait`

```python
retry_min_wait: int = Field(default=8, ge=0)
```

##### `openhands.sdk.llm.router.RouterLLM.retry_multiplier`

```python
retry_multiplier: float = Field(default=8.0, ge=0)
```

##### `openhands.sdk.llm.router.RouterLLM.router_name`

```python
router_name: str = Field(default='base_router', description='Name of the router')
```

##### `openhands.sdk.llm.router.RouterLLM.safety_settings`

```python
safety_settings: list[dict[str, str]] | None = Field(default=None, description='Safety settings for models that support them (like Mistral AI and Gemini)')
```

##### `openhands.sdk.llm.router.RouterLLM.seed`

```python
seed: int | None = Field(default=None, description='The seed to use for random number generation.')
```

##### `openhands.sdk.llm.router.RouterLLM.select_llm`

```python
select_llm(messages)
```

Select which LLM to use based on messages and events.

This method implements the core routing logic for the RouterLLM.
Subclasses should analyze the provided messages to determine which
LLM from llms_for_routing is most appropriate for handling the request.

**Parameters:**

- **messages** (<code>[list](#list)\[[Message](#openhands.sdk.llm.message.Message)\]</code>) – List of messages in the conversation that can be used
  to inform the routing decision.

**Returns:**

- <code>[str](#str)</code> – The key/name of the LLM to use from llms_for_routing dictionary.

##### `openhands.sdk.llm.router.RouterLLM.service_id`

```python
service_id: str
```

##### `openhands.sdk.llm.router.RouterLLM.set_placeholder_model`

```python
set_placeholder_model(data)
```

Guarantee `model` exists before LLM base validation runs.

##### `openhands.sdk.llm.router.RouterLLM.temperature`

```python
temperature: float | None = Field(default=0.0, ge=0)
```

##### `openhands.sdk.llm.router.RouterLLM.timeout`

```python
timeout: int | None = Field(default=None, ge=0, description='HTTP timeout (s).')
```

##### `openhands.sdk.llm.router.RouterLLM.top_k`

```python
top_k: float | None = Field(default=None, ge=0)
```

##### `openhands.sdk.llm.router.RouterLLM.top_p`

```python
top_p: float | None = Field(default=1.0, ge=0, le=1)
```

##### `openhands.sdk.llm.router.RouterLLM.usage_id`

```python
usage_id: str = Field(default='default', validation_alias=(AliasChoices('usage_id', 'service_id')), serialization_alias='usage_id', description='Unique usage identifier for the LLM. Used for registry lookups, telemetry, and spend tracking.')
```

##### `openhands.sdk.llm.router.RouterLLM.uses_responses_api`

```python
uses_responses_api()
```

Whether this model uses the OpenAI Responses API path.

##### `openhands.sdk.llm.router.RouterLLM.validate_llms_not_empty`

```python
validate_llms_not_empty(v)
```

##### `openhands.sdk.llm.router.RouterLLM.vision_is_active`

```python
vision_is_active()
```

#### `openhands.sdk.llm.router.base`

**Classes:**

- [**RouterLLM**](#openhands.sdk.llm.router.base.RouterLLM) – Base class for multiple LLM acting as a unified LLM.

**Attributes:**

- [**logger**](#openhands.sdk.llm.router.base.logger) –

##### `openhands.sdk.llm.router.base.RouterLLM`

Bases: <code>[LLM](#openhands.sdk.llm.llm.LLM)</code>

Base class for multiple LLM acting as a unified LLM.
This class provides a foundation for implementing model routing by
inheriting from LLM, allowing routers to work with multiple underlying
LLM models while presenting a unified LLM interface to consumers.
Key features:

- Works with multiple LLMs configured via llms_for_routing
- Delegates all other operations/properties to the selected LLM
- Provides routing interface through select_llm() method

**Functions:**

- [**completion**](#openhands.sdk.llm.router.base.RouterLLM.completion) – This method intercepts completion calls and routes them to the appropriate
- [**format_messages_for_llm**](#openhands.sdk.llm.router.base.RouterLLM.format_messages_for_llm) – Formats Message objects for LLM consumption.
- [**format_messages_for_responses**](#openhands.sdk.llm.router.base.RouterLLM.format_messages_for_responses) – Prepare (instructions, input[]) for the OpenAI Responses API.
- [**get_token_count**](#openhands.sdk.llm.router.base.RouterLLM.get_token_count) –
- [**is_caching_prompt_active**](#openhands.sdk.llm.router.base.RouterLLM.is_caching_prompt_active) – Check if prompt caching is supported and enabled for current model.
- [**is_context_window_exceeded_exception**](#openhands.sdk.llm.router.base.RouterLLM.is_context_window_exceeded_exception) – Check if the exception indicates a context window exceeded error.
- [**load_from_env**](#openhands.sdk.llm.router.base.RouterLLM.load_from_env) –
- [**load_from_json**](#openhands.sdk.llm.router.base.RouterLLM.load_from_json) –
- [**resolve_diff_from_deserialized**](#openhands.sdk.llm.router.base.RouterLLM.resolve_diff_from_deserialized) – Resolve differences between a deserialized LLM and the current instance.
- [**responses**](#openhands.sdk.llm.router.base.RouterLLM.responses) – Alternative invocation path using OpenAI Responses API via LiteLLM.
- [**restore_metrics**](#openhands.sdk.llm.router.base.RouterLLM.restore_metrics) –
- [**select_llm**](#openhands.sdk.llm.router.base.RouterLLM.select_llm) – Select which LLM to use based on messages and events.
- [**set_placeholder_model**](#openhands.sdk.llm.router.base.RouterLLM.set_placeholder_model) – Guarantee `model` exists before LLM base validation runs.
- [**uses_responses_api**](#openhands.sdk.llm.router.base.RouterLLM.uses_responses_api) – Whether this model uses the OpenAI Responses API path.
- [**validate_llms_not_empty**](#openhands.sdk.llm.router.base.RouterLLM.validate_llms_not_empty) –
- [**vision_is_active**](#openhands.sdk.llm.router.base.RouterLLM.vision_is_active) –

**Attributes:**

- [**OVERRIDE_ON_SERIALIZE**](#openhands.sdk.llm.router.base.RouterLLM.OVERRIDE_ON_SERIALIZE) (<code>[tuple](#tuple)\[[str](#str), ...\]</code>) –
- [**active_llm**](#openhands.sdk.llm.router.base.RouterLLM.active_llm) (<code>[LLM](#openhands.sdk.llm.llm.LLM) | None</code>) –
- [**api_key**](#openhands.sdk.llm.router.base.RouterLLM.api_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**api_version**](#openhands.sdk.llm.router.base.RouterLLM.api_version) (<code>[str](#str) | None</code>) –
- [**aws_access_key_id**](#openhands.sdk.llm.router.base.RouterLLM.aws_access_key_id) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**aws_region_name**](#openhands.sdk.llm.router.base.RouterLLM.aws_region_name) (<code>[str](#str) | None</code>) –
- [**aws_secret_access_key**](#openhands.sdk.llm.router.base.RouterLLM.aws_secret_access_key) (<code>[SecretStr](#pydantic.SecretStr) | None</code>) –
- [**base_url**](#openhands.sdk.llm.router.base.RouterLLM.base_url) (<code>[str](#str) | None</code>) –
- [**caching_prompt**](#openhands.sdk.llm.router.base.RouterLLM.caching_prompt) (<code>[bool](#bool)</code>) –
- [**custom_llm_provider**](#openhands.sdk.llm.router.base.RouterLLM.custom_llm_provider) (<code>[str](#str) | None</code>) –
- [**custom_tokenizer**](#openhands.sdk.llm.router.base.RouterLLM.custom_tokenizer) (<code>[str](#str) | None</code>) –
- [**disable_stop_word**](#openhands.sdk.llm.router.base.RouterLLM.disable_stop_word) (<code>[bool](#bool) | None</code>) –
- [**disable_vision**](#openhands.sdk.llm.router.base.RouterLLM.disable_vision) (<code>[bool](#bool) | None</code>) –
- [**drop_params**](#openhands.sdk.llm.router.base.RouterLLM.drop_params) (<code>[bool](#bool)</code>) –
- [**enable_encrypted_reasoning**](#openhands.sdk.llm.router.base.RouterLLM.enable_encrypted_reasoning) (<code>[bool](#bool)</code>) –
- [**extended_thinking_budget**](#openhands.sdk.llm.router.base.RouterLLM.extended_thinking_budget) (<code>[int](#int) | None</code>) –
- [**input_cost_per_token**](#openhands.sdk.llm.router.base.RouterLLM.input_cost_per_token) (<code>[float](#float) | None</code>) –
- [**llms_for_routing**](#openhands.sdk.llm.router.base.RouterLLM.llms_for_routing) (<code>[dict](#dict)\[[str](#str), [LLM](#openhands.sdk.llm.llm.LLM)\]</code>) –
- [**log_completions**](#openhands.sdk.llm.router.base.RouterLLM.log_completions) (<code>[bool](#bool)</code>) –
- [**log_completions_folder**](#openhands.sdk.llm.router.base.RouterLLM.log_completions_folder) (<code>[str](#str)</code>) –
- [**max_input_tokens**](#openhands.sdk.llm.router.base.RouterLLM.max_input_tokens) (<code>[int](#int) | None</code>) –
- [**max_message_chars**](#openhands.sdk.llm.router.base.RouterLLM.max_message_chars) (<code>[int](#int)</code>) –
- [**max_output_tokens**](#openhands.sdk.llm.router.base.RouterLLM.max_output_tokens) (<code>[int](#int) | None</code>) –
- [**metadata**](#openhands.sdk.llm.router.base.RouterLLM.metadata) (<code>[dict](#dict)\[[str](#str), [Any](#typing.Any)\]</code>) –
- [**metrics**](#openhands.sdk.llm.router.base.RouterLLM.metrics) (<code>[Metrics](#openhands.sdk.llm.utils.metrics.Metrics)</code>) –
- [**model**](#openhands.sdk.llm.router.base.RouterLLM.model) (<code>[str](#str)</code>) –
- [**model_config**](#openhands.sdk.llm.router.base.RouterLLM.model_config) (<code>[ConfigDict](#pydantic.ConfigDict)</code>) –
- [**model_info**](#openhands.sdk.llm.router.base.RouterLLM.model_info) (<code>[dict](#dict) | None</code>) – Returns the model info dictionary.
- [**modify_params**](#openhands.sdk.llm.router.base.RouterLLM.modify_params) (<code>[bool](#bool)</code>) –
- [**native_tool_calling**](#openhands.sdk.llm.router.base.RouterLLM.native_tool_calling) (<code>[bool](#bool)</code>) –
- [**num_retries**](#openhands.sdk.llm.router.base.RouterLLM.num_retries) (<code>[int](#int)</code>) –
- [**ollama_base_url**](#openhands.sdk.llm.router.base.RouterLLM.ollama_base_url) (<code>[str](#str) | None</code>) –
- [**openrouter_app_name**](#openhands.sdk.llm.router.base.RouterLLM.openrouter_app_name) (<code>[str](#str)</code>) –
- [**openrouter_site_url**](#openhands.sdk.llm.router.base.RouterLLM.openrouter_site_url) (<code>[str](#str)</code>) –
- [**output_cost_per_token**](#openhands.sdk.llm.router.base.RouterLLM.output_cost_per_token) (<code>[float](#float) | None</code>) –
- [**reasoning_effort**](#openhands.sdk.llm.router.base.RouterLLM.reasoning_effort) (<code>[Literal](#typing.Literal)['low', 'medium', 'high', 'none'] | None</code>) –
- [**retry_listener**](#openhands.sdk.llm.router.base.RouterLLM.retry_listener) (<code>[SkipJsonSchema](#pydantic.json_schema.SkipJsonSchema)\[[Callable](#collections.abc.Callable)\[\[[int](#int), [int](#int)\], None\] | None\]</code>) –
- [**retry_max_wait**](#openhands.sdk.llm.router.base.RouterLLM.retry_max_wait) (<code>[int](#int)</code>) –
- [**retry_min_wait**](#openhands.sdk.llm.router.base.RouterLLM.retry_min_wait) (<code>[int](#int)</code>) –
- [**retry_multiplier**](#openhands.sdk.llm.router.base.RouterLLM.retry_multiplier) (<code>[float](#float)</code>) –
- [**router_name**](#openhands.sdk.llm.router.base.RouterLLM.router_name) (<code>[str](#str)</code>) –
- [**safety_settings**](#openhands.sdk.llm.router.base.RouterLLM.safety_settings) (<code>[list](#list)\[[dict](#dict)\[[str](#str), [str](#str)\]\] | None</code>) –
- [**seed**](#openhands.sdk.llm.router.base.RouterLLM.seed) (<code>[int](#int) | None</code>) –
- [**service_id**](#openhands.sdk.llm.router.base.RouterLLM.service_id) (<code>[str](#str)</code>) –
- [**temperature**](#openhands.sdk.llm.router.base.RouterLLM.temperature) (<code>[float](#float) | None</code>) –
- [**timeout**](#openhands.sdk.llm.router.base.RouterLLM.timeout) (<code>[int](#int) | None</code>) –
- [**top_k**](#openhands.sdk.llm.router.base.RouterLLM.top_k) (<code>[float](#float) | None</code>) –
- [**top_p**](#openhands.sdk.llm.router.base.RouterLLM.top_p) (<code>[float](#float) | None</code>) –
- [**usage_id**](#openhands.sdk.llm.router.base.RouterLLM.usage_id) (<code>[str](#str)</code>) –

###### `openhands.sdk.llm.router.base.RouterLLM.OVERRIDE_ON_SERIALIZE`

```python
OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key')
```

###### `openhands.sdk.llm.router.base.RouterLLM.active_llm`

```python
active_llm: LLM | None = Field(default=None, description='Currently selected LLM instance')
```

###### `openhands.sdk.llm.router.base.RouterLLM.api_key`

```python
api_key: SecretStr | None = Field(default=None, description='API key.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.api_version`

```python
api_version: str | None = Field(default=None, description='API version (e.g., Azure).')
```

###### `openhands.sdk.llm.router.base.RouterLLM.aws_access_key_id`

```python
aws_access_key_id: SecretStr | None = Field(default=None)
```

###### `openhands.sdk.llm.router.base.RouterLLM.aws_region_name`

```python
aws_region_name: str | None = Field(default=None)
```

###### `openhands.sdk.llm.router.base.RouterLLM.aws_secret_access_key`

```python
aws_secret_access_key: SecretStr | None = Field(default=None)
```

###### `openhands.sdk.llm.router.base.RouterLLM.base_url`

```python
base_url: str | None = Field(default=None, description='Custom base URL.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.caching_prompt`

```python
caching_prompt: bool = Field(default=True, description='Enable caching of prompts.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.completion`

```python
completion(messages, tools=None, return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

This method intercepts completion calls and routes them to the appropriate
underlying LLM based on the routing logic implemented in select_llm().

###### `openhands.sdk.llm.router.base.RouterLLM.custom_llm_provider`

```python
custom_llm_provider: str | None = Field(default=None)
```

###### `openhands.sdk.llm.router.base.RouterLLM.custom_tokenizer`

```python
custom_tokenizer: str | None = Field(default=None, description='A custom tokenizer to use for token counting.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.disable_stop_word`

```python
disable_stop_word: bool | None = Field(default=False, description='Disable using of stop word.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.disable_vision`

```python
disable_vision: bool | None = Field(default=None, description='If model is vision capable, this option allows to disable image processing (useful for cost reduction).')
```

###### `openhands.sdk.llm.router.base.RouterLLM.drop_params`

```python
drop_params: bool = Field(default=True)
```

###### `openhands.sdk.llm.router.base.RouterLLM.enable_encrypted_reasoning`

```python
enable_encrypted_reasoning: bool = Field(default=False, description="If True, ask for ['reasoning.encrypted_content'] in Responses API include.")
```

###### `openhands.sdk.llm.router.base.RouterLLM.extended_thinking_budget`

```python
extended_thinking_budget: int | None = Field(default=200000, description='The budget tokens for extended thinking, supported by Anthropic models.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.format_messages_for_llm`

```python
format_messages_for_llm(messages)
```

Formats Message objects for LLM consumption.

###### `openhands.sdk.llm.router.base.RouterLLM.format_messages_for_responses`

```python
format_messages_for_responses(messages)
```

Prepare (instructions, input[]) for the OpenAI Responses API.

- Skips prompt caching flags and string serializer concerns
- Uses Message.to_responses_value to get either instructions (system)
  or input items (others)
- Concatenates system instructions into a single instructions string

###### `openhands.sdk.llm.router.base.RouterLLM.get_token_count`

```python
get_token_count(messages)
```

###### `openhands.sdk.llm.router.base.RouterLLM.input_cost_per_token`

```python
input_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per input token. This will available in logs for user.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.is_caching_prompt_active`

```python
is_caching_prompt_active()
```

Check if prompt caching is supported and enabled for current model.

**Returns:**

- **boolean** (<code>[bool](#bool)</code>) – True if prompt caching is supported and enabled for the given
  model.

###### `openhands.sdk.llm.router.base.RouterLLM.is_context_window_exceeded_exception`

```python
is_context_window_exceeded_exception(exception)
```

Check if the exception indicates a context window exceeded error.

Context window exceeded errors vary by provider, and LiteLLM does not do a
consistent job of identifying and wrapping them.

###### `openhands.sdk.llm.router.base.RouterLLM.llms_for_routing`

```python
llms_for_routing: dict[str, LLM] = Field(default_factory=dict)
```

###### `openhands.sdk.llm.router.base.RouterLLM.load_from_env`

```python
load_from_env(prefix='LLM_')
```

###### `openhands.sdk.llm.router.base.RouterLLM.load_from_json`

```python
load_from_json(json_path)
```

###### `openhands.sdk.llm.router.base.RouterLLM.log_completions`

```python
log_completions: bool = Field(default=False, description='Enable logging of completions.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.log_completions_folder`

```python
log_completions_folder: str = Field(default=(os.path.join(ENV_LOG_DIR, 'completions')), description='The folder to log LLM completions to. Required if log_completions is True.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.max_input_tokens`

```python
max_input_tokens: int | None = Field(default=None, ge=1, description='The maximum number of input tokens. Note that this is currently unused, and the value at runtime is actually the total tokens in OpenAI (e.g. 128,000 tokens for GPT-4).')
```

###### `openhands.sdk.llm.router.base.RouterLLM.max_message_chars`

```python
max_message_chars: int = Field(default=30000, ge=1, description='Approx max chars in each event/content sent to the LLM.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.max_output_tokens`

```python
max_output_tokens: int | None = Field(default=None, ge=1, description='The maximum number of output tokens. This is sent to the LLM.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.metadata`

```python
metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata for the LLM instance. Example structure: {'trace_version': '1.0.0', 'tags': ['model:gpt-4', 'agent:my-agent'], 'session_id': 'session-123', 'trace_user_id': 'user-456'}")
```

###### `openhands.sdk.llm.router.base.RouterLLM.metrics`

```python
metrics: Metrics
```

###### `openhands.sdk.llm.router.base.RouterLLM.model`

```python
model: str = Field(default='claude-sonnet-4-20250514', description='Model name.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.model_config`

```python
model_config: ConfigDict = ConfigDict(extra='forbid', arbitrary_types_allowed=True)
```

###### `openhands.sdk.llm.router.base.RouterLLM.model_info`

```python
model_info: dict | None
```

Returns the model info dictionary.

###### `openhands.sdk.llm.router.base.RouterLLM.modify_params`

```python
modify_params: bool = Field(default=True, description='Modify params allows litellm to do transformations like adding a default message, when a message is empty.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.native_tool_calling`

```python
native_tool_calling: bool = Field(default=True, description='Whether to use native tool calling.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.num_retries`

```python
num_retries: int = Field(default=5, ge=0)
```

###### `openhands.sdk.llm.router.base.RouterLLM.ollama_base_url`

```python
ollama_base_url: str | None = Field(default=None)
```

###### `openhands.sdk.llm.router.base.RouterLLM.openrouter_app_name`

```python
openrouter_app_name: str = Field(default='OpenHands')
```

###### `openhands.sdk.llm.router.base.RouterLLM.openrouter_site_url`

```python
openrouter_site_url: str = Field(default='https://docs.all-hands.dev/')
```

###### `openhands.sdk.llm.router.base.RouterLLM.output_cost_per_token`

```python
output_cost_per_token: float | None = Field(default=None, ge=0, description='The cost per output token. This will available in logs for user.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.reasoning_effort`

```python
reasoning_effort: Literal['low', 'medium', 'high', 'none'] | None = Field(default=None, description="The effort to put into reasoning. This is a string that can be one of 'low', 'medium', 'high', or 'none'. Can apply to all reasoning models.")
```

###### `openhands.sdk.llm.router.base.RouterLLM.resolve_diff_from_deserialized`

```python
resolve_diff_from_deserialized(persisted)
```

Resolve differences between a deserialized LLM and the current instance.

This is due to fields like api_key being serialized to "\*\*\*\*" in dumps,
and we want to ensure that when loading from a file, we still use the
runtime-provided api_key in the self instance.

Return a new LLM instance equivalent to `persisted` but with
explicitly whitelisted fields (e.g. api_key) taken from `self`.

###### `openhands.sdk.llm.router.base.RouterLLM.responses`

```python
responses(messages, tools=None, include=None, store=None, _return_metrics=False, add_security_risk_prediction=False, **kwargs)
```

Alternative invocation path using OpenAI Responses API via LiteLLM.

Maps Message[] -> (instructions, input[]) and returns LLMResponse.
Non-stream only for v1.

###### `openhands.sdk.llm.router.base.RouterLLM.restore_metrics`

```python
restore_metrics(metrics)
```

###### `openhands.sdk.llm.router.base.RouterLLM.retry_listener`

```python
retry_listener: SkipJsonSchema[Callable[[int, int], None] | None] = Field(default=None, exclude=True)
```

###### `openhands.sdk.llm.router.base.RouterLLM.retry_max_wait`

```python
retry_max_wait: int = Field(default=64, ge=0)
```

###### `openhands.sdk.llm.router.base.RouterLLM.retry_min_wait`

```python
retry_min_wait: int = Field(default=8, ge=0)
```

###### `openhands.sdk.llm.router.base.RouterLLM.retry_multiplier`

```python
retry_multiplier: float = Field(default=8.0, ge=0)
```

###### `openhands.sdk.llm.router.base.RouterLLM.router_name`

```python
router_name: str = Field(default='base_router', description='Name of the router')
```

###### `openhands.sdk.llm.router.base.RouterLLM.safety_settings`

```python
safety_settings: list[dict[str, str]] | None = Field(default=None, description='Safety settings for models that support them (like Mistral AI and Gemini)')
```

###### `openhands.sdk.llm.router.base.RouterLLM.seed`

```python
seed: int | None = Field(default=None, description='The seed to use for random number generation.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.select_llm`

```python
select_llm(messages)
```

Select which LLM to use based on messages and events.

This method implements the core routing logic for the RouterLLM.
Subclasses should analyze the provided messages to determine which
LLM from llms_for_routing is most appropriate for handling the request.

**Parameters:**

- **messages** (<code>[list](#list)\[[Message](#openhands.sdk.llm.message.Message)\]</code>) – List of messages in the conversation that can be used
  to inform the routing decision.

**Returns:**

- <code>[str](#str)</code> – The key/name of the LLM to use from llms_for_routing dictionary.

###### `openhands.sdk.llm.router.base.RouterLLM.service_id`

```python
service_id: str
```

###### `openhands.sdk.llm.router.base.RouterLLM.set_placeholder_model`

```python
set_placeholder_model(data)
```

Guarantee `model` exists before LLM base validation runs.

###### `openhands.sdk.llm.router.base.RouterLLM.temperature`

```python
temperature: float | None = Field(default=0.0, ge=0)
```

###### `openhands.sdk.llm.router.base.RouterLLM.timeout`

```python
timeout: int | None = Field(default=None, ge=0, description='HTTP timeout (s).')
```

###### `openhands.sdk.llm.router.base.RouterLLM.top_k`

```python
top_k: float | None = Field(default=None, ge=0)
```

###### `openhands.sdk.llm.router.base.RouterLLM.top_p`

```python
top_p: float | None = Field(default=1.0, ge=0, le=1)
```

###### `openhands.sdk.llm.router.base.RouterLLM.usage_id`

```python
usage_id: str = Field(default='default', validation_alias=(AliasChoices('usage_id', 'service_id')), serialization_alias='usage_id', description='Unique usage identifier for the LLM. Used for registry lookups, telemetry, and spend tracking.')
```

###### `openhands.sdk.llm.router.base.RouterLLM.uses_responses_api`

```python
uses_responses_api()
```

Whether this model uses the OpenAI Responses API path.

###### `openhands.sdk.llm.router.base.RouterLLM.validate_llms_not_empty`

```python
validate_llms_not_empty(v)
```

###### `openhands.sdk.llm.router.base.RouterLLM.vision_is_active`

```python
vision_is_active()
```

##### `openhands.sdk.llm.router.base.logger`

```python
logger = get_logger(__name__)
```
