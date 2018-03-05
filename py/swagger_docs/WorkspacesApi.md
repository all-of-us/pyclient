# swagger_client.WorkspacesApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_workspace**](WorkspacesApi.md#clone_workspace) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/clone | 
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /v1/workspaces | 
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /v1/workspaces/{workspaceNamespace}/{workspaceId} | 
[**get_note_book_list**](WorkspacesApi.md#get_note_book_list) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/notebook-list | Get details of Python files from google Bucket directory notebook
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId} | 
[**get_workspaces**](WorkspacesApi.md#get_workspaces) | **GET** /v1/workspaces | 
[**get_workspaces_for_review**](WorkspacesApi.md#get_workspaces_for_review) | **GET** /v1/admin/workspaces/review | 
[**localize_all_files**](WorkspacesApi.md#localize_all_files) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/localize-all-files | Get file details from google bucket and then localize to notebook server
[**review_workspace**](WorkspacesApi.md#review_workspace) | **POST** /v1/admin/workspaces/{workspaceNamespace}/{workspaceId}/review | 
[**share_workspace**](WorkspacesApi.md#share_workspace) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/share | 
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PATCH** /v1/workspaces/{workspaceNamespace}/{workspaceId} | 


# **clone_workspace**
> CloneWorkspaceResponse clone_workspace(workspace_namespace, workspace_id, body=body)



Clone an existing workspace, with given modifications to workspace metadata. Caller will own the newly cloned workspace, and must have read access to the source workspace. In addition to workspace metadata, the following will also be cloned:   - the associated Firecloud workspace   - cohorts, along with reviews and annotations   - notebooks located in the default notebook directory for this workspace 

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
body = swagger_client.CloneWorkspaceRequest() # CloneWorkspaceRequest |  (optional)

try: 
    api_response = api_instance.clone_workspace(workspace_namespace, workspace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->clone_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **body** | [**CloneWorkspaceRequest**](CloneWorkspaceRequest.md)|  | [optional] 

### Return type

[**CloneWorkspaceResponse**](CloneWorkspaceResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> Workspace create_workspace(workspace=workspace)



Creates a workspace

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace = swagger_client.Workspace() # Workspace | workspace definition (optional)

try: 
    api_response = api_instance.create_workspace(workspace=workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | [**Workspace**](Workspace.md)| workspace definition | [optional] 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> EmptyResponse delete_workspace(workspace_namespace, workspace_id)



Deletes the workspace definition with the specified ID and namespace

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)

try: 
    api_response = api_instance.delete_workspace(workspace_namespace, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_book_list**
> list[FileDetail] get_note_book_list(workspace_namespace, workspace_id)

Get details of Python files from google Bucket directory notebook

Returns list of name and path of python files from google bucket, directory notebook.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | workspaceNamespace
workspace_id = 'workspace_id_example' # str | workspaceId

try: 
    # Get details of Python files from google Bucket directory notebook
    api_response = api_instance.get_note_book_list(workspace_namespace, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_note_book_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| workspaceNamespace | 
 **workspace_id** | **str**| workspaceId | 

### Return type

[**list[FileDetail]**](FileDetail.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> WorkspaceResponse get_workspace(workspace_namespace, workspace_id)



Returns the workspace definition with the specified ID and namespace

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)

try: 
    api_response = api_instance.get_workspace(workspace_namespace, workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**
> WorkspaceResponseListResponse get_workspaces()



Returns all workspaces that a user has access to

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))

try: 
    api_response = api_instance.get_workspaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkspaceResponseListResponse**](WorkspaceResponseListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces_for_review**
> WorkspaceListResponse get_workspaces_for_review()



Returns workspaces that need research purpose review. Requires REVIEW_RESEARCH_PURPOSE authority. 

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))

try: 
    api_response = api_instance.get_workspaces_for_review()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces_for_review: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkspaceListResponse**](WorkspaceListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **localize_all_files**
> localize_all_files(workspace_namespace, workspace_id)

Get file details from google bucket and then localize to notebook server

Get files details from bucket folders config and notebooks and then localize to notebook server

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | workspaceNamespace
workspace_id = 'workspace_id_example' # str | workspaceId

try: 
    # Get file details from google bucket and then localize to notebook server
    api_instance.localize_all_files(workspace_namespace, workspace_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->localize_all_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| workspaceNamespace | 
 **workspace_id** | **str**| workspaceId | 

### Return type

void (empty response body)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_workspace**
> EmptyResponse review_workspace(workspace_namespace, workspace_id, review=review)



Sets a research purpose review result.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
review = swagger_client.ResearchPurposeReviewRequest() # ResearchPurposeReviewRequest | result of the research purpose review (optional)

try: 
    api_response = api_instance.review_workspace(workspace_namespace, workspace_id, review=review)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->review_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **review** | [**ResearchPurposeReviewRequest**](ResearchPurposeReviewRequest.md)| result of the research purpose review | [optional] 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_workspace**
> ShareWorkspaceResponse share_workspace(workspace_namespace, workspace_id, body=body)



Shares a workspace with users

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
body = swagger_client.ShareWorkspaceRequest() # ShareWorkspaceRequest | users to share the workspace with (optional)

try: 
    api_response = api_instance.share_workspace(workspace_namespace, workspace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->share_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **body** | [**ShareWorkspaceRequest**](ShareWorkspaceRequest.md)| users to share the workspace with | [optional] 

### Return type

[**ShareWorkspaceResponse**](ShareWorkspaceResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> Workspace update_workspace(workspace_namespace, workspace_id, workspace=workspace)



Modifies the workspace definition with the specified ID and namespace; fields that are omitted will not be modified 

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
workspace = swagger_client.UpdateWorkspaceRequest() # UpdateWorkspaceRequest | workspace definition (optional)

try: 
    api_response = api_instance.update_workspace(workspace_namespace, workspace_id, workspace=workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **workspace** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)| workspace definition | [optional] 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

