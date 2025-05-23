# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .response_type import ResponseType
from .search_status import SearchStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SearchResponse(UniversalBaseModel):
    """
    Schema for search response.
    """

    results: typing.List[typing.Dict[str, typing.Optional[typing.Any]]]
    response_type: ResponseType
    completion: typing.Optional[str] = None
    status: SearchStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
