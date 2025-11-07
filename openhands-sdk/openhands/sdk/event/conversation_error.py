from pydantic import Field

from openhands.sdk.event.base import Event


class ConversationErrorEvent(Event):
    """
    Conversation-level failure that is NOT sent back to the LLM.

    This event is emitted by the conversation runtime when an unexpected
    exception bubbles up and prevents the run loop from continuing. It is
    intended for client applications (e.g., UIs) to present a top-level error
    state, and for orchestration to react. It is not an observation and it is
    not LLM-convertible.

    How this differs from AgentErrorEvent:
    - Scope: ConversationErrorEvent represents a top-level runtime failure
      (e.g., auth/transport errors, unhandled exceptions). AgentErrorEvent is a
      tool-response observation for a specific tool call.
    - LLM visibility: ConversationErrorEvent does not implement
      LLMConvertibleEvent and is never included in the model's message history.
      AgentErrorEvent is LLM-convertible and is sent to the model as a
      tool message so the model can react and recover.
    - Coupling: ConversationErrorEvent carries no tool_name/tool_call_id because
      it is not tied to any tool invocation. AgentErrorEvent is coupled to the
      originating ActionEvent via tool_call_id and includes tool_name.
    - Source and semantics: ConversationErrorEvent typically uses source=
      "environment" and is terminal for the current run; the conversation state
      is set to ERROR and run() raises ConversationRunError. AgentErrorEvent has
      source="agent", does not change execution_status, and the conversation can
      continue normally.
    - Application behavior: Client UIs should surface ConversationErrorEvent as
      a banner/notification for the whole conversation, not as a tool result in
      the transcript. AgentErrorEvent should appear inline next to the failed
      tool call so the model/user can adjust.
    """

    code: str = Field(description="Code for the error - typically a type")
    detail: str = Field(description="Details about the error")
