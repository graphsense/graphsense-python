"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.1-dev
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
