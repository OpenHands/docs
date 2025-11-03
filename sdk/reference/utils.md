## `openhands.sdk.utils`

Utility functions for the OpenHands SDK.

**Modules:**

- [**async_executor**](#openhands.sdk.utils.async_executor) – Reusable async-to-sync execution utility.
- [**async_utils**](#openhands.sdk.utils.async_utils) – Async utilities for OpenHands SDK.
- [**cipher**](#openhands.sdk.utils.cipher) – Cipher utility for preventing accidental secret disclosure in serialized data
- [**command**](#openhands.sdk.utils.command) –
- [**json**](#openhands.sdk.utils.json) –
- [**models**](#openhands.sdk.utils.models) –
- [**pydantic_diff**](#openhands.sdk.utils.pydantic_diff) –
- [**pydantic_secrets**](#openhands.sdk.utils.pydantic_secrets) –
- [**truncate**](#openhands.sdk.utils.truncate) – Utility functions for truncating text content.
- [**visualize**](#openhands.sdk.utils.visualize) –

**Functions:**

- [**maybe_truncate**](#openhands.sdk.utils.maybe_truncate) – Truncate the middle of content if it exceeds the specified length.

**Attributes:**

- [**DEFAULT_TEXT_CONTENT_LIMIT**](#openhands.sdk.utils.DEFAULT_TEXT_CONTENT_LIMIT) –
- [**DEFAULT_TRUNCATE_NOTICE**](#openhands.sdk.utils.DEFAULT_TRUNCATE_NOTICE) –

### `openhands.sdk.utils.DEFAULT_TEXT_CONTENT_LIMIT`

```python
DEFAULT_TEXT_CONTENT_LIMIT = 50000
```

### `openhands.sdk.utils.DEFAULT_TRUNCATE_NOTICE`

```python
DEFAULT_TRUNCATE_NOTICE = '<response clipped><NOTE>Due to the max output limit, only part of the full response has been shown to you.</NOTE>'
```

### `openhands.sdk.utils.async_executor`

Reusable async-to-sync execution utility.

**Classes:**

- [**AsyncExecutor**](#openhands.sdk.utils.async_executor.AsyncExecutor) – Manages a background event loop for executing async code from sync contexts.

#### `openhands.sdk.utils.async_executor.AsyncExecutor`

```python
AsyncExecutor()
```

Manages a background event loop for executing async code from sync contexts.

This provides a robust async-to-sync bridge with proper resource management,
timeout support, and thread safety.

**Functions:**

- [**close**](#openhands.sdk.utils.async_executor.AsyncExecutor.close) – Close the async executor and cleanup resources.
- [**run_async**](#openhands.sdk.utils.async_executor.AsyncExecutor.run_async) – Run a coroutine or async function on the background loop from sync code.

##### `openhands.sdk.utils.async_executor.AsyncExecutor.close`

```python
close()
```

Close the async executor and cleanup resources.

##### `openhands.sdk.utils.async_executor.AsyncExecutor.run_async`

```python
run_async(awaitable_or_fn, *args, timeout=300.0, **kwargs)
```

Run a coroutine or async function on the background loop from sync code.

**Parameters:**

- **awaitable_or_fn** (<code>[Callable](#collections.abc.Callable)\[..., [Any](#typing.Any)\] | [Any](#typing.Any)</code>) – Coroutine or async function to execute
- \***args** – Arguments to pass to the function
- **timeout** (<code>[float](#float)</code>) – Timeout in seconds (default: 300)
- \*\***kwargs** – Keyword arguments to pass to the function

**Returns:**

- <code>[Any](#typing.Any)</code> – The result of the async operation

**Raises:**

- <code>[TypeError](#TypeError)</code> – If awaitable_or_fn is not a coroutine or async function
- <code>[TimeoutError](#asyncio.TimeoutError)</code> – If the operation times out

### `openhands.sdk.utils.async_utils`

Async utilities for OpenHands SDK.

This module provides utilities for working with async callbacks in the context
of synchronous conversation handling.

**Classes:**

- [**AsyncCallbackWrapper**](#openhands.sdk.utils.async_utils.AsyncCallbackWrapper) – Wrapper that executes async callbacks in a different thread's event loop.

**Attributes:**

- [**AsyncConversationCallback**](#openhands.sdk.utils.async_utils.AsyncConversationCallback) –

#### `openhands.sdk.utils.async_utils.AsyncCallbackWrapper`

```python
AsyncCallbackWrapper(async_callback, loop)
```

Wrapper that executes async callbacks in a different thread's event loop.

This class implements the ConversationCallbackType interface (synchronous)
but internally executes an async callback in an event loop running in a
different thread. This allows async callbacks to be used in synchronous
conversation contexts.

**Attributes:**

- [**async_callback**](#openhands.sdk.utils.async_utils.AsyncCallbackWrapper.async_callback) (<code>[AsyncConversationCallback](#openhands.sdk.utils.async_utils.AsyncConversationCallback)</code>) –
- [**loop**](#openhands.sdk.utils.async_utils.AsyncCallbackWrapper.loop) (<code>[AbstractEventLoop](#asyncio.AbstractEventLoop)</code>) –

##### `openhands.sdk.utils.async_utils.AsyncCallbackWrapper.async_callback`

```python
async_callback: AsyncConversationCallback = async_callback
```

##### `openhands.sdk.utils.async_utils.AsyncCallbackWrapper.loop`

```python
loop: asyncio.AbstractEventLoop = loop
```

#### `openhands.sdk.utils.async_utils.AsyncConversationCallback`

```python
AsyncConversationCallback = Callable[[Event], Coroutine[Any, Any, None]]
```

### `openhands.sdk.utils.cipher`

Cipher utility for preventing accidental secret disclosure in serialized data

SECURITY WARNINGS:

- The secret key is a string for ease of use but should contain at least 256
  bits of entropy

**Classes:**

- [**Cipher**](#openhands.sdk.utils.cipher.Cipher) – Simple encryption utility for preventing accidental secret disclosure.

#### `openhands.sdk.utils.cipher.Cipher`

```python
Cipher(secret_key)
```

Simple encryption utility for preventing accidental secret disclosure.

**Functions:**

- [**decrypt**](#openhands.sdk.utils.cipher.Cipher.decrypt) – Decrypt a secret value, returning None if decryption fails.
- [**encrypt**](#openhands.sdk.utils.cipher.Cipher.encrypt) –

**Attributes:**

- [**secret_key**](#openhands.sdk.utils.cipher.Cipher.secret_key) –

##### `openhands.sdk.utils.cipher.Cipher.decrypt`

```python
decrypt(secret)
```

Decrypt a secret value, returning None if decryption fails.

This handles cases where existing conversations were serialized with different
encryption keys or contain invalid encrypted data. A warning is logged when
decryption fails and a None is returned. This mimics the case where
no cipher was defined so secrets where redacted.

##### `openhands.sdk.utils.cipher.Cipher.encrypt`

```python
encrypt(secret)
```

##### `openhands.sdk.utils.cipher.Cipher.secret_key`

```python
secret_key = secret_key
```

### `openhands.sdk.utils.command`

**Functions:**

- [**execute_command**](#openhands.sdk.utils.command.execute_command) –

**Attributes:**

- [**logger**](#openhands.sdk.utils.command.logger) –

#### `openhands.sdk.utils.command.execute_command`

```python
execute_command(cmd, env=None, cwd=None, timeout=None, print_output=True)
```

#### `openhands.sdk.utils.command.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.utils.json`

**Classes:**

- [**OpenHandsJSONEncoder**](#openhands.sdk.utils.json.OpenHandsJSONEncoder) – Custom JSON encoder that handles datetime and other OH objects

**Functions:**

- [**dumps**](#openhands.sdk.utils.json.dumps) – Serialize an object to str format
- [**loads**](#openhands.sdk.utils.json.loads) – Create a JSON object from str

#### `openhands.sdk.utils.json.OpenHandsJSONEncoder`

Bases: <code>[JSONEncoder](#json.JSONEncoder)</code>

Custom JSON encoder that handles datetime and other OH objects

**Functions:**

- [**default**](#openhands.sdk.utils.json.OpenHandsJSONEncoder.default) –

##### `openhands.sdk.utils.json.OpenHandsJSONEncoder.default`

```python
default(o)
```

#### `openhands.sdk.utils.json.dumps`

```python
dumps(obj, **kwargs)
```

Serialize an object to str format

#### `openhands.sdk.utils.json.loads`

```python
loads(json_str, **kwargs)
```

Create a JSON object from str

### `openhands.sdk.utils.maybe_truncate`

```python
maybe_truncate(content, truncate_after=None, truncate_notice=DEFAULT_TRUNCATE_NOTICE)
```

Truncate the middle of content if it exceeds the specified length.

Keeps the head and tail of the content to preserve context at both ends.

**Parameters:**

- **content** (<code>[str](#str)</code>) – The text content to potentially truncate
- **truncate_after** (<code>[int](#int) | None</code>) – Maximum length before truncation. If None, no truncation occurs
- **truncate_notice** (<code>[str](#str)</code>) – Notice to insert in the middle when content is truncated

**Returns:**

- <code>[str](#str)</code> – Original content if under limit, or truncated content with head and tail
- <code>[str](#str)</code> – preserved

### `openhands.sdk.utils.models`

**Classes:**

- [**DiscriminatedUnionMixin**](#openhands.sdk.utils.models.DiscriminatedUnionMixin) – A Base class for members of tagged unions discriminated by the class name.
- [**OpenHandsModel**](#openhands.sdk.utils.models.OpenHandsModel) – Tags a class where the which may be a discriminated union or contain fields

**Functions:**

- [**get_known_concrete_subclasses**](#openhands.sdk.utils.models.get_known_concrete_subclasses) – Recursively returns all concrete subclasses in a stable order,
- [**kind_of**](#openhands.sdk.utils.models.kind_of) – Get the string value for the kind tag
- [**rebuild_all**](#openhands.sdk.utils.models.rebuild_all) – Rebuild all polymorphic classes.

**Attributes:**

- [**logger**](#openhands.sdk.utils.models.logger) –

#### `openhands.sdk.utils.models.DiscriminatedUnionMixin`

Bases: <code>[OpenHandsModel](#openhands.sdk.utils.models.OpenHandsModel)</code>, <code>[ABC](#abc.ABC)</code>

A Base class for members of tagged unions discriminated by the class name.

This class provides automatic subclass registration and discriminated union
functionality. Each subclass is automatically registered when defined and
can be used for polymorphic serialization/deserialization.

Child classes will automatically have a type field defined, which is used as a
discriminator for union types.

**Functions:**

- [**get_serializable_type**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_json_schema) –
- [**model_post_init**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_post_init) –
- [**model_rebuild**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_rebuild) –
- [**model_validate**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_validate) –
- [**model_validate_json**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.resolve_kind) –

**Attributes:**

- [**kind**](#openhands.sdk.utils.models.DiscriminatedUnionMixin.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.utils.models.DiscriminatedUnionMixin.resolve_kind`

```python
resolve_kind(kind)
```

#### `openhands.sdk.utils.models.OpenHandsModel`

Bases: <code>[BaseModel](#pydantic.BaseModel)</code>

Tags a class where the which may be a discriminated union or contain fields
which contain a discriminated union. The first time an instance is initialized,
the schema is loaded, or a model is validated after a subclass is defined we
regenerate all the polymorphic mappings.

**Functions:**

- [**model_dump_json**](#openhands.sdk.utils.models.OpenHandsModel.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.utils.models.OpenHandsModel.model_json_schema) –
- [**model_post_init**](#openhands.sdk.utils.models.OpenHandsModel.model_post_init) –
- [**model_validate**](#openhands.sdk.utils.models.OpenHandsModel.model_validate) –
- [**model_validate_json**](#openhands.sdk.utils.models.OpenHandsModel.model_validate_json) –

##### `openhands.sdk.utils.models.OpenHandsModel.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.utils.models.OpenHandsModel.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.utils.models.OpenHandsModel.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.utils.models.OpenHandsModel.model_validate`

```python
model_validate(*args, **kwargs)
```

##### `openhands.sdk.utils.models.OpenHandsModel.model_validate_json`

```python
model_validate_json(*args, **kwargs)
```

#### `openhands.sdk.utils.models.get_known_concrete_subclasses`

```python
get_known_concrete_subclasses(cls)
```

Recursively returns all concrete subclasses in a stable order,
without deduping classes that share the same (module, name).

#### `openhands.sdk.utils.models.kind_of`

```python
kind_of(obj)
```

Get the string value for the kind tag

#### `openhands.sdk.utils.models.logger`

```python
logger = logging.getLogger(__name__)
```

#### `openhands.sdk.utils.models.rebuild_all`

```python
rebuild_all()
```

Rebuild all polymorphic classes.

### `openhands.sdk.utils.pydantic_diff`

**Functions:**

- [**pretty_pydantic_diff**](#openhands.sdk.utils.pydantic_diff.pretty_pydantic_diff) –

#### `openhands.sdk.utils.pydantic_diff.pretty_pydantic_diff`

```python
pretty_pydantic_diff(a, b)
```

### `openhands.sdk.utils.pydantic_secrets`

**Functions:**

- [**serialize_secret**](#openhands.sdk.utils.pydantic_secrets.serialize_secret) – Serialize secret fields with encryption or redaction.
- [**validate_secret**](#openhands.sdk.utils.pydantic_secrets.validate_secret) – Deserialize secret fields, handling encryption and empty values.

#### `openhands.sdk.utils.pydantic_secrets.serialize_secret`

```python
serialize_secret(v, info)
```

Serialize secret fields with encryption or redaction.

- If a cipher is provided in context, encrypts the secret value
- If expose_secrets flag is True in context, exposes the actual value
- Otherwise, lets Pydantic handle default masking (redaction)
- This prevents accidental secret disclosure

#### `openhands.sdk.utils.pydantic_secrets.validate_secret`

```python
validate_secret(v, info)
```

Deserialize secret fields, handling encryption and empty values.

- Empty secrets are converted to None
- If a cipher is provided in context, attempts to decrypt the value
- If decryption fails, the cipher returns None and a warning is logged
- This gracefully handles conversations encrypted with different keys or were redacted

### `openhands.sdk.utils.truncate`

Utility functions for truncating text content.

**Functions:**

- [**maybe_truncate**](#openhands.sdk.utils.truncate.maybe_truncate) – Truncate the middle of content if it exceeds the specified length.

**Attributes:**

- [**DEFAULT_TEXT_CONTENT_LIMIT**](#openhands.sdk.utils.truncate.DEFAULT_TEXT_CONTENT_LIMIT) –
- [**DEFAULT_TRUNCATE_NOTICE**](#openhands.sdk.utils.truncate.DEFAULT_TRUNCATE_NOTICE) –

#### `openhands.sdk.utils.truncate.DEFAULT_TEXT_CONTENT_LIMIT`

```python
DEFAULT_TEXT_CONTENT_LIMIT = 50000
```

#### `openhands.sdk.utils.truncate.DEFAULT_TRUNCATE_NOTICE`

```python
DEFAULT_TRUNCATE_NOTICE = '<response clipped><NOTE>Due to the max output limit, only part of the full response has been shown to you.</NOTE>'
```

#### `openhands.sdk.utils.truncate.maybe_truncate`

```python
maybe_truncate(content, truncate_after=None, truncate_notice=DEFAULT_TRUNCATE_NOTICE)
```

Truncate the middle of content if it exceeds the specified length.

Keeps the head and tail of the content to preserve context at both ends.

**Parameters:**

- **content** (<code>[str](#str)</code>) – The text content to potentially truncate
- **truncate_after** (<code>[int](#int) | None</code>) – Maximum length before truncation. If None, no truncation occurs
- **truncate_notice** (<code>[str](#str)</code>) – Notice to insert in the middle when content is truncated

**Returns:**

- <code>[str](#str)</code> – Original content if under limit, or truncated content with head and tail
- <code>[str](#str)</code> – preserved

### `openhands.sdk.utils.visualize`

**Functions:**

- [**display_dict**](#openhands.sdk.utils.visualize.display_dict) – Create a Rich Text representation of a dictionary.

#### `openhands.sdk.utils.visualize.display_dict`

```python
display_dict(d)
```

Create a Rich Text representation of a dictionary.
