# Reference
## Health
<details><summary><code>client.health.<a href="src/airweave/health/client.py">health_check</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if the API is healthy.

Returns:
    dict: A dictionary containing the status of the API.
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
    base_url="https://yourhost.com/path/to/api",
)
client.health.health_check()

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

## ApiKeys
<details><summary><code>client.api_keys.<a href="src/airweave/api_keys/client.py">read_api_keys</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all API keys for the current user.

Args:
----
    db (AsyncSession): The database session.
    skip (int): Number of records to skip for pagination.
    limit (int): Maximum number of records to return.
    user (schemas.User): The current user.

Returns:
-------
    List[schemas.APIKey]: A list of API keys.
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
    base_url="https://yourhost.com/path/to/api",
)
client.api_keys.read_api_keys()

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

<details><summary><code>client.api_keys.<a href="src/airweave/api_keys/client.py">create_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new API key for the current user.

Returns a temporary plain key for the user to store securely.
This is not stored in the database.

Args:
----
    db (AsyncSession): The database session.
    api_key_in (schemas.APIKeyCreate): The API key creation data.
    user (schemas.User): The current user.

Returns:
-------
    schemas.APIKeyWithPlainKey: The created API key object, including the key.
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
    base_url="https://yourhost.com/path/to/api",
)
client.api_keys.create_api_key()

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

**expiration_date:** `typing.Optional[dt.datetime]` 
    
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

<details><summary><code>client.api_keys.<a href="src/airweave/api_keys/client.py">delete_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an API key.

Args:
----
    db (AsyncSession): The database session.
    id (UUID): The ID of the API key.
    user (schemas.User): The current user.

Returns:
-------
    schemas.APIKey: The revoked API key object.

Raises:
------
    HTTPException: If the API key is not found.
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
    base_url="https://yourhost.com/path/to/api",
)
client.api_keys.delete_api_key(
    id="id",
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

**id:** `str` 
    
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

<details><summary><code>client.api_keys.<a href="src/airweave/api_keys/client.py">read_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an API key by ID.

Args:
----
    db (AsyncSession): The database session.
    id (UUID): The ID of the API key.
    user (schemas.User): The current user.

Returns:
-------
    schemas.APIKey: The API key object.

Raises:
------
    HTTPException: If the API key is not found.
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
    base_url="https://yourhost.com/path/to/api",
)
client.api_keys.read_api_key(
    id="id",
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

**id:** `str` 
    
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

## Users
<details><summary><code>client.users.<a href="src/airweave/users/client.py">read_user</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current user.

Args:
----
    current_user (User): The current user.

Returns:
-------
    schemas.User: The user object.
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
    base_url="https://yourhost.com/path/to/api",
)
client.users.read_user()

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
    base_url="https://yourhost.com/path/to/api",
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

Get all sources for the current user.

Returns:
-------
    list[schemas.Source]: The list of sources.
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
    base_url="https://yourhost.com/path/to/api",
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

## Destinations
<details><summary><code>client.destinations.<a href="src/airweave/destinations/client.py">list_destinations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all available destinations.
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
    base_url="https://yourhost.com/path/to/api",
)
client.destinations.list_destinations()

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

<details><summary><code>client.destinations.<a href="src/airweave/destinations/client.py">read_destination</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get destination by short name.
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
    base_url="https://yourhost.com/path/to/api",
)
client.destinations.read_destination(
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

## EmbeddingModels
<details><summary><code>client.embedding_models.<a href="src/airweave/embedding_models/client.py">read_embedding_model</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get embedding model by id.

Args:
----
    db (AsyncSession): The database session.
    short_name (str): The short name of the embedding model.
    user (schemas.User): The current user.

Returns:
-------
    schemas.EmbeddingModel: The embedding model object.
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
    base_url="https://yourhost.com/path/to/api",
)
client.embedding_models.read_embedding_model(
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

<details><summary><code>client.embedding_models.<a href="src/airweave/embedding_models/client.py">read_embedding_models</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all embedding models.

Args:
----
    db (AsyncSession): The database session.
    user (schemas.User): The current user.

Returns:
-------
    list[schemas.EmbeddingModel]: The list of embedding models.
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
    base_url="https://yourhost.com/path/to/api",
)
client.embedding_models.read_embedding_models()

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

## Connections
<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">get_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific connection.
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.get_connection(
    connection_id="connection_id",
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

**connection_id:** `str` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">list_all_connected_integrations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all active connections for the current user across all integration types.
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.list_all_connected_integrations()

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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">list_connected_integrations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all integrations of specified type connected to the current user.

Args:
    integration_type (IntegrationType): The type of integration to get connections for.
    db (AsyncSession): The database session.
    user (schemas.User): The current user.

Returns:
    list[schemas.Connection]: The list of connections.
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.list_connected_integrations(
    integration_type="source",
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

**integration_type:** `IntegrationType` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">connect_integration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect to a source, destination, or embedding model.

Expects a POST body with:
```json
{
    "name": "required connection name",
    ... other config fields specific to the integration type ...
}
```
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.connect_integration(
    integration_type="source",
    short_name="short_name",
    config_fields={"key": "value"},
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

**integration_type:** `IntegrationType` 
    
</dd>
</dl>

<dl>
<dd>

**short_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config_fields:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">get_connection_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the credentials for a connection.

Args:
    connection_id (UUID): The ID of the connection to get credentials for
    db (AsyncSession): The database session
    user (schemas.User): The current user

Returns:
    dict: The credentials for the connection
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.get_connection_credentials(
    connection_id="connection_id",
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

**connection_id:** `str` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">delete_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a connection.

Deletes the connection and integration credential.

Args:
    db (AsyncSession): The database session
    connection_id (UUID): The ID of the connection to delete
    delete_syncs_and_data (bool): Whether to delete the associated syncs and data
    user (schemas.User): The current user

Returns:
    schemas.Connection: The deleted connection
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.delete_connection(
    connection_id="connection_id",
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

**connection_id:** `str` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">disconnect_source_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect from a source connection.

Args:
    db (AsyncSession): The database session
    connection_id (UUID): The ID of the connection to disconnect
    user (schemas.User): The current user
Returns:
    schemas.Connection: The disconnected connection
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.disconnect_source_connection(
    connection_id="connection_id",
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

**connection_id:** `str` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">disconnect_destination_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect from a destination connection.

Args:
    db (AsyncSession): The database session
    connection_id (UUID): The ID of the connection to disconnect
    user (schemas.User): The current user

Returns:
    schemas.Connection: The disconnected connection
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.disconnect_destination_connection(
    connection_id="connection_id",
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

**connection_id:** `str` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">get_oauth_2_auth_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the OAuth2 authorization URL for a source.
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.get_oauth_2_auth_url(
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">send_oauth_2_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send the OAuth2 authorization code for a source.

This will:
1. Get the OAuth2 settings for the source
2. Exchange the authorization code for a token
3. Create an integration credential with the token
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.send_oauth_2_code(
    short_name="short_name",
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

**short_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">send_oauth_2_white_label_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange the OAuth2 authorization code for a white label integration.
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.send_oauth_2_white_label_code(
    white_label_id="white_label_id",
    request="string",
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

**request:** `str` 
    
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

<details><summary><code>client.connections.<a href="src/airweave/connections/client.py">get_oauth_2_white_label_auth_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the OAuth2 authorization URL for a white label integration.
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
    base_url="https://yourhost.com/path/to/api",
)
client.connections.get_oauth_2_white_label_auth_url(
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

## Sync
<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">list_syncs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all syncs for the current user.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.list_syncs()

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

**with_source_connection:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">create_sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new sync configuration.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.create_sync(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**embedding_model_connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cron_schedule:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**white_label_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**white_label_user_identifier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**run_immediately:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">get_sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific sync by ID.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.get_sync(
    sync_id="sync_id",
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

**sync_id:** `str` 
    
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

<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">delete_sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a sync configuration and optionally its associated data.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.delete_sync(
    sync_id="sync_id",
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

**sync_id:** `str` 
    
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

<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">run_sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger a sync run.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.run_sync(
    sync_id="sync_id",
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

**sync_id:** `str` 
    
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

<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">list_sync_jobs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all jobs for a specific sync.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.list_sync_jobs(
    sync_id="sync_id",
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

**sync_id:** `str` 
    
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

<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">get_sync_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific sync job.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.get_sync_job(
    job_id="job_id",
    sync_id="sync_id",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sync_id:** `str` 
    
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

<details><summary><code>client.sync.<a href="src/airweave/sync/client.py">subscribe_sync_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Server-Sent Events (SSE) endpoint to subscribe to a sync job's progress.
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
    base_url="https://yourhost.com/path/to/api",
)
client.sync.subscribe_sync_job(
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
    base_url="https://yourhost.com/path/to/api",
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
    base_url="https://yourhost.com/path/to/api",
)
client.white_labels.create_white_label(
    name="name",
    source_id="source_id",
    redirect_url="redirect_url",
    client_id="client_id",
    client_secret="client_secret",
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

**source_id:** `str` 
    
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
    base_url="https://yourhost.com/path/to/api",
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
    base_url="https://yourhost.com/path/to/api",
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
    base_url="https://yourhost.com/path/to/api",
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

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">get_white_label_oauth_2_auth_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate the OAuth2 authorization URL by delegating to oauth2_service.
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
    base_url="https://yourhost.com/path/to/api",
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

Exchange OAuth2 code for tokens and create connection.
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
    base_url="https://yourhost.com/path/to/api",
)
client.white_labels.exchange_white_label_oauth_2_code(
    white_label_id="white_label_id",
    request="string",
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

**request:** `str` 
    
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

<details><summary><code>client.white_labels.<a href="src/airweave/white_labels/client.py">list_white_label_syncs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all syncs for a specific white label.
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
    base_url="https://yourhost.com/path/to/api",
)
client.white_labels.list_white_label_syncs(
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

## Chat
<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">openai_key_set</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if the OpenAI API key is set for the current user.

Returns:
    bool: True if the OpenAI API key is set, False otherwise.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.openai_key_set()

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

<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">list_chats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all chats for the current user.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.list_chats()

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

<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">create_chat</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new chat.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.create_chat(
    name="name",
    sync_id="sync_id",
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

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model_settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**search_settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">get_chat</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific chat by ID.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.get_chat(
    chat_id="chat_id",
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

**chat_id:** `str` 
    
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

<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">update_chat</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a chat.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.update_chat(
    chat_id="chat_id",
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

**chat_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model_settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**search_settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">delete_chat</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive a chat.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.delete_chat(
    chat_id="chat_id",
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

**chat_id:** `str` 
    
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

<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">send_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message to a chat.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.send_message(
    chat_id="chat_id",
    content="content",
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

**chat_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` 
    
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

<details><summary><code>client.chat.<a href="src/airweave/chat/client.py">stream_chat_response</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream an AI response for a chat message.
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
    base_url="https://yourhost.com/path/to/api",
)
client.chat.stream_chat_response(
    chat_id="chat_id",
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

**chat_id:** `str` 
    
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

