"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.general_api import GeneralApi  # noqa: E501


class TestGeneralApi(unittest.TestCase):
    """GeneralApi unit test stubs"""

    def setUp(self):
        self.api = GeneralApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_statistics(self):
        """Test case for get_statistics

        Get statistics of supported currencies  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        Returns matching addresses, transactions and labels  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
