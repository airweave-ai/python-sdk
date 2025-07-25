# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payload_field import PayloadField


class IsEmptyCondition(UniversalBaseModel):
    """
    Select points with empty payload for a specified field
    """

    is_empty: PayloadField = pydantic.Field()
    """
    Select points with empty payload for a specified field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
