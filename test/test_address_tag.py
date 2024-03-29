"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address_tag_all_of import AddressTagAllOf
from graphsense.model.tag import Tag
globals()['AddressTagAllOf'] = AddressTagAllOf
globals()['Tag'] = Tag
from graphsense.model.address_tag import AddressTag


class TestAddressTag(unittest.TestCase):
    """AddressTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddressTag(self):
        """Test AddressTag"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddressTag()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
