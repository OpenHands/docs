---
title: openhands.sdk.agent
description: API reference for openhands.sdk.agent
---

# openhands.sdk.agent package

<a id="module-openhands.sdk.agent"></a>

### *class* openhands.sdk.agent.Agent

**Parameters:**

- `\*`
- `kind: typing.Literal['Agent'] = 'Agent'`
- `llm: openhands.sdk.llm.llm.LLM`
- `tools: list[openhands.sdk.tool.spec.Tool] = `<factory>``
- `mcp_config: dict[str, typing.Any] = `<factory>``
- `filter_tools_regex: str | None = None`
- `agent_context: openhands.sdk.context.agent_context.AgentContext | None = None`
- `system_prompt_filename: str = 'system_prompt.j2'`
- `system_prompt_kwargs: dict[str, object] = `<factory>``
- `security_analyzer: openhands.sdk.security.analyzer.SecurityAnalyzerBase | None = None`
- `condenser: openhands.sdk.context.condenser.base.CondenserBase | None = None`


Bases: [`AgentBase`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)

#### init_state

**Parameters:**

- `state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState)`
- `on_event: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]) → [None](https://docs.python.org/3/library/constants.html#None`


Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### step

**Parameters:**

- `conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation)`
- `on_event: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]) → [None](https://docs.python.org/3/library/constants.html#None`


Taking a step in the conversation.

Typically this involves:
1. Making a LLM call
2. Executing the tool
3. Updating the conversation state with

> LLM calls (role=”assistant”) and tool results (role=”tool”)

4.1 If conversation is finished, set state.agent_status to FINISHED
4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['Agent']*

### *class* openhands.sdk.agent.AgentBase

**Parameters:**

- `\*`
- `kind: typing.Literal['Agent'] = 'Agent'`
- `llm: openhands.sdk.llm.llm.LLM`
- `tools: list[openhands.sdk.tool.spec.Tool] = `<factory>``
- `mcp_config: dict[str, typing.Any] = `<factory>``
- `filter_tools_regex: str | None = None`
- `agent_context: openhands.sdk.context.agent_context.AgentContext | None = None`
- `system_prompt_filename: str = 'system_prompt.j2'`
- `system_prompt_kwargs: dict[str, object] = `<factory>``
- `security_analyzer: openhands.sdk.security.analyzer.SecurityAnalyzerBase | None = None`
- `condenser: openhands.sdk.context.condenser.base.CondenserBase | None = None`


Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for agents.
Agents are stateless and should be fully defined by their configuration.

#### get_all_llms

**Parameters:**

- `) → [Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[[LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)`
- `[None](https://docs.python.org/3/library/constants.html#None)`
- `[None](https://docs.python.org/3/library/constants.html#None`


Recursively yield unique *base-class* LLM objects reachable from self.

- Returns actual object references (not copies).
- De-dupes by id(LLM).
- Cycle-safe via a visited set for *all* traversed objects.
- Only yields objects whose type is exactly LLM (no subclasses).
- Does not handle dataclasses.

#### init_state

**Parameters:**

- `state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.ConversationState)`
- `on_event: ConversationCallbackType) → [None](https://docs.python.org/3/library/constants.html#None`


Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_dump_succint(\*\*kwargs)

Like model_dump, but excludes None fields by default.

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### *property* name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Returns the name of the Agent.

#### *property* prompt_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Returns the directory where this class’s module file is located.

#### resolve_diff_from_deserialized

**Parameters:**

- `persisted: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)) → [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase`


Return a new AgentBase instance equivalent to persisted but with
explicitly whitelisted fields (e.g. api_key, security_analyzer) taken from
self.

#### *abstractmethod* step

**Parameters:**

- `conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation)`
- `on_event: ConversationCallbackType) → [None](https://docs.python.org/3/library/constants.html#None`


Taking a step in the conversation.

Typically this involves:
1. Making a LLM call
2. Executing the tool
3. Updating the conversation state with

> LLM calls (role=”assistant”) and tool results (role=”tool”)

4.1 If conversation is finished, set state.agent_status to FINISHED
4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

#### *property* system_message *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Compute system message on-demand to maintain statelessness.

#### *property* tools_map *: [dict]

**Parameters:**

- `https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str)`
- `[ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0`


Get the initialized tools map.
:raises RuntimeError: If the agent has not been initialized.

#### llm *: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)*

#### tools *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tool](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool)]*

#### mcp_config *: [dict]

**Parameters:**

- `https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str)`
- `[Any](https://docs.python.org/3/library/typing.html#typing.Any`


#### filter_tools_regex *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### agent_context *: [AgentContext]

**Parameters:**

- `https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext) | [None](https://docs.python.org/3/library/constants.html#None`


#### system_prompt_filename *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### system_prompt_kwargs *: [dict]

**Parameters:**

- `https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str)`
- `[object](https://docs.python.org/3/library/functions.html#object`


#### security_analyzer *: [SecurityAnalyzerBase]

**Parameters:**

- `https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase) | [None](https://docs.python.org/3/library/constants.html#None`


#### condenser *: [CondenserBase]

**Parameters:**

- `https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.CondenserBase) | [None](https://docs.python.org/3/library/constants.html#None`


## Submodules

* [openhands.sdk.agent.agent module](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md)
  * [`Agent`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent)
    * [`Agent.init_state()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.init_state)
    * [`Agent.step()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.step)
    * [`Agent.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.model_config)
    * [`Agent.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.model_post_init)
    * [`Agent.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.kind)
    * [`Agent.llm`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.llm)
    * [`Agent.tools`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.tools)
    * [`Agent.mcp_config`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.mcp_config)
    * [`Agent.filter_tools_regex`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.filter_tools_regex)
    * [`Agent.agent_context`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.agent_context)
    * [`Agent.system_prompt_filename`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.system_prompt_filename)
    * [`Agent.system_prompt_kwargs`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.system_prompt_kwargs)
    * [`Agent.security_analyzer`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.security_analyzer)
    * [`Agent.condenser`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.agent.md#openhands.sdk.agent.agent.Agent.condenser)
* [openhands.sdk.agent.base module](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md)
  * [`AgentBase`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)
    * [`AgentBase.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.model_config)
    * [`AgentBase.llm`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.llm)
    * [`AgentBase.tools`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.tools)
    * [`AgentBase.mcp_config`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.mcp_config)
    * [`AgentBase.filter_tools_regex`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.filter_tools_regex)
    * [`AgentBase.agent_context`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.agent_context)
    * [`AgentBase.system_prompt_filename`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.system_prompt_filename)
    * [`AgentBase.system_prompt_kwargs`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.system_prompt_kwargs)
    * [`AgentBase.security_analyzer`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.security_analyzer)
    * [`AgentBase.condenser`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.condenser)
    * [`AgentBase.prompt_dir`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.prompt_dir)
    * [`AgentBase.name`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.name)
    * [`AgentBase.system_message`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.system_message)
    * [`AgentBase.init_state()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.init_state)
    * [`AgentBase.step()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.step)
    * [`AgentBase.resolve_diff_from_deserialized()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.resolve_diff_from_deserialized)
    * [`AgentBase.model_dump_succint()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.model_dump_succint)
    * [`AgentBase.get_all_llms()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.get_all_llms)
    * [`AgentBase.tools_map`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.tools_map)
    * [`AgentBase.model_post_init()`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.model_post_init)
    * [`AgentBase.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase.kind)
