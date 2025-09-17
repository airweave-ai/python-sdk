# Reference
## sources
<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">read</a>(...)</code></summary>
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
client.sources.read(
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

<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">list</a>()</code></summary>
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
client.sources.list()

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

## AuthProviders
<details><summary><code>client.auth_providers.<a href="src/airweave/auth_providers/client.py">connect_or_update_auth_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update an auth provider connection.

If a connection for this auth provider already exists for the organization,
it will be updated with the new credentials and fields.
If no connection exists, a new one will be created.

Args:
-----
    db: The database session
    ctx: The current authentication context
    auth_provider_connection_in: The auth provider connection data

Returns:
--------
    schemas.AuthProviderConnection: The created or updated connection
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
client.auth_providers.connect_or_update_auth_provider(
    name="My Composio Connection",
    description="My Composio Connection",
    short_name="composio",
    auth_fields={"api_key": "comp_1234567890abcdef"},
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

**name:** `str` — Human-readable name for this auth provider connection
    
</dd>
</dl>

<dl>
<dd>

**short_name:** `str` — Technical identifier of the auth provider
    
</dd>
</dl>

<dl>
<dd>

**readable_id:** `typing.Optional[str]` — URL-safe unique identifier for the connection. Must contain only lowercase letters, numbers, and hyphens. If not provided, it will be automatically generated from the connection name with a random suffix for uniqueness (e.g., 'composio-connection-ab123').
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional detailed description of what this auth provider connection provides.
    
</dd>
</dl>

<dl>
<dd>

**auth_fields:** `typing.Optional[ConfigValues]` — Authentication credentials required to access the auth provider. The required fields vary by auth provider type.
    
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

<details><summary><code>client.auth_providers.<a href="src/airweave/auth_providers/client.py">get_auth_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific auth provider.

Args:
-----
    db: The database session
    short_name: The short name of the auth provider
    ctx: The current authentication context

Returns:
--------
    schemas.AuthProvider: The auth provider details
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
client.auth_providers.get_auth_provider(
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

**short_name:** `str` 
    
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

## collections
<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">list</a>(...)</code></summary>
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
client.collections.list()

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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">create</a>(...)</code></summary>
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
client.collections.create(
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">get</a>(...)</code></summary>
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
client.collections.get(
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">update</a>(...)</code></summary>
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
client.collections.update(
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">delete</a>(...)</code></summary>
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
client.collections.delete(
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">search</a>(...)</code></summary>
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
client.collections.search(
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">search_advanced</a>(...)</code></summary>
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
client.collections.search_advanced(
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

**limit:** `typing.Optional[int]` — Maximum number of results to return (DEFAULT: 100)
    
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
<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List source connections with minimal fields for performance.
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
client.source_connections.list()

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

**collection:** `typing.Optional[str]` — Filter by collection readable ID
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new source connection.

The authentication configuration determines the flow:
- DirectAuthentication: Immediate creation with provided credentials
- OAuthBrowserAuthentication: Returns shell with authentication URL
- OAuthTokenAuthentication: Immediate creation with provided token
- AuthProviderAuthentication: Using external auth provider

BYOC (Bring Your Own Client) is detected when client_id and client_secret
are provided in OAuthBrowserAuthentication.
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
from airweave import AirweaveSDK, DirectAuthentication

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.source_connections.create(
    name="name",
    short_name="short_name",
    readable_collection_id="readable_collection_id",
    authentication=DirectAuthentication(
        credentials={"key": "value"},
    ),
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

**name:** `str` — Connection name
    
</dd>
</dl>

<dl>
<dd>

**short_name:** `str` — Source identifier (e.g., 'slack', 'github')
    
</dd>
</dl>

<dl>
<dd>

**readable_collection_id:** `str` — Collection readable ID
    
</dd>
</dl>

<dl>
<dd>

**authentication:** `Authentication` — Authentication configuration
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Connection description
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Source-specific configuration
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ScheduleConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_immediately:** `typing.Optional[bool]` — Run initial sync after creation
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a source connection with optional depth expansion.
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
client.source_connections.get(
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

**source_connection_id:** `str` 
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a source connection and all related data.
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
client.source_connections.delete(
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

**source_connection_id:** `str` 
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger a sync run for a source connection.

Runs are always executed through Temporal workflow engine.
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
client.source_connections.run(
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

**source_connection_id:** `str` 
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">get_source_connection_jobs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get sync jobs for a source connection.
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
client.source_connections.get_source_connection_jobs(
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

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">cancel_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a running sync job for a source connection.

This will update the job status in the database to CANCELLED and
send a cancellation request to the Temporal workflow if it's running.
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
client.source_connections.cancel_job(
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

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` 
    
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

