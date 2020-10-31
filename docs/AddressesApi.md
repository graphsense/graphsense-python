# graphsense.AddressesApi

All URIs are relative to *http://openapi_server:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_with_tags**](AddressesApi.md#get_address_with_tags) | **GET** /{currency}/addresses/{address} | Get an address with tags
[**list_address_neighbors**](AddressesApi.md#list_address_neighbors) | **GET** /{currency}/addresses/{address}/neighbors | Get an addresses&#39; neighbors in the address graph
[**list_address_tags**](AddressesApi.md#list_address_tags) | **GET** /{currency}/addresses/{address}/tags | Get attribution tags for a given address
[**list_address_tags_csv**](AddressesApi.md#list_address_tags_csv) | **GET** /{currency}/addresses/{address}/tags.csv | Get attribution tags for a given address
[**list_address_txs**](AddressesApi.md#list_address_txs) | **GET** /{currency}/addresses/{address}/txs | Get all transactions an address has been involved in


# **get_address_with_tags**
> AddressWithTags get_address_with_tags(currency, address)

Get an address with tags

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
    api_instance = graphsense.AddressesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
address = '3Hrnn1UN78uXgLNvtqVXMjHwB41PmX66X4' # str | The cryptocurrency address

    try:
        # Get an address with tags
        api_response = api_instance.get_address_with_tags(currency, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->get_address_with_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **address** | **str**| The cryptocurrency address | 

### Return type

[**AddressWithTags**](AddressWithTags.md)

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
> Neighbors list_address_neighbors(currency, address, direction, page=page, pagesize=pagesize)

Get an addresses' neighbors in the address graph

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
    api_instance = graphsense.AddressesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
address = '3Hrnn1UN78uXgLNvtqVXMjHwB41PmX66X4' # str | The cryptocurrency address
direction = 'out' # str | Incoming or outgoing neighbors
page = '0400030bff00f07fffff9b00' # str | Resumption token for retrieving the next page (optional)
pagesize = 10 # int | Number of items returned in a single page (optional)

    try:
        # Get an addresses' neighbors in the address graph
        api_response = api_instance.list_address_neighbors(currency, address, direction, page=page, pagesize=pagesize)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->list_address_neighbors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **address** | **str**| The cryptocurrency address | 
 **direction** | **str**| Incoming or outgoing neighbors | 
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

# **list_address_tags**
> list[Tag] list_address_tags(currency, address)

Get attribution tags for a given address

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
    api_instance = graphsense.AddressesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
address = '3Hrnn1UN78uXgLNvtqVXMjHwB41PmX66X4' # str | The cryptocurrency address

    try:
        # Get attribution tags for a given address
        api_response = api_instance.list_address_tags(currency, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->list_address_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **address** | **str**| The cryptocurrency address | 

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

# **list_address_tags_csv**
> list[Tag] list_address_tags_csv(currency, address)

Get attribution tags for a given address

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
    api_instance = graphsense.AddressesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
address = '3Hrnn1UN78uXgLNvtqVXMjHwB41PmX66X4' # str | The cryptocurrency address

    try:
        # Get attribution tags for a given address
        api_response = api_instance.list_address_tags_csv(currency, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->list_address_tags_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **address** | **str**| The cryptocurrency address | 

### Return type

[**list[Tag]**](Tag.md)

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

# **list_address_txs**
> AddressTxs list_address_txs(currency, address, page=page, pagesize=pagesize)

Get all transactions an address has been involved in

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
    api_instance = graphsense.AddressesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
address = '3Hrnn1UN78uXgLNvtqVXMjHwB41PmX66X4' # str | The cryptocurrency address
page = '0400030bff00f07fffff9b00' # str | Resumption token for retrieving the next page (optional)
pagesize = 10 # int | Number of items returned in a single page (optional)

    try:
        # Get all transactions an address has been involved in
        api_response = api_instance.list_address_txs(currency, address, page=page, pagesize=pagesize)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->list_address_txs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) | 
 **address** | **str**| The cryptocurrency address | 
 **page** | **str**| Resumption token for retrieving the next page | [optional] 
 **pagesize** | **int**| Number of items returned in a single page | [optional] 

### Return type

[**AddressTxs**](AddressTxs.md)

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

