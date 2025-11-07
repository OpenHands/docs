from pydantic import Field

from openhands.sdk.event.base import Event


class ConversationErrorEvent(Event):
    code: str = Field(description="Code for the error - typically a type")
    detail: str = Field(description="Details about the error")
