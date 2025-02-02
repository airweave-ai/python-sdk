# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class WhiteLabel(UniversalBaseModel):
    """
    Schema for WhiteLabel.
    """

    name: str
    source_id: str
    redirect_url: str
    client_id: str
    client_secret: str
    id: str
    organization_id: str
    created_at: dt.datetime
    modified_at: dt.datetime
    created_by_email: str
    modified_by_email: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
