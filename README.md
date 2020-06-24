# GraphSense Python Interface



## Prerequisites


	pip install graphsense


## Using the GraphSense API


	import graphsense

Register API key

	graphsense.authenticate("https://api.graphsense.info", MY_API_KEY)


Retrieve available blockchains and statistics

	graphsense.stats


Access a specific blockchain

	btc_chain = graphsense.blockchain('btc')

Retrieve a specific block

	block = btc_chain.block(height=150000)

List block transaction hashes

	txs = block.transactions

Retrieve a specific transactions

	tx = block.transaction(
		hash=f7f4c281ee20ab8d1b00734b92b60582b922211a7e470accd147c6d70c9714a3)

...


## Using the Command Line Interface

Retrieve entity for a specific address

	graphsense -a 1QCmceWArP5qK31KciwFcdPM3tW3anGFN -c get_entity

Retrieve entities for a set of addresses stored in addresses.txt

	cat addresses.txt | graphsense -a -c get_entity > address_w_entities.txt

...