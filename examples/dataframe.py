import graphsense
from graphsense.api import bulk_api
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
    api_instance = bulk_api.BulkApi(api_client)

    CURRENCY = "btc"
    operation = "get_address_entity"
    body = {'address': address_df['address'].to_list()}

    try:
        # Read data into pandas dataframe.
        # Use _preload_content=False to stream
        # raw response data right into a dataframe.
        df_resp = pd.read_csv(
            api_instance.bulk_csv(CURRENCY,
                                  operation,
                                  body=body,
                                  num_pages=1,
                                  _preload_content=False))
        pprint(df_resp)
    except graphsense.ApiException as e:
        print("Exception when calling BulkApi->bulk_csv: %s\n" % e)
