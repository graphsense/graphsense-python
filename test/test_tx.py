"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 22.10
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.height import Height
from graphsense.model.tx_account import TxAccount
from graphsense.model.tx_utxo import TxUtxo
from graphsense.model.tx_values import TxValues
from graphsense.model.values import Values
globals()['Height'] = Height
globals()['TxAccount'] = TxAccount
globals()['TxUtxo'] = TxUtxo
globals()['TxValues'] = TxValues
globals()['Values'] = Values
from graphsense.model.tx import Tx


class TestTx(unittest.TestCase):
    """Tx unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTx(self):
        """Test Tx"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Tx()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
