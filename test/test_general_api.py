"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
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
