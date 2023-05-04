"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_csv(self):
        """Test case for bulk_csv

        Get data as CSV in bulk  # noqa: E501
        """
        pass

    def test_bulk_json(self):
        """Test case for bulk_json

        Get data as JSON in bulk  # noqa: E501
        """
        pass

    def test_get_actor(self):
        """Test case for get_actor

        Returns an actor given its unique id or (unique) label  # noqa: E501
        """
        pass

    def test_get_actor_tags(self):
        """Test case for get_actor_tags

        Returns the address tags for a given actor  # noqa: E501
        """
        pass

    def test_get_address(self):
        """Test case for get_address

        Get an address  # noqa: E501
        """
        pass

    def test_get_address_entity(self):
        """Test case for get_address_entity

        Get the entity of an address  # noqa: E501
        """
        pass

    def test_get_block(self):
        """Test case for get_block

        Get a block by its height  # noqa: E501
        """
        pass

    def test_get_entity(self):
        """Test case for get_entity

        Get an entity  # noqa: E501
        """
        pass

    def test_get_exchange_rates(self):
        """Test case for get_exchange_rates

        Returns exchange rate for a given height  # noqa: E501
        """
        pass

    def test_get_statistics(self):
        """Test case for get_statistics

        Get statistics of supported currencies  # noqa: E501
        """
        pass

    def test_get_tx(self):
        """Test case for get_tx

        Returns details of a specific transaction identified by its hash.  # noqa: E501
        """
        pass

    def test_get_tx_io(self):
        """Test case for get_tx_io

        Returns input/output values of a specific transaction identified by its hash.  # noqa: E501
        """
        pass

    def test_list_address_links(self):
        """Test case for list_address_links

        Get outgoing transactions between two addresses  # noqa: E501
        """
        pass

    def test_list_address_neighbors(self):
        """Test case for list_address_neighbors

        Get an address's neighbors in the address graph  # noqa: E501
        """
        pass

    def test_list_address_tags(self):
        """Test case for list_address_tags

        Returns address tags associated with a given label  # noqa: E501
        """
        pass

    def test_list_address_tags_by_entity(self):
        """Test case for list_address_tags_by_entity

        Get address tags for a given entity  # noqa: E501
        """
        pass

    def test_list_address_txs(self):
        """Test case for list_address_txs

        Get all transactions an address has been involved in  # noqa: E501
        """
        pass

    def test_list_block_txs(self):
        """Test case for list_block_txs

        Get block transactions  # noqa: E501
        """
        pass

    def test_list_concepts(self):
        """Test case for list_concepts

        Returns the supported concepts of a taxonomy  # noqa: E501
        """
        pass

    def test_list_entity_addresses(self):
        """Test case for list_entity_addresses

        Get an entity's addresses  # noqa: E501
        """
        pass

    def test_list_entity_links(self):
        """Test case for list_entity_links

        Get transactions between two entities  # noqa: E501
        """
        pass

    def test_list_entity_neighbors(self):
        """Test case for list_entity_neighbors

        Get an entity's direct neighbors  # noqa: E501
        """
        pass

    def test_list_entity_txs(self):
        """Test case for list_entity_txs

        Get all transactions an entity has been involved in  # noqa: E501
        """
        pass

    def test_list_supported_tokens(self):
        """Test case for list_supported_tokens

        Returns a list of supported token (sub)currencies.  # noqa: E501
        """
        pass

    def test_list_tags_by_address(self):
        """Test case for list_tags_by_address

        Get attribution tags for a given address  # noqa: E501
        """
        pass

    def test_list_taxonomies(self):
        """Test case for list_taxonomies

        Returns the supported taxonomies  # noqa: E501
        """
        pass

    def test_list_token_txs(self):
        """Test case for list_token_txs

        Returns all token transactions in a given transaction  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        Returns matching addresses, transactions and labels  # noqa: E501
        """
        pass

    def test_search_entity_neighbors(self):
        """Test case for search_entity_neighbors

        Search deeply for matching neighbors  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
