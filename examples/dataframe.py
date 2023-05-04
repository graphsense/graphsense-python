import graphsense
from graphsense.api import default_api
from pprint import pprint
import pandas as pd
import json

with open('./config.json') as config_file:
    config = json.load(config_file)
configuration = graphsense.Configuration(host=config['graphsense']['host'])
configuration.api_key['api_key'] = config['graphsense']['api_key']

data = {
    'address': [
        '1H7j2YeKwdatfmTmE6vUMotMNrnLA1JbyS',
        '19db74byS65R9FRhud3X34wKkSd9ZzQ1fX'
    ]
}
address_df = pd.DataFrame.from_dict(data)

with graphsense.ApiClient(configuration) as api_client:
    api_instance = default_api.DataFrame(api_client)

    CURRENCY = "btc"

    try:
        # Read data into pandas dataframe.
        # Use _preload_content=False to stream
        # raw response data right into a dataframe.
        df_resp = api_instance.get_address_entity(
            CURRENCY, address_df['address'].to_list())
        pprint(df_resp['total_received_value'])
    except graphsense.ApiException as e:
        print("Exception when calling BulkApi->bulk_csv: %s\n" % e)
