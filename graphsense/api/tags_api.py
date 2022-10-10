"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 22.10
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
from graphsense.model.address_tags import AddressTags
from graphsense.model.concept import Concept
from graphsense.model.taxonomy import Taxonomy


class TagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __list_address_tags(
            self,
            label,
            **kwargs
        ):
            """Returns address tags associated with a given label  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_address_tags(label, async_req=True)
            >>> result = thread.get()

            Args:
                label (str): The label of an entity

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
            kwargs['label'] = \
                label
            return self.call_with_http_info(**kwargs)

        self.list_address_tags = _Endpoint(
            settings={
                'response_type': (AddressTags,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/tags',
                'operation_id': 'list_address_tags',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'label',
                    'page',
                    'pagesize',
                ],
                'required': [
                    'label',
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
                    'label':
                        (str,),
                    'page':
                        (str,),
                    'pagesize':
                        (int,),
                },
                'attribute_map': {
                    'label': 'label',
                    'page': 'page',
                    'pagesize': 'pagesize',
                },
                'location_map': {
                    'label': 'query',
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
            callable=__list_address_tags
        )

        def __list_concepts(
            self,
            taxonomy,
            **kwargs
        ):
            """Returns the supported concepts of a taxonomy  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_concepts(taxonomy, async_req=True)
            >>> result = thread.get()

            Args:
                taxonomy (str): The taxonomy

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
                [Concept]
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
            kwargs['taxonomy'] = \
                taxonomy
            return self.call_with_http_info(**kwargs)

        self.list_concepts = _Endpoint(
            settings={
                'response_type': ([Concept],),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/tags/taxonomies/{taxonomy}/concepts',
                'operation_id': 'list_concepts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'taxonomy',
                ],
                'required': [
                    'taxonomy',
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
                    'taxonomy':
                        (str,),
                },
                'attribute_map': {
                    'taxonomy': 'taxonomy',
                },
                'location_map': {
                    'taxonomy': 'path',
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
            callable=__list_concepts
        )

        def __list_taxonomies(
            self,
            **kwargs
        ):
            """Returns the supported taxonomies  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_taxonomies(async_req=True)
            >>> result = thread.get()


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
                [Taxonomy]
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
            return self.call_with_http_info(**kwargs)

        self.list_taxonomies = _Endpoint(
            settings={
                'response_type': ([Taxonomy],),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/tags/taxonomies',
                'operation_id': 'list_taxonomies',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
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
                },
                'attribute_map': {
                },
                'location_map': {
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
            callable=__list_taxonomies
        )
