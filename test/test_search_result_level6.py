"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.1-dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address import Address
from graphsense.model.entity import Entity
from graphsense.model.neighbor import Neighbor
from graphsense.model.search_result_leaf import SearchResultLeaf
from graphsense.model.search_result_level6_all_of import SearchResultLevel6AllOf
globals()['Address'] = Address
globals()['Entity'] = Entity
globals()['Neighbor'] = Neighbor
globals()['SearchResultLeaf'] = SearchResultLeaf
globals()['SearchResultLevel6AllOf'] = SearchResultLevel6AllOf
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
