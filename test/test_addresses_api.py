"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.addresses_api import AddressesApi  # noqa: E501


class TestAddressesApi(unittest.TestCase):
    """AddressesApi unit test stubs"""

    def setUp(self):
        self.api = AddressesApi()  # noqa: E501

    def tearDown(self):
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

    def test_list_address_txs(self):
        """Test case for list_address_txs

        Get all transactions an address has been involved in  # noqa: E501
        """
        pass

    def test_list_tags_by_address(self):
        """Test case for list_tags_by_address

        Get attribution tags for a given address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
