"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.tx_summary import TxSummary
from graphsense.model.values import Values
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
