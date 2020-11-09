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
from graphsense.models.entity_with_tags_all_of import EntityWithTagsAllOf  # noqa: E501
from graphsense.rest import ApiException

class TestEntityWithTagsAllOf(unittest.TestCase):
    """EntityWithTagsAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EntityWithTagsAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = graphsense.models.entity_with_tags_all_of.EntityWithTagsAllOf()  # noqa: E501
        if include_optional :
            return EntityWithTagsAllOf(
                tag_coherence = null, 
                tags = [
                    graphsense.models.tag.tag(
                        abuse = '0', 
                        active = True, 
                        address = '0', 
                        category = '0', 
                        currency = '0', 
                        label = '0', 
                        lastmod = 56, 
                        source = '0', 
                        tagpack_uri = '0', )
                    ]
            )
        else :
            return EntityWithTagsAllOf(
                tags = [
                    graphsense.models.tag.tag(
                        abuse = '0', 
                        active = True, 
                        address = '0', 
                        category = '0', 
                        currency = '0', 
                        label = '0', 
                        lastmod = 56, 
                        source = '0', 
                        tagpack_uri = '0', )
                    ],
        )

    def testEntityWithTagsAllOf(self):
        """Test EntityWithTagsAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
