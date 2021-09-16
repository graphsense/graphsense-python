# graphsense.GeneralApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics**](GeneralApi.md#get_statistics) | **GET** /stats | Get statistics of supported currencies
[**search**](GeneralApi.md#search) | **GET** /search | Returns matching addresses, transactions and labels


# **get_statistics**
> Stats get_statistics()

Get statistics of supported currencies

### Example

```python
import time
import graphsense
from graphsense.api import general_api
from graphsense.model.stats import Stats
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = general_api.GeneralApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get statistics of supported currencies
        api_response = api_instance.get_statistics()
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling GeneralApi->get_statistics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Stats**](Stats.md)

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

# **search**
> SearchResult search(q)

Returns matching addresses, transactions and labels

### Example

```python
import time
import graphsense
from graphsense.api import general_api
from graphsense.model.search_result import SearchResult
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = general_api.GeneralApi(api_client)
    q = "foo" # str | It can be (the beginning of) an address, a transaction or a label
    currency = "btc" # str | The cryptocurrency (e.g., btc) (optional)
    limit = 10 # int | Maximum number of search results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns matching addresses, transactions and labels
        api_response = api_instance.search(q)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling GeneralApi->search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns matching addresses, transactions and labels
        api_response = api_instance.search(q, currency=currency, limit=limit)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling GeneralApi->search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| It can be (the beginning of) an address, a transaction or a label |
 **currency** | **str**| The cryptocurrency (e.g., btc) | [optional]
 **limit** | **int**| Maximum number of search results | [optional]

### Return type

[**SearchResult**](SearchResult.md)

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

