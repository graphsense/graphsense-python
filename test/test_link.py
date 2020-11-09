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
from graphsense.models.link import Link  # noqa: E501
from graphsense.rest import ApiException

class TestLink(unittest.TestCase):
    """Link unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Link
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = graphsense.models.link.Link()  # noqa: E501
        if include_optional :
            return Link(
                height = 1, 
                input_value = graphsense.models.values.values(
                    eur = 56, 
                    usd = 56, 
                    value = 56, ), 
                output_value = graphsense.models.values.values(
                    eur = 56, 
                    usd = 56, 
                    value = 56, ), 
                timestamp = 56, 
                tx_hash = '0'
            )
        else :
            return Link(
                height = 1,
                input_value = graphsense.models.values.values(
                    eur = 56, 
                    usd = 56, 
                    value = 56, ),
                output_value = graphsense.models.values.values(
                    eur = 56, 
                    usd = 56, 
                    value = 56, ),
                timestamp = 56,
                tx_hash = '0',
        )

    def testLink(self):
        """Test Link"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
