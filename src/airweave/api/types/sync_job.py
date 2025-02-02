# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .sync_job_status import SyncJobStatus


class SyncJob(pydantic.BaseModel):
    """
    Schema for SyncJob.
    """

    sync_id: str
    status: typing.Optional[SyncJobStatus]
    chunks_detected: typing.Optional[int]
    chunks_inserted: typing.Optional[int]
    chunks_deleted: typing.Optional[int]
    chunks_skipped: typing.Optional[int]
    error: typing.Optional[str]
    id: str
    organization_id: str
    created_by_email: str
    modified_by_email: str
    created_at: dt.datetime
    modified_at: dt.datetime
    started_at: typing.Optional[dt.datetime]
    completed_at: typing.Optional[dt.datetime]
    failed_at: typing.Optional[dt.datetime]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
