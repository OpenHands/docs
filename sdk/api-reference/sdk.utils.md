---
title: openhands.sdk.utils
description: API reference for openhands.sdk.utils
---

# openhands.sdk.utils package

<a id="module-openhands.sdk.utils"></a>

Utility functions for the OpenHands SDK.

### openhands.sdk.utils.maybe_truncate(content: [str](https://docs.python.org/3/library/stdtypes.html#str), truncate_after: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None) = None, truncate_notice: [str](https://docs.python.org/3/library/stdtypes.html#str) = '<response clipped><NOTE>Due to the max output limit, only part of the full response has been shown to you.</NOTE>') → [str](https://docs.python.org/3/library/stdtypes.html#str)

Truncate the middle of content if it exceeds the specified length.

Keeps the head and tail of the content to preserve context at both ends.

* **Parameters:**
  * **content** – The text content to potentially truncate
  * **truncate_after** – Maximum length before truncation. If None, no truncation occurs
  * **truncate_notice** – Notice to insert in the middle when content is truncated
* **Returns:**
  Original content if under limit, or truncated content with head and tail
  preserved

## Submodules

* [openhands.sdk.utils.async_executor module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_executor.md)
  * [`AsyncExecutor`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_executor.md#openhands.sdk.utils.async_executor.AsyncExecutor)
    * [`AsyncExecutor.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_executor.md#openhands.sdk.utils.async_executor.AsyncExecutor.__init__)
    * [`AsyncExecutor.run_async()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_executor.md#openhands.sdk.utils.async_executor.AsyncExecutor.run_async)
    * [`AsyncExecutor.close()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_executor.md#openhands.sdk.utils.async_executor.AsyncExecutor.close)
    * [`AsyncExecutor.__del__()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_executor.md#openhands.sdk.utils.async_executor.AsyncExecutor.__del__)
* [openhands.sdk.utils.async_utils module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_utils.md)
  * [`AsyncCallbackWrapper`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_utils.md#openhands.sdk.utils.async_utils.AsyncCallbackWrapper)
    * [`AsyncCallbackWrapper.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_utils.md#openhands.sdk.utils.async_utils.AsyncCallbackWrapper.__init__)
    * [`AsyncCallbackWrapper.async_callback`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_utils.md#openhands.sdk.utils.async_utils.AsyncCallbackWrapper.async_callback)
    * [`AsyncCallbackWrapper.loop`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.async_utils.md#openhands.sdk.utils.async_utils.AsyncCallbackWrapper.loop)
* [openhands.sdk.utils.cipher module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.cipher.md)
  * [`Cipher`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.cipher.md#openhands.sdk.utils.cipher.Cipher)
    * [`Cipher.__init__()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.cipher.md#openhands.sdk.utils.cipher.Cipher.__init__)
    * [`Cipher.encrypt()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.cipher.md#openhands.sdk.utils.cipher.Cipher.encrypt)
    * [`Cipher.decrypt()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.cipher.md#openhands.sdk.utils.cipher.Cipher.decrypt)
* [openhands.sdk.utils.command module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.command.md)
  * [`execute_command()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.command.md#openhands.sdk.utils.command.execute_command)
* [openhands.sdk.utils.json module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.json.md)
  * [`OpenHandsJSONEncoder`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.json.md#openhands.sdk.utils.json.OpenHandsJSONEncoder)
    * [`OpenHandsJSONEncoder.default()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.json.md#openhands.sdk.utils.json.OpenHandsJSONEncoder.default)
  * [`dumps()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.json.md#openhands.sdk.utils.json.dumps)
  * [`loads()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.json.md#openhands.sdk.utils.json.loads)
* [openhands.sdk.utils.models module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md)
  * [`rebuild_all()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.rebuild_all)
  * [`kind_of()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.kind_of)
  * [`get_known_concrete_subclasses()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.get_known_concrete_subclasses)
  * [`OpenHandsModel`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel)
    * [`OpenHandsModel.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel.model_post_init)
    * [`OpenHandsModel.model_validate()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel.model_validate)
    * [`OpenHandsModel.model_validate_json()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel.model_validate_json)
    * [`OpenHandsModel.model_json_schema()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel.model_json_schema)
    * [`OpenHandsModel.model_dump_json()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel.model_dump_json)
    * [`OpenHandsModel.__init_subclass__()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel.__init_subclass__)
    * [`OpenHandsModel.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel.model_config)
  * [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin)
    * [`DiscriminatedUnionMixin.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.kind)
    * [`DiscriminatedUnionMixin.resolve_kind()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.resolve_kind)
    * [`DiscriminatedUnionMixin.__get_pydantic_core_schema__()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.__get_pydantic_core_schema__)
    * [`DiscriminatedUnionMixin.__get_pydantic_json_schema__()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.__get_pydantic_json_schema__)
    * [`DiscriminatedUnionMixin.model_rebuild()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_rebuild)
    * [`DiscriminatedUnionMixin.get_serializable_type()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.get_serializable_type)
    * [`DiscriminatedUnionMixin.model_validate()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_validate)
    * [`DiscriminatedUnionMixin.model_validate_json()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_validate_json)
    * [`DiscriminatedUnionMixin.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_config)
* [openhands.sdk.utils.pydantic_diff module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.pydantic_diff.md)
  * [`pretty_pydantic_diff()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.pydantic_diff.md#openhands.sdk.utils.pydantic_diff.pretty_pydantic_diff)
* [openhands.sdk.utils.pydantic_secrets module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.pydantic_secrets.md)
  * [`serialize_secret()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.pydantic_secrets.md#openhands.sdk.utils.pydantic_secrets.serialize_secret)
  * [`validate_secret()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.pydantic_secrets.md#openhands.sdk.utils.pydantic_secrets.validate_secret)
* [openhands.sdk.utils.truncate module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.truncate.md)
  * [`maybe_truncate()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.truncate.md#openhands.sdk.utils.truncate.maybe_truncate)
* [openhands.sdk.utils.visualize module](https://github.com/OpenHands/software-agent-sdk/sdk.utils.visualize.md)
  * [`display_dict()`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.visualize.md#openhands.sdk.utils.visualize.display_dict)
