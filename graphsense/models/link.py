# coding: utf-8

"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.4.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from graphsense.configuration import Configuration


class Link(object):
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
        'height': 'int',
        'input_value': 'Values',
        'output_value': 'Values',
        'timestamp': 'int',
        'tx_hash': 'str'
    }

    attribute_map = {
        'height': 'height',
        'input_value': 'input_value',
        'output_value': 'output_value',
        'timestamp': 'timestamp',
        'tx_hash': 'tx_hash'
    }

    def __init__(self, height=None, input_value=None, output_value=None, timestamp=None, tx_hash=None, local_vars_configuration=None):  # noqa: E501
        """Link - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._height = None
        self._input_value = None
        self._output_value = None
        self._timestamp = None
        self._tx_hash = None
        self.discriminator = None

        self.height = height
        self.input_value = input_value
        self.output_value = output_value
        self.timestamp = timestamp
        self.tx_hash = tx_hash

    @property
    def height(self):
        """Gets the height of this Link.  # noqa: E501

        Height  # noqa: E501

        :return: The height of this Link.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Link.

        Height  # noqa: E501

        :param height: The height of this Link.  # noqa: E501
        :type height: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height < 1):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `1`")  # noqa: E501

        self._height = height

    @property
    def input_value(self):
        """Gets the input_value of this Link.  # noqa: E501


        :return: The input_value of this Link.  # noqa: E501
        :rtype: Values
        """
        return self._input_value

    @input_value.setter
    def input_value(self, input_value):
        """Sets the input_value of this Link.


        :param input_value: The input_value of this Link.  # noqa: E501
        :type input_value: Values
        """
        if self.local_vars_configuration.client_side_validation and input_value is None:  # noqa: E501
            raise ValueError("Invalid value for `input_value`, must not be `None`")  # noqa: E501

        self._input_value = input_value

    @property
    def output_value(self):
        """Gets the output_value of this Link.  # noqa: E501


        :return: The output_value of this Link.  # noqa: E501
        :rtype: Values
        """
        return self._output_value

    @output_value.setter
    def output_value(self, output_value):
        """Sets the output_value of this Link.


        :param output_value: The output_value of this Link.  # noqa: E501
        :type output_value: Values
        """
        if self.local_vars_configuration.client_side_validation and output_value is None:  # noqa: E501
            raise ValueError("Invalid value for `output_value`, must not be `None`")  # noqa: E501

        self._output_value = output_value

    @property
    def timestamp(self):
        """Gets the timestamp of this Link.  # noqa: E501

        Timestamp  # noqa: E501

        :return: The timestamp of this Link.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Link.

        Timestamp  # noqa: E501

        :param timestamp: The timestamp of this Link.  # noqa: E501
        :type timestamp: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def tx_hash(self):
        """Gets the tx_hash of this Link.  # noqa: E501

        Transaction hash  # noqa: E501

        :return: The tx_hash of this Link.  # noqa: E501
        :rtype: str
        """
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, tx_hash):
        """Sets the tx_hash of this Link.

        Transaction hash  # noqa: E501

        :param tx_hash: The tx_hash of this Link.  # noqa: E501
        :type tx_hash: str
        """
        if self.local_vars_configuration.client_side_validation and tx_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `tx_hash`, must not be `None`")  # noqa: E501

        self._tx_hash = tx_hash

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
        if not isinstance(other, Link):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Link):
            return True

        return self.to_dict() != other.to_dict()
