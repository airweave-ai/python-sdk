# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auth_type import AuthType
from .fields import Fields


class EmbeddingModelWithAuthenticationFields(UniversalBaseModel):
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
    auth_fields: typing.Optional[Fields] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
