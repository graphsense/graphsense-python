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
from graphsense.model.search_result_level3_all_of import SearchResultLevel3AllOf
from graphsense.model.search_result_level4 import SearchResultLevel4
globals()['Address'] = Address
globals()['Entity'] = Entity
globals()['Neighbor'] = Neighbor
globals()['SearchResultLeaf'] = SearchResultLeaf
globals()['SearchResultLevel3AllOf'] = SearchResultLevel3AllOf
globals()['SearchResultLevel4'] = SearchResultLevel4
from graphsense.model.search_result_level3 import SearchResultLevel3


class TestSearchResultLevel3(unittest.TestCase):
    """SearchResultLevel3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResultLevel3(self):
        """Test SearchResultLevel3"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResultLevel3()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()