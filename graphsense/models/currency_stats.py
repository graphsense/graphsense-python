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


class CurrencyStats(object):
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
        'name': 'str',
        'no_address_relations': 'int',
        'no_addresses': 'int',
        'no_blocks': 'int',
        'no_entities': 'int',
        'no_labels': 'int',
        'no_txs': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'name': 'name',
        'no_address_relations': 'no_address_relations',
        'no_addresses': 'no_addresses',
        'no_blocks': 'no_blocks',
        'no_entities': 'no_entities',
        'no_labels': 'no_labels',
        'no_txs': 'no_txs',
        'timestamp': 'timestamp'
    }

    def __init__(self, name=None, no_address_relations=None, no_addresses=None, no_blocks=None, no_entities=None, no_labels=None, no_txs=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """CurrencyStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._no_address_relations = None
        self._no_addresses = None
        self._no_blocks = None
        self._no_entities = None
        self._no_labels = None
        self._no_txs = None
        self._timestamp = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if no_address_relations is not None:
            self.no_address_relations = no_address_relations
        if no_addresses is not None:
            self.no_addresses = no_addresses
        if no_blocks is not None:
            self.no_blocks = no_blocks
        if no_entities is not None:
            self.no_entities = no_entities
        if no_labels is not None:
            self.no_labels = no_labels
        if no_txs is not None:
            self.no_txs = no_txs
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def name(self):
        """Gets the name of this CurrencyStats.  # noqa: E501


        :return: The name of this CurrencyStats.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrencyStats.


        :param name: The name of this CurrencyStats.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def no_address_relations(self):
        """Gets the no_address_relations of this CurrencyStats.  # noqa: E501


        :return: The no_address_relations of this CurrencyStats.  # noqa: E501
        :rtype: int
        """
        return self._no_address_relations

    @no_address_relations.setter
    def no_address_relations(self, no_address_relations):
        """Sets the no_address_relations of this CurrencyStats.


        :param no_address_relations: The no_address_relations of this CurrencyStats.  # noqa: E501
        :type no_address_relations: int
        """

        self._no_address_relations = no_address_relations

    @property
    def no_addresses(self):
        """Gets the no_addresses of this CurrencyStats.  # noqa: E501


        :return: The no_addresses of this CurrencyStats.  # noqa: E501
        :rtype: int
        """
        return self._no_addresses

    @no_addresses.setter
    def no_addresses(self, no_addresses):
        """Sets the no_addresses of this CurrencyStats.


        :param no_addresses: The no_addresses of this CurrencyStats.  # noqa: E501
        :type no_addresses: int
        """

        self._no_addresses = no_addresses

    @property
    def no_blocks(self):
        """Gets the no_blocks of this CurrencyStats.  # noqa: E501


        :return: The no_blocks of this CurrencyStats.  # noqa: E501
        :rtype: int
        """
        return self._no_blocks

    @no_blocks.setter
    def no_blocks(self, no_blocks):
        """Sets the no_blocks of this CurrencyStats.


        :param no_blocks: The no_blocks of this CurrencyStats.  # noqa: E501
        :type no_blocks: int
        """

        self._no_blocks = no_blocks

    @property
    def no_entities(self):
        """Gets the no_entities of this CurrencyStats.  # noqa: E501


        :return: The no_entities of this CurrencyStats.  # noqa: E501
        :rtype: int
        """
        return self._no_entities

    @no_entities.setter
    def no_entities(self, no_entities):
        """Sets the no_entities of this CurrencyStats.


        :param no_entities: The no_entities of this CurrencyStats.  # noqa: E501
        :type no_entities: int
        """

        self._no_entities = no_entities

    @property
    def no_labels(self):
        """Gets the no_labels of this CurrencyStats.  # noqa: E501


        :return: The no_labels of this CurrencyStats.  # noqa: E501
        :rtype: int
        """
        return self._no_labels

    @no_labels.setter
    def no_labels(self, no_labels):
        """Sets the no_labels of this CurrencyStats.


        :param no_labels: The no_labels of this CurrencyStats.  # noqa: E501
        :type no_labels: int
        """

        self._no_labels = no_labels

    @property
    def no_txs(self):
        """Gets the no_txs of this CurrencyStats.  # noqa: E501


        :return: The no_txs of this CurrencyStats.  # noqa: E501
        :rtype: int
        """
        return self._no_txs

    @no_txs.setter
    def no_txs(self, no_txs):
        """Sets the no_txs of this CurrencyStats.


        :param no_txs: The no_txs of this CurrencyStats.  # noqa: E501
        :type no_txs: int
        """

        self._no_txs = no_txs

    @property
    def timestamp(self):
        """Gets the timestamp of this CurrencyStats.  # noqa: E501


        :return: The timestamp of this CurrencyStats.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CurrencyStats.


        :param timestamp: The timestamp of this CurrencyStats.  # noqa: E501
        :type timestamp: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, CurrencyStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrencyStats):
            return True

        return self.to_dict() != other.to_dict()