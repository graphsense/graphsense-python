"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.address_tag import AddressTag
from graphsense.model.labeled_item_refs import LabeledItemRefs
from graphsense.model.token_values import TokenValues
from graphsense.model.tx_summary import TxSummary
from graphsense.model.values import Values
globals()['AddressTag'] = AddressTag
globals()['LabeledItemRefs'] = LabeledItemRefs
globals()['TokenValues'] = TokenValues
globals()['TxSummary'] = TxSummary
globals()['Values'] = Values
from graphsense.model.entity import Entity


class TestEntity(unittest.TestCase):
    """Entity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEntity(self):
        """Test Entity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Entity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
