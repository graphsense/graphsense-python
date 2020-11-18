# graphsense-python

GraphSense API

This Python package is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.4.5
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements

Python 2.7 and 3.4+

## Installation and Usage
### pip install

If the Python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/graphsense/graphsense-python.git
```

Then import the package:
```python
import graphsense
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import graphsense
```


### Generate from OpenAPI specification

In order to generate the client from
[GraphSense's OpenAPI specification](https://github.com/graphsense/graphsense-openapi)
run the [OpenAPI Generator CLI](https://openapi-generator.tech/),
e.g. using docker:

```
    URL=https://github.com/graphsense/graphsense-openapi/blob/master/graphsense.yaml
    docker run --rm \
      -v "${PWD}:/build" \
      openapitools/openapi-generator-cli:latest-release \
      generate -i "$URL" \
        -g python \
        -o /build
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run
the following:

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
    api_instance = graphsense.AddressesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
address = '1Archive1n2C579dMsAu3iC6tWzuQJz8dN' # str | The cryptocurrency address

    try:
        # Get an address with tags
        api_response = api_instance.get_address_entity(currency, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->get_address_entity: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://openapi_server:9000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressesApi* | [**get_address_entity**](docs/AddressesApi.md#get_address_entity) | **GET** /{currency}/addresses/{address}/entity | Get an address with tags
*AddressesApi* | [**get_address_with_tags**](docs/AddressesApi.md#get_address_with_tags) | **GET** /{currency}/addresses/{address} | Get an address with tags
*AddressesApi* | [**list_address_links**](docs/AddressesApi.md#list_address_links) | **GET** /{currency}/addresses/{address}/links | Get transactions between two addresses
*AddressesApi* | [**list_address_links_csv**](docs/AddressesApi.md#list_address_links_csv) | **GET** /{currency}/addresses/{address}/links.csv | Get transactions between two addresses as CSV
*AddressesApi* | [**list_address_neighbors**](docs/AddressesApi.md#list_address_neighbors) | **GET** /{currency}/addresses/{address}/neighbors | Get an addresses&#39; neighbors in the address graph
*AddressesApi* | [**list_address_neighbors_csv**](docs/AddressesApi.md#list_address_neighbors_csv) | **GET** /{currency}/addresses/{address}/neighbors.csv | Get an addresses&#39; neighbors in the address graph as CSV
*AddressesApi* | [**list_address_tags**](docs/AddressesApi.md#list_address_tags) | **GET** /{currency}/addresses/{address}/tags | Get attribution tags for a given address
*AddressesApi* | [**list_address_tags_csv**](docs/AddressesApi.md#list_address_tags_csv) | **GET** /{currency}/addresses/{address}/tags.csv | Get attribution tags for a given address
*AddressesApi* | [**list_address_txs**](docs/AddressesApi.md#list_address_txs) | **GET** /{currency}/addresses/{address}/txs | Get all transactions an address has been involved in
*AddressesApi* | [**list_address_txs_csv**](docs/AddressesApi.md#list_address_txs_csv) | **GET** /{currency}/addresses/{address}/txs.csv | Get all transactions an address has been involved in as CSV
*BlocksApi* | [**get_block**](docs/BlocksApi.md#get_block) | **GET** /{currency}/blocks/{height} | Get a block by its height
*BlocksApi* | [**list_block_txs**](docs/BlocksApi.md#list_block_txs) | **GET** /{currency}/blocks/{height}/txs | Get all blocks (100 per page)
*BlocksApi* | [**list_block_txs_csv**](docs/BlocksApi.md#list_block_txs_csv) | **GET** /{currency}/blocks/{height}/txs.csv | Get all blocks as CSV
*BlocksApi* | [**list_blocks**](docs/BlocksApi.md#list_blocks) | **GET** /{currency}/blocks | Get all blocks
*EntitiesApi* | [**get_entity_with_tags**](docs/EntitiesApi.md#get_entity_with_tags) | **GET** /{currency}/entities/{entity} | Get an entity with tags
*EntitiesApi* | [**list_entity_addresses**](docs/EntitiesApi.md#list_entity_addresses) | **GET** /{currency}/entities/{entity}/addresses | Get an entity&#39;s addresses
*EntitiesApi* | [**list_entity_addresses_csv**](docs/EntitiesApi.md#list_entity_addresses_csv) | **GET** /{currency}/entities/{entity}/addresses.csv | Get an entity&#39;s addresses as CSV
*EntitiesApi* | [**list_entity_neighbors**](docs/EntitiesApi.md#list_entity_neighbors) | **GET** /{currency}/entities/{entity}/neighbors | Get an entity&#39;s neighbors in the entity graph
*EntitiesApi* | [**list_entity_neighbors_csv**](docs/EntitiesApi.md#list_entity_neighbors_csv) | **GET** /{currency}/entities/{entity}/neighbors.csv | Get an entity&#39;s neighbors in the entity graph as CSV
*EntitiesApi* | [**list_entity_tags**](docs/EntitiesApi.md#list_entity_tags) | **GET** /{currency}/entities/{entity}/tags | Get attribution tags for a given entity
*EntitiesApi* | [**list_entity_tags_csv**](docs/EntitiesApi.md#list_entity_tags_csv) | **GET** /{currency}/entities/{entity}/tags.csv | Get attribution tags for a given entity as CSV
*EntitiesApi* | [**search_entity_neighbors**](docs/EntitiesApi.md#search_entity_neighbors) | **GET** /{currency}/entities/{entity}/search | Search deeply for matching neighbors
*GeneralApi* | [**get_statistics**](docs/GeneralApi.md#get_statistics) | **GET** /stats | Get statistics of supported currencies
*GeneralApi* | [**search**](docs/GeneralApi.md#search) | **GET** /search | Returns matching addresses, transactions and labels
*RatesApi* | [**get_exchange_rates**](docs/RatesApi.md#get_exchange_rates) | **GET** /{currency}/rates/{height} | Returns exchange rate for a given height
*TagsApi* | [**list_concepts**](docs/TagsApi.md#list_concepts) | **GET** /tags/taxonomies/{taxonomy}/concepts | Returns the supported concepts of a taxonomy
*TagsApi* | [**list_tags**](docs/TagsApi.md#list_tags) | **GET** /tags | Returns the tags associated with a given label
*TagsApi* | [**list_taxonomies**](docs/TagsApi.md#list_taxonomies) | **GET** /tags/taxonomies | Returns the supported taxonomies
*TxsApi* | [**get_tx**](docs/TxsApi.md#get_tx) | **GET** /{currency}/txs/{tx_hash} | Returns details of a specific transaction identified by its hash.
*TxsApi* | [**list_txs**](docs/TxsApi.md#list_txs) | **GET** /{currency}/txs | Returns transactions


## Documentation for Models

 - [Address](docs/Address.md)
 - [AddressTx](docs/AddressTx.md)
 - [AddressTxs](docs/AddressTxs.md)
 - [AddressWithTags](docs/AddressWithTags.md)
 - [AddressWithTagsAllOf](docs/AddressWithTagsAllOf.md)
 - [Block](docs/Block.md)
 - [BlockTxSummary](docs/BlockTxSummary.md)
 - [BlockTxs](docs/BlockTxs.md)
 - [Blocks](docs/Blocks.md)
 - [Concept](docs/Concept.md)
 - [CurrencyStats](docs/CurrencyStats.md)
 - [Entity](docs/Entity.md)
 - [EntityAddresses](docs/EntityAddresses.md)
 - [EntityWithTags](docs/EntityWithTags.md)
 - [EntityWithTagsAllOf](docs/EntityWithTagsAllOf.md)
 - [Link](docs/Link.md)
 - [Neighbor](docs/Neighbor.md)
 - [Neighbors](docs/Neighbors.md)
 - [Rates](docs/Rates.md)
 - [RatesRates](docs/RatesRates.md)
 - [SearchPaths](docs/SearchPaths.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultByCurrency](docs/SearchResultByCurrency.md)
 - [Stats](docs/Stats.md)
 - [StatsLedger](docs/StatsLedger.md)
 - [StatsLedgerVersion](docs/StatsLedgerVersion.md)
 - [StatsNote](docs/StatsNote.md)
 - [StatsTagsSource](docs/StatsTagsSource.md)
 - [StatsTool](docs/StatsTool.md)
 - [StatsVersion](docs/StatsVersion.md)
 - [Tag](docs/Tag.md)
 - [Taxonomy](docs/Taxonomy.md)
 - [Tx](docs/Tx.md)
 - [TxSummary](docs/TxSummary.md)
 - [TxValue](docs/TxValue.md)
 - [Txs](docs/Txs.md)
 - [Values](docs/Values.md)


## Documentation for Authorization

## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header
