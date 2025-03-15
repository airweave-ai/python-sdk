# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .auth_type import AuthType
import datetime as dt
from .fields import Fields
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SourceWithConfigFields(UniversalBaseModel):
    """
    Schema for Source with auth config.
    """

    name: str
    description: typing.Optional[str] = None
    auth_type: typing.Optional[AuthType] = None
    auth_config_class: typing.Optional[str] = None
    short_name: str
    class_name: str
    output_entity_definition_ids: typing.Optional[typing.List[str]] = None
    organization_id: typing.Optional[str] = None
    config_schema: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    labels: typing.Optional[typing.List[str]] = None
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
