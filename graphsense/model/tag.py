"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from graphsense.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from graphsense.exceptions import ApiAttributeError



class Tag(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'currency': (str,),  # noqa: E501
            'is_cluster_definer': (bool,),  # noqa: E501
            'label': (str,),  # noqa: E501
            'tagpack_creator': (str,),  # noqa: E501
            'tagpack_is_public': (bool,),  # noqa: E501
            'tagpack_title': (str,),  # noqa: E501
            'abuse': (str,),  # noqa: E501
            'actor': (str,),  # noqa: E501
            'category': (str,),  # noqa: E501
            'confidence': (str,),  # noqa: E501
            'confidence_level': (int,),  # noqa: E501
            'lastmod': (int,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'tagpack_uri': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'currency': 'currency',  # noqa: E501
        'is_cluster_definer': 'is_cluster_definer',  # noqa: E501
        'label': 'label',  # noqa: E501
        'tagpack_creator': 'tagpack_creator',  # noqa: E501
        'tagpack_is_public': 'tagpack_is_public',  # noqa: E501
        'tagpack_title': 'tagpack_title',  # noqa: E501
        'abuse': 'abuse',  # noqa: E501
        'actor': 'actor',  # noqa: E501
        'category': 'category',  # noqa: E501
        'confidence': 'confidence',  # noqa: E501
        'confidence_level': 'confidence_level',  # noqa: E501
        'lastmod': 'lastmod',  # noqa: E501
        'source': 'source',  # noqa: E501
        'tagpack_uri': 'tagpack_uri',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, currency, is_cluster_definer, label, tagpack_creator, tagpack_is_public, tagpack_title, *args, **kwargs):  # noqa: E501
        """Tag - a model defined in OpenAPI

        Args:
            currency (str): crypto currency code
            is_cluster_definer (bool): whether the address tag applies to the entity level
            label (str): Label
            tagpack_creator (str): Tagpack creator
            tagpack_is_public (bool): whether the address is public
            tagpack_title (str): Tagpack title

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            abuse (str): Abuses. [optional]  # noqa: E501
            actor (str): id of the actor that controlls the address. [optional]  # noqa: E501
            category (str): Category. [optional]  # noqa: E501
            confidence (str): Confidence name. [optional]  # noqa: E501
            confidence_level (int): Confidence level. [optional]  # noqa: E501
            lastmod (int): Last modified. [optional]  # noqa: E501
            source (str): Source. [optional]  # noqa: E501
            tagpack_uri (str): Tagpack URI. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.currency = currency
        self.is_cluster_definer = is_cluster_definer
        self.label = label
        self.tagpack_creator = tagpack_creator
        self.tagpack_is_public = tagpack_is_public
        self.tagpack_title = tagpack_title
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, currency, is_cluster_definer, label, tagpack_creator, tagpack_is_public, tagpack_title, *args, **kwargs):  # noqa: E501
        """Tag - a model defined in OpenAPI

        Args:
            currency (str): crypto currency code
            is_cluster_definer (bool): whether the address tag applies to the entity level
            label (str): Label
            tagpack_creator (str): Tagpack creator
            tagpack_is_public (bool): whether the address is public
            tagpack_title (str): Tagpack title

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            abuse (str): Abuses. [optional]  # noqa: E501
            actor (str): id of the actor that controlls the address. [optional]  # noqa: E501
            category (str): Category. [optional]  # noqa: E501
            confidence (str): Confidence name. [optional]  # noqa: E501
            confidence_level (int): Confidence level. [optional]  # noqa: E501
            lastmod (int): Last modified. [optional]  # noqa: E501
            source (str): Source. [optional]  # noqa: E501
            tagpack_uri (str): Tagpack URI. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.currency = currency
        self.is_cluster_definer = is_cluster_definer
        self.label = label
        self.tagpack_creator = tagpack_creator
        self.tagpack_is_public = tagpack_is_public
        self.tagpack_title = tagpack_title
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
