# graphsense-python
GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/graphsense/graphsense-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/graphsense/graphsense-python.git`)

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

In order to generate the client from [Graphsense's OpenAPI specification](https://github.com/graphsense/graphsense-openapi) run the [OpenAPI Generator CLI](https://openapi-generator.tech/), eg. using docker:

```
    URL=https://github.com/graphsense/graphsense-openapi/blob/master/graphsense.yaml
    docker run --rm \
      -v "${PWD}:/build" \
      openapitools/openapi-generator-cli:v5.1.1 \
      generate -i "$URL" \
        -g python \
        -o /build
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
from graphsense.model.links import Links
from graphsense.model.neighbor_addresses import NeighborAddresses
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://localhost"
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
address = "addressA" # str | The cryptocurrency address

    try:
        # Get an address, optionally with tags
        api_response = api_instance.get_address(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressesApi* | [**get_address**](docs/AddressesApi.md#get_address) | **GET** /{currency}/addresses/{address} | Get an address, optionally with tags
*AddressesApi* | [**get_address_entity**](docs/AddressesApi.md#get_address_entity) | **GET** /{currency}/addresses/{address}/entity | Get the entity of an address
*AddressesApi* | [**list_address_links**](docs/AddressesApi.md#list_address_links) | **GET** /{currency}/addresses/{address}/links | Get outgoing transactions between two addresses
*AddressesApi* | [**list_address_neighbors**](docs/AddressesApi.md#list_address_neighbors) | **GET** /{currency}/addresses/{address}/neighbors | Get an address&#39;s neighbors in the address graph
*AddressesApi* | [**list_address_txs**](docs/AddressesApi.md#list_address_txs) | **GET** /{currency}/addresses/{address}/txs | Get all transactions an address has been involved in
*AddressesApi* | [**list_tags_by_address**](docs/AddressesApi.md#list_tags_by_address) | **GET** /{currency}/addresses/{address}/tags | Get attribution tags for a given address
*BlocksApi* | [**get_block**](docs/BlocksApi.md#get_block) | **GET** /{currency}/blocks/{height} | Get a block by its height
*BlocksApi* | [**list_block_txs**](docs/BlocksApi.md#list_block_txs) | **GET** /{currency}/blocks/{height}/txs | Get block transactions
*BulkApi* | [**bulk_csv**](docs/BulkApi.md#bulk_csv) | **POST** /{currency}/bulk.csv/{operation} | Get data as CSV in bulk
*BulkApi* | [**bulk_json**](docs/BulkApi.md#bulk_json) | **POST** /{currency}/bulk.json/{operation} | Get data as JSON in bulk
*EntitiesApi* | [**get_entity**](docs/EntitiesApi.md#get_entity) | **GET** /{currency}/entities/{entity} | Get an entity, optionally with tags
*EntitiesApi* | [**list_address_tags_by_entity**](docs/EntitiesApi.md#list_address_tags_by_entity) | **GET** /{currency}/entities/{entity}/tags | Get address tags for a given entity
*EntitiesApi* | [**list_entity_addresses**](docs/EntitiesApi.md#list_entity_addresses) | **GET** /{currency}/entities/{entity}/addresses | Get an entity&#39;s addresses
*EntitiesApi* | [**list_entity_links**](docs/EntitiesApi.md#list_entity_links) | **GET** /{currency}/entities/{entity}/links | Get transactions between two entities
*EntitiesApi* | [**list_entity_neighbors**](docs/EntitiesApi.md#list_entity_neighbors) | **GET** /{currency}/entities/{entity}/neighbors | Get an entity&#39;s neighbors in the entity graph
*EntitiesApi* | [**list_entity_txs**](docs/EntitiesApi.md#list_entity_txs) | **GET** /{currency}/entities/{entity}/txs | Get all transactions an entity has been involved in
*EntitiesApi* | [**search_entity_neighbors**](docs/EntitiesApi.md#search_entity_neighbors) | **GET** /{currency}/entities/{entity}/search | Search deeply for matching neighbors
*GeneralApi* | [**get_statistics**](docs/GeneralApi.md#get_statistics) | **GET** /stats | Get statistics of supported currencies
*GeneralApi* | [**search**](docs/GeneralApi.md#search) | **GET** /search | Returns matching addresses, transactions and labels
*RatesApi* | [**get_exchange_rates**](docs/RatesApi.md#get_exchange_rates) | **GET** /{currency}/rates/{height} | Returns exchange rate for a given height
*TagsApi* | [**list_address_tags**](docs/TagsApi.md#list_address_tags) | **GET** /tags | Returns address tags associated with a given label
*TagsApi* | [**list_concepts**](docs/TagsApi.md#list_concepts) | **GET** /tags/taxonomies/{taxonomy}/concepts | Returns the supported concepts of a taxonomy
*TagsApi* | [**list_taxonomies**](docs/TagsApi.md#list_taxonomies) | **GET** /tags/taxonomies | Returns the supported taxonomies
*TxsApi* | [**get_tx**](docs/TxsApi.md#get_tx) | **GET** /{currency}/txs/{tx_hash} | Returns details of a specific transaction identified by its hash.
*TxsApi* | [**get_tx_io**](docs/TxsApi.md#get_tx_io) | **GET** /{currency}/txs/{tx_hash}/{io} | Returns input/output values of a specific transaction identified by its hash.


## Documentation For Models

 - [Address](docs/Address.md)
 - [AddressTag](docs/AddressTag.md)
 - [AddressTagAllOf](docs/AddressTagAllOf.md)
 - [AddressTags](docs/AddressTags.md)
 - [AddressTx](docs/AddressTx.md)
 - [AddressTxUtxo](docs/AddressTxUtxo.md)
 - [AddressTxs](docs/AddressTxs.md)
 - [Block](docs/Block.md)
 - [Concept](docs/Concept.md)
 - [CurrencyStats](docs/CurrencyStats.md)
 - [Entity](docs/Entity.md)
 - [EntityAddresses](docs/EntityAddresses.md)
 - [Height](docs/Height.md)
 - [Link](docs/Link.md)
 - [LinkUtxo](docs/LinkUtxo.md)
 - [Links](docs/Links.md)
 - [Neighbor](docs/Neighbor.md)
 - [NeighborAddress](docs/NeighborAddress.md)
 - [NeighborAddresses](docs/NeighborAddresses.md)
 - [NeighborEntities](docs/NeighborEntities.md)
 - [NeighborEntity](docs/NeighborEntity.md)
 - [OnlyEntityIds](docs/OnlyEntityIds.md)
 - [Rate](docs/Rate.md)
 - [Rates](docs/Rates.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultByCurrency](docs/SearchResultByCurrency.md)
 - [SearchResultLabels](docs/SearchResultLabels.md)
 - [SearchResultLeaf](docs/SearchResultLeaf.md)
 - [SearchResultLevel1](docs/SearchResultLevel1.md)
 - [SearchResultLevel1AllOf](docs/SearchResultLevel1AllOf.md)
 - [SearchResultLevel2](docs/SearchResultLevel2.md)
 - [SearchResultLevel2AllOf](docs/SearchResultLevel2AllOf.md)
 - [SearchResultLevel3](docs/SearchResultLevel3.md)
 - [SearchResultLevel3AllOf](docs/SearchResultLevel3AllOf.md)
 - [SearchResultLevel4](docs/SearchResultLevel4.md)
 - [SearchResultLevel4AllOf](docs/SearchResultLevel4AllOf.md)
 - [SearchResultLevel5](docs/SearchResultLevel5.md)
 - [SearchResultLevel5AllOf](docs/SearchResultLevel5AllOf.md)
 - [SearchResultLevel6](docs/SearchResultLevel6.md)
 - [SearchResultLevel6AllOf](docs/SearchResultLevel6AllOf.md)
 - [Stats](docs/Stats.md)
 - [Tag](docs/Tag.md)
 - [Taxonomy](docs/Taxonomy.md)
 - [Tx](docs/Tx.md)
 - [TxAccount](docs/TxAccount.md)
 - [TxSummary](docs/TxSummary.md)
 - [TxUtxo](docs/TxUtxo.md)
 - [TxValue](docs/TxValue.md)
 - [TxValues](docs/TxValues.md)
 - [Values](docs/Values.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## cookieAuth

- **Type**: API key
- **API key parameter name**: session
- **Location**: 


## Examples

In `./examples` you can find example Python scripts and [Jupyter](https://jupyter.org/) notebooks demonstrating how to use the GraphSense Python API. Please Follow these setup instructions to run them:

Clone this repository

    git clone git@github.com:graphsense/graphsense-python.git
    cd graphsense-python

Recommended: create and activate a virtual Python environment

    python3 -m venv venv-gpython
    . ./venv-gpython/bin/activate

Upgrade pip and install all dependencies
    
    python -m pip install --upgrade pip
    pip install -r examples/requirements.txt

Install the GraphSense python client

    pip install git+https://github.com/graphsense/graphsense-python.git

Install a custom iPython kernel that uses the virtual Python environment

    ipython kernel install --name=venv-gpython

Run the Jupyter notebook

    jupyter notebook

Open the notebooks in your browser

    http://localhost:8889/notebooks/examples/basic_entities_demo.ipynb
    http://localhost:8889/notebooks/examples/sextortion_study.ipynb

Make sure you select the right kernel (venv-gpython) before running the notebooks (Kernel -> Change kernel -> venv-gpython)

