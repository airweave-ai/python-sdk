# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApiKey(UniversalBaseModel):
    """
    Schema for API keys returned to clients - includes decrypted key.
    """

    id: str
    organization: str
    created_at: dt.datetime
    modified_at: dt.datetime
    last_used_date: typing.Optional[dt.datetime] = None
    expiration_date: dt.datetime
    created_by_email: typing.Optional[str] = None
    modified_by_email: typing.Optional[str] = None
    decrypted_key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
