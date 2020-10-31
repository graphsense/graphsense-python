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


class Neighbor(object):
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
        'balance': 'Values',
        'estimated_value': 'Values',
        'id': 'str',
        'labels': 'list[str]',
        'no_txs': 'int',
        'node_type': 'str',
        'received': 'Values'
    }

    attribute_map = {
        'balance': 'balance',
        'estimated_value': 'estimated_value',
        'id': 'id',
        'labels': 'labels',
        'no_txs': 'no_txs',
        'node_type': 'node_type',
        'received': 'received'
    }

    def __init__(self, balance=None, estimated_value=None, id=None, labels=None, no_txs=None, node_type=None, received=None, local_vars_configuration=None):  # noqa: E501
        """Neighbor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._balance = None
        self._estimated_value = None
        self._id = None
        self._labels = None
        self._no_txs = None
        self._node_type = None
        self._received = None
        self.discriminator = None

        self.balance = balance
        self.estimated_value = estimated_value
        self.id = id
        self.labels = labels
        self.no_txs = no_txs
        self.node_type = node_type
        self.received = received

    @property
    def balance(self):
        """Gets the balance of this Neighbor.  # noqa: E501


        :return: The balance of this Neighbor.  # noqa: E501
        :rtype: Values
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Neighbor.


        :param balance: The balance of this Neighbor.  # noqa: E501
        :type balance: Values
        """
        if self.local_vars_configuration.client_side_validation and balance is None:  # noqa: E501
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def estimated_value(self):
        """Gets the estimated_value of this Neighbor.  # noqa: E501


        :return: The estimated_value of this Neighbor.  # noqa: E501
        :rtype: Values
        """
        return self._estimated_value

    @estimated_value.setter
    def estimated_value(self, estimated_value):
        """Sets the estimated_value of this Neighbor.


        :param estimated_value: The estimated_value of this Neighbor.  # noqa: E501
        :type estimated_value: Values
        """
        if self.local_vars_configuration.client_side_validation and estimated_value is None:  # noqa: E501
            raise ValueError("Invalid value for `estimated_value`, must not be `None`")  # noqa: E501

        self._estimated_value = estimated_value

    @property
    def id(self):
        """Gets the id of this Neighbor.  # noqa: E501

        address or entity id  # noqa: E501

        :return: The id of this Neighbor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Neighbor.

        address or entity id  # noqa: E501

        :param id: The id of this Neighbor.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this Neighbor.  # noqa: E501

        labels  # noqa: E501

        :return: The labels of this Neighbor.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Neighbor.

        labels  # noqa: E501

        :param labels: The labels of this Neighbor.  # noqa: E501
        :type labels: list[str]
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def no_txs(self):
        """Gets the no_txs of this Neighbor.  # noqa: E501

        number of transactions  # noqa: E501

        :return: The no_txs of this Neighbor.  # noqa: E501
        :rtype: int
        """
        return self._no_txs

    @no_txs.setter
    def no_txs(self, no_txs):
        """Sets the no_txs of this Neighbor.

        number of transactions  # noqa: E501

        :param no_txs: The no_txs of this Neighbor.  # noqa: E501
        :type no_txs: int
        """
        if self.local_vars_configuration.client_side_validation and no_txs is None:  # noqa: E501
            raise ValueError("Invalid value for `no_txs`, must not be `None`")  # noqa: E501

        self._no_txs = no_txs

    @property
    def node_type(self):
        """Gets the node_type of this Neighbor.  # noqa: E501

        address or entity  # noqa: E501

        :return: The node_type of this Neighbor.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Neighbor.

        address or entity  # noqa: E501

        :param node_type: The node_type of this Neighbor.  # noqa: E501
        :type node_type: str
        """
        if self.local_vars_configuration.client_side_validation and node_type is None:  # noqa: E501
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501
        allowed_values = ["address", "entity"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and node_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def received(self):
        """Gets the received of this Neighbor.  # noqa: E501


        :return: The received of this Neighbor.  # noqa: E501
        :rtype: Values
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this Neighbor.


        :param received: The received of this Neighbor.  # noqa: E501
        :type received: Values
        """
        if self.local_vars_configuration.client_side_validation and received is None:  # noqa: E501
            raise ValueError("Invalid value for `received`, must not be `None`")  # noqa: E501

        self._received = received

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
        if not isinstance(other, Neighbor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Neighbor):
            return True

        return self.to_dict() != other.to_dict()
