# graphsense.AddressesApi

All URIs are relative to *http://graphsense-rest:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](AddressesApi.md#get_address) | **GET** /{currency}/addresses/{address} | Get an address, optionally with tags
[**get_address_entity**](AddressesApi.md#get_address_entity) | **GET** /{currency}/addresses/{address}/entity | Get the entity of an address
[**list_address_links**](AddressesApi.md#list_address_links) | **GET** /{currency}/addresses/{address}/links | Get transactions between two addresses
[**list_address_links_csv**](AddressesApi.md#list_address_links_csv) | **GET** /{currency}/addresses/{address}/links.csv | Get transactions between two addresses as CSV
[**list_address_neighbors**](AddressesApi.md#list_address_neighbors) | **GET** /{currency}/addresses/{address}/neighbors | Get an addresses&#39; neighbors in the address graph
[**list_address_neighbors_csv**](AddressesApi.md#list_address_neighbors_csv) | **GET** /{currency}/addresses/{address}/neighbors.csv | Get an addresses&#39; neighbors in the address graph as CSV
[**list_address_txs**](AddressesApi.md#list_address_txs) | **GET** /{currency}/addresses/{address}/txs | Get all transactions an address has been involved in
[**list_address_txs_csv**](AddressesApi.md#list_address_txs_csv) | **GET** /{currency}/addresses/{address}/txs.csv | Get all transactions an address has been involved in as CSV
[**list_addresses**](AddressesApi.md#list_addresses) | **GET** /{currency}/addresses | Get addresses
[**list_addresses_csv**](AddressesApi.md#list_addresses_csv) | **GET** /{currency}/addresses.csv | Get addresses as CSV
[**list_tags_by_address**](AddressesApi.md#list_tags_by_address) | **GET** /{currency}/addresses/{address}/tags | Get attribution tags for a given address
[**list_tags_by_address_csv**](AddressesApi.md#list_tags_by_address_csv) | **GET** /{currency}/addresses/{address}/tags.csv | Get attribution tags for a given address


# **get_address**
> Address get_address(currency, address)

Get an address, optionally with tags

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.address import Address
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address
    include_tags = False # bool | Whether tags should be included (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get an address, optionally with tags
        api_response = api_instance.get_address(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an address, optionally with tags
        api_response = api_instance.get_address(currency, address, include_tags=include_tags)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **include_tags** | **bool**| Whether tags should be included | [optional] if omitted the server will use the default value of False

### Return type

[**Address**](Address.md)

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

# **get_address_entity**
> Entity get_address_entity(currency, address)

Get the entity of an address

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.entity import Entity
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address
    include_tags = False # bool | Whether tags should be included (optional) if omitted the server will use the default value of False
    tag_coherence = False # bool | Whether to calculate coherence of address tags (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get the entity of an address
        api_response = api_instance.get_address_entity(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the entity of an address
        api_response = api_instance.get_address_entity(currency, address, include_tags=include_tags, tag_coherence=tag_coherence)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **include_tags** | **bool**| Whether tags should be included | [optional] if omitted the server will use the default value of False
 **tag_coherence** | **bool**| Whether to calculate coherence of address tags | [optional] if omitted the server will use the default value of False

### Return type

[**Entity**](Entity.md)

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

# **list_address_links**
> Links list_address_links(currency, address, neighbor)

Get transactions between two addresses

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.links import Links
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address
    neighbor = "addressE" # str | Neighbor address

    # example passing only required values which don't have defaults set
    try:
        # Get transactions between two addresses
        api_response = api_instance.list_address_links(currency, address, neighbor)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **neighbor** | **str**| Neighbor address |

### Return type

[**Links**](Links.md)

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

# **list_address_links_csv**
> str list_address_links_csv(currency, address, neighbor)

Get transactions between two addresses as CSV

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address
    neighbor = "addressE" # str | Neighbor address

    # example passing only required values which don't have defaults set
    try:
        # Get transactions between two addresses as CSV
        api_response = api_instance.list_address_links_csv(currency, address, neighbor)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_links_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **neighbor** | **str**| Neighbor address |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address_neighbors**
> Neighbors list_address_neighbors(currency, address, direction)

Get an addresses' neighbors in the address graph

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.neighbors import Neighbors
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address
    direction = "out" # str | Incoming or outgoing neighbors
    include_labels = False # bool | Whether labels of tags should be included (optional) if omitted the server will use the default value of False
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an addresses' neighbors in the address graph
        api_response = api_instance.list_address_neighbors(currency, address, direction)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_neighbors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an addresses' neighbors in the address graph
        api_response = api_instance.list_address_neighbors(currency, address, direction, include_labels=include_labels, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_neighbors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **direction** | **str**| Incoming or outgoing neighbors |
 **include_labels** | **bool**| Whether labels of tags should be included | [optional] if omitted the server will use the default value of False
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]

### Return type

[**Neighbors**](Neighbors.md)

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

# **list_address_neighbors_csv**
> str list_address_neighbors_csv(currency, address, direction)

Get an addresses' neighbors in the address graph as CSV

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address
    direction = "out" # str | Incoming or outgoing neighbors
    include_labels = False # bool | Whether labels of tags should be included (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get an addresses' neighbors in the address graph as CSV
        api_response = api_instance.list_address_neighbors_csv(currency, address, direction)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_neighbors_csv: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an addresses' neighbors in the address graph as CSV
        api_response = api_instance.list_address_neighbors_csv(currency, address, direction, include_labels=include_labels)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_neighbors_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **direction** | **str**| Incoming or outgoing neighbors |
 **include_labels** | **bool**| Whether labels of tags should be included | [optional] if omitted the server will use the default value of False

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address_txs**
> TxsAccount list_address_txs(currency, address)

Get all transactions an address has been involved in

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.txs_account import TxsAccount
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all transactions an address has been involved in
        api_response = api_instance.list_address_txs(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_txs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all transactions an address has been involved in
        api_response = api_instance.list_address_txs(currency, address, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]

### Return type

[**TxsAccount**](TxsAccount.md)

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

# **list_address_txs_csv**
> str list_address_txs_csv(currency, address)

Get all transactions an address has been involved in as CSV

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address

    # example passing only required values which don't have defaults set
    try:
        # Get all transactions an address has been involved in as CSV
        api_response = api_instance.list_address_txs_csv(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_address_txs_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addresses**
> Addresses list_addresses(currency)

Get addresses

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.addresses import Addresses
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    ids = [
        1,
    ] # [int] | Restrict result to given set of comma separated IDs (optional)
    page = "page_example" # str | Resumption token for retrieving the next page (optional)
    pagesize = 10 # int | Number of items returned in a single page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get addresses
        api_response = api_instance.list_addresses(currency)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_addresses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get addresses
        api_response = api_instance.list_addresses(currency, ids=ids, page=page, pagesize=pagesize)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **ids** | **[int]**| Restrict result to given set of comma separated IDs | [optional]
 **page** | **str**| Resumption token for retrieving the next page | [optional]
 **pagesize** | **int**| Number of items returned in a single page | [optional]

### Return type

[**Addresses**](Addresses.md)

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

# **list_addresses_csv**
> str list_addresses_csv(currency, ids)

Get addresses as CSV

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    ids = [
        "ids_example",
    ] # [str] | Set of comma separated IDs

    # example passing only required values which don't have defaults set
    try:
        # Get addresses as CSV
        api_response = api_instance.list_addresses_csv(currency, ids)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_addresses_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **ids** | **[str]**| Set of comma separated IDs |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_by_address**
> [AddressTag] list_tags_by_address(currency, address)

Get attribution tags for a given address

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from graphsense.model.address_tag import AddressTag
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address

    # example passing only required values which don't have defaults set
    try:
        # Get attribution tags for a given address
        api_response = api_instance.list_tags_by_address(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_tags_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |

### Return type

[**[AddressTag]**](AddressTag.md)

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

# **list_tags_by_address_csv**
> str list_tags_by_address_csv(currency, address)

Get attribution tags for a given address

### Example

```python
import time
import graphsense
from graphsense.api import addresses_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://graphsense-rest:9000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency (e.g., btc)
    address = "addressA" # str | The cryptocurrency address

    # example passing only required values which don't have defaults set
    try:
        # Get attribution tags for a given address
        api_response = api_instance.list_tags_by_address_csv(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->list_tags_by_address_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The cryptocurrency (e.g., btc) |
 **address** | **str**| The cryptocurrency address |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

