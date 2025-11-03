---
title: openhands.sdk.llm.message
description: API reference for openhands.sdk.llm.message
---

# openhands.sdk.llm.message module

<a id="module-openhands.sdk.llm.message"></a>

### *class* openhands.sdk.llm.message.MessageToolCall(, id: [str](https://docs.python.org/3/library/stdtypes.html#str), name: [str](https://docs.python.org/3/library/stdtypes.html#str), arguments: [str](https://docs.python.org/3/library/stdtypes.html#str), origin: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['completion', 'responses'])

Bases: `BaseModel`

Transport-agnostic tool call representation.

One canonical id is used for linking across actions/observations and
for Responses function_call_output call_id.

#### id : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### name : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### arguments : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### origin : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['completion', 'responses']

#### classmethod from_chat_tool_call(tool_call: ChatCompletionMessageToolCall) → [MessageToolCall](#openhands.sdk.llm.message.MessageToolCall)

Create a MessageToolCall from a Chat Completions tool call.

#### classmethod from_responses_function_call(item: ResponseFunctionToolCall | OutputFunctionToolCall) → [MessageToolCall](#openhands.sdk.llm.message.MessageToolCall)

Create a MessageToolCall from a typed OpenAI Responses function_call item.

Note: OpenAI Responses function_call.arguments is already a JSON string.

#### to_chat_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Serialize to OpenAI Chat Completions tool_calls format.

#### to_responses_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Serialize to OpenAI Responses ‘function_call’ input item format.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.llm.message.ThinkingBlock(, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['thinking'] = 'thinking', thinking: [str](https://docs.python.org/3/library/stdtypes.html#str), signature: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Anthropic thinking block for extended thinking feature.

This represents the raw thinking blocks returned by Anthropic models
when extended thinking is enabled. These blocks must be preserved
and passed back to the API for tool use scenarios.

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['thinking']

#### thinking : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### signature : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.llm.message.RedactedThinkingBlock(, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['redacted_thinking'] = 'redacted_thinking', data: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: `BaseModel`

Redacted thinking block for previous responses without extended thinking.

This is used as a placeholder for assistant messages that were generated
before extended thinking was enabled.

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['redacted_thinking']

#### data : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.llm.message.ReasoningItemModel(\*, id: str | None = None, summary: list[str] = `<factory>`, content: list[str] | None = None, encrypted_content: str | None = None, status: str | None = None)

Bases: `BaseModel`

OpenAI Responses reasoning item (non-stream, subset we consume).

Do not log or render encrypted_content.

#### id : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### summary : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

#### content : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)

#### encrypted_content : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### status : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.llm.message.BaseContent(, cache_prompt: [bool](https://docs.python.org/3/library/functions.html#bool) = False)

Bases: `BaseModel`

#### cache_prompt : [bool](https://docs.python.org/3/library/functions.html#bool)

#### abstractmethod to_llm_dict() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]]]

Convert to LLM API format. Always returns a list of dictionaries.

Subclasses should implement this method to return a list of dictionaries,
even if they only have a single item.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.llm.message.TextContent(, cache_prompt: [bool](https://docs.python.org/3/library/functions.html#bool) = False, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['text'] = 'text', text: [str](https://docs.python.org/3/library/stdtypes.html#str))

Bases: [`BaseContent`](#openhands.sdk.llm.message.BaseContent)

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['text']

#### text : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### model_config  : [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]*  = \{'extra': 'forbid', 'populate_by_name': True, 'validate_by_alias': True, 'validate_by_name': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### to_llm_dict() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]]]

Convert to LLM API format.

#### cache_prompt : [bool](https://docs.python.org/3/library/functions.html#bool)

### *class* openhands.sdk.llm.message.ImageContent(, cache_prompt: [bool](https://docs.python.org/3/library/functions.html#bool) = False, type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['image'] = 'image', image_urls: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)])

Bases: [`BaseContent`](#openhands.sdk.llm.message.BaseContent)

#### type : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['image']

#### image_urls : [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

#### to_llm_dict() → [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]]]

Convert to LLM API format.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### cache_prompt : [bool](https://docs.python.org/3/library/functions.html#bool)

### *class* openhands.sdk.llm.message.Message(\*, role: typing.Literal['user', 'system', 'assistant', 'tool'], content: ~collections.abc.Sequence[openhands.sdk.llm.message.TextContent | openhands.sdk.llm.message.ImageContent] = `<factory>`, cache_enabled: bool = False, vision_enabled: bool = False, function_calling_enabled: bool = False, tool_calls: list[openhands.sdk.llm.message.MessageToolCall] | None = None, tool_call_id: str | None = None, name: str | None = None, force_string_serializer: bool = False, reasoning_content: str | None = None, thinking_blocks: ~collections.abc.Sequence[openhands.sdk.llm.message.ThinkingBlock | openhands.sdk.llm.message.RedactedThinkingBlock] = `<factory>`, responses_reasoning_item: openhands.sdk.llm.message.ReasoningItemModel | None = None)

Bases: `BaseModel`

#### role : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['user', 'system', 'assistant', 'tool']

#### content : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)]

#### cache_enabled : [bool](https://docs.python.org/3/library/functions.html#bool)

#### vision_enabled : [bool](https://docs.python.org/3/library/functions.html#bool)

#### function_calling_enabled : [bool](https://docs.python.org/3/library/functions.html#bool)

#### tool_calls : [list](https://docs.python.org/3/library/stdtypes.html#list)[[MessageToolCall](#openhands.sdk.llm.message.MessageToolCall)] | [None](https://docs.python.org/3/library/constants.html#None)

#### tool_call_id : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### name : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### force_string_serializer : [bool](https://docs.python.org/3/library/functions.html#bool)

#### reasoning_content : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### thinking_blocks : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[ThinkingBlock](#openhands.sdk.llm.message.ThinkingBlock) | [RedactedThinkingBlock](#openhands.sdk.llm.message.RedactedThinkingBlock)]

#### responses_reasoning_item : [ReasoningItemModel](#openhands.sdk.llm.message.ReasoningItemModel) | [None](https://docs.python.org/3/library/constants.html#None)

#### property contains_image : [bool](https://docs.python.org/3/library/functions.html#bool)

#### to_chat_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]

Serialize message for OpenAI Chat Completions.

Chooses the appropriate content serializer and then injects threading keys:
- Assistant tool call turn: role == “assistant” and self.tool_calls
- Tool result turn: role == “tool” and self.tool_call_id (with name)

#### to_responses_value(, vision_enabled: [bool](https://docs.python.org/3/library/functions.html#bool)) → [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]]

Return serialized form.

Either an instructions string (for system) or input items (for other roles).

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

#### classmethod from_llm_chat_message(message: Message) → [Message](#openhands.sdk.llm.message.Message)

Convert a LiteLLMMessage (Chat Completions) to our Message class.

Provider-agnostic mapping for reasoning:
- Prefer message.reasoning_content if present (LiteLLM normalized field)
- Extract thinking_blocks from content array (Anthropic-specific)

#### classmethod from_llm_responses_output(output: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [Message](#openhands.sdk.llm.message.Message)

Convert OpenAI Responses API output items into a single assistant Message.

Policy (non-stream):
- Collect assistant text by concatenating output_text parts from message items
- Normalize function_call items to MessageToolCall list

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### openhands.sdk.llm.message.content_to_str(contents: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[TextContent](#openhands.sdk.llm.message.TextContent) | [ImageContent](#openhands.sdk.llm.message.ImageContent)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Convert a list of TextContent and ImageContent to a list of strings.

This is primarily used for display purposes.
