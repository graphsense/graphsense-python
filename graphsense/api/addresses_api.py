"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from graphsense.api_client import ApiClient, Endpoint as _Endpoint
from graphsense.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from graphsense.model.address import Address
from graphsense.model.address_tags import AddressTags
from graphsense.model.address_txs import AddressTxs
from graphsense.model.entity import Entity
from graphsense.model.links import Links
from graphsense.model.neighbor_addresses import NeighborAddresses


class AddressesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_address(
            self,
            currency,
            address,
            **kwargs
        ):
            """Get an address, optionally with tags  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_address(currency, address, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                address (str): The cryptocurrency address

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Address
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['currency'] = \
                currency
            kwargs['address'] = \
                address
            return self.call_with_http_info(**kwargs)

        self.get_address = _Endpoint(
            settings={
                'response_type': (Address,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/addresses/{address}',
                'operation_id': 'get_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'address',
                ],
                'required': [
                    'currency',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'address':
                        (str,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'address': 'address',
                },
                'location_map': {
                    'currency': 'path',
                    'address': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_address
        )

        def __get_address_entity(
            self,
            currency,
            address,
            **kwargs
        ):
            """Get the entity of an address  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_address_entity(currency, address, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                address (str): The cryptocurrency address

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Entity
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['currency'] = \
                currency
            kwargs['address'] = \
                address
            return self.call_with_http_info(**kwargs)

        self.get_address_entity = _Endpoint(
            settings={
                'response_type': (Entity,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/addresses/{address}/entity',
                'operation_id': 'get_address_entity',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'address',
                ],
                'required': [
                    'currency',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'address':
                        (str,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'address': 'address',
                },
                'location_map': {
                    'currency': 'path',
                    'address': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_address_entity
        )

        def __list_address_links(
            self,
            currency,
            address,
            neighbor,
            **kwargs
        ):
            """Get outgoing transactions between two addresses  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_address_links(currency, address, neighbor, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                address (str): The cryptocurrency address
                neighbor (str): Neighbor address

            Keyword Args:
                page (str): Resumption token for retrieving the next page. [optional]
                pagesize (int): Number of items returned in a single page. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Links
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['currency'] = \
                currency
            kwargs['address'] = \
                address
            kwargs['neighbor'] = \
                neighbor
            return self.call_with_http_info(**kwargs)

        self.list_address_links = _Endpoint(
            settings={
                'response_type': (Links,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/addresses/{address}/links',
                'operation_id': 'list_address_links',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'address',
                    'neighbor',
                    'page',
                    'pagesize',
                ],
                'required': [
                    'currency',
                    'address',
                    'neighbor',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pagesize',
                ]
            },
            root_map={
                'validations': {
                    ('pagesize',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'address':
                        (str,),
                    'neighbor':
                        (str,),
                    'page':
                        (str,),
                    'pagesize':
                        (int,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'address': 'address',
                    'neighbor': 'neighbor',
                    'page': 'page',
                    'pagesize': 'pagesize',
                },
                'location_map': {
                    'currency': 'path',
                    'address': 'path',
                    'neighbor': 'query',
                    'page': 'query',
                    'pagesize': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_address_links
        )

        def __list_address_neighbors(
            self,
            currency,
            address,
            direction,
            **kwargs
        ):
            """Get an address's neighbors in the address graph  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_address_neighbors(currency, address, direction, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                address (str): The cryptocurrency address
                direction (str): Incoming or outgoing neighbors

            Keyword Args:
                include_labels (bool): Whether to include labels of first page of tags. [optional] if omitted the server will use the default value of False
                page (str): Resumption token for retrieving the next page. [optional]
                pagesize (int): Number of items returned in a single page. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                NeighborAddresses
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['currency'] = \
                currency
            kwargs['address'] = \
                address
            kwargs['direction'] = \
                direction
            return self.call_with_http_info(**kwargs)

        self.list_address_neighbors = _Endpoint(
            settings={
                'response_type': (NeighborAddresses,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/addresses/{address}/neighbors',
                'operation_id': 'list_address_neighbors',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'address',
                    'direction',
                    'include_labels',
                    'page',
                    'pagesize',
                ],
                'required': [
                    'currency',
                    'address',
                    'direction',
                ],
                'nullable': [
                ],
                'enum': [
                    'direction',
                ],
                'validation': [
                    'pagesize',
                ]
            },
            root_map={
                'validations': {
                    ('pagesize',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('direction',): {

                        "IN": "in",
                        "OUT": "out"
                    },
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'address':
                        (str,),
                    'direction':
                        (str,),
                    'include_labels':
                        (bool,),
                    'page':
                        (str,),
                    'pagesize':
                        (int,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'address': 'address',
                    'direction': 'direction',
                    'include_labels': 'include_labels',
                    'page': 'page',
                    'pagesize': 'pagesize',
                },
                'location_map': {
                    'currency': 'path',
                    'address': 'path',
                    'direction': 'query',
                    'include_labels': 'query',
                    'page': 'query',
                    'pagesize': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_address_neighbors
        )

        def __list_address_txs(
            self,
            currency,
            address,
            **kwargs
        ):
            """Get all transactions an address has been involved in  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_address_txs(currency, address, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                address (str): The cryptocurrency address

            Keyword Args:
                page (str): Resumption token for retrieving the next page. [optional]
                pagesize (int): Number of items returned in a single page. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AddressTxs
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['currency'] = \
                currency
            kwargs['address'] = \
                address
            return self.call_with_http_info(**kwargs)

        self.list_address_txs = _Endpoint(
            settings={
                'response_type': (AddressTxs,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/addresses/{address}/txs',
                'operation_id': 'list_address_txs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'address',
                    'page',
                    'pagesize',
                ],
                'required': [
                    'currency',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pagesize',
                ]
            },
            root_map={
                'validations': {
                    ('pagesize',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'address':
                        (str,),
                    'page':
                        (str,),
                    'pagesize':
                        (int,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'address': 'address',
                    'page': 'page',
                    'pagesize': 'pagesize',
                },
                'location_map': {
                    'currency': 'path',
                    'address': 'path',
                    'page': 'query',
                    'pagesize': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_address_txs
        )

        def __list_tags_by_address(
            self,
            currency,
            address,
            **kwargs
        ):
            """Get attribution tags for a given address  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_tags_by_address(currency, address, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                address (str): The cryptocurrency address

            Keyword Args:
                page (str): Resumption token for retrieving the next page. [optional]
                pagesize (int): Number of items returned in a single page. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AddressTags
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['currency'] = \
                currency
            kwargs['address'] = \
                address
            return self.call_with_http_info(**kwargs)

        self.list_tags_by_address = _Endpoint(
            settings={
                'response_type': (AddressTags,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/addresses/{address}/tags',
                'operation_id': 'list_tags_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'address',
                    'page',
                    'pagesize',
                ],
                'required': [
                    'currency',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pagesize',
                ]
            },
            root_map={
                'validations': {
                    ('pagesize',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'address':
                        (str,),
                    'page':
                        (str,),
                    'pagesize':
                        (int,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'address': 'address',
                    'page': 'page',
                    'pagesize': 'pagesize',
                },
                'location_map': {
                    'currency': 'path',
                    'address': 'path',
                    'page': 'query',
                    'pagesize': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_tags_by_address
        )
