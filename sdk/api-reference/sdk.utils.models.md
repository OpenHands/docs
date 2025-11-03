---
title: openhands.sdk.utils.models
description: API reference for openhands.sdk.utils.models
---

# openhands.sdk.utils.models module

<a id="module-openhands.sdk.utils.models"></a>

### openhands.sdk.utils.models.rebuild_all()

Rebuild all polymorphic classes.

### openhands.sdk.utils.models.kind_of(obj) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Get the string value for the kind tag

### openhands.sdk.utils.models.get_known_concrete_subclasses(cls) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[type](https://docs.python.org/3/library/functions.html#type)]

Recursively returns all concrete subclasses in a stable order,
without deduping classes that share the same (module, name).

### *class* openhands.sdk.utils.models.OpenHandsModel

Bases: `BaseModel`

Tags a class where the which may be a discriminated union or contain fields
which contain a discriminated union. The first time an instance is initialized,
the schema is loaded, or a model is validated after a subclass is defined we
regenerate all the polymorphic mappings.

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### *classmethod* model_validate(\*args, \*\*kwargs) → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

Validate a pydantic model instance.

* **Parameters:**
  * **obj** – The object to validate.
  * **strict** – Whether to enforce types strictly.
  * **extra** – Whether to ignore, allow, or forbid extra data during model validation.
    See the [extra configuration value][pydantic.ConfigDict.extra] for details.
  * **from_attributes** – Whether to extract data from object attributes.
  * **context** – Additional context to pass to the validator.
  * **by_alias** – Whether to use the field’s alias when validating against the provided input data.
  * **by_name** – Whether to use the field’s name when validating against the provided input data.
* **Raises:**
  **ValidationError** – If the object could not be validated.
* **Returns:**
  The validated model instance.

#### *classmethod* model_validate_json(\*args, \*\*kwargs) → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

!!! abstract “Usage Documentation”
: [JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

* **Parameters:**
  * **json_data** – The JSON data to validate.
  * **strict** – Whether to enforce types strictly.
  * **extra** – Whether to ignore, allow, or forbid extra data during model validation.
    See the [extra configuration value][pydantic.ConfigDict.extra] for details.
  * **context** – Extra variables to pass to the validator.
  * **by_alias** – Whether to use the field’s alias when validating against the provided input data.
  * **by_name** – Whether to use the field’s name when validating against the provided input data.
* **Returns:**
  The validated Pydantic model.
* **Raises:**
  **ValidationError** – If json_data is not a JSON string or the object could not be validated.

#### *classmethod* model_json_schema(\*args, \*\*kwargs) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Generates a JSON schema for a model class.

* **Parameters:**
  * **by_alias** – Whether to use attribute aliases or not.
  * **ref_template** – The reference template.
  * **union_format** – 

    The format to use when combining schemas from unions together. Can be one of:
    - ’any_of’: Use the [anyOf]([https://json-schema.org/understanding-json-schema/reference/combining#anyOf](https://json-schema.org/understanding-json-schema/reference/combining#anyOf))

    keyword to combine schemas (the default).
    - ‘primitive_type_array’: Use the [type]([https://json-schema.org/understanding-json-schema/reference/type](https://json-schema.org/understanding-json-schema/reference/type))
    keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
    type (string, boolean, null, integer or number) or contains constraints/metadata, falls back to
    any_of.
  * **schema_generator** – To override the logic used to generate the JSON schema, as a subclass of
    GenerateJsonSchema with your desired modifications
  * **mode** – The mode in which to generate the schema.
* **Returns:**
  The JSON schema for the given model class.

#### model_dump_json(\*\*kwargs)

!!! abstract “Usage Documentation”
: [model_dump_json](../concepts/serialization.md#json-mode)

Generates a JSON representation of the model using Pydantic’s to_json method.

* **Parameters:**
  * **indent** – Indentation to use in the JSON output. If None is passed, the output will be compact.
  * **ensure_ascii** – If True, the output is guaranteed to have all incoming non-ASCII characters escaped.
    If False (the default), these characters will be output as-is.
  * **include** – Field(s) to include in the JSON output.
  * **exclude** – Field(s) to exclude from the JSON output.
  * **context** – Additional context to pass to the serializer.
  * **by_alias** – Whether to serialize using field aliases.
  * **exclude_unset** – Whether to exclude fields that have not been explicitly set.
  * **exclude_defaults** – Whether to exclude fields that are set to their default value.
  * **exclude_none** – Whether to exclude fields that have a value of None.
  * **exclude_computed_fields** – Whether to exclude computed fields.
    While this can be useful for round-tripping, it is usually recommended to use the dedicated
    round_trip parameter instead.
  * **round_trip** – If True, dumped values should be valid as input for non-idempotent types such as Json[T].
  * **warnings** – How to handle serialization errors. False/”none” ignores them, True/”warn” logs errors,
    “error” raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].
  * **fallback** – A function to call when an unknown value is encountered. If not provided,
    a [PydanticSerializationError][pydantic_core.PydanticSerializationError] error is raised.
  * **serialize_as_any** – Whether to serialize fields with duck-typing serialization behavior.
* **Returns:**
  A JSON string representation of the model.

#### *classmethod* \_\_init_subclass_\_(\*\*kwargs)

When a new subclass is defined, mark that we will need
to rebuild everything

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.utils.models.DiscriminatedUnionMixin(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['Agent', 'LLMSummarizingCondenser', 'NoOpCondenser', 'PipelineCondenser', 'LookupSecret', 'StaticSecret', 'Condensation', 'CondensationRequest', 'CondensationSummaryEvent', 'ConversationStateUpdateEvent', 'ActionEvent', 'MessageEvent', 'AgentErrorEvent', 'ObservationEvent', 'UserRejectObservation', 'SystemPromptEvent', 'PauseEvent', 'MCPToolAction', 'MCPToolObservation', 'MCPToolDefinition', 'AlwaysConfirm', 'ConfirmRisky', 'NeverConfirm', 'LLMSecurityAnalyzer', 'FinishAction', 'FinishObservation', 'ThinkAction', 'ThinkObservation', 'Schema', 'ToolDefinition', 'ToolDefinition[MCPToolAction, MCPToolObservation]', 'LocalWorkspace', 'RemoteWorkspace'] = 'Agent')

Bases: [`OpenHandsModel`](#openhands.sdk.utils.models.OpenHandsModel), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

A Base class for members of tagged unions discriminated by the class name.

This class provides automatic subclass registration and discriminated union
functionality. Each subclass is automatically registered when defined and
can be used for polymorphic serialization/deserialization.

Child classes will automatically have a type field defined, which is used as a
discriminator for union types.

#### kind *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *classmethod* resolve_kind(kind: [str](https://docs.python.org/3/library/stdtypes.html#str)) → [type](https://docs.python.org/3/library/functions.html#type)

#### *classmethod* \_\_get_pydantic_core_schema_\_(source_type, handler)

Generate discriminated union schema for TypeAdapter compatibility.

#### *classmethod* \_\_get_pydantic_json_schema_\_(core_schema, handler)

Add discriminator to OpenAPI schema and ensure component generation.

#### *classmethod* model_rebuild(, force=False, raise_errors=True, \_parent_namespace_depth=2, \_types_namespace=None)

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

* **Parameters:**
  * **force** – Whether to force the rebuilding of the model schema, defaults to False.
  * **raise_errors** – Whether to raise errors, defaults to True.
  * **\_parent_namespace_depth** – The depth level of the parent namespace, defaults to 2.
  * **\_types_namespace** – The types namespace, defaults to None.
* **Returns:**
  Returns None if the schema is already “complete” and rebuilding was not required.
  If rebuilding \_was_ required, returns True if rebuilding was successful, otherwise False.

#### *classmethod* get_serializable_type() → [type](https://docs.python.org/3/library/functions.html#type)

Custom method to get the union of all currently loaded
non absract subclasses

#### *classmethod* model_validate(obj: [Any](https://docs.python.org/3/library/typing.html#typing.Any), \*\*kwargs) → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

Validate a pydantic model instance.

* **Parameters:**
  * **obj** – The object to validate.
  * **strict** – Whether to enforce types strictly.
  * **extra** – Whether to ignore, allow, or forbid extra data during model validation.
    See the [extra configuration value][pydantic.ConfigDict.extra] for details.
  * **from_attributes** – Whether to extract data from object attributes.
  * **context** – Additional context to pass to the validator.
  * **by_alias** – Whether to use the field’s alias when validating against the provided input data.
  * **by_name** – Whether to use the field’s name when validating against the provided input data.
* **Raises:**
  **ValidationError** – If the object could not be validated.
* **Returns:**
  The validated model instance.

#### *classmethod* model_validate_json(json_data: [str](https://docs.python.org/3/library/stdtypes.html#str) | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray), \*\*kwargs) → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

!!! abstract “Usage Documentation”
: [JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.

* **Parameters:**
  * **json_data** – The JSON data to validate.
  * **strict** – Whether to enforce types strictly.
  * **extra** – Whether to ignore, allow, or forbid extra data during model validation.
    See the [extra configuration value][pydantic.ConfigDict.extra] for details.
  * **context** – Extra variables to pass to the validator.
  * **by_alias** – Whether to use the field’s alias when validating against the provided input data.
  * **by_name** – Whether to use the field’s name when validating against the provided input data.
* **Returns:**
  The validated Pydantic model.
* **Raises:**
  **ValidationError** – If json_data is not a JSON string or the object could not be validated.

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
