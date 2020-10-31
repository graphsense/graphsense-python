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


class Block(object):
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
        'block_hash': 'str',
        'height': 'int',
        'no_txs': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'block_hash': 'block_hash',
        'height': 'height',
        'no_txs': 'no_txs',
        'timestamp': 'timestamp'
    }

    def __init__(self, block_hash=None, height=None, no_txs=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """Block - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._block_hash = None
        self._height = None
        self._no_txs = None
        self._timestamp = None
        self.discriminator = None

        if block_hash is not None:
            self.block_hash = block_hash
        if height is not None:
            self.height = height
        if no_txs is not None:
            self.no_txs = no_txs
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def block_hash(self):
        """Gets the block_hash of this Block.  # noqa: E501


        :return: The block_hash of this Block.  # noqa: E501
        :rtype: str
        """
        return self._block_hash

    @block_hash.setter
    def block_hash(self, block_hash):
        """Sets the block_hash of this Block.


        :param block_hash: The block_hash of this Block.  # noqa: E501
        :type block_hash: str
        """

        self._block_hash = block_hash

    @property
    def height(self):
        """Gets the height of this Block.  # noqa: E501

        Height  # noqa: E501

        :return: The height of this Block.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Block.

        Height  # noqa: E501

        :param height: The height of this Block.  # noqa: E501
        :type height: int
        """
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height < 1):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `1`")  # noqa: E501

        self._height = height

    @property
    def no_txs(self):
        """Gets the no_txs of this Block.  # noqa: E501


        :return: The no_txs of this Block.  # noqa: E501
        :rtype: int
        """
        return self._no_txs

    @no_txs.setter
    def no_txs(self, no_txs):
        """Sets the no_txs of this Block.


        :param no_txs: The no_txs of this Block.  # noqa: E501
        :type no_txs: int
        """

        self._no_txs = no_txs

    @property
    def timestamp(self):
        """Gets the timestamp of this Block.  # noqa: E501


        :return: The timestamp of this Block.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Block.


        :param timestamp: The timestamp of this Block.  # noqa: E501
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
        if not isinstance(other, Block):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Block):
            return True

        return self.to_dict() != other.to_dict()
