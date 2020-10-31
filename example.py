from __future__ import print_function

import time
import graphsense
from graphsense.rest import ApiException
from pprint import pprint
import pandas as pd

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
configuration = graphsense.Configuration(
    host = "http://localhost:9000",
    api_key = {
        'api_key': 'alicekey'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graphsense.AddressesApi(api_client)
    currency = 'btc' # str | The cryptocurrency (e.g., btc)
    address = '3Hrnn1UN78uXgLNvtqVXMjHwB41PmX66X4' # str | The cryptocurrency address

    try:
        # Get an address with tags
        api_response = api_instance.get_address_with_tags(currency, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->get_address_with_tags: %s\n" % e)


