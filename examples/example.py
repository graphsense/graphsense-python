from __future__ import print_function

import time
import graphsense
from pprint import pprint
from graphsense.api import txs_api, blocks_api
from graphsense.model.address_tag import AddressTag
from graphsense.model.address_txs import AddressTxs
from graphsense.model.address_with_tags import AddressWithTags
from graphsense.model.entity_with_tags import EntityWithTags
from graphsense.model.link import Link
from graphsense.model.neighbors import Neighbors
from graphsense.model.txs_eth import TxsEth
# Defining the host is optional and defaults to http://openapi_server:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "http://localhost:9000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
#configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = txs_api.TxsApi(api_client)
    currency = "ltc" # str | The cryptocurrency (e.g., btc)
    #tx = "d70651c9d60153f22cb552c9cfd903cb369a25393b0a869b00a3a77a2b244bb2" # str | The cryptocurrency address
    tx = "12345007b0e3e16eafbcc60d55021a4e7599ef3a3c5dccd4329a0dc69fe0ef47"
    tx = ''.join([tx[i%(len(tx))] for i in range(0,100000)])

    try:
        # Get an address with tags
        api_response = api_instance.get_tx(currency, tx)
        print(type(api_response[0]))
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address_entity: %s\n" % e)

