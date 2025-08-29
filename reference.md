# Reference
## sources
<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">read_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed information about a specific data source connector.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.sources.read_source(
    short_name="short_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**short_name:** `str` — Technical identifier of the source type (e.g., 'github', 'stripe', 'slack')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">read_sources</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all available data source connectors.

<br/><br/>
Returns the complete catalog of source types that Airweave can connect to.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.sources.read_sources()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## collections
<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">list_collections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all collections that belong to your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.list_collections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of collections to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of collections to return (1-1000)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">create_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new collection.

The newly created collection is initially empty and does not contain any data
until you explicitly add source connections to it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.create_collection(
    name="Finance Data",
    readable_id="finance-data-reports",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable display name for the collection. This appears in the UI and should clearly describe the data contained within (e.g., 'Finance Data').
    
</dd>
</dl>

<dl>
<dd>

**readable_id:** `typing.Optional[str]` — URL-safe unique identifier used in API endpoints. Must contain only lowercase letters, numbers, and hyphens. If not provided, it will be automatically generated from the collection name with a random suffix for uniqueness (e.g., 'finance-data-ab123').
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">get_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific collection by its readable ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.get_collection(
    readable_id="readable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**readable_id:** `str` — The unique readable identifier of the collection (e.g., 'finance-data-ab123')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">update_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a collection's properties.

Modifies the display name of an existing collection.
Note that the readable ID cannot be changed after creation to maintain stable
API endpoints and preserve any existing integrations or bookmarks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.update_collection(
    readable_id="readable_id",
    name="Updated Finance Data",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**readable_id:** `str` — The unique readable identifier of the collection to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated display name for the collection. Must be between 4 and 64 characters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">delete_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a collection and all associated data.

Permanently removes a collection from your organization including all synced data
from the destination systems. All source connections within this collection
will also be deleted as part of the cleanup process. This action cannot be undone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.delete_collection(
    readable_id="readable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**readable_id:** `str` — The unique readable identifier of the collection to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">search_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search across all data sources within the specified collection.

This GET endpoint provides basic search functionality. For advanced filtering
and options, use the POST /search endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.search_collection(
    readable_id="readable_id",
    query="customer payment issues",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**readable_id:** `str` — The unique readable identifier of the collection to search
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query text to find relevant documents and data
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `typing.Optional[ResponseType]` — Format of the response: 'raw' returns search results, 'completion' returns AI-generated answers
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**recency_bias:** `typing.Optional[float]` — How much to weigh recency vs similarity (0..1). 0 = no recency effect; 1 = rank by recency only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">search_collection_advanced</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Advanced search with comprehensive filtering and options.

This endpoint supports:
- Metadata filtering using Qdrant's native filter syntax
- Pagination with offset and limit
- Score threshold filtering
- Query expansion strategies (default: AUTO, generates up to 4 variations)
- Automatic filter extraction from natural language (default: ON)
- LLM-based result reranking (default: ON)

Default behavior:
- Query expansion: ON (AUTO strategy)
- Query interpretation: ON (extracts filters from natural language)
- Reranking: ON (improves relevance using LLM)
- Score threshold: None (no filtering)

To disable features, explicitly set:
- enable_reranking: false
- enable_query_interpretation: false
- expansion_strategy: "no_expansion"
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK, FieldCondition, Filter

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.search_collection_advanced(
    readable_id="readable_id",
    query="customer payment issues",
    filter=Filter(
        must=FieldCondition(
            key="key",
        ),
    ),
    limit=10,
    score_threshold=0.7,
    response_type="completion",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**readable_id:** `str` — The unique readable identifier of the collection to search
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query text
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` — Qdrant native filter for metadata-based filtering
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip (DEFAULT: 0)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return (DEFAULT: 20)
    
</dd>
</dl>

<dl>
<dd>

**score_threshold:** `typing.Optional[float]` — Minimum similarity score threshold (DEFAULT: None - no filtering)
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `typing.Optional[ResponseType]` — Type of response - 'raw' or 'completion' (DEFAULT: 'raw')
    
</dd>
</dl>

<dl>
<dd>

**search_method:** `typing.Optional[SearchRequestSearchMethod]` — Search method to use (DEFAULT: 'hybrid' - combines neural + BM25)
    
</dd>
</dl>

<dl>
<dd>

**recency_bias:** `typing.Optional[float]` — How much document age penalizes the similarity score (0..1). 0 = no age penalty (pure similarity); 0.5 = old docs lose up to 50% of their score; 1 = old docs get zero score (pure recency). Applied as: score × (1 - bias + bias × age_factor). Works within top ~10,000 semantic matches. DEFAULT: 0.3
    
</dd>
</dl>

<dl>
<dd>

**expansion_strategy:** `typing.Optional[QueryExpansionStrategy]` — Query expansion strategy (DEFAULT: 'auto' - generates up to 4 query variations). Options: 'auto', 'llm', 'no_expansion'
    
</dd>
</dl>

<dl>
<dd>

**enable_reranking:** `typing.Optional[bool]` — Enable LLM-based reranking to improve result relevance (DEFAULT: True - enabled, set to False to disable)
    
</dd>
</dl>

<dl>
<dd>

**enable_query_interpretation:** `typing.Optional[bool]` — Enable automatic filter extraction from natural language query (DEFAULT: True - enabled, set to False to disable)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">refresh_all_source_connections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger data synchronization for all source connections in the collection.

The sync jobs run asynchronously in the background, so this endpoint
returns immediately with job details that you can use to track progress. You can
monitor the status of individual data synchronization using the source connection
endpoints.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.refresh_all_source_connections(
    readable_id="readable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**readable_id:** `str` — The unique readable identifier of the collection to refresh
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## source-connections
<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">list_source_connections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List source connections across your organization.

By default, returns ALL source connections from every collection in your
organization. Use the 'collection' parameter to filter results to a specific
collection. This is useful for getting an overview of all your data sources
or managing connections within a particular collection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.list_source_connections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection:** `typing.Optional[str]` — Filter source connections by collection readable ID
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of source connections to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of source connections to return (1-1000)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">create_source_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new source connection to sync data into your collection.

**This endpoint only works for sources that do not use OAuth2.0.**
Sources that do use OAuth2.0 like Google Drive, Slack, or HubSpot must be
connected through the UI where you can complete the OAuth consent flow
or using Auth Providers (see [Auth Providers](/docs/auth-providers)).<br/><br/>

Credentials for a source have to be provided using the `auth_fields` field.
Currently, it is not automatically checked if the provided credentials are valid.
If they are not valid, the data synchronization will fail.<br/><br/>

Check the documentation of a specific source (for example
[Github](https://docs.airweave.ai/docs/connectors/github)) to see what kind
of authentication is used.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.create_source_connection(
    name="Production Stripe Account",
    short_name="stripe",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable name for the source connection. This helps you identify the connection in the UI and should clearly describe what data it connects to.
    
</dd>
</dl>

<dl>
<dd>

**short_name:** `str` — Technical identifier of the source type that determines which connector to use for data synchronization.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional detailed description of what this source connection provides. Use this to document the purpose, data types, or any special considerations for this connection.
    
</dd>
</dl>

<dl>
<dd>

**config_fields:** `typing.Optional[ConfigValues]` — Source-specific configuration parameters required for data extraction. These vary by source type and control how data is retrieved (e.g., database queries, API filters, file paths). Check the documentation of a specific source (for example [Github](https://docs.airweave.ai/docs/connectors/github)) to see what is required.
    
</dd>
</dl>

<dl>
<dd>

**collection:** `typing.Optional[str]` — Readable ID of the collection where synced data will be stored. If not provided, a new collection will be automatically created.
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `typing.Optional[str]` — Cron expression for automatic data synchronization schedule. If not provided, data will only sync when manually triggered. Use standard cron format: minute hour day month weekday.
    
</dd>
</dl>

<dl>
<dd>

**auth_fields:** `typing.Optional[ConfigValues]` — Authentication credentials required to access the data source. The required fields vary by source type. Check the documentation of a specific source (for example [Github](https://docs.airweave.ai/docs/connectors/github)) to see what is required.
    
</dd>
</dl>

<dl>
<dd>

**auth_provider:** `typing.Optional[str]` — Unique readable ID of a connected auth provider to use for authentication instead of providing auth_fields directly. When specified, credentials for the source will be obtained and refreshed automatically by Airweave interaction with the auth provider. To see which auth providers are supported and learn more about how to use them, check [this page](https://docs.airweave.ai/docs/auth-providers).
    
</dd>
</dl>

<dl>
<dd>

**auth_provider_config:** `typing.Optional[ConfigValues]` — Configuration for the auth provider when using auth_provider field. Required fields vary by auth provider. For Composio, use auth_config_id and  account_id to specify which integration and account from Composio you want to use to connect to the source.
    
</dd>
</dl>

<dl>
<dd>

**sync_immediately:** `typing.Optional[bool]` — Whether to start an initial data synchronization immediately after creating the connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">get_source_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific source connection by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.get_source_connection(
    source_connection_id="source_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_connection_id:** `str` — The unique identifier of the source connection
    
</dd>
</dl>

<dl>
<dd>

**show_auth_fields:** `typing.Optional[bool]` — Whether to reveal authentication credentials.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">update_source_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a source connection's properties.

Modify the configuration of an existing source connection including its name,
authentication credentials, configuration fields, sync schedule, or source-specific settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.update_source_connection(
    source_connection_id="source_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_connection_id:** `str` — The unique identifier of the source connection to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated name for the source connection. Must be between 4 and 42 characters.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Updated description of what this source connection provides.
    
</dd>
</dl>

<dl>
<dd>

**auth_fields:** `typing.Optional[SourceConnectionUpdateAuthFields]` — Updated authentication credentials for the data source. Provide new credentials to refresh or update authentication.
    
</dd>
</dl>

<dl>
<dd>

**config_fields:** `typing.Optional[ConfigValues]` — Source-specific configuration parameters required for data extraction. These vary by source type and control how data is retrieved (e.g., database queries, API filters, file paths). Check the documentation of a specific source (for example [Github](https://docs.airweave.ai/docs/connectors/github)) to see what is required.
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `typing.Optional[str]` — Updated cron expression for automatic synchronization schedule. Set to null to disable automatic syncing.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — Internal connection identifier. This is typically managed automatically and should not be modified manually.
    
</dd>
</dl>

<dl>
<dd>

**white_label_id:** `typing.Optional[str]` — ID of the white label integration. Used for custom OAuth integrations with your own branding.
    
</dd>
</dl>

<dl>
<dd>

**auth_provider:** `typing.Optional[str]` — Updated auth provider readable ID. Only relevant if the connection uses an auth provider.
    
</dd>
</dl>

<dl>
<dd>

**auth_provider_config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Updated configuration for the auth provider. Only relevant if the connection uses an auth provider.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">delete_source_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a source connection and all associated data.

Permanently removes the source connection configuration and credentials.
By default, previously synced data remains in your destination systems for continuity.
Use delete_data=true to also remove all associated data from destination systems.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.delete_source_connection(
    source_connection_id="source_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_connection_id:** `str` — The unique identifier of the source connection to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">run_source_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually trigger a data sync for this source connection.

Starts an immediate synchronization job that extracts fresh data from your source,
transforms it according to your configuration, and updates the destination systems.
The job runs asynchronously and endpoint returns immediately with tracking information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.run_source_connection(
    source_connection_id="source_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_connection_id:** `str` — The unique identifier of the source connection to sync
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — This parameter gives you the ability to start a sync job with an access token for an OAuth2.0 source directly instead of using the credentials that Airweave has stored for you. Learn more about direct token injection [here](https://docs.airweave.ai/direct-token-injection).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">list_source_connection_jobs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all sync jobs for a source connection.

Returns the complete history of data synchronization jobs including successful syncs,
failed attempts, and currently running operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.list_source_connection_jobs(
    source_connection_id="source_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_connection_id:** `str` — The unique identifier of the source connection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">get_source_connection_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed information about a specific sync job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.get_source_connection_job(
    source_connection_id="source_connection_id",
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_connection_id:** `str` — The unique identifier of the source connection
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — The unique identifier of the sync job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">cancel_source_connection_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a running sync job.

Sends a cancellation signal to stop an in-progress data synchronization.
The job will complete its current operation and then terminate gracefully.
Only jobs in 'created', 'pending', or 'in_progress' states can be cancelled.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.cancel_source_connection_job(
    source_connection_id="source_connection_id",
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_connection_id:** `str` — The unique identifier of the source connection
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — The unique identifier of the sync job to cancel
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## white-labels
<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">list_white_labels</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all white label integrations for your organization.

<br/><br/>
Returns all custom OAuth integrations configured with your own branding and
credentials. These integrations allow you to present OAuth consent screens with
your company name instead of Airweave.<br/><br/>**White label integrations only
work with OAuth2.0 sources** like Slack, Google Drive, or HubSpot that require
OAuth consent flows.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.list_white_labels()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">create_white_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new white label integration.

<br/><br/>
**This only works for sources that use OAuth2.0 authentication** like Slack,
Google Drive, GitHub, or HubSpot.<br/><br/>Sets up a custom OAuth integration
using your own OAuth application credentials and branding. Once created,
customers will see your company name during OAuth consent flows instead of
Airweave. This requires you to have already configured your own OAuth
application with the target service provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.create_white_label(
    name="Customer Portal Slack Integration",
    source_short_name="slack",
    redirect_url="https://yourapp.com/auth/slack/callback",
    client_id="1234567890.1234567890123",
    client_secret="abcdefghijklmnopqrstuvwxyz123456",
    allowed_origins="https://yourapp.com,https://app.yourapp.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable name for the white label integration. This helps you identify the integration in the UI and should clearly describe its purpose (e.g., 'Customer Portal Slack Integration', 'Enterprise Google Drive Access').
    
</dd>
</dl>

<dl>
<dd>

**source_short_name:** `str` — Technical identifier of the source type that this integration supports (e.g., 'slack', 'google_drive', 'github'). This determines which service provider the OAuth integration connects to.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `str` — OAuth2 callback URL where users are redirected after completing authentication. This must be a valid HTTPS URL that your application can handle to receive the authorization code.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — OAuth2 client identifier provided by the service provider. This identifies your application during the OAuth consent flow and must match the client ID configured in the service provider's developer console.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — OAuth2 client secret from your registered application. This is used to securely authenticate your application when exchanging authorization codes for access tokens. Keep this value secure and never expose it in client-side code.
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `str` — Comma-separated list of allowed domains for OAuth flows and CORS. This prevents unauthorized websites from using your OAuth credentials and should include all domains where your application is hosted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">get_white_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific white label integration by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.get_white_label(
    white_label_id="white_label_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**white_label_id:** `str` — The unique identifier of the white label integration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">update_white_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a white label integration's configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.update_white_label(
    white_label_id="white_label_id",
    name="Updated Customer Portal Integration",
    redirect_url="https://v2.yourapp.com/auth/slack/callback",
    allowed_origins="https://v2.yourapp.com,https://api.yourapp.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**white_label_id:** `str` — The unique identifier of the white label integration to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated name for the white label integration.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — Updated OAuth callback URL. Must be a valid HTTPS URL that matches your OAuth application configuration.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Updated OAuth2 client ID. Must match the client ID in your service provider's developer console.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — Updated OAuth2 client secret. This will replace the existing secret and affect all future OAuth flows.
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[str]` — Updated comma-separated list of allowed domains for OAuth flows.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">delete_white_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a white label integration.

<br/><br/>
Permanently removes the white label configuration and OAuth credentials.
Existing source connections created through this integration will continue to work,
but no new OAuth flows can be initiated until a new white label integration is created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.delete_white_label(
    white_label_id="white_label_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**white_label_id:** `str` — The unique identifier of the white label integration to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">get_white_label_oauth_2_auth_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a branded OAuth2 authorization URL for customer authentication.

<br/><br/>
Creates the OAuth consent URL that customers should be redirected to for
authentication. The OAuth consent screen will display your company name and
branding instead of Airweave.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.get_white_label_oauth_2_auth_url(
    white_label_id="white_label_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**white_label_id:** `str` — The unique identifier of the white label integration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">list_white_label_source_connections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all source connections created through a specific white label integration.

<br/><br/>
Returns source connections that were established using this white label's OAuth flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.list_white_label_source_connections(
    white_label_id="white_label_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**white_label_id:** `str` — The unique identifier of the white label integration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">exchange_white_label_oauth_2_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Complete the OAuth flow and create a source connection.

<br/><br/>
**This is the core endpoint that converts OAuth authorization codes into working
source connections.**<br/><br/>The OAuth credentials are obtained automatically
from the authorization code - you do not need to provide auth_fields. The white
label integration is automatically linked to the created source connection for
tracking and branding purposes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.white_labels.exchange_white_label_oauth_2_code(
    white_label_id="white_label_id",
    code="4/P7q7W91a-oMsCeLvIaQm6bTrgtp7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**white_label_id:** `str` — The unique identifier of the white label integration
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — The OAuth2 authorization code received from the OAuth callback after customer authentication
    
</dd>
</dl>

<dl>
<dd>

**source_connection_in:** `typing.Optional[SourceConnectionCreateWithWhiteLabel]` — Optional configuration for the source connection. If not provided, a source connection will be created automatically with default settings. The white label integration is automatically linked to the source connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

