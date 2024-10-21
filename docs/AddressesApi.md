# graphsense.AddressesApi

All URIs are relative to *https://api.ikna.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](AddressesApi.md#get_address) | **GET** /{currency}/addresses/{address} | Get an address
[**get_address_entity**](AddressesApi.md#get_address_entity) | **GET** /{currency}/addresses/{address}/entity | Get the entity of an address
[**get_tag_summary_by_address**](AddressesApi.md#get_tag_summary_by_address) | **GET** /{currency}/addresses/{address}/tag_summary | Get attribution tag summary for a given address
[**list_address_links**](AddressesApi.md#list_address_links) | **GET** /{currency}/addresses/{address}/links | Get outgoing transactions between two addresses
[**list_address_neighbors**](AddressesApi.md#list_address_neighbors) | **GET** /{currency}/addresses/{address}/neighbors | Get an address&#39;s neighbors in the address graph
[**list_address_txs**](AddressesApi.md#list_address_txs) | **GET** /{currency}/addresses/{address}/txs | Get all transactions an address has been involved in
[**list_tags_by_address**](AddressesApi.md#list_tags_by_address) | **GET** /{currency}/addresses/{address}/tags | Get attribution tags for a given address


# **get_address**
> Address get_address(currency, address)

Get an address

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.address import Address
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address
    include_actors = True # bool | Whether to include information about the actor behind the address (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get an address
        api_response = api_instance.get_address(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an address
        api_response = api_instance.get_address(currency, address, include_actors=include_actors)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **include_actors** | **bool**| Whether to include information about the actor behind the address | [optional] if omitted the server will use the default value of True
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**Address**](Address.md)

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

# **get_address_entity**
> Entity get_address_entity(currency, address)

Get the entity of an address

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import addresses_api
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address

    # example passing only required values which don't have defaults set
    try:
        # Get the entity of an address
        api_response = api_instance.get_address_entity(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
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

# **get_tag_summary_by_address**
> TagSummary get_tag_summary_by_address(currency, address)

Get attribution tag summary for a given address

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.tag_summary import TagSummary
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address
    include_best_cluster_tag = False # bool | If the best cluster tag should be inherited to the address level, often helpful for exchanges where not every address is tagged. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get attribution tag summary for a given address
        api_response = api_instance.get_tag_summary_by_address(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_tag_summary_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get attribution tag summary for a given address
        api_response = api_instance.get_tag_summary_by_address(currency, address, include_best_cluster_tag=include_best_cluster_tag)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_tag_summary_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **include_best_cluster_tag** | **bool**| If the best cluster tag should be inherited to the address level, often helpful for exchanges where not every address is tagged. | [optional] if omitted the server will use the default value of False
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**TagSummary**](TagSummary.md)

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

# **list_address_links**
> Links list_address_links(currency, address, neighbor)

Get outgoing transactions between two addresses

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.height import Height
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address
    neighbor = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | Neighbor address
    min_height = Height(1) # Height | Return transactions starting from given height (optional)
    max_height = Height(2) # Height | Return transactions up to (including) given height (optional)
    order = "desc" # str | Sorting order (optional) if omitted the server will use the default value of "desc"
    page = "" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get outgoing transactions between two addresses
        api_response = api_instance.list_address_links(currency, address, neighbor)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_links: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get outgoing transactions between two addresses
        api_response = api_instance.list_address_links(currency, address, neighbor, min_height=min_height, max_height=max_height, order=order, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **neighbor** | **str**| Neighbor address |
 **min_height** | **Height**| Return transactions starting from given height | [optional]
 **max_height** | **Height**| Return transactions up to (including) given height | [optional]
 **order** | **str**| Sorting order | [optional] if omitted the server will use the default value of "desc"
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

# **list_address_neighbors**
> NeighborAddresses list_address_neighbors(currency, address, direction)

Get an address's neighbors in the address graph

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.neighbor_addresses import NeighborAddresses
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address
    direction = "out" # str | Incoming or outgoing neighbors
    only_ids = [
        "only_ids_example",
    ] # [str] | Restrict result to given set of comma separated addresses (optional)
    include_labels = False # bool | Whether to include labels of first page of address tags (optional) if omitted the server will use the default value of False
    include_actors = True # bool | Whether to include information about the actor behind the address (optional) if omitted the server will use the default value of True
    page = "" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an address's neighbors in the address graph
        api_response = api_instance.list_address_neighbors(currency, address, direction)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_neighbors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an address's neighbors in the address graph
        api_response = api_instance.list_address_neighbors(currency, address, direction, only_ids=only_ids, include_labels=include_labels, include_actors=include_actors, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_neighbors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **direction** | **str**| Incoming or outgoing neighbors |
 **only_ids** | **[str]**| Restrict result to given set of comma separated addresses | [optional]
 **include_labels** | **bool**| Whether to include labels of first page of address tags | [optional] if omitted the server will use the default value of False
 **include_actors** | **bool**| Whether to include information about the actor behind the address | [optional] if omitted the server will use the default value of True
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**NeighborAddresses**](NeighborAddresses.md)

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

# **list_address_txs**
> AddressTxs list_address_txs(currency, address)

Get all transactions an address has been involved in

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.height import Height
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address
    direction = "out" # str | Incoming or outgoing transactions (optional)
    min_height = Height(1) # Height | Return transactions starting from given height (optional)
    max_height = Height(2) # Height | Return transactions up to (including) given height (optional)
    order = "desc" # str | Sorting order (optional) if omitted the server will use the default value of "desc"
    token_currency = "WETH" # str | Return transactions of given token currency (optional)
    page = "" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all transactions an address has been involved in
        api_response = api_instance.list_address_txs(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_txs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all transactions an address has been involved in
        api_response = api_instance.list_address_txs(currency, address, direction=direction, min_height=min_height, max_height=max_height, order=order, token_currency=token_currency, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **direction** | **str**| Incoming or outgoing transactions | [optional]
 **min_height** | **Height**| Return transactions starting from given height | [optional]
 **max_height** | **Height**| Return transactions up to (including) given height | [optional]
 **order** | **str**| Sorting order | [optional] if omitted the server will use the default value of "desc"
 **token_currency** | **str**| Return transactions of given token currency | [optional]
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

# **list_tags_by_address**
> AddressTags list_tags_by_address(currency, address)

Get attribution tags for a given address

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import addresses_api
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address
    page = "" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)
    include_best_cluster_tag = False # bool | If the best cluster tag should be inherited to the address level, often helpful for exchanges where not every address is tagged. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get attribution tags for a given address
        api_response = api_instance.list_tags_by_address(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_tags_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get attribution tags for a given address
        api_response = api_instance.list_tags_by_address(currency, address, page=page, pagesize=pagesize, include_best_cluster_tag=include_best_cluster_tag)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_tags_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]
 **include_best_cluster_tag** | **bool**| If the best cluster tag should be inherited to the address level, often helpful for exchanges where not every address is tagged. | [optional] if omitted the server will use the default value of False
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

