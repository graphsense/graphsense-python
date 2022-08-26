"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.tags_api import TagsApi  # noqa: E501


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_address_tags(self):
        """Test case for list_address_tags

        Returns address tags associated with a given label  # noqa: E501
        """
        pass

    def test_list_concepts(self):
        """Test case for list_concepts

        Returns the supported concepts of a taxonomy  # noqa: E501
        """
        pass

    def test_list_taxonomies(self):
        """Test case for list_taxonomies

        Returns the supported taxonomies  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
