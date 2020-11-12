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


class StatsLedger(object):
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
        'id': 'str',
        'report_uuid': 'str',
        'version': 'StatsLedgerVersion',
        'visible_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'report_uuid': 'report_uuid',
        'version': 'version',
        'visible_name': 'visible_name'
    }

    def __init__(self, id=None, report_uuid=None, version=None, visible_name=None, local_vars_configuration=None):  # noqa: E501
        """StatsLedger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._report_uuid = None
        self._version = None
        self._visible_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if report_uuid is not None:
            self.report_uuid = report_uuid
        if version is not None:
            self.version = version
        if visible_name is not None:
            self.visible_name = visible_name

    @property
    def id(self):
        """Gets the id of this StatsLedger.  # noqa: E501


        :return: The id of this StatsLedger.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatsLedger.


        :param id: The id of this StatsLedger.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def report_uuid(self):
        """Gets the report_uuid of this StatsLedger.  # noqa: E501


        :return: The report_uuid of this StatsLedger.  # noqa: E501
        :rtype: str
        """
        return self._report_uuid

    @report_uuid.setter
    def report_uuid(self, report_uuid):
        """Sets the report_uuid of this StatsLedger.


        :param report_uuid: The report_uuid of this StatsLedger.  # noqa: E501
        :type report_uuid: str
        """

        self._report_uuid = report_uuid

    @property
    def version(self):
        """Gets the version of this StatsLedger.  # noqa: E501


        :return: The version of this StatsLedger.  # noqa: E501
        :rtype: StatsLedgerVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StatsLedger.


        :param version: The version of this StatsLedger.  # noqa: E501
        :type version: StatsLedgerVersion
        """

        self._version = version

    @property
    def visible_name(self):
        """Gets the visible_name of this StatsLedger.  # noqa: E501


        :return: The visible_name of this StatsLedger.  # noqa: E501
        :rtype: str
        """
        return self._visible_name

    @visible_name.setter
    def visible_name(self, visible_name):
        """Sets the visible_name of this StatsLedger.


        :param visible_name: The visible_name of this StatsLedger.  # noqa: E501
        :type visible_name: str
        """

        self._visible_name = visible_name

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
        if not isinstance(other, StatsLedger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsLedger):
            return True

        return self.to_dict() != other.to_dict()
