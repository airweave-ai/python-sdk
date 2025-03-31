# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import AirweaveSDKEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .users.client import UsersClient
from .sources.client import SourcesClient
from .destinations.client import DestinationsClient
from .embedding_models.client import EmbeddingModelsClient
from .connections.client import ConnectionsClient
from .sync.client import SyncClient
from .search.client import SearchClient
from .white_labels.client import WhiteLabelsClient
from .entities.client import EntitiesClient
from .transformers.client import TransformersClient
from .core.client_wrapper import AsyncClientWrapper
from .users.client import AsyncUsersClient
from .sources.client import AsyncSourcesClient
from .destinations.client import AsyncDestinationsClient
from .embedding_models.client import AsyncEmbeddingModelsClient
from .connections.client import AsyncConnectionsClient
from .sync.client import AsyncSyncClient
from .search.client import AsyncSearchClient
from .white_labels.client import AsyncWhiteLabelsClient
from .entities.client import AsyncEntitiesClient
from .transformers.client import AsyncTransformersClient


class AirweaveSDK:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : AirweaveSDKEnvironment
        The environment to use for requests from the client. from .environment import AirweaveSDKEnvironment



        Defaults to AirweaveSDKEnvironment.PRODUCTION



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from airweave import AirweaveSDK

    client = AirweaveSDK(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AirweaveSDKEnvironment = AirweaveSDKEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.users = UsersClient(client_wrapper=self._client_wrapper)
        self.sources = SourcesClient(client_wrapper=self._client_wrapper)
        self.destinations = DestinationsClient(client_wrapper=self._client_wrapper)
        self.embedding_models = EmbeddingModelsClient(client_wrapper=self._client_wrapper)
        self.connections = ConnectionsClient(client_wrapper=self._client_wrapper)
        self.sync = SyncClient(client_wrapper=self._client_wrapper)
        self.search = SearchClient(client_wrapper=self._client_wrapper)
        self.white_labels = WhiteLabelsClient(client_wrapper=self._client_wrapper)
        self.entities = EntitiesClient(client_wrapper=self._client_wrapper)
        self.transformers = TransformersClient(client_wrapper=self._client_wrapper)


class AsyncAirweaveSDK:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : AirweaveSDKEnvironment
        The environment to use for requests from the client. from .environment import AirweaveSDKEnvironment



        Defaults to AirweaveSDKEnvironment.PRODUCTION



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from airweave import AsyncAirweaveSDK

    client = AsyncAirweaveSDK(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AirweaveSDKEnvironment = AirweaveSDKEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        self.sources = AsyncSourcesClient(client_wrapper=self._client_wrapper)
        self.destinations = AsyncDestinationsClient(client_wrapper=self._client_wrapper)
        self.embedding_models = AsyncEmbeddingModelsClient(client_wrapper=self._client_wrapper)
        self.connections = AsyncConnectionsClient(client_wrapper=self._client_wrapper)
        self.sync = AsyncSyncClient(client_wrapper=self._client_wrapper)
        self.search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        self.white_labels = AsyncWhiteLabelsClient(client_wrapper=self._client_wrapper)
        self.entities = AsyncEntitiesClient(client_wrapper=self._client_wrapper)
        self.transformers = AsyncTransformersClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: AirweaveSDKEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
