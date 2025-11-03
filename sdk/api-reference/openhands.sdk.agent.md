---
title: openhands.sdk.agent
description: API reference for openhands.sdk.agent
---

# openhands.sdk.agent module

### Agent

Bases: [`AgentBase`](#openhands.sdk.agent.AgentBase)

Main agent implementation for OpenHands.

The Agent class provides the core functionality for running AI agents that can
interact with tools, process messages, and execute actions. It inherits from
AgentBase and implements the agent execution logic.

### Example

```pycon
>`>`>` from openhands.sdk import LLM, Agent, Tool
>`>`>` llm = LLM(model="claude-sonnet-4-20250514", api_key=SecretStr("key"))
>`>`>` tools = [Tool(name="BashTool"), Tool(name="FileEditorTool")]
>`>`>` agent = Agent(llm=llm, tools=tools)
```

#### agent_context *: [AgentContext]

#### condenser : CondenserBase | None

#### filter_tools_regex : str | None

#### init_state

Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

#### kind : Literal['Agent']

#### llm *: [LLM]

#### mcp_config : dict[str, Any]

#### model_config : ClassVar[ConfigDict] = {'arbitrary_types_allowed': True, 'frozen': True}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### security_analyzer : analyzer.SecurityAnalyzerBase | None

#### step

Taking a step in the conversation.

Typically this involves:
1. Making a LLM call
2. Executing the tool
3. Updating the conversation state with

>` LLM calls (role=”assistant”) and tool results (role=”tool”)

4.1 If conversation is finished, set state.agent_status to FINISHED
4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

#### system_prompt_filename : str

#### system_prompt_kwargs : dict[str, object]

#### tools *: list[[Tool]

### AgentBase

Bases: `DiscriminatedUnionMixin`, `ABC`

Abstract base class for OpenHands agents.

Agents are stateless and should be fully defined by their configuration.
This base class provides the common interface and functionality that all
agent implementations must follow.

#### agent_context *: [AgentContext]

#### condenser : CondenserBase | None

#### filter_tools_regex : str | None

#### get_all_llms

Recursively yield unique base-class LLM objects reachable from self.

- Returns actual object references (not copies).
- De-dupes by id(LLM).
- Cycle-safe via a visited set for all traversed objects.
- Only yields objects whose type is exactly LLM (no subclasses).
- Does not handle dataclasses.

#### init_state

Initialize the empty conversation state to prepare the agent for user
messages.

Typically this involves adding system message

NOTE: state will be mutated in-place.

#### kind : str

#### llm *: [LLM]

#### mcp_config : dict[str, Any]

#### model_config : ClassVar[ConfigDict] = {'arbitrary_types_allowed': True, 'frozen': True}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_dump_succint

Like model_dump, but excludes None fields by default.

#### model_post_init

Override this method to perform additional initialization after __init__ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.

#### property name : str

Returns the name of the Agent.

#### property prompt_dir : str

Returns the directory where this class’s module file is located.

#### resolve_diff_from_deserialized

Return a new AgentBase instance equivalent to persisted but with
explicitly whitelisted fields (e.g. api_key, security_analyzer) taken from
self.

#### security_analyzer : SecurityAnalyzerBase | None

#### abstractmethod step

Taking a step in the conversation.

Typically this involves:
1. Making a LLM call
2. Executing the tool
3. Updating the conversation state with

>` LLM calls (role=”assistant”) and tool results (role=”tool”)

4.1 If conversation is finished, set state.agent_status to FINISHED
4.2 Otherwise, just return, Conversation will kick off the next step

NOTE: state will be mutated in-place.

#### property system_message : str

Compute system message on-demand to maintain statelessness.

#### system_prompt_filename : str

#### system_prompt_kwargs : dict[str, object]

#### tools *: list[[Tool]

#### property tools_map *: dict[str, [ToolDefinition]

Get the initialized tools map.
:raises RuntimeError: If the agent has not been initialized.
