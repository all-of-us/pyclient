# swagger_client.CohortsApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cohort_annotations**](CohortsApi.md#get_cohort_annotations) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/getCohortAnnotations | 
[**get_data_table_query**](CohortsApi.md#get_data_table_query) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/getDataTableQuery | 


# **get_cohort_annotations**
> CohortAnnotationsResponse get_cohort_annotations(workspace_namespace, workspace_id, request=request)



Retrieves annotations for a cohort in the workspace 

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
request = swagger_client.CohortAnnotationsRequest() # CohortAnnotationsRequest | a request indicating what annotations to retrieve (optional)

try: 
    api_response = api_instance.get_cohort_annotations(workspace_namespace, workspace_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortsApi->get_cohort_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **request** | [**CohortAnnotationsRequest**](CohortAnnotationsRequest.md)| a request indicating what annotations to retrieve | [optional] 

### Return type

[**CohortAnnotationsResponse**](CohortAnnotationsResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_table_query**
> CdrQuery get_data_table_query(workspace_namespace, workspace_id, request=request)



Translates a data table specification into a SQL query to run against the CDR. 

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
request = swagger_client.DataTableSpecification() # DataTableSpecification | a query specification for a data table (optional)

try: 
    api_response = api_instance.get_data_table_query(workspace_namespace, workspace_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortsApi->get_data_table_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **request** | [**DataTableSpecification**](DataTableSpecification.md)| a query specification for a data table | [optional] 

### Return type

[**CdrQuery**](CdrQuery.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

