"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.1-dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import graphsense
from graphsense.api.rates_api import RatesApi  # noqa: E501


class TestRatesApi(unittest.TestCase):
    """RatesApi unit test stubs"""

    def setUp(self):
        self.api = RatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_exchange_rates(self):
        """Test case for get_exchange_rates

        Returns exchange rate for a given height  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
