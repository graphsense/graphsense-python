# graphsense.RatesApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rates**](RatesApi.md#get_exchange_rates) | **GET** /{currency}/rates/{height} | Returns exchange rate for a given height


# **get_exchange_rates**
> Rates get_exchange_rates(currency, height)

Returns exchange rate for a given height

### Example

```python
import time
import graphsense
from graphsense.api import rates_api
from graphsense.model.rates import Rates
from graphsense.model.height import Height
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rates_api.RatesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
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
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **height** | **Height**| The block height |

### Return type

[**Rates**](Rates.md)

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

