from __future__ import print_function

import time
import graphsense
from pprint import pprint
from graphsense.api import entities_api, addresses_api
from graphsense.model.address import Address
from graphsense.model.address_tag import AddressTag
from graphsense.model.address_txs import AddressTxs
from graphsense.model.address_with_tags import AddressWithTags
from graphsense.model.entity_with_tags import EntityWithTags
from graphsense.model.link import Link
from graphsense.model.neighbors import Neighbors
from graphsense.model.txs_eth import TxsEth
import pandas as pd
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
        host="http://spark-master:9001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
#configuration.api_key['api_key'] = 'ooheGZnCVBQ7eMStJI7pYQAZOtAUQjy4'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

CURRENCY = 'btc'


def get_address_details(address: str) -> Address:
    with graphsense.ApiClient(configuration) as api_client:
        api_instance = addresses_api.AddressesApi(api_client)
        try:
            response = api_instance.get_address(CURRENCY, address)
            return response
        except graphsense.ApiException as e:
            print("Exception when calling Addresses Api: %s\n" % e)


print(get_address_details('1PUUEepsbdHZ5cKDTD4r4GforhN2ktCT7A'))


# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    currency = "btc"  # str | The cryptocurrency (e.g., btc)

    entities = [144534, 10102718]
    try:

        api_instance = entities_api.EntitiesApi(api_client)
        response = api_instance.list_entities(currency, ids=[2491912, 153065054])
        print(response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address_entity: %s\n" % e)

