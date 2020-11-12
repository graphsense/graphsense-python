# coding: utf-8

"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from graphsense.configuration import Configuration


class Stats(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currencies': 'list[CurrencyStats]',
        'notes': 'list[StatsNote]',
        'tags_source': 'StatsTagsSource',
        'tools': 'list[StatsTool]',
        'version': 'StatsVersion'
    }

    attribute_map = {
        'currencies': 'currencies',
        'notes': 'notes',
        'tags_source': 'tags_source',
        'tools': 'tools',
        'version': 'version'
    }

    def __init__(self, currencies=None, notes=None, tags_source=None, tools=None, version=None, local_vars_configuration=None):  # noqa: E501
        """Stats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currencies = None
        self._notes = None
        self._tags_source = None
        self._tools = None
        self._version = None
        self.discriminator = None

        if currencies is not None:
            self.currencies = currencies
        if notes is not None:
            self.notes = notes
        if tags_source is not None:
            self.tags_source = tags_source
        if tools is not None:
            self.tools = tools
        if version is not None:
            self.version = version

    @property
    def currencies(self):
        """Gets the currencies of this Stats.  # noqa: E501


        :return: The currencies of this Stats.  # noqa: E501
        :rtype: list[CurrencyStats]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """Sets the currencies of this Stats.


        :param currencies: The currencies of this Stats.  # noqa: E501
        :type currencies: list[CurrencyStats]
        """

        self._currencies = currencies

    @property
    def notes(self):
        """Gets the notes of this Stats.  # noqa: E501


        :return: The notes of this Stats.  # noqa: E501
        :rtype: list[StatsNote]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Stats.


        :param notes: The notes of this Stats.  # noqa: E501
        :type notes: list[StatsNote]
        """

        self._notes = notes

    @property
    def tags_source(self):
        """Gets the tags_source of this Stats.  # noqa: E501


        :return: The tags_source of this Stats.  # noqa: E501
        :rtype: StatsTagsSource
        """
        return self._tags_source

    @tags_source.setter
    def tags_source(self, tags_source):
        """Sets the tags_source of this Stats.


        :param tags_source: The tags_source of this Stats.  # noqa: E501
        :type tags_source: StatsTagsSource
        """

        self._tags_source = tags_source

    @property
    def tools(self):
        """Gets the tools of this Stats.  # noqa: E501


        :return: The tools of this Stats.  # noqa: E501
        :rtype: list[StatsTool]
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        """Sets the tools of this Stats.


        :param tools: The tools of this Stats.  # noqa: E501
        :type tools: list[StatsTool]
        """

        self._tools = tools

    @property
    def version(self):
        """Gets the version of this Stats.  # noqa: E501


        :return: The version of this Stats.  # noqa: E501
        :rtype: StatsVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Stats.


        :param version: The version of this Stats.  # noqa: E501
        :type version: StatsVersion
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Stats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Stats):
            return True

        return self.to_dict() != other.to_dict()
