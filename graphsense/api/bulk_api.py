"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5.2
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


class BulkApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __bulk_csv(
            self,
            currency,
            operation,
            num_pages,
            body,
            **kwargs
        ):
            """Get data as CSV in bulk  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.bulk_csv(currency, operation, num_pages, body, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                operation (str): The operation to execute in bulk
                num_pages (int): Number of pages to retrieve for operations with list response
                body ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Map of the operation's parameter names to (arrays of) values

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
                str
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
            kwargs['operation'] = \
                operation
            kwargs['num_pages'] = \
                num_pages
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.bulk_csv = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/bulk.csv/{operation}',
                'operation_id': 'bulk_csv',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'operation',
                    'num_pages',
                    'body',
                ],
                'required': [
                    'currency',
                    'operation',
                    'num_pages',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                    'operation',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('operation',): {

                        "GET_BLOCK": "get_block",
                        "LIST_BLOCK_TXS": "list_block_txs",
                        "GET_ADDRESS": "get_address",
                        "LIST_ADDRESS_TXS": "list_address_txs",
                        "LIST_TAGS_BY_ADDRESS": "list_tags_by_address",
                        "LIST_ADDRESS_NEIGHBORS": "list_address_neighbors",
                        "GET_ADDRESS_ENTITY": "get_address_entity",
                        "LIST_ADDRESS_LINKS": "list_address_links",
                        "GET_ENTITY": "get_entity",
                        "LIST_TAGS_BY_ENTITY": "list_tags_by_entity",
                        "LIST_ENTITY_NEIGHBORS": "list_entity_neighbors",
                        "LIST_ENTITY_TXS": "list_entity_txs",
                        "LIST_ENTITY_LINKS": "list_entity_links",
                        "LIST_ENTITY_ADDRESSES": "list_entity_addresses",
                        "GET_TX": "get_tx",
                        "GET_TX_IO": "get_tx_io",
                        "GET_EXCHANGE_RATES": "get_exchange_rates"
                    },
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'operation':
                        (str,),
                    'num_pages':
                        (int,),
                    'body':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'operation': 'operation',
                    'num_pages': 'num_pages',
                },
                'location_map': {
                    'currency': 'path',
                    'operation': 'path',
                    'num_pages': 'query',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/csv'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__bulk_csv
        )

        def __bulk_json(
            self,
            currency,
            operation,
            num_pages,
            body,
            **kwargs
        ):
            """Get data as JSON in bulk  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.bulk_json(currency, operation, num_pages, body, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency code (e.g., btc)
                operation (str): The operation to execute in bulk
                num_pages (int): Number of pages to retrieve for operations with list response
                body ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Map of the operation's parameter names to (arrays of) values

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
                [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
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
            kwargs['operation'] = \
                operation
            kwargs['num_pages'] = \
                num_pages
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.bulk_json = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/{currency}/bulk.json/{operation}',
                'operation_id': 'bulk_json',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'currency',
                    'operation',
                    'num_pages',
                    'body',
                ],
                'required': [
                    'currency',
                    'operation',
                    'num_pages',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                    'operation',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('operation',): {

                        "GET_BLOCK": "get_block",
                        "LIST_BLOCK_TXS": "list_block_txs",
                        "GET_ADDRESS": "get_address",
                        "LIST_ADDRESS_TXS": "list_address_txs",
                        "LIST_TAGS_BY_ADDRESS": "list_tags_by_address",
                        "LIST_ADDRESS_NEIGHBORS": "list_address_neighbors",
                        "GET_ADDRESS_ENTITY": "get_address_entity",
                        "LIST_ADDRESS_LINKS": "list_address_links",
                        "GET_ENTITY": "get_entity",
                        "LIST_TAGS_BY_ENTITY": "list_tags_by_entity",
                        "LIST_ENTITY_NEIGHBORS": "list_entity_neighbors",
                        "LIST_ENTITY_TXS": "list_entity_txs",
                        "LIST_ENTITY_LINKS": "list_entity_links",
                        "LIST_ENTITY_ADDRESSES": "list_entity_addresses",
                        "GET_TX": "get_tx",
                        "GET_TX_IO": "get_tx_io",
                        "GET_EXCHANGE_RATES": "get_exchange_rates"
                    },
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'operation':
                        (str,),
                    'num_pages':
                        (int,),
                    'body':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                },
                'attribute_map': {
                    'currency': 'currency',
                    'operation': 'operation',
                    'num_pages': 'num_pages',
                },
                'location_map': {
                    'currency': 'path',
                    'operation': 'path',
                    'num_pages': 'query',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__bulk_json
        )
