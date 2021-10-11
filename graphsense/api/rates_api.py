"""
    GraphSense API

    GraphSense API  # noqa: E501

    The version of the OpenAPI document: 0.5
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
from graphsense.model.rates import Rates


class RatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_exchange_rates(
            self,
            currency,
            height,
            **kwargs
        ):
            """Returns exchange rate for a given height  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_exchange_rates(currency, height, async_req=True)
            >>> result = thread.get()

            Args:
                currency (str): The cryptocurrency (e.g., btc)
                height (int): The block height

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
                Rates
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

        self.get_exchange_rates = _Endpoint(
            settings={
                'response_type': (Rates,),
                'auth': [],
                'endpoint_path': '/{currency}/rates/{height}',
                'operation_id': 'get_exchange_rates',
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
                    'height',
                ]
            },
            root_map={
                'validations': {
                    ('height',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'currency':
                        (str,),
                    'height':
                        (int,),
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
            callable=__get_exchange_rates
        )
