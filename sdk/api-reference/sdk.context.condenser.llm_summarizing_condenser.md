---
title: openhands.sdk.context.condenser.llm_summarizing_condenser
description: API reference for openhands.sdk.context.condenser.llm_summarizing_condenser
---

# openhands.sdk.context.condenser.llm_summarizing_condenser module

<a id="module-openhands.sdk.context.condenser.llm_summarizing_condenser"></a>

### *class* openhands.sdk.context.condenser.llm_summarizing_condenser.LLMSummarizingCondenser(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LLMSummarizingCondenser'] = 'LLMSummarizingCondenser', llm: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM), max_size: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[int](https://docs.python.org/3/library/functions.html#int), Gt(gt=0)] = 120, keep_first: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[int](https://docs.python.org/3/library/functions.html#int), Ge(ge=0)] = 4)

Bases: [`RollingCondenser`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.RollingCondenser)

#### llm *: [LLM](https://github.com/OpenHands/software-agent-sdk/sdk.llm.llm.md#openhands.sdk.llm.llm.LLM)*

#### max_size *: [int](https://docs.python.org/3/library/functions.html#int)*

#### keep_first *: [int](https://docs.python.org/3/library/functions.html#int)*

#### validate_keep_first_vs_max_size()

#### handles_condensation_requests() → [bool](https://docs.python.org/3/library/functions.html#bool)

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent’s own logic decides to do so (e.g. context
window exceeded).

**Returns:**
  True if the condenser handles explicit condensation requests, False
  otherwise.
- **Return type:**
  [bool](https://docs.python.org/3/library/functions.html#bool)

#### should_condense(view: [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View)) → [bool](https://docs.python.org/3/library/functions.html#bool)

Determine if a view should be condensed.

#### get_condensation(view: [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View)) → [Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation)

Get the condensation from a view.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LLMSummarizingCondenser']*
