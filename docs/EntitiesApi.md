# graphsense.EntitiesApi

All URIs are relative to *http://openapi_server:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_with_tags**](EntitiesApi.md#get_entity_with_tags) | **GET** /{currency}/entities/{entity} | Get an entity with tags
[**list_entity_addresses**](EntitiesApi.md#list_entity_addresses) | **GET** /{currency}/entities/{entity}/addresses | Get an entity&#39;s addresses
[**list_entity_neighbors**](EntitiesApi.md#list_entity_neighbors) | **GET** /{currency}/entities/{entity}/neighbors | Get an entity&#39;s neighbors in the entity graph
[**list_entity_neighbors_csv**](EntitiesApi.md#list_entity_neighbors_csv) | **GET** /{currency}/entities/{entity}/neighbors.csv | Get an entity&#39;s neighbors in the entity graph as CSV
[**list_entity_tags**](EntitiesApi.md#list_entity_tags) | **GET** /{currency}/entities/{entity}/tags | Get attribution tags for a given entity
[**list_entity_tags_csv**](EntitiesApi.md#list_entity_tags_csv) | **GET** /{currency}/entities/{entity}/tags.csv | Get attribution tags for a given entity as CSV
[**search_entity_neighbors**](EntitiesApi.md#search_entity_neighbors) | **GET** /{currency}/entities/{entity}/search | Search deeply for matching neighbors


# **get_entity_with_tags**
> EntityWithTags get_entity_with_tags(currency, entity)

Get an entity with tags

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.EntitiesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
entity = 67065 # int | The entity ID

    try:
        # Get an entity with tags
        api_response = api_instance.get_entity_with_tags(currency, entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntitiesApi->get_entity_with_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **entity** | **int**| The entity ID | 

### Return type

[**EntityWithTags**](EntityWithTags.md)

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
> EntityAddresses list_entity_addresses(currency, entity, page=page, pagesize=pagesize)

Get an entity's addresses

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.EntitiesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
entity = 67065 # int | The entity ID
page = '0400030bff00f07fffff9b00' # str | Resumption token for retrieving the next page (optional)
pagesize = 10 # int | Number of items returned in a single page (optional)

    try:
        # Get an entity's addresses
        api_response = api_instance.list_entity_addresses(currency, entity, page=page, pagesize=pagesize)
        pprint(api_response)
    except ApiException as e:
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
> Neighbors list_entity_neighbors(currency, entity, direction, targets=targets, page=page, pagesize=pagesize)

Get an entity's neighbors in the entity graph

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.EntitiesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
entity = 67065 # int | The entity ID
direction = 'out' # str | Incoming or outgoing neighbors
targets = [56] # list[int] | Restrict result to given set of comma separated IDs (optional)
page = '0400030bff00f07fffff9b00' # str | Resumption token for retrieving the next page (optional)
pagesize = 10 # int | Number of items returned in a single page (optional)

    try:
        # Get an entity's neighbors in the entity graph
        api_response = api_instance.list_entity_neighbors(currency, entity, direction, targets=targets, page=page, pagesize=pagesize)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **entity** | **int**| The entity ID | 
 **direction** | **str**| Incoming or outgoing neighbors | 
 **targets** | [**list[int]**](int.md)| Restrict result to given set of comma separated IDs | [optional] 
 **page** | **str**| Resumption token for retrieving the next page | [optional] 
 **pagesize** | **int**| Number of items returned in a single page | [optional] 

### Return type

[**Neighbors**](Neighbors.md)

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

# **list_entity_neighbors_csv**
> str list_entity_neighbors_csv(currency, entity, direction)

Get an entity's neighbors in the entity graph as CSV

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.EntitiesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
entity = 67065 # int | The entity ID
direction = 'out' # str | Incoming or outgoing neighbors

    try:
        # Get an entity's neighbors in the entity graph as CSV
        api_response = api_instance.list_entity_neighbors_csv(currency, entity, direction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_neighbors_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **entity** | **int**| The entity ID | 
 **direction** | **str**| Incoming or outgoing neighbors | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_tags**
> list[Tag] list_entity_tags(currency, entity)

Get attribution tags for a given entity

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.EntitiesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
entity = 67065 # int | The entity ID

    try:
        # Get attribution tags for a given entity
        api_response = api_instance.list_entity_tags(currency, entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **entity** | **int**| The entity ID | 

### Return type

[**list[Tag]**](Tag.md)

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

# **list_entity_tags_csv**
> str list_entity_tags_csv(currency, entity)

Get attribution tags for a given entity as CSV

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.EntitiesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
entity = 67065 # int | The entity ID

    try:
        # Get attribution tags for a given entity as CSV
        api_response = api_instance.list_entity_tags_csv(currency, entity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntitiesApi->list_entity_tags_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **entity** | **int**| The entity ID | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entity_neighbors**
> SearchPaths search_entity_neighbors(currency, entity, direction, key, value, depth, breadth=breadth, skip_num_addresses=skip_num_addresses)

Search deeply for matching neighbors

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.EntitiesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
entity = 67065 # int | The entity ID
direction = 'out' # str | Incoming or outgoing neighbors
key = 'category' # str | Match neighbors against one and only one of these properties: - the category the entity belongs to - addresses the entity contains - total_received: amount the entity received in total - balance: amount the entity holds finally
value = ['Miner'] # list[str] | If key is - category: comma separated list of category names - addresses: comma separated list of address IDs - total_received/balance: comma separated tuple of (currency, min, max)
depth = 56 # int | How many hops should the transaction graph be searched
breadth = 16 # int | How many siblings of each neighbor should be tried (optional) (default to 16)
skip_num_addresses = 56 # int | Skip entities containing more addresses (optional)

    try:
        # Search deeply for matching neighbors
        api_response = api_instance.search_entity_neighbors(currency, entity, direction, key, value, depth, breadth=breadth, skip_num_addresses=skip_num_addresses)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntitiesApi->search_entity_neighbors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **entity** | **int**| The entity ID | 
 **direction** | **str**| Incoming or outgoing neighbors | 
 **key** | **str**| Match neighbors against one and only one of these properties: - the category the entity belongs to - addresses the entity contains - total_received: amount the entity received in total - balance: amount the entity holds finally | 
 **value** | [**list[str]**](str.md)| If key is - category: comma separated list of category names - addresses: comma separated list of address IDs - total_received/balance: comma separated tuple of (currency, min, max) | 
 **depth** | **int**| How many hops should the transaction graph be searched | 
 **breadth** | **int**| How many siblings of each neighbor should be tried | [optional] [default to 16]
 **skip_num_addresses** | **int**| Skip entities containing more addresses | [optional] 

### Return type

[**SearchPaths**](SearchPaths.md)

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

