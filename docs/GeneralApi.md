# graphsense.GeneralApi

All URIs are relative to *http://openapi_server:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics**](GeneralApi.md#get_statistics) | **GET** /stats | Get statistics of supported currencies


# **get_statistics**
> Stats get_statistics()

Get statistics of supported currencies

### Example

```python
from __future__ import print_function
import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graphsense.GeneralApi(api_client)
    
    try:
        # Get statistics of supported currencies
        api_response = api_instance.get_statistics()
        pprint(api_response)
    except ApiException as e:
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

