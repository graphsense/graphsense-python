# graphsense.TxsApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tx**](TxsApi.md#get_tx) | **GET** /{currency}/txs/{tx_hash} | Returns details of a specific transaction identified by its hash.
[**list_txs**](TxsApi.md#list_txs) | **GET** /{currency}/txs | Returns transactions


# **get_tx**
> Tx get_tx(currency, tx_hash)

Returns details of a specific transaction identified by its hash.

### Example

```python
import time
import graphsense
from graphsense.api import txs_api
from graphsense.model.tx import Tx
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = txs_api.TxsApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    tx_hash = "ab188013" # str | The transaction hash

    # example passing only required values which don't have defaults set
    try:
        # Returns details of a specific transaction identified by its hash.
        api_response = api_instance.get_tx(currency, tx_hash)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->get_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **tx_hash** | **str**| The transaction hash |

### Return type

[**Tx**](Tx.md)

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

# **list_txs**
> Txs list_txs(currency)

Returns transactions

### Example

```python
import time
import graphsense
from graphsense.api import txs_api
from graphsense.model.txs import Txs
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = txs_api.TxsApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    page = "page_example" # str | Resumption token for retrieving the next page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns transactions
        api_response = api_instance.list_txs(currency)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->list_txs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns transactions
        api_response = api_instance.list_txs(currency, page=page)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->list_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **page** | **str**| Resumption token for retrieving the next page | [optional]

### Return type

[**Txs**](Txs.md)

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

