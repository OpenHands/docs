---
title: openhands.sdk.conversation.state
description: API reference for openhands.sdk.conversation.state
---

# openhands.sdk.conversation.state module

<a id="module-openhands.sdk.conversation.state"></a>

### *class* openhands.sdk.conversation.state.AgentExecutionStatus(\*values)

Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Enum representing the current execution state of the agent.

#### IDLE *= 'idle'*

#### RUNNING *= 'running'*

#### PAUSED *= 'paused'*

#### WAITING_FOR_CONFIRMATION *= 'waiting_for_confirmation'*

#### FINISHED *= 'finished'*

#### ERROR *= 'error'*

#### STUCK *= 'stuck'*

### *class* openhands.sdk.conversation.state.ConversationState(\*, id: uuid.UUID, agent: openhands.sdk.agent.base.AgentBase, workspace: openhands.sdk.workspace.base.BaseWorkspace, persistence_dir: str | None = 'workspace/conversations', max_iterations: typing.Annotated[int, annotated_types.Gt(gt=0)] = 500, stuck_detection: bool = True, agent_status: openhands.sdk.conversation.state.AgentExecutionStatus = AgentExecutionStatus.IDLE, confirmation_policy: openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase = NeverConfirm(kind='NeverConfirm'), activated_knowledge_skills: list[str] = `<factory>`, stats: openhands.sdk.conversation.conversation_stats.ConversationStats = `<factory>`, secret_registry: openhands.sdk.conversation.secret_registry.SecretRegistry = `<factory>`)

Bases: [`OpenHandsModel`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.OpenHandsModel)

#### id *: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID)*

#### agent *: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase)*

#### workspace *: [BaseWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace)*

#### persistence_dir *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### max_iterations *: [int](https://docs.python.org/3/library/functions.html#int)*

#### stuck_detection *: [bool](https://docs.python.org/3/library/functions.html#bool)*

#### agent_status *: [AgentExecutionStatus](#openhands.sdk.conversation.state.AgentExecutionStatus)*

#### confirmation_policy *: [ConfirmationPolicyBase](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)*

#### activated_knowledge_skills *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### stats *: [ConversationStats](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.conversation_stats.md#openhands.sdk.conversation.conversation_stats.ConversationStats)*

#### secret_registry *: [SecretRegistry](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.secret_registry.md#openhands.sdk.conversation.secret_registry.SecretRegistry)*

#### *property* events *: [EventLog](https://github.com/OpenHands/software-agent-sdk/sdk.conversation.event_store.md#openhands.sdk.conversation.event_store.EventLog)*

#### set_on_state_change(callback: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)], [None](https://docs.python.org/3/library/constants.html#None)] | [None](https://docs.python.org/3/library/constants.html#None)) → [None](https://docs.python.org/3/library/constants.html#None)

Set a callback to be called when state changes.

* **Parameters:**
  **callback** – A function that takes an Event (ConversationStateUpdateEvent)
  or None to remove the callback

#### *classmethod* create(id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID), agent: [AgentBase](https://github.com/OpenHands/software-agent-sdk/sdk.agent.base.md#openhands.sdk.agent.base.AgentBase), workspace: [BaseWorkspace](https://github.com/OpenHands/software-agent-sdk/sdk.workspace.base.md#openhands.sdk.workspace.base.BaseWorkspace), persistence_dir: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None, max_iterations: [int](https://docs.python.org/3/library/functions.html#int) = 500, stuck_detection: [bool](https://docs.python.org/3/library/functions.html#bool) = True) → [ConversationState](#openhands.sdk.conversation.state.ConversationState)

If base_state.json exists: resume (attach EventLog,
: reconcile agent, enforce id).

Else: create fresh (agent required), persist base, and return.

#### *static* get_unmatched_actions(events: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[ActionEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent)]

Find actions in the event history that don’t have matching observations.

This method identifies ActionEvents that don’t have corresponding
ObservationEvents or UserRejectObservations, which typically indicates
actions that are pending confirmation or execution.

* **Parameters:**
  **events** – List of events to search through
* **Returns:**
  List of ActionEvent objects that don’t have corresponding observations,
  in chronological order

#### acquire(blocking: [bool](https://docs.python.org/3/library/functions.html#bool) = True, timeout: [float](https://docs.python.org/3/library/functions.html#float) = -1) → [bool](https://docs.python.org/3/library/functions.html#bool)

Acquire the lock.

* **Parameters:**
  * **blocking** – If True, block until lock is acquired. If False, return
    immediately.
  * **timeout** – Maximum time to wait for lock (ignored if blocking=False).
    -1 means wait indefinitely.
* **Returns:**
  True if lock was acquired, False otherwise.

#### release() → [None](https://docs.python.org/3/library/constants.html#None)

Release the lock.

* **Raises:**
  [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) – If the current thread doesn’t own the lock.

#### \_\_enter_\_() → [Self](https://docs.python.org/3/library/typing.html#typing.Self)

Context manager entry.

#### \_\_exit_\_(exc_type: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_val: [Any](https://docs.python.org/3/library/typing.html#typing.Any), exc_tb: [Any](https://docs.python.org/3/library/typing.html#typing.Any)) → [None](https://docs.python.org/3/library/constants.html#None)

Context manager exit.

#### locked() → [bool](https://docs.python.org/3/library/functions.html#bool)

Return True if the lock is currently held by any thread.

#### owned() → [bool](https://docs.python.org/3/library/functions.html#bool)

Return True if the lock is currently held by the calling thread.

#### model_config  : ClassVar[ConfigDict]*  = \{\}*

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### model_post_init(\_context)

Override this method to perform additional initialization after \_\_init_\_ and model_construct.
This is useful if you want to do some validation that requires the entire model to be initialized.
