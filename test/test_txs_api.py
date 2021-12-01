"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.1
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


if __name__ == '__main__':
    unittest.main()
