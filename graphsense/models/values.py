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


class Values(object):
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
        'eur': 'int',
        'usd': 'int',
        'value': 'int'
    }

    attribute_map = {
        'eur': 'eur',
        'usd': 'usd',
        'value': 'value'
    }

    def __init__(self, eur=None, usd=None, value=None, local_vars_configuration=None):  # noqa: E501
        """Values - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._eur = None
        self._usd = None
        self._value = None
        self.discriminator = None

        if eur is not None:
            self.eur = eur
        if usd is not None:
            self.usd = usd
        if value is not None:
            self.value = value

    @property
    def eur(self):
        """Gets the eur of this Values.  # noqa: E501


        :return: The eur of this Values.  # noqa: E501
        :rtype: int
        """
        return self._eur

    @eur.setter
    def eur(self, eur):
        """Sets the eur of this Values.


        :param eur: The eur of this Values.  # noqa: E501
        :type eur: int
        """

        self._eur = eur

    @property
    def usd(self):
        """Gets the usd of this Values.  # noqa: E501


        :return: The usd of this Values.  # noqa: E501
        :rtype: int
        """
        return self._usd

    @usd.setter
    def usd(self, usd):
        """Sets the usd of this Values.


        :param usd: The usd of this Values.  # noqa: E501
        :type usd: int
        """

        self._usd = usd

    @property
    def value(self):
        """Gets the value of this Values.  # noqa: E501


        :return: The value of this Values.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Values.


        :param value: The value of this Values.  # noqa: E501
        :type value: int
        """

        self._value = value

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
        if not isinstance(other, Values):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Values):
            return True

        return self.to_dict() != other.to_dict()
