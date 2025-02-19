# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .sync_job_status import SyncJobStatus
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SyncJob(UniversalBaseModel):
    """
    Schema for SyncJob.
    """

    sync_id: str
    status: typing.Optional[SyncJobStatus] = None
    entities_detected: typing.Optional[int] = None
    entities_inserted: typing.Optional[int] = None
    entities_deleted: typing.Optional[int] = None
    entities_skipped: typing.Optional[int] = None
    error: typing.Optional[str] = None
    id: str
    organization_id: str
    created_by_email: str
    modified_by_email: str
    created_at: dt.datetime
    modified_at: dt.datetime
    started_at: typing.Optional[dt.datetime] = None
    completed_at: typing.Optional[dt.datetime] = None
    failed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
