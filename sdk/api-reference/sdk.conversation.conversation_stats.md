---
title: openhands.sdk.conversation.conversation_stats
description: API reference for openhands.sdk.conversation.conversation_stats
---

# openhands.sdk.conversation.conversation_stats module

<a id="module-openhands.sdk.conversation.conversation_stats"></a>

### *class* openhands.sdk.conversation.conversation_stats.ConversationStats(\*, usage_to_metrics: dict[str, ~openhands.sdk.llm.utils.metrics.Metrics] = `<factory>`)

Bases: `BaseModel`

Track per-LLM usage metrics observed during conversations.

#### usage_to_metrics *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Metrics](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Metrics)]*

#### *property* service_to_metrics *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Metrics](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Metrics)]*

#### get_combined_metrics() → [Metrics](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Metrics)

#### get_metrics_for_usage(usage_id: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [Metrics](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Metrics)

#### get_metrics_for_service(service_id: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [Metrics](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.Metrics)

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(context: Any,)  → [None](https://docs.python.org/3/library/constants.html#None)

This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that’s what pydantic-core passes when calling it.

**Parameters:**
  - **self** – The BaseModel instance.
  - **context** – The context.

#### register_llm(event: [RegistryEvent](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm_registry.md#openhands.sdk.llm.llm_registry.RegistryEvent))
