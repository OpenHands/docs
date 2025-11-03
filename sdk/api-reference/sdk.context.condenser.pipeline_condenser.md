---
title: openhands.sdk.context.condenser.pipeline_condenser
description: API reference for openhands.sdk.context.condenser.pipeline_condenser
---

# openhands.sdk.context.condenser.pipeline_condenser module

<a id="module-openhands.sdk.context.condenser.pipeline_condenser"></a>

### *class* openhands.sdk.context.condenser.pipeline_condenser.PipelineCondenser(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['PipelineCondenser'] = 'PipelineCondenser', condensers: [list](https://docs.python.org/3/library/stdtypes.html#list)[[CondenserBase](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.CondenserBase)])

Bases: [`CondenserBase`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.CondenserBase)

A condenser that applies a sequence of condensers in order.

All condensers are defined primarily by their condense method, which takes a
View and returns either a new View or a Condensation event. That means we can
chain multiple condensers together by passing View\`s along and exiting early if any
condenser returns a \`Condensation.

For example:

> # Use the pipeline condenser to chain multiple other condensers together
> condenser = PipelineCondenser(condensers=[

> > CondenserA(…),
> > CondenserB(…),
> > CondenserC(…),

> ])

> result = condenser.condense(view)

> # Doing the same thing without the pipeline condenser requires more boilerplate
> # for the monadic chaining
> other_result = view

> if isinstance(other_result, View):
> : other_result = CondenserA(…).condense(other_result)

> if isinstance(other_result, View):
> : other_result = CondenserB(…).condense(other_result)

> if isinstance(other_result, View):
> : other_result = CondenserC(…).condense(other_result)

> assert result == other_result

#### condensers *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[CondenserBase](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.CondenserBase)]*

The list of condensers to apply in order.

#### condense(view: [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View)) → [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View) | [Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation)

Condense a sequence of events into a potentially smaller list.

New condenser strategies should override this method to implement their own
condensation logic. Call self.add_metadata in the implementation to record any
relevant per-condensation diagnostic information.

* **Parameters:**
  **view** – A view of the history containing all events that should be condensed.
* **Returns:**
  A condensed view of the events or an event indicating
  the history has been condensed.
* **Return type:**
  [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View) | [Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.md#openhands.sdk.event.Condensation)

#### handles_condensation_requests() → [bool](https://docs.python.org/3/library/functions.html#bool)

Whether this condenser handles explicit condensation requests.

If this returns True, the agent will trigger the condenser whenever a
CondensationRequest event is added to the history. If False, the condenser will
only be triggered when the agent’s own logic decides to do so (e.g. context
window exceeded).

* **Returns:**
  True if the condenser handles explicit condensation requests, False
  otherwise.
* **Return type:**
  [bool](https://docs.python.org/3/library/functions.html#bool)

#### model_config *: ClassVar[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['PipelineCondenser']*
