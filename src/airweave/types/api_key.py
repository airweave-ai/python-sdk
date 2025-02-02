# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ApiKey(UniversalBaseModel):
    """
    Schema for APIKey.
    """

    id: str
    key_prefix: str
    organization: typing.Optional[str] = None
    created_at: dt.datetime
    modified_at: dt.datetime
    last_used_date: typing.Optional[dt.datetime] = None
    expiration_date: dt.datetime
    created_by_email: str
    modified_by_email: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
