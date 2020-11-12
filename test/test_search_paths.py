# coding: utf-8

"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import graphsense
from graphsense.models.search_paths import SearchPaths  # noqa: E501
from graphsense.rest import ApiException

class TestSearchPaths(unittest.TestCase):
    """SearchPaths unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SearchPaths
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = graphsense.models.search_paths.SearchPaths()  # noqa: E501
        if include_optional :
            return SearchPaths(
                matching_addresses = [
                    null
                    ], 
                node = null, 
                paths = [
                    graphsense.models.search_paths.search_paths(
                        matching_addresses = [
                            null
                            ], 
                        node = null, 
                        paths = [
                            graphsense.models.search_paths.search_paths(
                                relation = graphsense.models.neighbor.neighbor(
                                    balance = graphsense.models.values.values(
                                        eur = 56, 
                                        usd = 56, 
                                        value = 56, ), 
                                    estimated_value = graphsense.models.values.values(
                                        eur = 56, 
                                        usd = 56, 
                                        value = 56, ), 
                                    id = '0', 
                                    labels = [
                                        '0'
                                        ], 
                                    no_txs = 56, 
                                    node_type = 'address', 
                                    received = graphsense.models.values.values(
                                        eur = 56, 
                                        usd = 56, 
                                        value = 56, ), ), )
                            ], 
                        relation = graphsense.models.neighbor.neighbor(
                            balance = graphsense.models.values.values(
                                eur = 56, 
                                usd = 56, 
                                value = 56, ), 
                            estimated_value = graphsense.models.values.values(
                                eur = 56, 
                                usd = 56, 
                                value = 56, ), 
                            id = '0', 
                            labels = [
                                '0'
                                ], 
                            no_txs = 56, 
                            node_type = 'address', 
                            received = graphsense.models.values.values(
                                eur = 56, 
                                usd = 56, 
                                value = 56, ), ), )
                    ], 
                relation = graphsense.models.neighbor.neighbor(
                    balance = graphsense.models.values.values(
                        eur = 56, 
                        usd = 56, 
                        value = 56, ), 
                    estimated_value = graphsense.models.values.values(
                        eur = 56, 
                        usd = 56, 
                        value = 56, ), 
                    id = '0', 
                    labels = [
                        '0'
                        ], 
                    no_txs = 56, 
                    node_type = 'address', 
                    received = graphsense.models.values.values(
                        eur = 56, 
                        usd = 56, 
                        value = 56, ), )
            )
        else :
            return SearchPaths(
        )

    def testSearchPaths(self):
        """Test SearchPaths"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
