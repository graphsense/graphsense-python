"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address_tag import AddressTag
from graphsense.model.entity_tag import EntityTag
globals()['AddressTag'] = AddressTag
globals()['EntityTag'] = EntityTag
from graphsense.model.tags import Tags


class TestTags(unittest.TestCase):
    """Tags unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTags(self):
        """Test Tags"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Tags()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()