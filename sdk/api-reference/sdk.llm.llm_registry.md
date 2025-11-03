---
title: openhands.sdk.llm.llm_registry
description: API reference for openhands.sdk.llm.llm_registry
---

# openhands.sdk.llm.llm_registry module

<a id="module-openhands.sdk.llm.llm_registry"></a>

### *class* openhands.sdk.llm.llm_registry.RegistryEvent(, llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM))

Bases: `BaseModel`

#### llm *: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)*

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {'arbitrary_types_allowed': True}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.llm.llm_registry.LLMRegistry(retry_listener: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A minimal LLM registry for managing LLM instances by usage ID.

This registry provides a simple way to manage multiple LLM instances,
avoiding the need to recreate LLMs with the same configuration.

#### \_\_init_\_(retry_listener: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None) = None)

Initialize the LLM registry.

* **Parameters:**
  **retry_listener** – Optional callback for retry events.

#### registry_id *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### retry_listener *: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### subscriber *: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None)*

#### subscribe(callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)], [None](https://docs.python.org/3/library/constants.html#None)]) → [None](https://docs.python.org/3/library/constants.html#None)

Subscribe to registry events.

* **Parameters:**
  **callback** – Function to call when LLMs are created or updated.

#### notify(event: [RegistryEvent](#openhands.sdk.llm.llm_registry.RegistryEvent)) → [None](https://docs.python.org/3/library/constants.html#None)

Notify subscribers of registry events.

* **Parameters:**
  **event** – The registry event to notify about.

#### *property* usage_to_llm *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)]*

Access the internal usage-ID-to-LLM mapping.

#### *property* service_to_llm *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)]*

#### add(llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)) → [None](https://docs.python.org/3/library/constants.html#None)

Add an LLM instance to the registry.

* **Parameters:**
  **llm** – The LLM instance to register.
* **Raises:**
  [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) – If llm.usage_id already exists in the registry.

#### get(usage_id: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)

Get an LLM instance from the registry.

* **Parameters:**
  **usage_id** – Unique identifier for the LLM usage slot.
* **Returns:**
  The LLM instance.
* **Raises:**
  [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError) – If usage_id is not found in the registry.

#### list_usage_ids() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

List all registered usage IDs.

#### list_services() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Deprecated alias for [`list_usage_ids()`](#openhands.sdk.llm.llm_registry.LLMRegistry.list_usage_ids).
