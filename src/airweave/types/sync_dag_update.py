# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .dag_node_create import DagNodeCreate
from .dag_edge_create import DagEdgeCreate
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SyncDagUpdate(UniversalBaseModel):
    """
    Schema for updating a sync DAG definition.
    """

    name: str
    description: typing.Optional[str] = None
    sync_id: str
    nodes: typing.Optional[typing.List[DagNodeCreate]] = None
    edges: typing.Optional[typing.List[DagEdgeCreate]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
