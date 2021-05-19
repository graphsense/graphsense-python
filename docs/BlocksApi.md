# graphsense.BlocksApi

All URIs are relative to *http://openapi_server:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block**](BlocksApi.md#get_block) | **GET** /{currency}/blocks/{height} | Get a block by its height
[**list_block_txs**](BlocksApi.md#list_block_txs) | **GET** /{currency}/blocks/{height}/txs | Get block transactions (100 per page)
[**list_block_txs_csv**](BlocksApi.md#list_block_txs_csv) | **GET** /{currency}/blocks/{height}/txs.csv | Get block transactions as CSV
[**list_blocks**](BlocksApi.md#list_blocks) | **GET** /{currency}/blocks | Get all blocks


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
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blocks_api.BlocksApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    height = 1 # int | The block height

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
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **height** | **int**| The block height |

### Return type

[**Block**](Block.md)

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
> [BlockTx] list_block_txs(currency, height)

Get block transactions (100 per page)

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import blocks_api
from graphsense.model.block_tx import BlockTx
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
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blocks_api.BlocksApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    height = 1 # int | The block height

    # example passing only required values which don't have defaults set
    try:
        # Get block transactions (100 per page)
        api_response = api_instance.list_block_txs(currency, height)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BlocksApi->list_block_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **height** | **int**| The block height |

### Return type

[**[BlockTx]**](BlockTx.md)

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

# **list_block_txs_csv**
> str list_block_txs_csv(currency, height)

Get block transactions as CSV

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import blocks_api
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
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blocks_api.BlocksApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    height = 1 # int | The block height

    # example passing only required values which don't have defaults set
    try:
        # Get block transactions as CSV
        api_response = api_instance.list_block_txs_csv(currency, height)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BlocksApi->list_block_txs_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **height** | **int**| The block height |

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

# **list_blocks**
> Blocks list_blocks(currency)

Get all blocks

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import blocks_api
from graphsense.model.blocks import Blocks
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
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blocks_api.BlocksApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    page = "0400030bff00f07fffff9b00" # str | Resumption token for retrieving the next page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all blocks
        api_response = api_instance.list_blocks(currency)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BlocksApi->list_blocks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all blocks
        api_response = api_instance.list_blocks(currency, page=page)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BlocksApi->list_blocks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **page** | **str**| Resumption token for retrieving the next page | [optional]

### Return type

[**Blocks**](Blocks.md)

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

