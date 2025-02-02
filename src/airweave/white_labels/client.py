# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.white_label import WhiteLabel
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.jsonable_encoder import jsonable_encoder
from ..types.connection import Connection
from ..types.sync import Sync
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WhiteLabelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_white_labels(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[WhiteLabel]:
        """
        List all white labels for the current user's organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhiteLabel]
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.list_white_labels()
        """
        _response = self._client_wrapper.httpx_client.request(
            "white_labels/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[WhiteLabel],
                    parse_obj_as(
                        type_=typing.List[WhiteLabel],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_white_label(
        self,
        *,
        name: str,
        source_id: str,
        redirect_url: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhiteLabel:
        """
        Create new white label integration.

        Parameters
        ----------
        name : str

        source_id : str

        redirect_url : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.create_white_label(
            name="name",
            source_id="source_id",
            redirect_url="redirect_url",
            client_id="client_id",
            client_secret="client_secret",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "white_labels/",
            method="POST",
            json={
                "name": name,
                "source_id": source_id,
                "redirect_url": redirect_url,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_white_label(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhiteLabel:
        """
        Get a specific white label integration.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.get_white_label(
            white_label_id="white_label_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_white_label(
        self,
        white_label_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhiteLabel:
        """
        Update a white label integration.

        Parameters
        ----------
        white_label_id : str

        name : typing.Optional[str]

        redirect_url : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.update_white_label(
            white_label_id="white_label_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}",
            method="PUT",
            json={
                "name": name,
                "redirect_url": redirect_url,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_white_label(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhiteLabel:
        """
        Delete a white label integration.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.delete_white_label(
            white_label_id="white_label_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_white_label_oauth_2_auth_url(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Generate the OAuth2 authorization URL by delegating to oauth2_service.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.get_white_label_oauth_2_auth_url(
            white_label_id="white_label_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}/oauth2/auth_url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def exchange_white_label_oauth_2_code(
        self, white_label_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Connection:
        """
        Exchange OAuth2 code for tokens and create connection.

        Parameters
        ----------
        white_label_id : str

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.exchange_white_label_oauth_2_code(
            white_label_id="white_label_id",
            request="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}/oauth2/code",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Connection,
                    parse_obj_as(
                        type_=Connection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_white_label_syncs(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Sync]:
        """
        List all syncs for a specific white label.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Sync]
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.white_labels.list_white_label_syncs(
            white_label_id="white_label_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}/syncs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Sync],
                    parse_obj_as(
                        type_=typing.List[Sync],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWhiteLabelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_white_labels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhiteLabel]:
        """
        List all white labels for the current user's organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhiteLabel]
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.list_white_labels()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "white_labels/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[WhiteLabel],
                    parse_obj_as(
                        type_=typing.List[WhiteLabel],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_white_label(
        self,
        *,
        name: str,
        source_id: str,
        redirect_url: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhiteLabel:
        """
        Create new white label integration.

        Parameters
        ----------
        name : str

        source_id : str

        redirect_url : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.create_white_label(
                name="name",
                source_id="source_id",
                redirect_url="redirect_url",
                client_id="client_id",
                client_secret="client_secret",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "white_labels/",
            method="POST",
            json={
                "name": name,
                "source_id": source_id,
                "redirect_url": redirect_url,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_white_label(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhiteLabel:
        """
        Get a specific white label integration.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.get_white_label(
                white_label_id="white_label_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_white_label(
        self,
        white_label_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhiteLabel:
        """
        Update a white label integration.

        Parameters
        ----------
        white_label_id : str

        name : typing.Optional[str]

        redirect_url : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.update_white_label(
                white_label_id="white_label_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}",
            method="PUT",
            json={
                "name": name,
                "redirect_url": redirect_url,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_white_label(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhiteLabel:
        """
        Delete a white label integration.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhiteLabel
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.delete_white_label(
                white_label_id="white_label_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WhiteLabel,
                    parse_obj_as(
                        type_=WhiteLabel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_white_label_oauth_2_auth_url(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Generate the OAuth2 authorization URL by delegating to oauth2_service.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.get_white_label_oauth_2_auth_url(
                white_label_id="white_label_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}/oauth2/auth_url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def exchange_white_label_oauth_2_code(
        self, white_label_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Connection:
        """
        Exchange OAuth2 code for tokens and create connection.

        Parameters
        ----------
        white_label_id : str

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.exchange_white_label_oauth_2_code(
                white_label_id="white_label_id",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}/oauth2/code",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Connection,
                    parse_obj_as(
                        type_=Connection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_white_label_syncs(
        self, white_label_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Sync]:
        """
        List all syncs for a specific white label.

        Parameters
        ----------
        white_label_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Sync]
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.white_labels.list_white_label_syncs(
                white_label_id="white_label_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"white_labels/{jsonable_encoder(white_label_id)}/syncs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Sync],
                    parse_obj_as(
                        type_=typing.List[Sync],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
