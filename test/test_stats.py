"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import graphsense
from graphsense.model.currency_stats import CurrencyStats
from graphsense.model.stats_note import StatsNote
from graphsense.model.stats_tags_source import StatsTagsSource
from graphsense.model.stats_tool import StatsTool
from graphsense.model.stats_version import StatsVersion
globals()['CurrencyStats'] = CurrencyStats
globals()['StatsNote'] = StatsNote
globals()['StatsTagsSource'] = StatsTagsSource
globals()['StatsTool'] = StatsTool
globals()['StatsVersion'] = StatsVersion
from graphsense.model.stats import Stats


class TestStats(unittest.TestCase):
    """Stats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStats(self):
        """Test Stats"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Stats()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
