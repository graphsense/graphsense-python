"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address import Address
from graphsense.model.entity import Entity
from graphsense.model.neighbor import Neighbor
from graphsense.model.search_result_leaf import SearchResultLeaf
from graphsense.model.search_result_level1_all_of import SearchResultLevel1AllOf
from graphsense.model.search_result_level2 import SearchResultLevel2
globals()['Address'] = Address
globals()['Entity'] = Entity
globals()['Neighbor'] = Neighbor
globals()['SearchResultLeaf'] = SearchResultLeaf
globals()['SearchResultLevel1AllOf'] = SearchResultLevel1AllOf
globals()['SearchResultLevel2'] = SearchResultLevel2
from graphsense.model.search_result_level1 import SearchResultLevel1


class TestSearchResultLevel1(unittest.TestCase):
    """SearchResultLevel1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResultLevel1(self):
        """Test SearchResultLevel1"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResultLevel1()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
