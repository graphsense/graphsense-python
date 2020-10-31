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
from graphsense.models.tag import Tag  # noqa: E501
from graphsense.rest import ApiException

class TestTag(unittest.TestCase):
    """Tag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Tag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = graphsense.models.tag.Tag()  # noqa: E501
        if include_optional :
            return Tag(
                abuse = '0', 
                active = True, 
                address = '0', 
                category = '0', 
                currency = '0', 
                label = '0', 
                lastmod = 56, 
                source = '0', 
                tagpack_uri = '0'
            )
        else :
            return Tag(
                active = True,
                address = '0',
                currency = '0',
                label = '0',
        )

    def testTag(self):
        """Test Tag"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
