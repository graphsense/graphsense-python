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


class EntityWithTagsAllOf(object):
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
        'tag_coherence': 'float',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'tag_coherence': 'tag_coherence',
        'tags': 'tags'
    }

    def __init__(self, tag_coherence=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """EntityWithTagsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag_coherence = None
        self._tags = None
        self.discriminator = None

        if tag_coherence is not None:
            self.tag_coherence = tag_coherence
        self.tags = tags

    @property
    def tag_coherence(self):
        """Gets the tag_coherence of this EntityWithTagsAllOf.  # noqa: E501

        Tag coherence  # noqa: E501

        :return: The tag_coherence of this EntityWithTagsAllOf.  # noqa: E501
        :rtype: float
        """
        return self._tag_coherence

    @tag_coherence.setter
    def tag_coherence(self, tag_coherence):
        """Sets the tag_coherence of this EntityWithTagsAllOf.

        Tag coherence  # noqa: E501

        :param tag_coherence: The tag_coherence of this EntityWithTagsAllOf.  # noqa: E501
        :type tag_coherence: float
        """

        self._tag_coherence = tag_coherence

    @property
    def tags(self):
        """Gets the tags of this EntityWithTagsAllOf.  # noqa: E501

        Tags  # noqa: E501

        :return: The tags of this EntityWithTagsAllOf.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EntityWithTagsAllOf.

        Tags  # noqa: E501

        :param tags: The tags of this EntityWithTagsAllOf.  # noqa: E501
        :type tags: list[Tag]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if not isinstance(other, EntityWithTagsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityWithTagsAllOf):
            return True

        return self.to_dict() != other.to_dict()
