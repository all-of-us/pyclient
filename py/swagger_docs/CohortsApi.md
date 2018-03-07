# swagger_client.CohortsApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**materialize_cohort**](CohortsApi.md#materialize_cohort) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/materializeCohort | 


# **materialize_cohort**
> MaterializeCohortResponse materialize_cohort(workspace_namespace, workspace_id, request=request)



Materializes a cohort for a given CDR version to specified output

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: aou_oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CohortsApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
request = swagger_client.MaterializeCohortRequest() # MaterializeCohortRequest | cohort materialization request (optional)

try: 
    api_response = api_instance.materialize_cohort(workspace_namespace, workspace_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortsApi->materialize_cohort: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **request** | [**MaterializeCohortRequest**](MaterializeCohortRequest.md)| cohort materialization request | [optional] 

### Return type

[**MaterializeCohortResponse**](MaterializeCohortResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

