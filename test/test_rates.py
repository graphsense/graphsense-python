"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.height import Height
from graphsense.model.rate import Rate
globals()['Height'] = Height
globals()['Rate'] = Rate
from graphsense.model.rates import Rates


class TestRates(unittest.TestCase):
    """Rates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRates(self):
        """Test Rates"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Rates()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
