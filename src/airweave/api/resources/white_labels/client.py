# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.connection import Connection
from ...types.http_validation_error import HTTPValidationError
from ...types.sync import Sync
from ...types.white_label import WhiteLabel


class WhiteLabelsClient:
    def __init__(self, *, environment: str, api_key: typing.Optional[str] = None):
        self._environment = environment
        self.api_key = api_key

    def list_white_labels(self) -> typing.List[WhiteLabel]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "white_labels/list"),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[WhiteLabel], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_white_label(
        self, *, name: str, source_id: str, redirect_url: str, client_id: str, client_secret: str
    ) -> WhiteLabel:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "white_labels/"),
            json=jsonable_encoder(
                {
                    "name": name,
                    "source_id": source_id,
                    "redirect_url": redirect_url,
                    "client_id": client_id,
                    "client_secret": client_secret,
                }
            ),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WhiteLabel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_white_label(self, white_label_id: str) -> WhiteLabel:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"white_labels/{white_label_id}"),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WhiteLabel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_white_label(
        self,
        white_label_id: str,
        *,
        name: typing.Optional[str] = None,
        redirect_url: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
    ) -> WhiteLabel:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment}/", f"white_labels/{white_label_id}"),
            json=jsonable_encoder(
                {"name": name, "redirect_url": redirect_url, "client_id": client_id, "client_secret": client_secret}
            ),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WhiteLabel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_white_label(self, white_label_id: str) -> WhiteLabel:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment}/", f"white_labels/{white_label_id}"),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(WhiteLabel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_white_label_oauth_2_auth_url(self, white_label_id: str) -> str:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"white_labels/{white_label_id}/oauth2/auth_url"),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def exchange_white_label_oauth_2_code(self, white_label_id: str, *, request: str) -> Connection:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", f"white_labels/{white_label_id}/oauth2/code"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Connection, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_white_label_syncs(self, white_label_id: str) -> typing.List[Sync]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"white_labels/{white_label_id}/syncs"),
            headers=remove_none_from_headers({"x-api-key": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Sync], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HTTPValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
