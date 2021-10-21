# graphsense.BulkApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk**](BulkApi.md#bulk) | **POST** /{currency}/bulk/{api}/{operation} | Get data as CSV or JSON in bulk


# **bulk**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] bulk(currency, api, operation, body)

Get data as CSV or JSON in bulk

### Example

```python
import time
import graphsense
from graphsense.api import bulk_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bulk_api.BulkApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    api = "blocks" # str | The api of the operation to execute in bulk
    operation = "get_block" # str | The operation to execute in bulk
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Map of the operation's parameter names to (arrays of) values
    form = "csv" # str | The response data format (optional) if omitted the server will use the default value of "csv"

    # example passing only required values which don't have defaults set
    try:
        # Get data as CSV or JSON in bulk
        api_response = api_instance.bulk(currency, api, operation, body)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BulkApi->bulk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data as CSV or JSON in bulk
        api_response = api_instance.bulk(currency, api, operation, body, form=form)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BulkApi->bulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **api** | **str**| The api of the operation to execute in bulk |
 **operation** | **str**| The operation to execute in bulk |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Map of the operation&#39;s parameter names to (arrays of) values |
 **form** | **str**| The response data format | [optional] if omitted the server will use the default value of "csv"

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

