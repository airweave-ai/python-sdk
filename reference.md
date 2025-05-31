# Reference
## Sources
<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">read_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get source by id.

Args:
----
    db (AsyncSession): The database session.
    short_name (str): The short name of the source.
    user (schemas.User): The current user.

Returns:
-------
    schemas.Source: The source object.

Raises:
    HTTPException:
        - 404 if source not found
        - 400 if source missing required configuration classes
        - 500 if there's an error retrieving auth configuration
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

<details><summary><code>client.sources.<a href="src/airweave/sources/client.py">read_sources</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all sources with their authentication fields.
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

## Collections
<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">list_collections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all collections for the current user's organization.
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

<details><summary><code>client.collections.<a href="src/airweave/collections/client.py">create_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new collection.
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
    name="name",
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

**name:** `str` — Display name for the collection
    
</dd>
</dl>

<dl>
<dd>

**readable_id:** `typing.Optional[str]` — Unique lowercase identifier (e.g., respectable-sparrow, collection-123)
    
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

Get a specific collection by its readable ID.
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

**readable_id:** `str` 
    
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

Delete a collection by its readable ID.

Args:
    readable_id: The readable ID of the collection to delete
    delete_data: Whether to delete the data in destinations
    db: The database session
    current_user: The current user

Returns:
    The deleted collection
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

**readable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**delete_data:** `typing.Optional[bool]` 
    
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

Search within a collection identified by readable ID.

Args:
    readable_id: The readable ID of the collection to search
    query: The search query
    response_type: Type of response (raw results or AI completion)
    db: The database session
    current_user: The current user

Returns:
    dict: Search results or AI completion response
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
    query="query",
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

**readable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — Search query
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `typing.Optional[ResponseType]` — Type of response: raw search results or AI completion
    
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

Start sync jobs for all source connections in the collection.

Args:
    readable_id: The readable ID of the collection
    db: The database session
    current_user: The current user
    background_tasks: Background tasks for async operations

Returns:
    A list of created sync jobs
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

**readable_id:** `str` 
    
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

## SourceConnections
<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">list_source_connections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all source connections for the current user.

Args:
    db: The database session
    collection: The collection to filter by
    skip: The number of connections to skip
    limit: The number of connections to return
    user: The current user

Returns:
    A list of source connection list items with essential information
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

**collection:** `typing.Optional[str]` — Filter by collection
    
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

<details><summary><code>client.source_connections.<a href="src/airweave/source_connections/client.py">create_source_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new source connection.

This endpoint creates:
1. An integration credential with the provided auth fields
2. A collection if not provided
3. The source connection
4. A sync configuration and DAG
5. A sync job if immediate execution is requested

Args:
    db: The database session
    source_connection_in: The source connection to create
    user: The current user
    background_tasks: Background tasks for async operations

Returns:
    The created source connection
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
    name="name",
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

**name:** `str` — Name of the source connection
    
</dd>
</dl>

<dl>
<dd>

**short_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**config_fields:** `typing.Optional[ConfigValues]` 
    
</dd>
</dl>

<dl>
<dd>

**white_label_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collection:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_fields:** `typing.Optional[ConfigValues]` 
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_immediately:** `typing.Optional[bool]` 
    
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

Get a specific source connection by ID.

Args:
    db: The database session
    source_connection_id: The ID of the source connection
    show_auth_fields: Whether to show the auth fields, default is False
    user: The current user

Returns:
    The source connection
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

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**show_auth_fields:** `typing.Optional[bool]` 
    
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

Update a source connection.

Args:
    db: The database session
    source_connection_id: The ID of the source connection to update
    source_connection_in: The updated source connection data
    user: The current user

Returns:
    The updated source connection
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

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the source connection
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_fields:** `typing.Optional[SourceConnectionUpdateAuthFields]` 
    
</dd>
</dl>

<dl>
<dd>

**config_fields:** `typing.Optional[ConfigValues]` 
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**white_label_id:** `typing.Optional[str]` 
    
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

Delete a source connection and all related components.

Args:
    db: The database session
    source_connection_id: The ID of the source connection to delete
    delete_data: Whether to delete the associated data in destinations
    user: The current user

Returns:
    The deleted source connection
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

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**delete_data:** `typing.Optional[bool]` 
    
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

Trigger a sync run for a source connection.

Args:
    db: The database session
    source_connection_id: The ID of the source connection to run
    access_token: Optional access token to use instead of stored credentials
    user: The current user
    background_tasks: Background tasks for async operations

Returns:
    The created sync job
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

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` 
    
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

Args:
    db: The database session
    source_connection_id: The ID of the source connection
    user: The current user

Returns:
    A list of sync jobs
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

