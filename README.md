# GraphSense Python Interface

This Python interface allows you to interact with the [GraphSense REST API](https://github.com/graphsense/graphsense-REST) and perform cross-ledger cryptocurrency analytics.

## Prerequisites


	pip install graphsense


## Using the GraphSense API


	import graphsense as gs

Register API key

	gs.authenticate("https://api.graphsense.info", MY_API_KEY)


Retrieve available blockchains and statistics

	gs.stats


Access a specific blockchain

	btc_chain = gs.blockchain('btc')

Retrieve a specific block

	block = btc_chain.block(height=150000)

List block transaction hashes

	[tx.hash for tx in block.transactions]

Retrieve a specific transaction

	tx = btc_chain.transaction(
		hash=f7f4c281ee20ab8d1b00734b92b60582b922211a7e470accd147c6d70c9714a3)

List addresses transaction inputs

	[i.address for i in tx.inputs]

List output entities in a transaction

	[btc_chain.get_address_entity(out.address) for out in tx.outputs]


...


## Using the Command Line Interface

Retrieve entity for a specific address

	graphsense -a 1QCmceWArP5qK31KciwFcdPM3tW3anGFN -c get_entity

Retrieve entities for a set of addresses stored in addresses.txt

	cat addresses.txt | graphsense -a -c get_address_entity > address_w_entities.txt

...