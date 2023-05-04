import sys
import graphsense
from graphsense.api.api import Api, Bulk
import json

with open('./config.json') as config_file:
    config = json.load(config_file)
configuration = graphsense.Configuration(host=config['graphsense']['host'])
configuration.api_key['api_key'] = config['graphsense']['api_key']

with graphsense.ApiClient(configuration) as api_client:
    api = Api(api_client)
    bulk = Bulk(api_client)

    print("\n#### Address")
    print(api.get_address("btc", "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"))
    print(bulk.get_address("btc", ["1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"]))
    print(
        bulk.get_address("btc", [
            "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB",
            "19vRqiFxFVGHNd4vqtE6TZM29XVZyQFu8Q"
        ]))

    print("\n#### Address cluster")
    print(api.get_address_entity("btc", "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"))
    print(
        bulk.get_address_entity("btc", ["1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"]))
    print(
        bulk.get_address_entity("btc", [
            "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB",
            "19vRqiFxFVGHNd4vqtE6TZM29XVZyQFu8Q"
        ]))

    print("\n#### Address links")
    print(
        api.list_address_links("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3",
                               "1A22dW3oPaefLeU5oWrEZUJt2Q4jfvuznH"))
    print(
        bulk.list_address_links("btc", ["1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"],
                                ["1A22dW3oPaefLeU5oWrEZUJt2Q4jfvuznH"]))

    print("\n#### Address neighbors")
    print(
        api.list_address_neighbors("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3",
                                   "in"))
    print(
        bulk.list_address_neighbors("btc",
                                    ["1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"],
                                    "in"))

    print("\n#### Address txs")
    print(
        api.list_address_txs("btc",
                             "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3",
                             direction="in"))
    print(
        bulk.list_address_txs("btc", ["1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"],
                              "in"))
    print(
        bulk.list_address_txs("btc", ["1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"],
                              "out"))

    print("\n#### Txs")
    print(
        api.get_tx(
            "btc",
            "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965",
            include_io=True,
        ))
    print(
        bulk.get_tx("btc", [
            "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965",
            "961a2782af63304c2e395ddefb01d0820994602afcd0ebf85addca69b3a46c76",
        ],
                    include_io=True))

    print(
        api.get_tx_io(
            "btc",
            "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965",
            "inputs"))
    print(
        bulk.get_tx_io("btc", [
            "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965"
        ], "inputs"))
    print(
        bulk.get_tx_io("btc", [
            "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965"
        ], "outputs"))

    print("\n#### Tags")
    print(api.get_actor("binance"))
    print(api.get_actor_tags("binance"))
    # print(api.tags.actor_as_df("binance"))

    # need bulk rest interface for tags
    # print(api.tags.actor_tags_as_df("binance"))

    print(api.list_taxonomies())
    print(api.list_concepts("abuse"))

    # print(api.tags.taxonomies_as_df())
    # print(api.tags.concepts_as_df("abuse"))

    print("\n#### General")
    print(api.get_statistics())
    # print(api.general.statistics_as_df())
    print(api.list_supported_tokens("eth"))
    # print(api.list_supported_tokens_as_df("eth"))
    print(api.search("binance"))

    print("\n#### Rates")
    print(api.get_exchange_rates("btc", 1))
    print(bulk.get_exchange_rates("btc", [1, 2, 3, 4]))

    print("\n#### Blocks")
    print(api.get_block("btc", 1))
    print(bulk.get_block("btc", [1, 2, 3, 4]))

    print("\n#### Block txs")
    print(api.list_block_txs("btc", 1))
    print(bulk.list_block_txs("btc", [1, 2, 3, 10000]))
    print(bulk.list_block_txs("btc", [110000])["inputs"][1][0])

    print("\n#### Cluster")
    print(api.get_entity("btc", 1))
    print(bulk.get_entity("btc", [1, 2, 3, 10000]))

    print("\n#### Cluster Tags")
    print(api.list_address_tags_by_entity("btc", 15027757))
    #print(api.cluster.tags_as_df("btc", [1, 2, 3, 15027757]))
    #print(api.cluster.tags_as_df("btc", 15027757))

    print("\n#### Cluster addresses")
    print(api.list_entity_addresses("btc", 1000))
    print(bulk.list_entity_addresses("btc", [1, 2, 3, 1000]))

    print("\n#### Cluster links")
    print(api.list_entity_links("btc", 15027757, 1479561))
    print(bulk.list_entity_links("btc", [15027757], [1479561]))

    print("\n#### Cluster neighbors")
    print(api.list_entity_neighbors("btc", 542007, "in"))
    print(bulk.list_entity_neighbors("btc", [542007], "in"))
    print(bulk.list_entity_neighbors("btc", [542007], "out"))

    print("\n#### Cluster txs")
    print(api.list_entity_txs("btc", 542007, direction="in"))
    print(bulk.list_entity_txs("btc", [542007], "in"))
