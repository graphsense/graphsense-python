# graphsense.TagsApi

All URIs are relative to *http://openapi_server:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_concepts**](TagsApi.md#list_concepts) | **GET** /tags/taxonomies/{taxonomy}/concepts | Returns the supported concepts of a taxonomy
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags | Returns the tags associated with a given label
[**list_taxonomies**](TagsApi.md#list_taxonomies) | **GET** /tags/taxonomies | Returns the supported taxonomies


# **list_concepts**
> list[Concept] list_concepts(taxonomy)

Returns the supported concepts of a taxonomy

### Example

* Api Key Authentication (api_key):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.TagsApi(api_client)
    taxonomy = 'foo' # str | The taxonomy

    try:
        # Returns the supported concepts of a taxonomy
        api_response = api_instance.list_concepts(taxonomy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->list_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy** | **str**| The taxonomy | 

### Return type

[**list[Concept]**](Concept.md)

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
> list[Tag] list_tags(label, currency=currency)

Returns the tags associated with a given label

### Example

* Api Key Authentication (api_key):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.TagsApi(api_client)
    label = 'cimedy' # str | The label of an entity
currency = 'btc' # str | The cryptocurrency (e.g., btc) (optional)

    try:
        # Returns the tags associated with a given label
        api_response = api_instance.list_tags(label, currency=currency)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| The label of an entity | 
 **currency** | **str**| The cryptocurrency (e.g., btc) | [optional] 

### Return type

[**list[Tag]**](Tag.md)

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
> list[Taxonomy] list_taxonomies()

Returns the supported taxonomies

### Example

* Api Key Authentication (api_key):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = graphsense.Configuration(
    host = "http://openapi_server:9000",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.TagsApi(api_client)
    
    try:
        # Returns the supported taxonomies
        api_response = api_instance.list_taxonomies()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->list_taxonomies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Taxonomy]**](Taxonomy.md)

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

