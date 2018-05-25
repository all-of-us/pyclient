# swagger_client.ConceptsApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_concepts**](ConceptsApi.md#search_concepts) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/searchConcepts | 


# **search_concepts**
> ConceptListResponse search_concepts(workspace_namespace, workspace_id, request=request)



Searches for concepts in concept table by name, and optionally filter on domain, vocabulary IDs, or standard concept status. Uses the CDR version affiliated with the workspace specified in the path. 

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
api_instance = swagger_client.ConceptsApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
request = swagger_client.SearchConceptsRequest() # SearchConceptsRequest | concept search request (optional)

try: 
    api_response = api_instance.search_concepts(workspace_namespace, workspace_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->search_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **request** | [**SearchConceptsRequest**](SearchConceptsRequest.md)| concept search request | [optional] 

### Return type

[**ConceptListResponse**](ConceptListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

