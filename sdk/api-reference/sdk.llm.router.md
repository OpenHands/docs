---
title: openhands.sdk.llm.router
description: API reference for openhands.sdk.llm.router
---

# openhands.sdk.llm.router package

<a id="module-openhands.sdk.llm.router"></a>

### *class* openhands.sdk.llm.router.RouterLLM(\*, model: str = 'claude-sonnet-4-20250514', api_key: ~pydantic.types.SecretStr | None = None, base_url: str | None = None, api_version: str | None = None, aws_access_key_id: ~pydantic.types.SecretStr | None = None, aws_secret_access_key: ~pydantic.types.SecretStr | None = None, aws_region_name: str | None = None, openrouter_site_url: str = 'https://docs.all-hands.dev/', openrouter_app_name: str = 'OpenHands', num_retries: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 5, retry_multiplier: ~typing.Annotated[float, ~annotated_types.Ge(ge=0)] = 8.0, retry_min_wait: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 8, retry_max_wait: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 64, timeout: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=0)] = None, max_message_chars: ~typing.Annotated[int, ~annotated_types.Ge(ge=1)] = 30000, temperature: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = 0.0, top_p: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0), ~annotated_types.Le(le=1)] = 1.0, top_k: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, custom_llm_provider: str | None = None, max_input_tokens: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=1)] = None, max_output_tokens: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=1)] = None, input_cost_per_token: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, output_cost_per_token: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, ollama_base_url: str | None = None, drop_params: bool = True, modify_params: bool = True, disable_vision: bool | None = None, disable_stop_word: bool | None = False, caching_prompt: bool = True, log_completions: bool = False, log_completions_folder: str = 'logs/completions', custom_tokenizer: str | None = None, native_tool_calling: bool = True, reasoning_effort: ~typing.Literal['low', 'medium', 'high', 'none'] | None = None, enable_encrypted_reasoning: bool = False, extended_thinking_budget: int | None = 200000, seed: int | None = None, safety_settings: list[dict[str, str]] | None = None, usage_id: str = 'default', metadata: dict[str, ~typing.Any] = <factory>, retry_listener: ~typing.Annotated[~collections.abc.Callable[[int, int], None] | None, ~pydantic.json_schema.SkipJsonSchema()] = None, OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key'), router_name: str = 'base_router', llms_for_routing: dict[str, ~openhands.sdk.llm.llm.LLM] = <factory>, active_llm: ~openhands.sdk.llm.llm.LLM | None = None)

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

#### completion(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)], tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ToolBase](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#openhands.sdk.tool.tool.ToolBase)] | [None](https://docs.python.org/3/library/constants.html#None) = None, return_metrics: [bool](https://docs.python.org/3/library/functions.html#bool) = False, add_security_risk_prediction: [bool](https://docs.python.org/3/library/functions.html#bool) = False, \*\*kwargs) → [LLMResponse](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_response.md#openhands.sdk.llm.llm_response.LLMResponse)

This method intercepts completion calls and routes them to the appropriate
underlying LLM based on the routing logic implemented in select_llm().

#### model_config *: ClassVar[ConfigDict]* *= {'arbitrary_types_allowed': True, 'extra': 'forbid'}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: Any,)  → [None](https://docs.python.org/3/library/constants.html#None)

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

* **Parameters:**
  * **self** – The BaseModel instance.
  * **context** – The context.

#### *abstractmethod* select_llm(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Select which LLM to use based on messages and events.

This method implements the core routing logic for the RouterLLM.
Subclasses should analyze the provided messages to determine which
LLM from llms_for_routing is most appropriate for handling the request.

* **Parameters:**
  **messages** – List of messages in the conversation that can be used
  to inform the routing decision.
* **Returns:**
  The key/name of the LLM to use from llms_for_routing dictionary.

#### *classmethod* set_placeholder_model(data)

Guarantee model exists before LLM base validation runs.

#### *classmethod* validate_llms_not_empty(v)

#### router_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### llms_for_routing *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)]*

#### active_llm *: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM) | [None](https://docs.python.org/3/library/constants.html#None)*

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

### *class* openhands.sdk.llm.router.RandomRouter(\*, model: str = 'claude-sonnet-4-20250514', api_key: ~pydantic.types.SecretStr | None = None, base_url: str | None = None, api_version: str | None = None, aws_access_key_id: ~pydantic.types.SecretStr | None = None, aws_secret_access_key: ~pydantic.types.SecretStr | None = None, aws_region_name: str | None = None, openrouter_site_url: str = 'https://docs.all-hands.dev/', openrouter_app_name: str = 'OpenHands', num_retries: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 5, retry_multiplier: ~typing.Annotated[float, ~annotated_types.Ge(ge=0)] = 8.0, retry_min_wait: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 8, retry_max_wait: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 64, timeout: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=0)] = None, max_message_chars: ~typing.Annotated[int, ~annotated_types.Ge(ge=1)] = 30000, temperature: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = 0.0, top_p: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0), ~annotated_types.Le(le=1)] = 1.0, top_k: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, custom_llm_provider: str | None = None, max_input_tokens: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=1)] = None, max_output_tokens: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=1)] = None, input_cost_per_token: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, output_cost_per_token: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, ollama_base_url: str | None = None, drop_params: bool = True, modify_params: bool = True, disable_vision: bool | None = None, disable_stop_word: bool | None = False, caching_prompt: bool = True, log_completions: bool = False, log_completions_folder: str = 'logs/completions', custom_tokenizer: str | None = None, native_tool_calling: bool = True, reasoning_effort: ~typing.Literal['low', 'medium', 'high', 'none'] | None = None, enable_encrypted_reasoning: bool = False, extended_thinking_budget: int | None = 200000, seed: int | None = None, safety_settings: list[dict[str, str]] | None = None, usage_id: str = 'default', metadata: dict[str, ~typing.Any] = <factory>, retry_listener: ~typing.Annotated[~collections.abc.Callable[[int, int], None] | None, ~pydantic.json_schema.SkipJsonSchema()] = None, OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key'), router_name: str = 'random_router', llms_for_routing: dict[str, ~openhands.sdk.llm.llm.LLM] = <factory>, active_llm: ~openhands.sdk.llm.llm.LLM | None = None)

Bases: [`RouterLLM`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM)

A simple implementation of RouterLLM that randomly selects an LLM from
llms_for_routing for each completion request.

#### model_config *: ClassVar[ConfigDict]* *= {'arbitrary_types_allowed': True, 'extra': 'forbid'}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: Any,)  → [None](https://docs.python.org/3/library/constants.html#None)

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

* **Parameters:**
  * **self** – The BaseModel instance.
  * **context** – The context.

#### select_llm(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Select which LLM to use based on messages and events.

This method implements the core routing logic for the RouterLLM.
Subclasses should analyze the provided messages to determine which
LLM from llms_for_routing is most appropriate for handling the request.

* **Parameters:**
  **messages** – List of messages in the conversation that can be used
  to inform the routing decision.
* **Returns:**
  The key/name of the LLM to use from llms_for_routing dictionary.

#### router_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* openhands.sdk.llm.router.MultimodalRouter(\*, model: str = 'claude-sonnet-4-20250514', api_key: ~pydantic.types.SecretStr | None = None, base_url: str | None = None, api_version: str | None = None, aws_access_key_id: ~pydantic.types.SecretStr | None = None, aws_secret_access_key: ~pydantic.types.SecretStr | None = None, aws_region_name: str | None = None, openrouter_site_url: str = 'https://docs.all-hands.dev/', openrouter_app_name: str = 'OpenHands', num_retries: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 5, retry_multiplier: ~typing.Annotated[float, ~annotated_types.Ge(ge=0)] = 8.0, retry_min_wait: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 8, retry_max_wait: ~typing.Annotated[int, ~annotated_types.Ge(ge=0)] = 64, timeout: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=0)] = None, max_message_chars: ~typing.Annotated[int, ~annotated_types.Ge(ge=1)] = 30000, temperature: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = 0.0, top_p: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0), ~annotated_types.Le(le=1)] = 1.0, top_k: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, custom_llm_provider: str | None = None, max_input_tokens: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=1)] = None, max_output_tokens: ~typing.Annotated[int | None, ~annotated_types.Ge(ge=1)] = None, input_cost_per_token: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, output_cost_per_token: ~typing.Annotated[float | None, ~annotated_types.Ge(ge=0)] = None, ollama_base_url: str | None = None, drop_params: bool = True, modify_params: bool = True, disable_vision: bool | None = None, disable_stop_word: bool | None = False, caching_prompt: bool = True, log_completions: bool = False, log_completions_folder: str = 'logs/completions', custom_tokenizer: str | None = None, native_tool_calling: bool = True, reasoning_effort: ~typing.Literal['low', 'medium', 'high', 'none'] | None = None, enable_encrypted_reasoning: bool = False, extended_thinking_budget: int | None = 200000, seed: int | None = None, safety_settings: list[dict[str, str]] | None = None, usage_id: str = 'default', metadata: dict[str, ~typing.Any] = <factory>, retry_listener: ~typing.Annotated[~collections.abc.Callable[[int, int], None] | None, ~pydantic.json_schema.SkipJsonSchema()] = None, OVERRIDE_ON_SERIALIZE: tuple[str, ...] = ('api_key', 'aws_access_key_id', 'aws_secret_access_key'), router_name: str = 'multimodal_router', llms_for_routing: dict[str, ~openhands.sdk.llm.llm.LLM] = <factory>, active_llm: ~openhands.sdk.llm.llm.LLM | None = None)

Bases: [`RouterLLM`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM)

A RouterLLM implementation that routes requests based on multimodal content
(e.g., images) and token limits. If any message contains multimodal content
or if the token limit of the secondary model is exceeded, it routes to the
primary model. Otherwise, it routes to the secondary model.

Note: The primary model is expected to support multimodal content, while
the secondary model is typically a text-only model with a lower context window.

#### PRIMARY_MODEL_KEY *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[[str](https://docs.python.org/3/library/stdtypes.html#str)]* *= 'primary'*

#### SECONDARY_MODEL_KEY *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[[str](https://docs.python.org/3/library/stdtypes.html#str)]* *= 'secondary'*

#### model_config *: ClassVar[ConfigDict]* *= {'arbitrary_types_allowed': True, 'extra': 'forbid'}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: Any,)  → [None](https://docs.python.org/3/library/constants.html#None)

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

* **Parameters:**
  * **self** – The BaseModel instance.
  * **context** – The context.

#### select_llm(messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Message](https://github.com/OpenHands/software-agent-sdk/sdk.llm.message.md#openhands.sdk.llm.message.Message)]) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Select LLM based on multimodal content and token limits.

#### router_name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

## Submodules

* [openhands.sdk.llm.router.base module](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md)
  * [`RouterLLM`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM)
    * [`RouterLLM.router_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.router_name)
    * [`RouterLLM.llms_for_routing`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.llms_for_routing)
    * [`RouterLLM.active_llm`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.active_llm)
    * [`RouterLLM.validate_llms_not_empty()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.validate_llms_not_empty)
    * [`RouterLLM.completion()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.completion)
    * [`RouterLLM.select_llm()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.select_llm)
    * [`RouterLLM.__getattr__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.__getattr__)
    * [`RouterLLM.__str__()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.__str__)
    * [`RouterLLM.set_placeholder_model()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.set_placeholder_model)
    * [`RouterLLM.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.model_config)
    * [`RouterLLM.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.model_post_init)
    * [`RouterLLM.model`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.model)
    * [`RouterLLM.api_key`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.api_key)
    * [`RouterLLM.base_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.base_url)
    * [`RouterLLM.api_version`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.api_version)
    * [`RouterLLM.aws_access_key_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.aws_access_key_id)
    * [`RouterLLM.aws_secret_access_key`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.aws_secret_access_key)
    * [`RouterLLM.aws_region_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.aws_region_name)
    * [`RouterLLM.openrouter_site_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.openrouter_site_url)
    * [`RouterLLM.openrouter_app_name`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.openrouter_app_name)
    * [`RouterLLM.num_retries`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.num_retries)
    * [`RouterLLM.retry_multiplier`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.retry_multiplier)
    * [`RouterLLM.retry_min_wait`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.retry_min_wait)
    * [`RouterLLM.retry_max_wait`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.retry_max_wait)
    * [`RouterLLM.timeout`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.timeout)
    * [`RouterLLM.max_message_chars`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.max_message_chars)
    * [`RouterLLM.temperature`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.temperature)
    * [`RouterLLM.top_p`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.top_p)
    * [`RouterLLM.top_k`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.top_k)
    * [`RouterLLM.custom_llm_provider`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.custom_llm_provider)
    * [`RouterLLM.max_input_tokens`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.max_input_tokens)
    * [`RouterLLM.max_output_tokens`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.max_output_tokens)
    * [`RouterLLM.input_cost_per_token`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.input_cost_per_token)
    * [`RouterLLM.output_cost_per_token`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.output_cost_per_token)
    * [`RouterLLM.ollama_base_url`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.ollama_base_url)
    * [`RouterLLM.drop_params`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.drop_params)
    * [`RouterLLM.modify_params`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.modify_params)
    * [`RouterLLM.disable_vision`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.disable_vision)
    * [`RouterLLM.disable_stop_word`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.disable_stop_word)
    * [`RouterLLM.caching_prompt`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.caching_prompt)
    * [`RouterLLM.log_completions`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.log_completions)
    * [`RouterLLM.log_completions_folder`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.log_completions_folder)
    * [`RouterLLM.custom_tokenizer`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.custom_tokenizer)
    * [`RouterLLM.native_tool_calling`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.native_tool_calling)
    * [`RouterLLM.reasoning_effort`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.reasoning_effort)
    * [`RouterLLM.enable_encrypted_reasoning`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.enable_encrypted_reasoning)
    * [`RouterLLM.extended_thinking_budget`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.extended_thinking_budget)
    * [`RouterLLM.seed`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.seed)
    * [`RouterLLM.safety_settings`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.safety_settings)
    * [`RouterLLM.usage_id`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.usage_id)
    * [`RouterLLM.metadata`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.metadata)
    * [`RouterLLM.retry_listener`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.retry_listener)
    * [`RouterLLM.OVERRIDE_ON_SERIALIZE`](https://github.com/OpenHands/software-agent-sdk/sdk.llm.router.base.md#openhands.sdk.llm.router.base.RouterLLM.OVERRIDE_ON_SERIALIZE)
