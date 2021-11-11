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
from graphsense.model.search_result_level5_all_of import SearchResultLevel5AllOf
from graphsense.model.search_result_level6 import SearchResultLevel6
globals()['Address'] = Address
globals()['Entity'] = Entity
globals()['Neighbor'] = Neighbor
globals()['SearchResultLeaf'] = SearchResultLeaf
globals()['SearchResultLevel5AllOf'] = SearchResultLevel5AllOf
globals()['SearchResultLevel6'] = SearchResultLevel6
from graphsense.model.search_result_level5 import SearchResultLevel5


class TestSearchResultLevel5(unittest.TestCase):
    """SearchResultLevel5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResultLevel5(self):
        """Test SearchResultLevel5"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResultLevel5()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
