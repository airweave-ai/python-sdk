# Reference
## sources
<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all available data source connectors.

Returns the complete catalog of source types that Airweave can connect to,
including their authentication methods, configuration requirements, and
supported features. Use this endpoint to discover which integrations are
available for your organization.

Each source includes:
- **Authentication methods**: How to connect (OAuth, API key, etc.)
- **Configuration schemas**: What settings are required or optional
- **Supported auth providers**: Pre-configured OAuth providers available
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

<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed information about a specific data source connector.

Returns the complete configuration for a source type, including:

- **Authentication fields**: Schema for credentials required to connect
- **Configuration fields**: Schema for optional settings and customization
- **Supported auth providers**: Pre-configured OAuth providers available for this source

Use this endpoint before creating a source connection to understand what
authentication and configuration values are required.
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
client.sources.get(
    short_name="github",
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

## collections
<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all collections belonging to your organization.

Collections are containers that group related data from one or more source
connections, enabling unified search across multiple data sources.

Results are sorted by creation date (newest first) and support pagination
and text search filtering.
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
client.collections.list(
    skip=0,
    limit=100,
    search="customer",
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

**search:** `typing.Optional[str]` — Search term to filter collections by name or readable_id
    
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

Create a new collection in your organization.

Collections are containers for organizing and searching across data from multiple
sources. After creation, add source connections to begin syncing data.

The collection will be assigned a unique `readable_id` based on the name you provide,
which is used in URLs and API calls. You can optionally configure:

- **Sync schedule**: How frequently to automatically sync data from all sources
- **Custom readable_id**: Provide your own identifier (must be unique and URL-safe)
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

**sync_config:** `typing.Optional[SyncConfig]` — Default sync configuration for all syncs in this collection. This provides collection-level defaults that can be overridden at sync or job level.
    
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

Retrieve details of a specific collection by its readable ID.

Returns the complete collection configuration including sync settings, status,
and metadata. Use this to check the current state of a collection or to get
configuration details before making updates.
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
    readable_id="customer-support-tickets-x7k9m",
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a collection and all associated data.

This operation:
- Removes all synced data from the vector database
- Deletes all source connections within the collection
- Cancels any scheduled sync jobs
- Cleans up all related resources

**Warning**: This action cannot be undone. All data will be permanently deleted.
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
    readable_id="customer-support-tickets-x7k9m",
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing collection's properties.

You can modify:
- **Name**: The display name shown in the UI
- **Sync configuration**: Schedule settings for automatic data synchronization

Note that the `readable_id` cannot be changed after creation to maintain stable
API endpoints and preserve existing integrations.
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
    readable_id="customer-support-tickets-x7k9m",
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

**sync_config:** `typing.Optional[SyncConfig]` — Default sync configuration for all syncs in this collection. This provides collection-level defaults that can be overridden at sync or job level.
    
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">search_get_legacy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**DEPRECATED**: Use POST /collections/{readable_id}/search instead.

This legacy GET endpoint provides basic search functionality via query parameters.
Migrate to the POST endpoint for access to advanced features like:
- Structured filters
- Query expansion
- Reranking
- Streaming responses
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
client.collections.search_get_legacy(
    readable_id="customer-support-tickets-x7k9m",
    query="How do I reset my password?",
    response_type="raw",
    limit=10,
    offset=0,
    recency_bias=1.1,
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

**recency_bias:** `typing.Optional[float]` — How much to weigh recency vs similarity (0=similarity only, 1=recency only)
    
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

Search your collection using semantic and hybrid search.

This is the primary search endpoint providing powerful AI-powered search capabilities:

**Search Strategies:**
- **hybrid** (default): Combines neural (semantic) and keyword (BM25) matching
- **neural**: Pure semantic search using embeddings
- **keyword**: Traditional keyword-based BM25 search

**Features:**
- **Query expansion**: Generate query variations to improve recall
- **Filter interpretation**: Extract structured filters from natural language
- **Reranking**: LLM-based reranking for improved relevance
- **Answer generation**: AI-generated answers based on search results

**Note**: Accepts both new SearchRequest and legacy LegacySearchRequest formats
for backwards compatibility.
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
from airweave import AirweaveSDK, SearchRequest

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.collections.search(
    readable_id="customer-support-tickets-x7k9m",
    request=SearchRequest(
        query="How do I reset my password?",
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

**readable_id:** `str` — The unique readable identifier of the collection to search
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchCollectionsReadableIdSearchPostRequest` 
    
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

Retrieve all source connections for your organization.

Returns a lightweight list of source connections with essential fields for
display and navigation. Use the collection filter to see connections within
a specific collection.

For full connection details including sync history, use the GET /{id} endpoint.
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
client.source_connections.list(
    collection="collection",
    skip=0,
    limit=100,
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

**collection:** `typing.Optional[str]` — Filter by collection readable ID
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of connections to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of connections to return (1-1000)
    
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

Create a new source connection to sync data from an external source.

The authentication method determines the creation flow:

- **Direct**: Provide credentials (API key, token) directly. Connection is created immediately.
- **OAuth Browser**: Returns a connection with an `auth_url` to redirect users for authentication.
- **OAuth Token**: Provide an existing OAuth token. Connection is created immediately.
- **Auth Provider**: Use a pre-configured auth provider (e.g., Composio, Pipedream).

After successful authentication, data sync can begin automatically or on-demand.
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
client.source_connections.create(
    short_name="github",
    readable_collection_id="customer-support-tickets-x7k9m",
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

**short_name:** `str` — Source type identifier (e.g., 'slack', 'github', 'notion')
    
</dd>
</dl>

<dl>
<dd>

**readable_collection_id:** `str` — The readable ID of the collection to add this connection to
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name for the connection. If not provided, defaults to '{Source Name} Connection'.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of what this connection is used for
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Source-specific configuration (e.g., repository name, filters)
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ScheduleConfig]` — Optional sync schedule configuration
    
</dd>
</dl>

<dl>
<dd>

**sync_immediately:** `typing.Optional[bool]` — Run initial sync after creation. Defaults to True for direct/token/auth_provider, False for OAuth browser/BYOC flows (which sync after authentication)
    
</dd>
</dl>

<dl>
<dd>

**authentication:** `typing.Optional[Authentication]` — Authentication configuration. Type is auto-detected from provided fields.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — URL to redirect to after OAuth flow completes (only used for OAuth flows)
    
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

Retrieve details of a specific source connection.

Returns complete information about the connection including:
- Configuration settings
- Authentication status
- Sync schedule and history
- Entity statistics
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
    source_connection_id="550e8400-e29b-41d4-a716-446655440000",
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

**source_connection_id:** `str` — Unique identifier of the source connection (UUID)
    
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

Permanently delete a source connection and all its synced data.

**What happens when you delete:**

1. Any running sync is cancelled and the API waits (up to 15 s) for the
   worker to stop writing.
2. The source connection, sync configuration, job history, and entity
   metadata are cascade-deleted from the database.
3. A background cleanup workflow is scheduled to remove data from the
   vector database (Vespa) and raw data storage (ARF). This may take
   several minutes for large datasets but does **not** block the response.

The API returns immediately after step 2. Vector database cleanup happens
asynchronously -- the data becomes unsearchable as soon as the database
records are deleted.

**Warning**: This action cannot be undone.
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
    source_connection_id="550e8400-e29b-41d4-a716-446655440000",
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

**source_connection_id:** `str` — Unique identifier of the source connection to delete (UUID)
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing source connection's configuration.

You can modify:
- **Name and description**: Display information
- **Configuration**: Source-specific settings (e.g., repository name, filters)
- **Schedule**: Cron expression for automatic syncs
- **Authentication**: Update credentials (direct auth only)

Only include the fields you want to change; omitted fields retain their current values.
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
client.source_connections.update(
    source_connection_id="550e8400-e29b-41d4-a716-446655440000",
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

**source_connection_id:** `str` — Unique identifier of the source connection to update (UUID)
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated display name for the connection
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Updated description
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Updated source-specific configuration
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ScheduleConfig]` — Updated sync schedule configuration
    
</dd>
</dl>

<dl>
<dd>

**authentication:** `typing.Optional[Authentication]` — Updated authentication credentials (direct auth only)
    
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

Trigger a data synchronization job for a source connection.

Starts an asynchronous sync job that pulls the latest data from the connected
source. The job runs in the background and you can monitor its progress using
the jobs endpoint.

For continuous sync connections, this performs an incremental sync by default.
Use `force_full_sync=true` to perform a complete re-sync of all data.
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
    source_connection_id="550e8400-e29b-41d4-a716-446655440000",
    force_full_sync=False,
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

**source_connection_id:** `str` — Unique identifier of the source connection to sync (UUID)
    
</dd>
</dl>

<dl>
<dd>

**force_full_sync:** `typing.Optional[bool]` — Force a full sync ignoring cursor data. Only applies to continuous sync connections. Non-continuous connections always perform full syncs.
    
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

Retrieve the sync job history for a source connection.

Returns a list of sync jobs ordered by creation time (newest first). Each job
includes status, timing information, and entity counts.

Job statuses:
- **PENDING**: Job is queued, waiting for the worker to pick it up
- **RUNNING**: Sync is actively pulling and processing data
- **COMPLETED**: Sync finished successfully
- **FAILED**: Sync encountered an unrecoverable error
- **CANCELLING**: Cancellation has been requested. The worker is
  gracefully stopping the pipeline and cleaning up destination data.
- **CANCELLED**: Sync was cancelled. The worker has fully stopped
  and destination data cleanup has been scheduled.
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
    source_connection_id="550e8400-e29b-41d4-a716-446655440000",
    limit=100,
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

**source_connection_id:** `str` — Unique identifier of the source connection (UUID)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of jobs to return (1-1000)
    
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

Request cancellation of a running sync job.

**State lifecycle**: `PENDING` / `RUNNING` → `CANCELLING` → `CANCELLED`

1. The API immediately marks the job as **CANCELLING** in the database.
2. A cancellation signal is sent to the Temporal workflow.
3. The worker receives the signal, gracefully stops the sync pipeline
   (cancels worker pool, source stream), and marks the job as **CANCELLED**.

Already-processed entities are retained in the vector database.
If the worker is unresponsive, a background cleanup job will force the
transition to CANCELLED after 3 minutes.

**Note**: Only jobs in `PENDING` or `RUNNING` state can be cancelled.
Attempting to cancel a `COMPLETED`, `FAILED`, or `CANCELLED` job returns 400.
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
    source_connection_id="550e8400-e29b-41d4-a716-446655440000",
    job_id="660e8400-e29b-41d4-a716-446655440001",
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

**source_connection_id:** `str` — Unique identifier of the source connection (UUID)
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — Unique identifier of the sync job to cancel (UUID)
    
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

## webhooks
<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">get_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all webhook messages for your organization.

Webhook messages represent payloads that were sent (or attempted to be sent)
to your subscribed endpoints. Each message contains the event type, payload data,
and delivery status information.

Use the `event_types` query parameter to filter messages by specific event types,
such as `sync.completed` or `sync.failed`.
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
client.webhooks.get_messages()

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

**event_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter messages by event type(s). Accepts multiple values, e.g., `?event_types=sync.completed&event_types=sync.failed`.
    
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

<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">get_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific webhook message by its ID.

Returns the full message details including the event type, payload data,
timestamp, and delivery channel information. Use this to inspect the
exact payload that was sent to your webhook endpoints.

Use `include_attempts=true` to also retrieve delivery attempts for this message,
which include HTTP response codes, response bodies, and timestamps for debugging
delivery failures.
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
client.webhooks.get_message(
    message_id="550e8400-e29b-41d4-a716-446655440000",
    include_attempts=True,
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

**message_id:** `str` — The unique identifier of the message to retrieve (UUID).
    
</dd>
</dl>

<dl>
<dd>

**include_attempts:** `typing.Optional[bool]` — Include delivery attempts for this message. Each attempt includes the HTTP response code, response body, and timestamp.
    
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

<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">get_subscriptions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all webhook subscriptions for your organization.

Returns all configured webhook endpoints, including their URLs, subscribed
event types, and current status (enabled/disabled). Use this to audit
your webhook configuration or find a specific subscription.
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
client.webhooks.get_subscriptions()

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

<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">create_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook subscription.

Webhook subscriptions allow you to receive real-time notifications when events
occur in Airweave. When you create a subscription, you specify:

- **URL**: The HTTPS endpoint where events will be delivered
- **Event Types**: Which events you want to receive (e.g., `sync.completed`, `sync.failed`)
- **Secret** (optional): A custom signing secret for verifying webhook signatures

After creation, Airweave will send HTTP POST requests to your URL whenever
matching events occur. Each request includes a signature header for verification.
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
client.webhooks.create_subscription(
    url="https://api.mycompany.com/webhooks/airweave",
    event_types=["sync.completed", "sync.failed"],
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

**url:** `str` — The HTTPS URL where webhook events will be delivered. Must be a publicly accessible endpoint that returns a 2xx status code.
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Sequence[EventType]` — List of event types to subscribe to. Events not in this list will not be delivered to this subscription. Available types: `sync.pending`, `sync.running`, `sync.completed`, `sync.failed`, `sync.cancelled`, `source_connection.created`, `source_connection.auth_completed`, `source_connection.deleted`, `collection.created`, `collection.updated`, `collection.deleted`.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — Optional custom signing secret for webhook signature verification. If not provided, a secure secret will be auto-generated. Must be at least 24 characters if specified.
    
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

<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">get_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific webhook subscription with its recent delivery attempts.

Returns the subscription configuration along with a history of message delivery
attempts. This is useful for debugging delivery issues or verifying that your
endpoint is correctly receiving events.

Use `include_secret=true` to also retrieve the signing secret for webhook
signature verification. Keep this secret secure.
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
client.webhooks.get_subscription(
    subscription_id="550e8400-e29b-41d4-a716-446655440000",
    include_secret=True,
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

**subscription_id:** `str` — The unique identifier of the subscription to retrieve (UUID).
    
</dd>
</dl>

<dl>
<dd>

**include_secret:** `typing.Optional[bool]` — Include the signing secret for webhook signature verification. Keep this secret secure and use it to verify the 'svix-signature' header.
    
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

<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">delete_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a webhook subscription.

Once deleted, Airweave will stop sending events to this endpoint immediately.
This action cannot be undone. Any pending message deliveries will be cancelled.

If you want to temporarily stop receiving events, consider disabling the
subscription instead using the PATCH endpoint.
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
client.webhooks.delete_subscription(
    subscription_id="550e8400-e29b-41d4-a716-446655440000",
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

**subscription_id:** `str` — The unique identifier of the subscription to delete (UUID).
    
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

<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">patch_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing webhook subscription.

Use this endpoint to modify a subscription's configuration. You can:

- **Change the URL**: Update where events are delivered
- **Update event types**: Modify which events trigger notifications
- **Enable/disable**: Temporarily pause delivery without deleting the subscription
- **Recover messages**: When re-enabling, optionally recover missed messages

Only include the fields you want to change. Omitted fields will retain their
current values.

When re-enabling a subscription (`disabled: false`), you can optionally provide
`recover_since` to automatically retry all messages that were generated while
the subscription was disabled.
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
client.webhooks.patch_subscription(
    subscription_id="550e8400-e29b-41d4-a716-446655440000",
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

**subscription_id:** `str` — The unique identifier of the subscription to update (UUID).
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — New URL for webhook delivery. Must be a publicly accessible HTTPS endpoint.
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[EventType]]` — New list of event types to subscribe to. This replaces the existing list entirely.
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — Set to `true` to pause delivery to this subscription, or `false` to resume. Disabled subscriptions will not receive events.
    
</dd>
</dl>

<dl>
<dd>

**recover_since:** `typing.Optional[dt.datetime]` — When re-enabling a subscription (`disabled: false`), optionally recover failed messages from this timestamp. Only applies when enabling.
    
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

<details><summary><code>client.webhooks.<a href="src/airweave/webhooks/client.py">recover_failed_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retry failed message deliveries for a webhook subscription.

Triggers a recovery process that replays all failed messages within the
specified time window. This is useful when:

- Your endpoint was temporarily down and you want to catch up
- You've fixed a bug in your webhook handler
- You want to reprocess events after re-enabling a disabled subscription

Messages are retried in chronological order. Successfully delivered messages
are skipped; only failed or pending messages are retried.
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
import datetime

from airweave import AirweaveSDK

client = AirweaveSDK(
    api_key="YOUR_API_KEY",
)
client.webhooks.recover_failed_messages(
    subscription_id="550e8400-e29b-41d4-a716-446655440000",
    since=datetime.datetime.fromisoformat(
        "2024-03-14 00:00:00+00:00",
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

**subscription_id:** `str` — The unique identifier of the subscription to recover messages for (UUID).
    
</dd>
</dl>

<dl>
<dd>

**since:** `dt.datetime` — Start of the recovery time window (inclusive). All failed messages from this time onward will be retried.
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[dt.datetime]` — End of the recovery time window (exclusive). If not specified, recovers all failed messages up to now.
    
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

