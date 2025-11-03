---
title: openhands.sdk.context.view
description: API reference for openhands.sdk.context.view
---

# openhands.sdk.context.view module

<a id="module-openhands.sdk.context.view"></a>

### *class* openhands.sdk.context.view.View(, events: [list](https://docs.python.org/3/library/stdtypes.html#list)[[LLMConvertibleEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)], unhandled_condensation_request: [bool](https://docs.python.org/3/library/functions.html#bool) = False, condensations: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation)] = [])

Bases: `BaseModel`

Linearly ordered view of events.

Produced by a condenser to indicate the included events are ready to process as LLM
input. Also contains fields with information from the condensation process to aid
in deciding whether further condensation is needed.

#### events *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[LLMConvertibleEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)]*

#### unhandled_condensation_request *: [bool](https://docs.python.org/3/library/functions.html#bool)*

Whether there is an unhandled condensation request in the view.

#### condensations *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation)]*

A list of condensations that were processed to produce the view.

#### *property* most_recent_condensation *: [Condensation](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.Condensation) | [None](https://docs.python.org/3/library/constants.html#None)*

Return the most recent condensation, or None if no condensations exist.

#### *property* summary_event_index *: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

Return the index of the summary event, or None if no summary exists.

#### *property* summary_event *: [CondensationSummaryEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.condenser.md#openhands.sdk.event.condenser.CondensationSummaryEvent) | [None](https://docs.python.org/3/library/constants.html#None)*

Return the summary event, or None if no summary exists.

#### *static* filter_unmatched_tool_calls(events: [list](https://docs.python.org/3/library/stdtypes.html#list)[[LLMConvertibleEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[LLMConvertibleEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.LLMConvertibleEvent)]

Filter out unmatched tool call events.

Removes ActionEvents and ObservationEvents that have tool_call_ids
but don’t have matching pairs.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### *static* from_events(events: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)]) → [View](#openhands.sdk.context.view.View)

Create a view from a list of events, respecting the semantics of any
condensation events.
