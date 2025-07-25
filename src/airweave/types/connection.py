# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connection_status import ConnectionStatus
from .integration_type import IntegrationType


class Connection(UniversalBaseModel):
    """
    Schema for connection with config fields.
    """

    name: str = pydantic.Field()
    """
    Human-readable display name for the connection.
    """

    readable_id: str = pydantic.Field()
    """
    URL-safe unique identifier used in API endpoints. This becomes non-optional once the connection is created.
    """

    description: typing.Optional[str] = None
    integration_type: IntegrationType
    integration_credential_id: typing.Optional[str] = None
    status: ConnectionStatus
    short_name: str
    id: str = pydantic.Field()
    """
    Unique system identifier for the connection.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp when the connection was created (ISO 8601 format).
    """

    modified_at: dt.datetime = pydantic.Field()
    """
    Timestamp when the connection was last modified (ISO 8601 format).
    """

    organization_id: typing.Optional[str] = None
    created_by_email: typing.Optional[str] = None
    modified_by_email: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
