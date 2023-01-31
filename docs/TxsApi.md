# graphsense.TxsApi

All URIs are relative to *https://api.ikna.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tx**](TxsApi.md#get_tx) | **GET** /{currency}/txs/{tx_hash} | Returns details of a specific transaction identified by its hash.
[**get_tx_io**](TxsApi.md#get_tx_io) | **GET** /{currency}/txs/{tx_hash}/{io} | Returns input/output values of a specific transaction identified by its hash.
[**list_token_txs**](TxsApi.md#list_token_txs) | **GET** /{currency}/token_txs/{tx_hash} | Returns all token transactions in a given transaction


# **get_tx**
> Tx get_tx(currency, tx_hash)

Returns details of a specific transaction identified by its hash.

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import txs_api
from graphsense.model.tx import Tx
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
    api_instance = txs_api.TxsApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    tx_hash = "ab188013" # str | The transaction hash
    include_io = False # bool | Whether to include inputs/outputs of a transaction (UTXO only) (optional) if omitted the server will use the default value of False
    token_tx_id = 1 # int | Select a specific token_transaction (Account model only) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns details of a specific transaction identified by its hash.
        api_response = api_instance.get_tx(currency, tx_hash)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->get_tx: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns details of a specific transaction identified by its hash.
        api_response = api_instance.get_tx(currency, tx_hash, include_io=include_io, token_tx_id=token_tx_id)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->get_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **tx_hash** | **str**| The transaction hash |
 **include_io** | **bool**| Whether to include inputs/outputs of a transaction (UTXO only) | [optional] if omitted the server will use the default value of False
 **token_tx_id** | **int**| Select a specific token_transaction (Account model only) | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**Tx**](Tx.md)

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

# **get_tx_io**
> TxValues get_tx_io(currency, tx_hash, io)

Returns input/output values of a specific transaction identified by its hash.

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import txs_api
from graphsense.model.tx_values import TxValues
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
    api_instance = txs_api.TxsApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    tx_hash = "ab188013" # str | The transaction hash
    io = "outputs" # str | Input or outpus values of a transaction

    # example passing only required values which don't have defaults set
    try:
        # Returns input/output values of a specific transaction identified by its hash.
        api_response = api_instance.get_tx_io(currency, tx_hash, io)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->get_tx_io: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **tx_hash** | **str**| The transaction hash |
 **io** | **str**| Input or outpus values of a transaction |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**TxValues**](TxValues.md)

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

# **list_token_txs**
> TxsAccount list_token_txs(currency, tx_hash)

Returns all token transactions in a given transaction

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import txs_api
from graphsense.model.txs_account import TxsAccount
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
    api_instance = txs_api.TxsApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    tx_hash = "ab188013" # str | The transaction hash

    # example passing only required values which don't have defaults set
    try:
        # Returns all token transactions in a given transaction
        api_response = api_instance.list_token_txs(currency, tx_hash)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->list_token_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **tx_hash** | **str**| The transaction hash |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**TxsAccount**](TxsAccount.md)

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

