# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
# configuration.api_key['api_key'] = 'ooheGZnCVBQ7eMStJI7pYQAZOtAUQjy4'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

from graphsense.model.get_tx_io import GetTxIo
from graphsense.model.get_tx_io_parameters import GetTxIoParameters
from graphsense.model.io import Io
import graphsense
from graphsense.api import batch_api, blocks_api
from pprint import pprint
# Defining the host is optional and defaults to http://graphsense-rest:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host="http://localhost:5000"
)


# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    addresses_api_instance = blocks_api.BlocksApi(api_client)
    batch_api_instance = batch_api.BatchApi(api_client)
    currency = "btc"  # str | The cryptocurrency (e.g., btc)

    txs = ['1d8149eb8d8475b98113b5011cf70e0b7a4dccff71286d28b8b4b641f94f1e46',
           'ed25927576988e38e4cc8e4b19d1272c480f113fb605271b190df05aa983714e',
           '744556a5586736471d496c928ccca8fd58dadac6071394eca846c180b0dec6fe',
           'adfcbcbd4f87a725337ab0b4eb657f97123806d30ccd50fa0c107b5124692e1d',
           'afe5de49b7a84bb5d79d114601d81645264ebb4fcb8e1b45c280f6d788a8a7ba',
           'b2b8328e5e7af3f17449109b449517cc6641b7a1a525e0c1d019cda078ee03be',
           '9421c806a8f3fd46841241659637d75b944b42af61fabe7b9359349bc50d2ea6',
           '4ef86047959d9125746266c4a87d84e217efbc6ce799639e5c27c42cd7521e08',
           '46951cfd631ff75140c8ec38af1927909dd2e5ed4192500982b591902d7e4fbb',
           'bcf84712500459da1670546601ef7373946fbca624f2e9957a53f5205102a224']

    pprint(txs)
    params = [GetTxIoParameters(tx_hash=tx_hash, io=Io('inputs')) for tx_hash in txs]

    # example passing only required values which don't have defaults set
    try:
        # Get data as CSV in batch
        api_response = \
            batch_api_instance.batch(currency,
                                     batch_operation=GetTxIo(parameters=params))
        print(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling BatchApi->batch: %s\n" % e)
