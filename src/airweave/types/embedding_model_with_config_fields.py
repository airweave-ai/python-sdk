# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .auth_type import AuthType
import datetime as dt
from .fields import Fields
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class EmbeddingModelWithConfigFields(UniversalBaseModel):
    """
    Schema for EmbeddingModel with auth config.
    """

    name: str
    short_name: str
    description: typing.Optional[str] = None
    provider: str
    model_name: typing.Optional[str] = None
    model_version: typing.Optional[str] = None
    auth_type: typing.Optional[AuthType] = None
    auth_config_class: typing.Optional[str] = None
    id: str
    created_at: dt.datetime
    modified_at: dt.datetime
    config_fields: typing.Optional[Fields] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
