"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.2-dev
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

    def test_list_concepts(self):
        """Test case for list_concepts

        Returns the supported concepts of a taxonomy  # noqa: E501
        """
        pass

    def test_list_tags(self):
        """Test case for list_tags

        Returns address or entity tags associated with a given label  # noqa: E501
        """
        pass

    def test_list_taxonomies(self):
        """Test case for list_taxonomies

        Returns the supported taxonomies  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
