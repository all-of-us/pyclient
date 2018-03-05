# swagger_client.CohortAnnotationDefinitionApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cohort_annotation_definition**](CohortAnnotationDefinitionApi.md#create_cohort_annotation_definition) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/cohorts/{cohortId}/annotationdefinitions | 
[**delete_cohort_annotation_definition**](CohortAnnotationDefinitionApi.md#delete_cohort_annotation_definition) | **DELETE** /v1/workspaces/{workspaceNamespace}/{workspaceId}/cohorts/{cohortId}/annotationdefinitions/{annotationDefinitionId} | 
[**get_cohort_annotation_definition**](CohortAnnotationDefinitionApi.md#get_cohort_annotation_definition) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/cohorts/{cohortId}/annotationdefinitions/{annotationDefinitionId} | 
[**get_cohort_annotation_definitions**](CohortAnnotationDefinitionApi.md#get_cohort_annotation_definitions) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/cohorts/{cohortId}/annotationdefinitions | 
[**update_cohort_annotation_definition**](CohortAnnotationDefinitionApi.md#update_cohort_annotation_definition) | **PUT** /v1/workspaces/{workspaceNamespace}/{workspaceId}/cohorts/{cohortId}/annotationdefinitions/{annotationDefinitionId} | 


# **create_cohort_annotation_definition**
> CohortAnnotationDefinition create_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, request)



This endpoint will create a CohortAnnotationDefinition.

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
api_instance = swagger_client.CohortAnnotationDefinitionApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
request = swagger_client.CohortAnnotationDefinition() # CohortAnnotationDefinition | CohortAnnotationDefinition creation request body

try: 
    api_response = api_instance.create_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortAnnotationDefinitionApi->create_cohort_annotation_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **request** | [**CohortAnnotationDefinition**](CohortAnnotationDefinition.md)| CohortAnnotationDefinition creation request body | 

### Return type

[**CohortAnnotationDefinition**](CohortAnnotationDefinition.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cohort_annotation_definition**
> EmptyResponse delete_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, annotation_definition_id)



Deletes the CohortAnnotationDefinition with the specified ID

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
api_instance = swagger_client.CohortAnnotationDefinitionApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
annotation_definition_id = 789 # int | specifies which CohortAnnotationDefinition.

try: 
    api_response = api_instance.delete_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, annotation_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortAnnotationDefinitionApi->delete_cohort_annotation_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **annotation_definition_id** | **int**| specifies which CohortAnnotationDefinition. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cohort_annotation_definition**
> CohortAnnotationDefinition get_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, annotation_definition_id)



Returns a CohortAnnotationDefinition.

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
api_instance = swagger_client.CohortAnnotationDefinitionApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
annotation_definition_id = 789 # int | specifies which CohortAnnotationDefinition.

try: 
    api_response = api_instance.get_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, annotation_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortAnnotationDefinitionApi->get_cohort_annotation_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **annotation_definition_id** | **int**| specifies which CohortAnnotationDefinition. | 

### Return type

[**CohortAnnotationDefinition**](CohortAnnotationDefinition.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cohort_annotation_definitions**
> CohortAnnotationDefinitionListResponse get_cohort_annotation_definitions(workspace_namespace, workspace_id, cohort_id)



Returns a collection of CohortAnnotationDefinition.

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
api_instance = swagger_client.CohortAnnotationDefinitionApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID

try: 
    api_response = api_instance.get_cohort_annotation_definitions(workspace_namespace, workspace_id, cohort_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortAnnotationDefinitionApi->get_cohort_annotation_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 

### Return type

[**CohortAnnotationDefinitionListResponse**](CohortAnnotationDefinitionListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cohort_annotation_definition**
> CohortAnnotationDefinition update_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, annotation_definition_id, modify_cohort_annotation_definition_request=modify_cohort_annotation_definition_request)



modify the CohortAnnotationDefinition.

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
api_instance = swagger_client.CohortAnnotationDefinitionApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
annotation_definition_id = 789 # int | specifies which CohortAnnotationDefinition.
modify_cohort_annotation_definition_request = swagger_client.ModifyCohortAnnotationDefinitionRequest() # ModifyCohortAnnotationDefinitionRequest | Contains the new CohortAnnotationDefinition (optional)

try: 
    api_response = api_instance.update_cohort_annotation_definition(workspace_namespace, workspace_id, cohort_id, annotation_definition_id, modify_cohort_annotation_definition_request=modify_cohort_annotation_definition_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortAnnotationDefinitionApi->update_cohort_annotation_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **annotation_definition_id** | **int**| specifies which CohortAnnotationDefinition. | 
 **modify_cohort_annotation_definition_request** | [**ModifyCohortAnnotationDefinitionRequest**](ModifyCohortAnnotationDefinitionRequest.md)| Contains the new CohortAnnotationDefinition | [optional] 

### Return type

[**CohortAnnotationDefinition**](CohortAnnotationDefinition.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

