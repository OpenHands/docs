---
title: openhands.sdk.agent.agent
description: API reference for openhands.sdk.agent.agent
---

# openhands.sdk.agent.agent module

<a id="module-openhands.sdk.agent.agent"></a>

### class openhands.sdk.agent.agent.Agent(kind: typing.Literal['Agent'] = 'Agent', llm: openhands.sdk.llm.llm.LLM, tools: list[openhands.sdk.tool.spec.Tool] = `<factory>`, mcp_config: dict[str, typing.Any] = `<factory>`, filter_tools_regex: str | None = None, agent_context: openhands.sdk.context.agent_context.AgentContext | None = None, system_prompt_filename: str = 'system_prompt.j2', system_prompt_kwargs: dict[str, object] = `<factory>`, security_analyzer: openhands.sdk.security.analyzer.SecurityAnalyzerBase | None = None, condenser: openhands.sdk.context.condenser.base.CondenserBase | None = None)

Bases: [`AgentBase`](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)

Main agent implementation for OpenHands.

The Agent class provides the core functionality for running AI agents that can
interact with tools, process messages, and execute actions. It inherits from
AgentBase and implements the agent execution logic.

### Example

```pycon
>>> from openhands.sdk import LLM, Agent, Tool
>>> llm = LLM(model="claude-sonnet-4-20250514", api_key=SecretStr("key"))
>>> tools = [Tool(name="BashTool"), Tool(name="FileEditorTool")]
>>> agent = Agent(llm=llm, tools=tools)
```

#### init_state(state: [ConversationState](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.state.md#openhands.sdk.conversation.state.ConversationState), on_event: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]) → [None](https://docs.python.org/3/library/constants.html#None)

Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

#### step(conversation: [LocalConversation](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.impl.local_conversation.md#openhands.sdk.conversation.impl.local_conversation.LocalConversation), on_event: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)]) → [None](https://docs.python.org/3/library/constants.html#None)

Taking a step in the conversation.

Typically this involves:
1. Making a LLM call
2. Executing the tool
3. Updating the conversation state with

> LLM calls (role=”assistant”) and tool results (role=”tool”)

4.1 If conversation is finished, set state.agent_status to FINISHED
4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

#### model_config  : ClassVar[ConfigDict]*  = \{'arbitrary_types_allowed': True, 'frozen': True\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['Agent']

#### llm : [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.md#openhands.sdk.llm.LLM)

#### tools : [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tool](https://github.com/OpenHands/software-agent-sdk/sdk.tool.md#openhands.sdk.tool.Tool)]

#### mcp_config : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any]

#### filter_tools_regex : [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)

#### agent_context : [AgentContext](https://github.com/OpenHands/software-agent-sdk/sdk.context.md#openhands.sdk.context.AgentContext) | [None](https://docs.python.org/3/library/constants.html#None)

#### system_prompt_filename : [str](https://docs.python.org/3/library/stdtypes.html#str)

#### system_prompt_kwargs : [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [object](https://docs.python.org/3/library/functions.html#object)]

#### security_analyzer : [analyzer.SecurityAnalyzerBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase) | [None](https://docs.python.org/3/library/constants.html#None)

#### condenser : [CondenserBase](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.md#openhands.sdk.context.condenser.CondenserBase) | [None](https://docs.python.org/3/library/constants.html#None)
