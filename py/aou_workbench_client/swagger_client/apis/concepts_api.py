# coding: utf-8

"""
    AllOfUs Client API

    The API used by AllOfUs workbench clients (including both notebooks and our UI.)

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class ConceptsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_concepts(self, workspace_namespace, workspace_id, **kwargs):
        """
        Searches for concepts in concept table by name, and optionally filter on domain, vocabulary IDs, or standard concept status. Uses the CDR version affiliated with the workspace specified in the path. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_concepts(workspace_namespace, workspace_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str workspace_namespace: The Workspace namespace (required)
        :param str workspace_id: The Workspace ID (a.k.a. the workspace's Firecloud name) (required)
        :param SearchConceptsRequest request: concept search request
        :return: ConceptListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_concepts_with_http_info(workspace_namespace, workspace_id, **kwargs)
        else:
            (data) = self.search_concepts_with_http_info(workspace_namespace, workspace_id, **kwargs)
            return data

    def search_concepts_with_http_info(self, workspace_namespace, workspace_id, **kwargs):
        """
        Searches for concepts in concept table by name, and optionally filter on domain, vocabulary IDs, or standard concept status. Uses the CDR version affiliated with the workspace specified in the path. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_concepts_with_http_info(workspace_namespace, workspace_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str workspace_namespace: The Workspace namespace (required)
        :param str workspace_id: The Workspace ID (a.k.a. the workspace's Firecloud name) (required)
        :param SearchConceptsRequest request: concept search request
        :return: ConceptListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_namespace', 'workspace_id', 'request']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_concepts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_namespace' is set
        if ('workspace_namespace' not in params) or (params['workspace_namespace'] is None):
            raise ValueError("Missing the required parameter `workspace_namespace` when calling `search_concepts`")
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `search_concepts`")


        collection_formats = {}

        path_params = {}
        if 'workspace_namespace' in params:
            path_params['workspaceNamespace'] = params['workspace_namespace']
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['aou_oauth']

        return self.api_client.call_api('/v1/workspaces/{workspaceNamespace}/{workspaceId}/searchConcepts', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ConceptListResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
