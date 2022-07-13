"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.height import Height
from graphsense.model.values import Values
globals()['Height'] = Height
globals()['Values'] = Values
from graphsense.model.link_utxo import LinkUtxo


class TestLinkUtxo(unittest.TestCase):
    """LinkUtxo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLinkUtxo(self):
        """Test LinkUtxo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LinkUtxo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
