---
title: openhands.sdk.agent.base
description: API reference for openhands.sdk.agent.base
---

# openhands.sdk.agent.base module

<a id="module-openhands.sdk.agent.base"></a>

### *class* openhands.sdk.agent.base.AgentBase(\*, kind: ~typing.Literal['Agent'] = 'Agent', llm: ~openhands.sdk.llm.llm.LLM, tools: list[~openhands.sdk.tool.spec.Tool] = <factory>, mcp_config: dict[str, ~typing.Any] = <factory>, filter_tools_regex: str | None = None, agent_context: ~openhands.sdk.context.agent_context.AgentContext | None = None, system_prompt_filename: str = 'system_prompt.j2', system_prompt_kwargs: dict[str, object] = <factory>, security_analyzer: ~openhands.sdk.security.analyzer.SecurityAnalyzerBase | None = None, condenser: ~openhands.sdk.context.condenser.base.CondenserBase | None = None)

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for agents.
Agents are stateless and should be fully defined by their configuration.

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### llm *: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)*

#### tools *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tool](https://github.com/OpenHands/software-agent-sdk/sdk.tool.spec.md#openhands.sdk.tool.spec.Tool)]*

#### mcp_config *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*

#### filter_tools_regex *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### agent_context *: [AgentContext](https://github.com/OpenHands/software-agent-sdk/sdk.context.agent_context.md#openhands.sdk.context.agent_context.AgentContext) | [None](https://docs.python.org/3/library/constants.html#None)*

#### system_prompt_filename *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### system_prompt_kwargs *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [object](https://docs.python.org/3/library/functions.html#object)]*

#### security_analyzer *: [SecurityAnalyzerBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase) | [None](https://docs.python.org/3/library/constants.html#None)*

#### condenser *: [CondenserBase](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.CondenserBase) | [None](https://docs.python.org/3/library/constants.html#None)*

#### *property* prompt_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Returns the directory where this class’s module file is located.

#### *property* name *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Returns the name of the Agent.

#### *property* system_message *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Compute system message on-demand to maintain statelessness.

#### init_state(state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.ConversationState), on_event: ConversationCallbackType) → [None](https://docs.python.org/3/library/constants.html#None)

Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

#### *abstractmethod* step(conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.md#openhands.sdk.conversation.LocalConversation), on_event: ConversationCallbackType) → [None](https://docs.python.org/3/library/constants.html#None)

Taking a step in the conversation.

Typically this involves:
1. Making a LLM call
2. Executing the tool
3. Updating the conversation state with

> LLM calls (role=”assistant”) and tool results (role=”tool”)

4.1 If conversation is finished, set state.agent_status to FINISHED
4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

#### resolve_diff_from_deserialized(persisted: [AgentBase](#openhands.sdk.agent.base.AgentBase)) → [AgentBase](#openhands.sdk.agent.base.AgentBase)

Return a new AgentBase instance equivalent to persisted but with
explicitly whitelisted fields (e.g. api_key, security_analyzer) taken from
self.

#### model_dump_succint(\*\*kwargs)

Like model_dump, but excludes None fields by default.

#### get_all_llms() → [Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[[LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM), [None](https://docs.python.org/3/library/constants.html#None), [None](https://docs.python.org/3/library/constants.html#None)]

Recursively yield unique *base-class* LLM objects reachable from self.

- Returns actual object references (not copies).
- De-dupes by id(LLM).
- Cycle-safe via a visited set for *all* traversed objects.
- Only yields objects whose type is exactly LLM (no subclasses).
- Does not handle dataclasses.

#### *property* tools_map *: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [ToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.tool.tool.md#id0)]*

Get the initialized tools map.
:raises RuntimeError: If the agent has not been initialized.

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### kind *: [str](https://docs.python.org/3/library/stdtypes.html#str)*
