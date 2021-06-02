"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.blocks_api import BlocksApi  # noqa: E501


class TestBlocksApi(unittest.TestCase):
    """BlocksApi unit test stubs"""

    def setUp(self):
        self.api = BlocksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_block(self):
        """Test case for get_block

        Get a block by its height  # noqa: E501
        """
        pass

    def test_get_block_eth(self):
        """Test case for get_block_eth

        Get a ethereum block by its height  # noqa: E501
        """
        pass

    def test_list_block_txs(self):
        """Test case for list_block_txs

        Get block transactions (100 per page)  # noqa: E501
        """
        pass

    def test_list_block_txs_csv(self):
        """Test case for list_block_txs_csv

        Get block transactions as CSV  # noqa: E501
        """
        pass

    def test_list_block_txs_csv_eth(self):
        """Test case for list_block_txs_csv_eth

        Get block transactions as CSV  # noqa: E501
        """
        pass

    def test_list_block_txs_eth(self):
        """Test case for list_block_txs_eth

        Get block transactions (100 per page)  # noqa: E501
        """
        pass

    def test_list_blocks(self):
        """Test case for list_blocks

        Get all blocks  # noqa: E501
        """
        pass

    def test_list_blocks_eth(self):
        """Test case for list_blocks_eth

        Get all blocks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
