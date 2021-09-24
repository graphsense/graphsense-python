# graphsense.EntitiesApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity**](EntitiesApi.md#get_entity) | **GET** /{currency}/entities/{entity} | Get an entity, optionally with tags
[**list_entities**](EntitiesApi.md#list_entities) | **GET** /{currency}/entities | Get entities
[**list_entities_csv**](EntitiesApi.md#list_entities_csv) | **GET** /{currency}/entities.csv | Get entities as CSV
[**list_entity_addresses**](EntitiesApi.md#list_entity_addresses) | **GET** /{currency}/entities/{entity}/addresses | Get an entity&#39;s addresses
[**list_entity_addresses_csv**](EntitiesApi.md#list_entity_addresses_csv) | **GET** /{currency}/entities/{entity}/addresses.csv | Get an entity&#39;s addresses as CSV
[**list_entity_links**](EntitiesApi.md#list_entity_links) | **GET** /{currency}/entities/{entity}/links | Get transactions between two entities
[**list_entity_links_csv**](EntitiesApi.md#list_entity_links_csv) | **GET** /{currency}/entities/{entity}/links.csv | Get transactions between two entities as CSV
[**list_entity_neighbors**](EntitiesApi.md#list_entity_neighbors) | **GET** /{currency}/entities/{entity}/neighbors | Get an entity&#39;s neighbors in the entity graph
[**list_entity_neighbors_csv**](EntitiesApi.md#list_entity_neighbors_csv) | **GET** /{currency}/entities/{entity}/neighbors.csv | Get an entity&#39;s neighbors in the entity graph as CSV
[**list_tags_by_entity**](EntitiesApi.md#list_tags_by_entity) | **GET** /{currency}/entities/{entity}/tags | Get tags for a given entity
[**list_tags_by_entity_by_level_csv**](EntitiesApi.md#list_tags_by_entity_by_level_csv) | **GET** /{currency}/entities/{entity}/tags.csv | Get address or entity tags for a given entity as CSV
[**search_entity_neighbors**](EntitiesApi.md#search_entity_neighbors) | **GET** /{currency}/entities/{entity}/search | Search deeply for matching neighbors


# **get_entity**
> Entity get_entity(currency, entity)

Get an entity, optionally with tags

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    include_tags = False # bool | Whether tags should be included (optional) if omitted the server will use the default value of False
    tag_coherence = False # bool | Whether to calculate coherence of address tags (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get an entity, optionally with tags
        api_response = api_instance.get_entity(currency, entity)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->get_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an entity, optionally with tags
        api_response = api_instance.get_entity(currency, entity, include_tags=include_tags, tag_coherence=tag_coherence)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->get_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **include_tags** | **bool**| Whether tags should be included | [optional] if omitted the server will use the default value of False
 **tag_coherence** | **bool**| Whether to calculate coherence of address tags | [optional] if omitted the server will use the default value of False

### Return type

[**Entity**](Entity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entities**
> Entities list_entities(currency)

Get entities

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.entities import Entities
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    ids = [
        1,
    ] # [int] | Restrict result to given set of comma separated IDs (optional)
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get entities
        api_response = api_instance.list_entities(currency)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entities: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get entities
        api_response = api_instance.list_entities(currency, ids=ids, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **ids** | **[int]**| Restrict result to given set of comma separated IDs | [optional]
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]

### Return type

[**Entities**](Entities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entities_csv**
> str list_entities_csv(currency, ids)

Get entities as CSV

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    ids = [
        "ids_example",
    ] # [str] | Set of comma separated IDs

    # example passing only required values which don't have defaults set
    try:
        # Get entities as CSV
        api_response = api_instance.list_entities_csv(currency, ids)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entities_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **ids** | **[str]**| Set of comma separated IDs |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_addresses**
> EntityAddresses list_entity_addresses(currency, entity)

Get an entity's addresses

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.entity_addresses import EntityAddresses
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an entity's addresses
        api_response = api_instance.list_entity_addresses(currency, entity)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_addresses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an entity's addresses
        api_response = api_instance.list_entity_addresses(currency, entity, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]

### Return type

[**EntityAddresses**](EntityAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_addresses_csv**
> str list_entity_addresses_csv(currency, entity)

Get an entity's addresses as CSV

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID

    # example passing only required values which don't have defaults set
    try:
        # Get an entity's addresses as CSV
        api_response = api_instance.list_entity_addresses_csv(currency, entity)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_addresses_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_links**
> Links list_entity_links(currency, entity, neighbor)

Get transactions between two entities

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.links import Links
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    neighbor = 123456 # int | Neighbor entity

    # example passing only required values which don't have defaults set
    try:
        # Get transactions between two entities
        api_response = api_instance.list_entity_links(currency, entity, neighbor)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **neighbor** | **int**| Neighbor entity |

### Return type

[**Links**](Links.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_links_csv**
> str list_entity_links_csv(currency, entity, neighbor)

Get transactions between two entities as CSV

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    neighbor = 123456 # int | Neighbor entity

    # example passing only required values which don't have defaults set
    try:
        # Get transactions between two entities as CSV
        api_response = api_instance.list_entity_links_csv(currency, entity, neighbor)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_links_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **neighbor** | **int**| Neighbor entity |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_neighbors**
> Neighbors list_entity_neighbors(currency, entity, direction)

Get an entity's neighbors in the entity graph

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.neighbors import Neighbors
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    direction = "out" # str | Incoming or outgoing neighbors
    ids = [
        1,
    ] # [int] | Restrict result to given set of comma separated IDs (optional)
    include_labels = False # bool | Whether labels of tags should be included (optional) if omitted the server will use the default value of False
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an entity's neighbors in the entity graph
        api_response = api_instance.list_entity_neighbors(currency, entity, direction)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an entity's neighbors in the entity graph
        api_response = api_instance.list_entity_neighbors(currency, entity, direction, ids=ids, include_labels=include_labels, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **direction** | **str**| Incoming or outgoing neighbors |
 **ids** | **[int]**| Restrict result to given set of comma separated IDs | [optional]
 **include_labels** | **bool**| Whether labels of tags should be included | [optional] if omitted the server will use the default value of False
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]

### Return type

[**Neighbors**](Neighbors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_neighbors_csv**
> str list_entity_neighbors_csv(currency, entity, direction)

Get an entity's neighbors in the entity graph as CSV

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    direction = "out" # str | Incoming or outgoing neighbors
    include_labels = False # bool | Whether labels of tags should be included (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get an entity's neighbors in the entity graph as CSV
        api_response = api_instance.list_entity_neighbors_csv(currency, entity, direction)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors_csv: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an entity's neighbors in the entity graph as CSV
        api_response = api_instance.list_entity_neighbors_csv(currency, entity, direction, include_labels=include_labels)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **direction** | **str**| Incoming or outgoing neighbors |
 **include_labels** | **bool**| Whether labels of tags should be included | [optional] if omitted the server will use the default value of False

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_by_entity**
> Tags list_tags_by_entity(currency, entity)

Get tags for a given entity

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.tags import Tags
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    tag_coherence = False # bool | Whether to calculate coherence of address tags (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get tags for a given entity
        api_response = api_instance.list_tags_by_entity(currency, entity)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_tags_by_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get tags for a given entity
        api_response = api_instance.list_tags_by_entity(currency, entity, tag_coherence=tag_coherence)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_tags_by_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **tag_coherence** | **bool**| Whether to calculate coherence of address tags | [optional] if omitted the server will use the default value of False

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_by_entity_by_level_csv**
> str list_tags_by_entity_by_level_csv(currency, entity, level)

Get address or entity tags for a given entity as CSV

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    level = "address" # str | Whether tags on the address or entity level are requested

    # example passing only required values which don't have defaults set
    try:
        # Get address or entity tags for a given entity as CSV
        api_response = api_instance.list_tags_by_entity_by_level_csv(currency, entity, level)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_tags_by_entity_by_level_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **level** | **str**| Whether tags on the address or entity level are requested |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entity_neighbors**
> [SearchResultLevel1] search_entity_neighbors(currency, entity, direction, key, value, depth)

Search deeply for matching neighbors

### Example

```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.search_result_level1 import SearchResultLevel1
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    entity = 67065 # int | The entity ID
    direction = "out" # str | Incoming or outgoing neighbors
    key = "category" # str | Match neighbors against one and only one of these properties: - the category the entity belongs to - addresses the entity contains - entity ids - total_received: amount the entity received in total - balance: amount the entity holds finally
    value = [
        "Miner",
    ] # [str] | If key is - category: comma separated list of category names - addresses: comma separated list of address IDs - entities: comma separated list of entity IDs - total_received/balance: comma separated tuple of (currency, min, max) where currency is 'value' for the cryptocurrency value or an ISO currency code
    depth = 2 # int | How many hops should the transaction graph be searched
    breadth = 16 # int | How many siblings of each neighbor should be tried (optional) if omitted the server will use the default value of 16
    skip_num_addresses = 1 # int | Skip entities containing more addresses (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search deeply for matching neighbors
        api_response = api_instance.search_entity_neighbors(currency, entity, direction, key, value, depth)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->search_entity_neighbors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search deeply for matching neighbors
        api_response = api_instance.search_entity_neighbors(currency, entity, direction, key, value, depth, breadth=breadth, skip_num_addresses=skip_num_addresses)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->search_entity_neighbors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **entity** | **int**| The entity ID |
 **direction** | **str**| Incoming or outgoing neighbors |
 **key** | **str**| Match neighbors against one and only one of these properties: - the category the entity belongs to - addresses the entity contains - entity ids - total_received: amount the entity received in total - balance: amount the entity holds finally |
 **value** | **[str]**| If key is - category: comma separated list of category names - addresses: comma separated list of address IDs - entities: comma separated list of entity IDs - total_received/balance: comma separated tuple of (currency, min, max) where currency is &#39;value&#39; for the cryptocurrency value or an ISO currency code |
 **depth** | **int**| How many hops should the transaction graph be searched |
 **breadth** | **int**| How many siblings of each neighbor should be tried | [optional] if omitted the server will use the default value of 16
 **skip_num_addresses** | **int**| Skip entities containing more addresses | [optional]

### Return type

[**[SearchResultLevel1]**](SearchResultLevel1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

