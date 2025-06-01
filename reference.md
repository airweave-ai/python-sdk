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
    name="Finance Data",
    readable_id="finance-data",
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
    name="My Stripe Connection",
    description="Production Stripe account for payment data",
    short_name="stripe",
    collection="finance-data",
    cron_schedule="0 */6 * * *",
    auth_fields={"api_key": "sk_live_51H..."},
    sync_immediately=True,
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

## WhiteLabels
<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">list_white_labels</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all white labels for the current user's organization.

Args:
-----
    db: The database session
    current_user: The current user

Returns:
--------
    list[schemas.WhiteLabel]: A list of white labels
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

Create new white label integration.

Args:
-----
    db: The database session
    current_user: The current user
    white_label_in: The white label to create

Returns:
--------
    white_label (schemas.WhiteLabel): The created white label
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
    name="Company Slack Integration",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_short_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `str` 
    
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

Get a specific white label integration.

Args:
-----
    db: The database session
    white_label_id: The ID of the white label to get
    current_user: The current user

Returns:
--------
    white_label (schemas.WhiteLabel): The white label
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

**white_label_id:** `str` 
    
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

Update a white label integration.

Args:
-----
    db: The database session
    current_user: The current user
    white_label_id: The ID of the white label to update
    white_label_in: The white label to update

Returns:
--------
    white_label (schemas.WhiteLabel): The updated white label
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

**white_label_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[str]` 
    
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

Args:
-----
    db: The database session
    current_user: The current user
    white_label_id: The ID of the white label to delete

Returns:
--------
    white_label (schemas.WhiteLabel): The deleted white label
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

**white_label_id:** `str` 
    
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

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">get_white_label_oauth_2_auth_url_white_labels_white_label_id_oauth_2_auth_url_options</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate the OAuth2 authorization URL by delegating to oauth2_service.

Args:
-----
    request: The HTTP request
    response: The HTTP response
    db: The database session
    white_label_id: The ID of the white label to get the auth URL for
    user: The current user

Returns:
--------
    str: The OAuth2 authorization URL
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
client.white_labels.get_white_label_oauth_2_auth_url_white_labels_white_label_id_oauth_2_auth_url_options(
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

**white_label_id:** `str` 
    
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

List all source connections for a specific white label.

Args:
-----
    white_label_id: The ID of the white label to list source connections for
    db: The database session
    current_user: The current user

Returns:
--------
    list[schemas.SourceConnectionListItem]: A list of source connections
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

**white_label_id:** `str` 
    
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

Exchange OAuth2 code for tokens and create connection with source connection.

Args:
-----
    request: The HTTP request
    response: The HTTP response
    white_label_id: The ID of the white label to exchange the code for
    code: The OAuth2 code
    source_connection_in: Optional source connection configuration
    db: The database session
    user: The current user
    background_tasks: Background tasks for async operations

Returns:
--------
    source_connection (schemas.SourceConnection): The created source connection
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
    code="code",
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

**white_label_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_connection_in:** `typing.Optional[SourceConnectionCreate]` 
    
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

