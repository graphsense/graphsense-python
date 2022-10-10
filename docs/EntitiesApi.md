# graphsense.EntitiesApi

All URIs are relative to *https://api.ikna.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity**](EntitiesApi.md#get_entity) | **GET** /{currency}/entities/{entity} | Get an entity
[**list_address_tags_by_entity**](EntitiesApi.md#list_address_tags_by_entity) | **GET** /{currency}/entities/{entity}/tags | Get address tags for a given entity
[**list_entity_addresses**](EntitiesApi.md#list_entity_addresses) | **GET** /{currency}/entities/{entity}/addresses | Get an entity&#39;s addresses
[**list_entity_links**](EntitiesApi.md#list_entity_links) | **GET** /{currency}/entities/{entity}/links | Get transactions between two entities
[**list_entity_neighbors**](EntitiesApi.md#list_entity_neighbors) | **GET** /{currency}/entities/{entity}/neighbors | Get an entity&#39;s direct neighbors
[**list_entity_txs**](EntitiesApi.md#list_entity_txs) | **GET** /{currency}/entities/{entity}/txs | Get all transactions an entity has been involved in
[**search_entity_neighbors**](EntitiesApi.md#search_entity_neighbors) | **GET** /{currency}/entities/{entity}/search | Search deeply for matching neighbors


# **get_entity**
> Entity get_entity(currency, entity)

Get an entity

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    entity = 67065 # int | The entity ID

    # example passing only required values which don't have defaults set
    try:
        # Get an entity
        api_response = api_instance.get_entity(currency, entity)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->get_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **entity** | **int**| The entity ID |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**Entity**](Entity.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address_tags_by_entity**
> AddressTags list_address_tags_by_entity(currency, entity)

Get address tags for a given entity

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.address_tags import AddressTags
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    entity = 67065 # int | The entity ID
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get address tags for a given entity
        api_response = api_instance.list_address_tags_by_entity(currency, entity)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_address_tags_by_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get address tags for a given entity
        api_response = api_instance.list_address_tags_by_entity(currency, entity, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_address_tags_by_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **entity** | **int**| The entity ID |
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**AddressTags**](AddressTags.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_addresses**
> EntityAddresses list_entity_addresses(currency, entity)

Get an entity's addresses

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.entity_addresses import EntityAddresses
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
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
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **entity** | **int**| The entity ID |
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**EntityAddresses**](EntityAddresses.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_links**
> Links list_entity_links(currency, entity, neighbor)

Get transactions between two entities

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.links import Links
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    entity = 67065 # int | The entity ID
    neighbor = 123456 # int | Neighbor entity
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get transactions between two entities
        api_response = api_instance.list_entity_links(currency, entity, neighbor)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_links: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get transactions between two entities
        api_response = api_instance.list_entity_links(currency, entity, neighbor, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **entity** | **int**| The entity ID |
 **neighbor** | **int**| Neighbor entity |
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**Links**](Links.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_neighbors**
> NeighborEntities list_entity_neighbors(currency, entity, direction)

Get an entity's direct neighbors

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.neighbor_entities import NeighborEntities
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    entity = 67065 # int | The entity ID
    direction = "out" # str | Incoming or outgoing neighbors
    only_ids = [
        1,
    ] # [int] | Restrict result to given set of comma separated IDs (optional)
    include_labels = False # bool | Whether to include labels of first page of tags (optional) if omitted the server will use the default value of False
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an entity's direct neighbors
        api_response = api_instance.list_entity_neighbors(currency, entity, direction)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an entity's direct neighbors
        api_response = api_instance.list_entity_neighbors(currency, entity, direction, only_ids=only_ids, include_labels=include_labels, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **entity** | **int**| The entity ID |
 **direction** | **str**| Incoming or outgoing neighbors |
 **only_ids** | **[int]**| Restrict result to given set of comma separated IDs | [optional]
 **include_labels** | **bool**| Whether to include labels of first page of tags | [optional] if omitted the server will use the default value of False
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**NeighborEntities**](NeighborEntities.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_txs**
> AddressTxs list_entity_txs(currency, entity)

Get all transactions an entity has been involved in

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.address_txs import AddressTxs
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    entity = 67065 # int | The entity ID
    direction = "out" # str | Incoming or outgoing transactions (optional)
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all transactions an entity has been involved in
        api_response = api_instance.list_entity_txs(currency, entity)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_txs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all transactions an entity has been involved in
        api_response = api_instance.list_entity_txs(currency, entity, direction=direction, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **entity** | **int**| The entity ID |
 **direction** | **str**| Incoming or outgoing transactions | [optional]
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**AddressTxs**](AddressTxs.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entity_neighbors**
> [SearchResultLevel1] search_entity_neighbors(currency, entity, direction, key, value, depth)

Search deeply for matching neighbors

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import entities_api
from graphsense.model.search_result_level1 import SearchResultLevel1
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
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
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **entity** | **int**| The entity ID |
 **direction** | **str**| Incoming or outgoing neighbors |
 **key** | **str**| Match neighbors against one and only one of these properties: - the category the entity belongs to - addresses the entity contains - entity ids - total_received: amount the entity received in total - balance: amount the entity holds finally |
 **value** | **[str]**| If key is - category: comma separated list of category names - addresses: comma separated list of address IDs - entities: comma separated list of entity IDs - total_received/balance: comma separated tuple of (currency, min, max) where currency is &#39;value&#39; for the cryptocurrency value or an ISO currency code |
 **depth** | **int**| How many hops should the transaction graph be searched |
 **breadth** | **int**| How many siblings of each neighbor should be tried | [optional] if omitted the server will use the default value of 16
 **skip_num_addresses** | **int**| Skip entities containing more addresses | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**[SearchResultLevel1]**](SearchResultLevel1.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

