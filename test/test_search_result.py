"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.search_result_by_currency import SearchResultByCurrency
from graphsense.model.search_result_labels import SearchResultLabels
globals()['SearchResultByCurrency'] = SearchResultByCurrency
globals()['SearchResultLabels'] = SearchResultLabels
from graphsense.model.search_result import SearchResult


class TestSearchResult(unittest.TestCase):
    """SearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResult(self):
        """Test SearchResult"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResult()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
