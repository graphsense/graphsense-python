# graphsense.TxsApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tx**](TxsApi.md#get_tx) | **GET** /{currency}/txs/{tx_hash} | Returns details of a specific transaction identified by its hash.
[**get_tx_io**](TxsApi.md#get_tx_io) | **GET** /{currency}/txs/{tx_hash}/{io} | Returns input/output values of a specific transaction identified by its hash.


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
    include_io = False # bool | Whether to include inputs/outputs of a transaction (UTXO only) (optional) if omitted the server will use the default value of False

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
        api_response = api_instance.get_tx(currency, tx_hash, include_io=include_io)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TxsApi->get_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **tx_hash** | **str**| The transaction hash |
 **include_io** | **bool**| Whether to include inputs/outputs of a transaction (UTXO only) | [optional] if omitted the server will use the default value of False

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

# **get_tx_io**
> TxValues get_tx_io(currency, tx_hash, io)

Returns input/output values of a specific transaction identified by its hash.

### Example

```python
import time
import graphsense
from graphsense.api import txs_api
from graphsense.model.tx_values import TxValues
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
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **tx_hash** | **str**| The transaction hash |
 **io** | **str**| Input or outpus values of a transaction |

### Return type

[**TxValues**](TxValues.md)

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

