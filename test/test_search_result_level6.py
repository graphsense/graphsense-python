"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address import Address
from graphsense.model.neighbor_entity import NeighborEntity
from graphsense.model.search_result_leaf import SearchResultLeaf
globals()['Address'] = Address
globals()['NeighborEntity'] = NeighborEntity
globals()['SearchResultLeaf'] = SearchResultLeaf
from graphsense.model.search_result_level6 import SearchResultLevel6


class TestSearchResultLevel6(unittest.TestCase):
    """SearchResultLevel6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResultLevel6(self):
        """Test SearchResultLevel6"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResultLevel6()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
