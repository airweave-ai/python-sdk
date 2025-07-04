# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.source import Source
from .raw_client import AsyncRawSourcesClient, RawSourcesClient


class SourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourcesClient
        """
        return self._raw_client

    def read_source(self, short_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Source:
        """
        Get source by id.

        Args:
        ----
            db (AsyncSession): The database session.
            short_name (str): The short name of the source.
            auth_context (schemas.AuthContext): The current auth context.

        Returns:
        -------
            schemas.Source: The source object.

        Raises:
            HTTPException:
                - 404 if source not found
                - 400 if source missing required configuration classes
                - 500 if there's an error retrieving auth configuration

        Parameters
        ----------
        short_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            organization_id="YOUR_ORGANIZATION_ID",
        )
        client.sources.read_source(
            short_name="short_name",
        )
        """
        _response = self._raw_client.read_source(short_name, request_options=request_options)
        return _response.data

    def read_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Source]:
        """
        Get all sources with their authentication fields.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]
            Successful Response

        Examples
        --------
        from airweave import AirweaveSDK

        client = AirweaveSDK(
            api_key="YOUR_API_KEY",
            organization_id="YOUR_ORGANIZATION_ID",
        )
        client.sources.read_sources()
        """
        _response = self._raw_client.read_sources(request_options=request_options)
        return _response.data


class AsyncSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourcesClient
        """
        return self._raw_client

    async def read_source(self, short_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Source:
        """
        Get source by id.

        Args:
        ----
            db (AsyncSession): The database session.
            short_name (str): The short name of the source.
            auth_context (schemas.AuthContext): The current auth context.

        Returns:
        -------
            schemas.Source: The source object.

        Raises:
            HTTPException:
                - 404 if source not found
                - 400 if source missing required configuration classes
                - 500 if there's an error retrieving auth configuration

        Parameters
        ----------
        short_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            organization_id="YOUR_ORGANIZATION_ID",
        )


        async def main() -> None:
            await client.sources.read_source(
                short_name="short_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_source(short_name, request_options=request_options)
        return _response.data

    async def read_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Source]:
        """
        Get all sources with their authentication fields.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]
            Successful Response

        Examples
        --------
        import asyncio

        from airweave import AsyncAirweaveSDK

        client = AsyncAirweaveSDK(
            api_key="YOUR_API_KEY",
            organization_id="YOUR_ORGANIZATION_ID",
        )


        async def main() -> None:
            await client.sources.read_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_sources(request_options=request_options)
        return _response.data
