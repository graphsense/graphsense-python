# graphsense.BatchApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch**](BatchApi.md#batch) | **POST** /{currency}/batch | Get data as CSV in batch


# **batch**
> str batch(currency)

Get data as CSV in batch

### Example

```python
import time
import graphsense
from graphsense.api import batch_api
from graphsense.model.batch_operation import BatchOperation
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = batch_api.BatchApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    batch_operation = BatchOperation(
        api="txs",
        operation="get_tx_io",
        parameters=[
            GetTxIoParameters(
                io=Io("inputs"),
                tx_hash="tx_hash_example",
            ),
        ],
    ) # BatchOperation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data as CSV in batch
        api_response = api_instance.batch(currency)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BatchApi->batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data as CSV in batch
        api_response = api_instance.batch(currency, batch_operation=batch_operation)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BatchApi->batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **batch_operation** | [**BatchOperation**](BatchOperation.md)|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

