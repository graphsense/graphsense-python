"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address import Address
from graphsense.model.token_values import TokenValues
from graphsense.model.values import Values
globals()['Address'] = Address
globals()['TokenValues'] = TokenValues
globals()['Values'] = Values
from graphsense.model.neighbor_address import NeighborAddress


class TestNeighborAddress(unittest.TestCase):
    """NeighborAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNeighborAddress(self):
        """Test NeighborAddress"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NeighborAddress()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
