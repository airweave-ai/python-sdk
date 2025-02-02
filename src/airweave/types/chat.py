# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .chat_message import ChatMessage
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Chat(UniversalBaseModel):
    """
    Schema for chat responses.
    """

    name: str
    sync_id: str
    description: typing.Optional[str] = None
    model_name: typing.Optional[str] = None
    model_settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    search_settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    id: str
    messages: typing.Optional[typing.List[ChatMessage]] = None
    created_at: dt.datetime
    modified_at: dt.datetime
    created_by_email: str
    modified_by_email: str
    organization_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
