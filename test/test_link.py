"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.2-dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.height import Height
from graphsense.model.link_utxo import LinkUtxo
from graphsense.model.tx_account import TxAccount
from graphsense.model.values import Values
globals()['Height'] = Height
globals()['LinkUtxo'] = LinkUtxo
globals()['TxAccount'] = TxAccount
globals()['Values'] = Values
from graphsense.model.link import Link


class TestLink(unittest.TestCase):
    """Link unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLink(self):
        """Test Link"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Link()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
