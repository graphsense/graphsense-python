# graphsense.BlocksApi

All URIs are relative to *https://api.ikna.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block**](BlocksApi.md#get_block) | **GET** /{currency}/blocks/{height} | Get a block by its height
[**get_block_by_date**](BlocksApi.md#get_block_by_date) | **GET** /{currency}/block_by_date/{date} | Get the closest blocks given a timestamp
[**list_block_txs**](BlocksApi.md#list_block_txs) | **GET** /{currency}/blocks/{height}/txs | Get block transactions


# **get_block**
> Block get_block(currency, height)

Get a block by its height

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import blocks_api
from graphsense.model.block import Block
from graphsense.model.height import Height
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
    api_instance = blocks_api.BlocksApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    height = Height(1) # Height | The block height

    # example passing only required values which don't have defaults set
    try:
        # Get a block by its height
        api_response = api_instance.get_block(currency, height)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BlocksApi->get_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **height** | **Height**| The block height |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**Block**](Block.md)

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

# **get_block_by_date**
> BlockAtDate get_block_by_date(currency, date)

Get the closest blocks given a timestamp

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from dateutil.parser import parse
from graphsense.api import blocks_api
from graphsense.model.block_at_date import BlockAtDate
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
    api_instance = blocks_api.BlocksApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    date = parse('2017-07-21T17:32:28Z') # datetime | The time of the block

    # example passing only required values which don't have defaults set
    try:
        # Get the closest blocks given a timestamp
        api_response = api_instance.get_block_by_date(currency, date)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BlocksApi->get_block_by_date: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **date** | **datetime**| The time of the block |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**BlockAtDate**](BlockAtDate.md)

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

# **list_block_txs**
> [Tx] list_block_txs(currency, height)

Get block transactions

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import blocks_api
from graphsense.model.tx import Tx
from graphsense.model.height import Height
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
    api_instance = blocks_api.BlocksApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    height = Height(1) # Height | The block height

    # example passing only required values which don't have defaults set
    try:
        # Get block transactions
        api_response = api_instance.list_block_txs(currency, height)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BlocksApi->list_block_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **height** | **Height**| The block height |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**[Tx]**](Tx.md)

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

