# graphsense.GeneralApi

All URIs are relative to *https://api.test.ikna.io*

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
# Defining the host is optional and defaults to https://api.test.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.test.ikna.io"
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
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**Stats**](Stats.md)

**Notes:**

* If `async_req` parameter is True, the request will be called asynchronously.  The method will return the request thread.  If parameter `async_req` is False or missing, then the method will return the response directly.

* If the HTTP response code is `429 Too Many Requests` due to rate limit policies, the underlying `urllib3` HTTP client will automatically stall the request as long as advised by the `Retry-After` header.

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

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import general_api
from graphsense.model.search_result import SearchResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.test.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.test.ikna.io"
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
    api_instance = general_api.GeneralApi(api_client)
    q = "foo" # str | It can be (the beginning of) an address, a transaction or a label
    currency = "btc" # str | The cryptocurrency (e.g., btc) (optional)
    limit = 10 # int | Maximum number of search results (optional) if omitted the server will use the default value of 10

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
 **limit** | **int**| Maximum number of search results | [optional] if omitted the server will use the default value of 10
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**SearchResult**](SearchResult.md)

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

