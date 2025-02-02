# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .auth_type import AuthType
from .fields import Fields


class EmbeddingModelWithConfigFields(pydantic.BaseModel):
    """
    Schema for EmbeddingModel with auth config.
    """

    name: str
    short_name: str
    description: typing.Optional[str]
    provider: str
    model_name: typing.Optional[str]
    model_version: typing.Optional[str]
    auth_type: typing.Optional[AuthType]
    auth_config_class: typing.Optional[str]
    id: str
    created_at: dt.datetime
    modified_at: dt.datetime
    config_fields: typing.Optional[Fields]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
