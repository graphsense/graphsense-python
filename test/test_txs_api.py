"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.txs_api import TxsApi  # noqa: E501


class TestTxsApi(unittest.TestCase):
    """TxsApi unit test stubs"""

    def setUp(self):
        self.api = TxsApi()  # noqa: E501

    def tearDown(self):
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

    def test_list_token_txs(self):
        """Test case for list_token_txs

        Returns all token transactions in a given transaction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
