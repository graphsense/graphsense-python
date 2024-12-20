"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 1.8.0
    Contact: contact@ikna.io
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
from graphsense.model.block import Block
from graphsense.model.block_at_date import BlockAtDate
from graphsense.model.height import Height
from graphsense.model.tx import Tx


class BlocksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_block(
            self,
            currency,
            height,
            **kwargs
        ):
            """Get a block by its height  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_block(currency, height, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                height (Height): The block height

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
                Block
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
            kwargs['height'] = \
                height
            return self.call_with_http_info(**kwargs)

        self.get_block = _Endpoint(
            settings={
                'response_type': (Block,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/blocks/{height}',
                'operation_id': 'get_block',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'height',
                ],
                'required': [
                    'currency',
                    'height',
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
                    'height':
                        (Height,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'height': 'height',
                },
                'location_map': {
                    'currency': 'path',
                    'height': 'path',
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
            callable=__get_block
        )

        def __get_block_by_date(
            self,
            currency,
            date,
            **kwargs
        ):
            """Get the closest blocks given a timestamp  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_block_by_date(currency, date, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                date (datetime): The time of the block

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
                BlockAtDate
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
            kwargs['date'] = \
                date
            return self.call_with_http_info(**kwargs)

        self.get_block_by_date = _Endpoint(
            settings={
                'response_type': (BlockAtDate,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/block_by_date/{date}',
                'operation_id': 'get_block_by_date',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'date',
                ],
                'required': [
                    'currency',
                    'date',
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
                    'date':
                        (datetime,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'date': 'date',
                },
                'location_map': {
                    'currency': 'path',
                    'date': 'path',
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
            callable=__get_block_by_date
        )

        def __list_block_txs(
            self,
            currency,
            height,
            **kwargs
        ):
            """Get block transactions  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_block_txs(currency, height, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                height (Height): The block height

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
                [Tx]
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
            kwargs['height'] = \
                height
            return self.call_with_http_info(**kwargs)

        self.list_block_txs = _Endpoint(
            settings={
                'response_type': ([Tx],),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/blocks/{height}/txs',
                'operation_id': 'list_block_txs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'height',
                ],
                'required': [
                    'currency',
                    'height',
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
                    'height':
                        (Height,),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'height': 'height',
                },
                'location_map': {
                    'currency': 'path',
                    'height': 'path',
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
            callable=__list_block_txs
        )
