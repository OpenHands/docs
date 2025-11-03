---
title: openhands.sdk.context.condenser.no_op_condenser
description: API reference for openhands.sdk.context.condenser.no_op_condenser
---

# openhands.sdk.context.condenser.no_op_condenser module

<a id="module-openhands.sdk.context.condenser.no_op_condenser"></a>

### *class* openhands.sdk.context.condenser.no_op_condenser.NoOpCondenser(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['NoOpCondenser'] = 'NoOpCondenser')

Bases: [`CondenserBase`](https://github.com/OpenHands/software-agent-sdk/sdk.context.condenser.base.md#openhands.sdk.context.condenser.base.CondenserBase)

Simple condenser that returns a view un-manipulated.

Primarily intended for testing purposes.

#### condense(view: [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View)) → [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View) | [Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation)

Condense a sequence of events into a potentially smaller list.

New condenser strategies should override this method to implement their own
condensation logic. Call self.add_metadata in the implementation to record any
relevant per-condensation diagnostic information.

**Parameters:**
  **view** – A view of the history containing all events that should be condensed.
**Returns:**
  A condensed view of the events or an event indicating
  the history has been condensed.
* **Return type:**
  [View](https://github.com/OpenHands/software-agent-sdk/sdk.context.view.md#openhands.sdk.context.view.View) | [Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.md#openhands.sdk.event.Condensation)

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind *: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['NoOpCondenser']*
