"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.block_tx_utxo import BlockTxUtxo
from graphsense.model.height import Height
from graphsense.model.tx_account import TxAccount
from graphsense.model.values import Values
globals()['BlockTxUtxo'] = BlockTxUtxo
globals()['Height'] = Height
globals()['TxAccount'] = TxAccount
globals()['Values'] = Values
from graphsense.model.block_tx import BlockTx


class TestBlockTx(unittest.TestCase):
    """BlockTx unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBlockTx(self):
        """Test BlockTx"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BlockTx()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
