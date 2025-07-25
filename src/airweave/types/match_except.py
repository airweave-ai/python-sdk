# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .except_ import Except


class MatchExcept(UniversalBaseModel):
    """
    Should have at least one value not matching the any given values
    """

    except_: typing_extensions.Annotated[Except, FieldMetadata(alias="except")] = pydantic.Field()
    """
    Should have at least one value not matching the any given values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
