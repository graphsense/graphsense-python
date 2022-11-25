"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
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


def lazy_import():
    from graphsense.model.height import Height
    from graphsense.model.tx_values import TxValues
    from graphsense.model.values import Values
    globals()['Height'] = Height
    globals()['TxValues'] = TxValues
    globals()['Values'] = Values


class TxUtxo(ModelNormal):
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
        lazy_import()
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
        lazy_import()
        return {
            'coinbase': (bool,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'height': (Height,),  # noqa: E501
            'no_inputs': (int,),  # noqa: E501
            'no_outputs': (int,),  # noqa: E501
            'timestamp': (int,),  # noqa: E501
            'total_input': (Values,),  # noqa: E501
            'total_output': (Values,),  # noqa: E501
            'tx_hash': (str,),  # noqa: E501
            'tx_type': (str,),  # noqa: E501
            'inputs': (TxValues,),  # noqa: E501
            'outputs': (TxValues,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'coinbase': 'coinbase',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'height': 'height',  # noqa: E501
        'no_inputs': 'no_inputs',  # noqa: E501
        'no_outputs': 'no_outputs',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'total_input': 'total_input',  # noqa: E501
        'total_output': 'total_output',  # noqa: E501
        'tx_hash': 'tx_hash',  # noqa: E501
        'tx_type': 'tx_type',  # noqa: E501
        'inputs': 'inputs',  # noqa: E501
        'outputs': 'outputs',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, coinbase, currency, height, no_inputs, no_outputs, timestamp, total_input, total_output, tx_hash, *args, **kwargs):  # noqa: E501
        """TxUtxo - a model defined in OpenAPI

        Args:
            coinbase (bool): Coinbase transaction flag
            currency (str): crypto currency code
            height (Height):
            no_inputs (int): number of input addresses
            no_outputs (int): number of output addresses
            timestamp (int): Timestamp
            total_input (Values):
            total_output (Values):
            tx_hash (str): Transaction hash

        Keyword Args:
            tx_type (str): defaults to "utxo"  # noqa: E501
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
            inputs (TxValues): [optional]  # noqa: E501
            outputs (TxValues): [optional]  # noqa: E501
        """

        tx_type = kwargs.get('tx_type', "utxo")
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

        self.coinbase = coinbase
        self.currency = currency
        self.height = height
        self.no_inputs = no_inputs
        self.no_outputs = no_outputs
        self.timestamp = timestamp
        self.total_input = total_input
        self.total_output = total_output
        self.tx_hash = tx_hash
        self.tx_type = tx_type
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
    def __init__(self, coinbase, currency, height, no_inputs, no_outputs, timestamp, total_input, total_output, tx_hash, *args, **kwargs):  # noqa: E501
        """TxUtxo - a model defined in OpenAPI

        Args:
            coinbase (bool): Coinbase transaction flag
            currency (str): crypto currency code
            height (Height):
            no_inputs (int): number of input addresses
            no_outputs (int): number of output addresses
            timestamp (int): Timestamp
            total_input (Values):
            total_output (Values):
            tx_hash (str): Transaction hash

        Keyword Args:
            tx_type (str): defaults to "utxo"  # noqa: E501
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
            inputs (TxValues): [optional]  # noqa: E501
            outputs (TxValues): [optional]  # noqa: E501
        """

        tx_type = kwargs.get('tx_type', "utxo")
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

        self.coinbase = coinbase
        self.currency = currency
        self.height = height
        self.no_inputs = no_inputs
        self.no_outputs = no_outputs
        self.timestamp = timestamp
        self.total_input = total_input
        self.total_output = total_output
        self.tx_hash = tx_hash
        self.tx_type = tx_type
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
