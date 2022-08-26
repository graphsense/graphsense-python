"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address import Address
from graphsense.model.neighbor_entity import NeighborEntity
from graphsense.model.search_result_leaf import SearchResultLeaf
from graphsense.model.search_result_level4_all_of import SearchResultLevel4AllOf
from graphsense.model.search_result_level5 import SearchResultLevel5
globals()['Address'] = Address
globals()['NeighborEntity'] = NeighborEntity
globals()['SearchResultLeaf'] = SearchResultLeaf
globals()['SearchResultLevel4AllOf'] = SearchResultLevel4AllOf
globals()['SearchResultLevel5'] = SearchResultLevel5
from graphsense.model.search_result_level4 import SearchResultLevel4


class TestSearchResultLevel4(unittest.TestCase):
    """SearchResultLevel4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResultLevel4(self):
        """Test SearchResultLevel4"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResultLevel4()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
