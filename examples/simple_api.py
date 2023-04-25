import sys
from graphsense.simple import Api

if len(sys.argv) < 2:
    print("please provide a api key as commandline argument")
    sys.exit(2)

with Api(api_key=sys.argv[1]) as api:


    print("\n#### Address")
    print(api.address.get("btc", "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"))
    print(api.address.get_as_df("btc", "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"))
    print(api.address.get_as_df("btc", ["1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB", "19vRqiFxFVGHNd4vqtE6TZM29XVZyQFu8Q"]))


    print("\n#### Address cluster")
    print(api.address.cluster("btc", "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"))
    print(api.address.cluster_as_df("btc", "1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB"))
    print(api.address.cluster_as_df("btc",["1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB", "19vRqiFxFVGHNd4vqtE6TZM29XVZyQFu8Q"]))


    print("\n#### Address Tags")
    print(api.address.tags("btc", "16V9EZtv9f8rHzcv2WRfetxj4TPzmYMhky"))
    print(api.address.tags_as_df("btc", "16V9EZtv9f8rHzcv2WRfetxj4TPzmYMhky"))
    print(api.address.tags_as_df("btc", ["1PNg9PrxjmZZ51TnzGzCbFvtop8h3fUtVB", "19vRqiFxFVGHNd4vqtE6TZM29XVZyQFu8Q", "16V9EZtv9f8rHzcv2WRfetxj4TPzmYMhky"]))

    print("\n#### Address links")
    print(api.address.links("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3", "1A22dW3oPaefLeU5oWrEZUJt2Q4jfvuznH"))
    print(api.address.links_as_df("btc", ["1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"], ["1A22dW3oPaefLeU5oWrEZUJt2Q4jfvuznH"]))
    print(api.address.links_as_df("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3", "1A22dW3oPaefLeU5oWrEZUJt2Q4jfvuznH"))

    print("\n#### Address neighbors")
    print(api.address.neighbors("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3", "in"))
    print(api.address.incoming_neighbors("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"))
    print(api.address.incoming_neighbors_as_df("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"))
    print(api.address.outgoing_neighbors_as_df("btc", ["1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3", "1A22dW3oPaefLeU5oWrEZUJt2Q4jfvuznH"]))

    print("\n#### Address txs")
    print(api.address.txs("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3", direction="in"))
    print(api.address.incoming_txs("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"))
    print(api.address.incoming_txs("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"))
    print(api.address.incoming_txs_as_df("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"))
    print(api.address.outgoing_txs_as_df("btc", "1G5GHnRzVXi8NP591wVpXRrERhHW47iSe3"))


    print("\n#### Txs")
    print(
        api.txs.get(
            "btc", "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965",include_io=True,
        )
    )
    print(
        api.txs.get_as_df(
            "btc",
            "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965",
            include_io=True,
        )
    )
    print(
        api.txs.get_as_df(
            "btc",
            [
                "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965",
                "961a2782af63304c2e395ddefb01d0820994602afcd0ebf85addca69b3a46c76",
            ], include_io=True
        )
    )

    print(api.txs.inputs("btc", "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965"))
    print(api.txs.inputs_as_df("btc", "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965"))
    print(api.txs.outputs("btc", "caba0b0478e4c2c4b1646006d901a32fc77e0eab151796e3cc47ec951dd3b965"))

    print("\n#### Tags")
    print(api.tags.actor("binance"))
    print(api.tags.actor_tags("binance"))
    # print(api.tags.actor_as_df("binance"))

    print(api.tags.actor_tags_as_df("binance"))
    print(api.tags.get("internet archive"))
    print(api.tags.get_as_df("internet archive"))

    print(api.tags.taxonomies())
    print(api.tags.concepts("abuse"))

    print(api.tags.taxonomies_as_df())
    print(api.tags.concepts_as_df("abuse"))

    print("\n#### General")
    print(api.general.statistics())
    print(api.general.statistics_as_df())
    print(api.general.supported_tokens("eth"))
    print(api.general.supported_tokens_as_df("eth"))
    print(api.general.search("binance"))

    print("\n#### Rates")
    print(api.rates.get("btc", 1))
    print(api.rates.get_as_df("btc", 1))
    print(api.rates.get_as_df("btc", [1, 2, 3, 4]))

    print("\n#### Blocks")
    print(api.block.get("btc", 1))
    print(api.block.get_as_df("btc", 1))
    print(api.block.get_as_df("btc", [1, 2, 3, 4]))

    print("\n#### Block txs")
    print(api.block.txs("btc", 1))
    print(api.block.txs_as_df("btc", 1))
    print(api.block.txs_as_df("btc", [1, 2, 3, 10000]))
    print(api.block.txs_as_df("btc", 110000)["inputs"][1][0])

    print("\n#### Cluster")
    print(api.cluster.get("btc", 1))
    print(api.cluster.get_as_df("btc", 1))
    print(api.cluster.get_as_df("btc", [1, 2, 3, 10000]))

    print("\n#### Cluster Tags")
    print(api.cluster.tags("btc", 15027757))
    print(api.cluster.tags_as_df("btc", [1, 2, 3, 15027757]))
    print(api.cluster.tags_as_df("btc", 15027757))

    print("\n#### Cluster addresses")
    print(api.cluster.addresses("btc", 1000))
    print(api.cluster.addresses_as_df("btc", [1, 2, 3, 1000]))
    print(api.cluster.addresses_as_df("btc", 100))

    print("\n#### Cluster links")
    print(api.cluster.links("btc", 15027757, 1479561))
    print(api.cluster.links_as_df("btc", [15027757], [1479561]))
    print(api.cluster.links_as_df("btc", 15027757, 1479561))

    print("\n#### Cluster neighbors")
    print(api.cluster.neighbors("btc", 542007, "in"))
    print(api.cluster.incoming_neighbors("btc", 542007))
    print(api.cluster.incoming_neighbors_as_df("btc", 542007))
    print(api.cluster.outgoing_neighbors_as_df("btc", 542007))

    print("\n#### Cluster txs")
    print(api.cluster.txs("btc", 542007, direction="in"))
    print(api.cluster.incoming_txs("btc", 542007))
    print(api.cluster.incoming_txs("btc", 542007))
    print(api.cluster.incoming_txs_as_df("btc", 542007))
    print(api.cluster.outgoing_txs_as_df("btc", 542007))
