# graphsense.TokensApi

All URIs are relative to *https://api.ikna.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_supported_tokens**](TokensApi.md#list_supported_tokens) | **GET** /{currency}/supported_tokens | Returns a list of supported token (sub)currencies


# **list_supported_tokens**
> TokenConfigs list_supported_tokens(currency)

Returns a list of supported token (sub)currencies

### Example

* Api Key Authentication (api_key):
```python
import time
from dateutil.parser import parse as dateutil_parser
import graphsense
from graphsense.api import tokens_api
from graphsense.model.token_configs import TokenConfigs
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
    api_instance = tokens_api.TokensApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of supported token (sub)currencies
        api_response = api_instance.list_supported_tokens(currency)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TokensApi->list_supported_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**TokenConfigs**](TokenConfigs.md)

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

