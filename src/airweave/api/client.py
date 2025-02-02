# This file was auto-generated by Fern from our API Definition.

import typing

from backports.cached_property import cached_property

from .resources.api_keys.client import ApiKeysClient
from .resources.chat.client import ChatClient
from .resources.connections.client import ConnectionsClient
from .resources.destinations.client import DestinationsClient
from .resources.embedding_models.client import EmbeddingModelsClient
from .resources.health.client import HealthClient
from .resources.sources.client import SourcesClient
from .resources.sync.client import SyncClient
from .resources.users.client import UsersClient
from .resources.white_labels.client import WhiteLabelsClient


class AirweaveSDK:
    def __init__(self, *, environment: str, api_key: typing.Optional[str] = None):
        self._environment = environment
        self.api_key = api_key

    @cached_property
    def health(self) -> HealthClient:
        return HealthClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def api_keys(self) -> ApiKeysClient:
        return ApiKeysClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def users(self) -> UsersClient:
        return UsersClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def sources(self) -> SourcesClient:
        return SourcesClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def destinations(self) -> DestinationsClient:
        return DestinationsClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def embedding_models(self) -> EmbeddingModelsClient:
        return EmbeddingModelsClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def connections(self) -> ConnectionsClient:
        return ConnectionsClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def sync(self) -> SyncClient:
        return SyncClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def white_labels(self) -> WhiteLabelsClient:
        return WhiteLabelsClient(environment=self._environment, api_key=self.api_key)

    @cached_property
    def chat(self) -> ChatClient:
        return ChatClient(environment=self._environment, api_key=self.api_key)
