# graphsense-python
GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.7.0
- Package version: 1.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

You can install graphsense-python via pypi using:

```sh
pip install graphsense-python
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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import graphsense
from pprint import pprint
from graphsense.api import addresses_api
from graphsense.model.address import Address
from graphsense.model.address_tags import AddressTags
from graphsense.model.address_txs import AddressTxs
from graphsense.model.entity import Entity
from graphsense.model.height import Height
from graphsense.model.links import Links
from graphsense.model.neighbor_addresses import NeighborAddresses
from graphsense.model.tag_summary import TagSummary
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
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address = "1Archive1n2C579dMsAu3iC6tWzuQJz8dN" # str | The cryptocurrency address
    include_actors = True # bool | Whether to include information about the actor behind the address (optional) (default to True)

    try:
        # Get an address
        api_response = api_instance.get_address(currency, address, include_actors=include_actors)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.ikna.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressesApi* | [**get_address**](docs/AddressesApi.md#get_address) | **GET** /{currency}/addresses/{address} | Get an address
*AddressesApi* | [**get_address_entity**](docs/AddressesApi.md#get_address_entity) | **GET** /{currency}/addresses/{address}/entity | Get the entity of an address
*AddressesApi* | [**get_tag_summary_by_address**](docs/AddressesApi.md#get_tag_summary_by_address) | **GET** /{currency}/addresses/{address}/tag_summary | Get attribution tag summary for a given address
*AddressesApi* | [**list_address_links**](docs/AddressesApi.md#list_address_links) | **GET** /{currency}/addresses/{address}/links | Get outgoing transactions between two addresses
*AddressesApi* | [**list_address_neighbors**](docs/AddressesApi.md#list_address_neighbors) | **GET** /{currency}/addresses/{address}/neighbors | Get an address&#39;s neighbors in the address graph
*AddressesApi* | [**list_address_txs**](docs/AddressesApi.md#list_address_txs) | **GET** /{currency}/addresses/{address}/txs | Get all transactions an address has been involved in
*AddressesApi* | [**list_tags_by_address**](docs/AddressesApi.md#list_tags_by_address) | **GET** /{currency}/addresses/{address}/tags | Get attribution tags for a given address
*BlocksApi* | [**get_block**](docs/BlocksApi.md#get_block) | **GET** /{currency}/blocks/{height} | Get a block by its height
*BlocksApi* | [**get_block_by_date**](docs/BlocksApi.md#get_block_by_date) | **GET** /{currency}/block_by_date/{date} | Get the closest blocks given a timestamp
*BlocksApi* | [**list_block_txs**](docs/BlocksApi.md#list_block_txs) | **GET** /{currency}/blocks/{height}/txs | Get block transactions
*BulkApi* | [**bulk_csv**](docs/BulkApi.md#bulk_csv) | **POST** /{currency}/bulk.csv/{operation} | Get data as CSV in bulk
*BulkApi* | [**bulk_json**](docs/BulkApi.md#bulk_json) | **POST** /{currency}/bulk.json/{operation} | Get data as JSON in bulk
*EntitiesApi* | [**get_entity**](docs/EntitiesApi.md#get_entity) | **GET** /{currency}/entities/{entity} | Get an entity
*EntitiesApi* | [**list_address_tags_by_entity**](docs/EntitiesApi.md#list_address_tags_by_entity) | **GET** /{currency}/entities/{entity}/tags | Get address tags for a given entity
*EntitiesApi* | [**list_entity_addresses**](docs/EntitiesApi.md#list_entity_addresses) | **GET** /{currency}/entities/{entity}/addresses | Get an entity&#39;s addresses
*EntitiesApi* | [**list_entity_links**](docs/EntitiesApi.md#list_entity_links) | **GET** /{currency}/entities/{entity}/links | Get transactions between two entities
*EntitiesApi* | [**list_entity_neighbors**](docs/EntitiesApi.md#list_entity_neighbors) | **GET** /{currency}/entities/{entity}/neighbors | Get an entity&#39;s direct neighbors
*EntitiesApi* | [**list_entity_txs**](docs/EntitiesApi.md#list_entity_txs) | **GET** /{currency}/entities/{entity}/txs | Get all transactions an entity has been involved in
*EntitiesApi* | [**search_entity_neighbors**](docs/EntitiesApi.md#search_entity_neighbors) | **GET** /{currency}/entities/{entity}/search | Search deeply for matching neighbors
*GeneralApi* | [**get_statistics**](docs/GeneralApi.md#get_statistics) | **GET** /stats | Get statistics of supported currencies
*GeneralApi* | [**search**](docs/GeneralApi.md#search) | **GET** /search | Returns matching addresses, transactions and labels
*RatesApi* | [**get_exchange_rates**](docs/RatesApi.md#get_exchange_rates) | **GET** /{currency}/rates/{height} | Returns exchange rate for a given height
*TagsApi* | [**get_actor**](docs/TagsApi.md#get_actor) | **GET** /tags/actors/{actor} | Returns an actor given its unique id or (unique) label
*TagsApi* | [**get_actor_tags**](docs/TagsApi.md#get_actor_tags) | **GET** /tags/actors/{actor}/tags | Returns the address tags for a given actor
*TagsApi* | [**list_address_tags**](docs/TagsApi.md#list_address_tags) | **GET** /tags | Returns address tags associated with a given label
*TagsApi* | [**list_concepts**](docs/TagsApi.md#list_concepts) | **GET** /tags/taxonomies/{taxonomy}/concepts | Returns the supported concepts of a taxonomy
*TagsApi* | [**list_taxonomies**](docs/TagsApi.md#list_taxonomies) | **GET** /tags/taxonomies | Returns the supported taxonomies
*TokensApi* | [**list_supported_tokens**](docs/TokensApi.md#list_supported_tokens) | **GET** /{currency}/supported_tokens | Returns a list of supported token (sub)currencies
*TxsApi* | [**get_spending_txs**](docs/TxsApi.md#get_spending_txs) | **GET** /{currency}/txs/{tx_hash}/spending | Returns in which other transaction&#39;s outputs the asked transaction spent. Think backwards references is the transaction graph. This endpoint is only available for utxo like currencies.
*TxsApi* | [**get_spent_in_txs**](docs/TxsApi.md#get_spent_in_txs) | **GET** /{currency}/txs/{tx_hash}/spent_in | Returns in which other transactions, outputs from the asked transaction are spent. Think forward references in the transaction graph. This endpoint is only available for utxo like currencies.
*TxsApi* | [**get_tx**](docs/TxsApi.md#get_tx) | **GET** /{currency}/txs/{tx_hash} | Returns details of a specific transaction identified by its hash
*TxsApi* | [**get_tx_io**](docs/TxsApi.md#get_tx_io) | **GET** /{currency}/txs/{tx_hash}/{io} | Returns input/output values of a specific transaction identified by its hash
*TxsApi* | [**list_token_txs**](docs/TxsApi.md#list_token_txs) | **GET** /{currency}/token_txs/{tx_hash} | Returns all token transactions in a given transaction


## Documentation For Models

 - [Actor](docs/Actor.md)
 - [ActorContext](docs/ActorContext.md)
 - [Actors](docs/Actors.md)
 - [Address](docs/Address.md)
 - [AddressTag](docs/AddressTag.md)
 - [AddressTagAllOf](docs/AddressTagAllOf.md)
 - [AddressTags](docs/AddressTags.md)
 - [AddressTx](docs/AddressTx.md)
 - [AddressTxUtxo](docs/AddressTxUtxo.md)
 - [AddressTxs](docs/AddressTxs.md)
 - [Block](docs/Block.md)
 - [BlockAtDate](docs/BlockAtDate.md)
 - [Concept](docs/Concept.md)
 - [CurrencyStats](docs/CurrencyStats.md)
 - [Entity](docs/Entity.md)
 - [EntityAddresses](docs/EntityAddresses.md)
 - [Height](docs/Height.md)
 - [LabelSummary](docs/LabelSummary.md)
 - [LabeledItemRef](docs/LabeledItemRef.md)
 - [LabeledItemRefs](docs/LabeledItemRefs.md)
 - [Link](docs/Link.md)
 - [LinkUtxo](docs/LinkUtxo.md)
 - [Links](docs/Links.md)
 - [NeighborAddress](docs/NeighborAddress.md)
 - [NeighborAddresses](docs/NeighborAddresses.md)
 - [NeighborEntities](docs/NeighborEntities.md)
 - [NeighborEntity](docs/NeighborEntity.md)
 - [Rate](docs/Rate.md)
 - [Rates](docs/Rates.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultByCurrency](docs/SearchResultByCurrency.md)
 - [SearchResultLabels](docs/SearchResultLabels.md)
 - [SearchResultLeaf](docs/SearchResultLeaf.md)
 - [SearchResultLevel1](docs/SearchResultLevel1.md)
 - [SearchResultLevel2](docs/SearchResultLevel2.md)
 - [SearchResultLevel3](docs/SearchResultLevel3.md)
 - [SearchResultLevel4](docs/SearchResultLevel4.md)
 - [SearchResultLevel5](docs/SearchResultLevel5.md)
 - [SearchResultLevel6](docs/SearchResultLevel6.md)
 - [Stats](docs/Stats.md)
 - [Tag](docs/Tag.md)
 - [TagCloudEntry](docs/TagCloudEntry.md)
 - [TagSummary](docs/TagSummary.md)
 - [Taxonomy](docs/Taxonomy.md)
 - [TokenConfig](docs/TokenConfig.md)
 - [TokenConfigs](docs/TokenConfigs.md)
 - [TokenValues](docs/TokenValues.md)
 - [Tx](docs/Tx.md)
 - [TxAccount](docs/TxAccount.md)
 - [TxRef](docs/TxRef.md)
 - [TxSummary](docs/TxSummary.md)
 - [TxUtxo](docs/TxUtxo.md)
 - [TxValue](docs/TxValue.md)
 - [TxValues](docs/TxValues.md)
 - [TxsAccount](docs/TxsAccount.md)
 - [Values](docs/Values.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Examples

In `./examples` you can find example Python scripts and [Jupyter](https://jupyter.org/) notebooks demonstrating how to use the GraphSense Python API. Please Follow these setup instructions to run them:

Setup a Python environment with [Anaconda](https://www.anaconda.com/products/distribution):

    conda env create -f environment.yml
    conda activate graphsense-python

Copy the config temp file and enter your Iknaio API key

    cp config.json.tmp config.json
    vi config.json

Run the jupyter notebooks

    jupyter notebook



## Generation from OpenAPI specification

This python package has been generated from [Graphsense's OpenAPI specification](https://api.ikna.io) hosted by [Iknaio Cryptoasset Analytics GmbH](https://ikna.io) using this command:

```
make GS_REST_SERVICE_URL="https://api.ikna.io" generate-openapi-client
```

