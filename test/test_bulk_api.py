"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.bulk_api import BulkApi  # noqa: E501


class TestBulkApi(unittest.TestCase):
    """BulkApi unit test stubs"""

    def setUp(self):
        self.api = BulkApi()  # noqa: E501

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


if __name__ == '__main__':
    unittest.main()
