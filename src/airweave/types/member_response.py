# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MemberResponse(UniversalBaseModel):
    """
    Schema for organization member responses.
    """

    id: str
    email: str
    name: str
    role: str
    status: typing.Optional[str] = None
    is_primary: typing.Optional[bool] = None
    auth_0_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auth0_id")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
