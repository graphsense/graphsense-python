"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.1-dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.entities_api import EntitiesApi  # noqa: E501


class TestEntitiesApi(unittest.TestCase):
    """EntitiesApi unit test stubs"""

    def setUp(self):
        self.api = EntitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_entity(self):
        """Test case for get_entity

        Get an entity, optionally with tags  # noqa: E501
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

        Get an entity's neighbors in the entity graph  # noqa: E501
        """
        pass

    def test_list_entity_txs(self):
        """Test case for list_entity_txs

        Get all transactions an entity has been involved in  # noqa: E501
        """
        pass

    def test_list_tags_by_entity(self):
        """Test case for list_tags_by_entity

        Get tags for a given entity for the given level  # noqa: E501
        """
        pass

    def test_search_entity_neighbors(self):
        """Test case for search_entity_neighbors

        Search deeply for matching neighbors  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
