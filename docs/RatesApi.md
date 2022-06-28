# graphsense.RatesApi

All URIs are relative to *http://localhost:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rates**](RatesApi.md#get_exchange_rates) | **GET** /{currency}/rates/{height} | Returns exchange rate for a given height


# **get_exchange_rates**
> Rates get_exchange_rates(currency, height)

Returns exchange rate for a given height

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import rates_api
from graphsense.model.rates import Rates
from graphsense.model.height import Height
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://localhost:9000"
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
    api_instance = rates_api.RatesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    height = Height(1) # Height | The block height

    # example passing only required values which don't have defaults set
    try:
        # Returns exchange rate for a given height
        api_response = api_instance.get_exchange_rates(currency, height)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling RatesApi->get_exchange_rates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency code (e.g., btc) |
 **height** | **Height**| The block height |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**Rates**](Rates.md)

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

