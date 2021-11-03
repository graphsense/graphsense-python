# graphsense.TagsApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_concepts**](TagsApi.md#list_concepts) | **GET** /tags/taxonomies/{taxonomy}/concepts | Returns the supported concepts of a taxonomy
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | Returns address and entity tags associated with a given label
[**list_taxonomies**](TagsApi.md#list_taxonomies) | **GET** /tags/taxonomies | Returns the supported taxonomies


# **list_concepts**
> [Concept] list_concepts(taxonomy)

Returns the supported concepts of a taxonomy

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import tags_api
from graphsense.model.concept import Concept
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
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
    api_instance = tags_api.TagsApi(api_client)
    taxonomy = "foo" # str | The taxonomy

    # example passing only required values which don't have defaults set
    try:
        # Returns the supported concepts of a taxonomy
        api_response = api_instance.list_concepts(taxonomy)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TagsApi->list_concepts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy** | **str**| The taxonomy |
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**[Concept]**](Concept.md)

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

# **list_tags**
> [Tags] list_tags(label)

Returns address and entity tags associated with a given label

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import tags_api
from graphsense.model.tags import Tags
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
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
    api_instance = tags_api.TagsApi(api_client)
    label = "cimedy" # str | The label of an entity
    currency = "btc" # str | The cryptocurrency (e.g., btc) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns address and entity tags associated with a given label
        api_response = api_instance.list_tags(label)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns address and entity tags associated with a given label
        api_response = api_instance.list_tags(label, currency=currency)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| The label of an entity |
 **currency** | **str**| The cryptocurrency (e.g., btc) | [optional]
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**[Tags]**](Tags.md)

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

# **list_taxonomies**
> [Taxonomy] list_taxonomies()

Returns the supported taxonomies

### Example

* Api Key Authentication (api_key):
```python
import time
import graphsense
from graphsense.api import tags_api
from graphsense.model.taxonomy import Taxonomy
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
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
    api_instance = tags_api.TagsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the supported taxonomies
        api_response = api_instance.list_taxonomies()
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TagsApi->list_taxonomies: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.
**_preload_content** | **bool** | If False, the urllib3.HTTPResponse object will be returned without reading/decoding response data. | [optional] default is True. 
**async_req** | **bool** | Execute request asynchronously | [optional] default is False.

### Return type

[**[Taxonomy]**](Taxonomy.md)

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

