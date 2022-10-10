"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address_tx_utxo import AddressTxUtxo
from graphsense.model.height import Height
from graphsense.model.tx_account import TxAccount
from graphsense.model.values import Values
globals()['AddressTxUtxo'] = AddressTxUtxo
globals()['Height'] = Height
globals()['TxAccount'] = TxAccount
globals()['Values'] = Values
from graphsense.model.address_tx import AddressTx


class TestAddressTx(unittest.TestCase):
    """AddressTx unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddressTx(self):
        """Test AddressTx"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddressTx()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
