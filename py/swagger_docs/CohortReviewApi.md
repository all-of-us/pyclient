# swagger_client.CohortReviewApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cohort_review**](CohortReviewApi.md#create_cohort_review) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId} | 
[**create_participant_cohort_annotation**](CohortReviewApi.md#create_participant_cohort_annotation) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants/{participantId}/annotations | 
[**delete_participant_cohort_annotation**](CohortReviewApi.md#delete_participant_cohort_annotation) | **DELETE** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants/{participantId}/annotations/{annotationId} | 
[**get_cohort_summary**](CohortReviewApi.md#get_cohort_summary) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/charts/{domain} | 
[**get_participant_cohort_annotation**](CohortReviewApi.md#get_participant_cohort_annotation) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants/{participantId}/annotations/{annotationId} | 
[**get_participant_cohort_annotations**](CohortReviewApi.md#get_participant_cohort_annotations) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants/{participantId}/annotations | 
[**get_participant_cohort_status**](CohortReviewApi.md#get_participant_cohort_status) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants/{participantId} | 
[**get_participant_cohort_statuses**](CohortReviewApi.md#get_participant_cohort_statuses) | **POST** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants | 
[**get_participant_demographics**](CohortReviewApi.md#get_participant_demographics) | **GET** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/demographics | 
[**update_participant_cohort_annotation**](CohortReviewApi.md#update_participant_cohort_annotation) | **PUT** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants/{participantId}/annotations/{annotationId} | 
[**update_participant_cohort_status**](CohortReviewApi.md#update_participant_cohort_status) | **PUT** /v1/workspaces/{workspaceNamespace}/{workspaceId}/review/{cohortId}/{cdrVersionId}/participants/{participantId} | 


# **create_cohort_review**
> CohortReview create_cohort_review(workspace_namespace, workspace_id, cohort_id, cdr_version_id, request)



This endpoint will create an cohort review which is a participant cohort sample specified by the review size parameter. 

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
request = swagger_client.CreateReviewRequest() # CreateReviewRequest | cohort review creation request body

try: 
    api_response = api_instance.create_cohort_review(workspace_namespace, workspace_id, cohort_id, cdr_version_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->create_cohort_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **request** | [**CreateReviewRequest**](CreateReviewRequest.md)| cohort review creation request body | 

### Return type

[**CohortReview**](CohortReview.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_participant_cohort_annotation**
> ParticipantCohortAnnotation create_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, request)



This endpoint will create a ParticipantCohortAnnotation.

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
participant_id = 789 # int | specifies which participant
request = swagger_client.ParticipantCohortAnnotation() # ParticipantCohortAnnotation | ParticipantCohortAnnotation creation request body

try: 
    api_response = api_instance.create_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->create_participant_cohort_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **participant_id** | **int**| specifies which participant | 
 **request** | [**ParticipantCohortAnnotation**](ParticipantCohortAnnotation.md)| ParticipantCohortAnnotation creation request body | 

### Return type

[**ParticipantCohortAnnotation**](ParticipantCohortAnnotation.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_participant_cohort_annotation**
> EmptyResponse delete_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, annotation_id)



Deletes the ParticipantCohortAnnotation with the specified ID

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
participant_id = 789 # int | specifies which participant
annotation_id = 789 # int | specifies which annotation

try: 
    api_response = api_instance.delete_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, annotation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->delete_participant_cohort_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **participant_id** | **int**| specifies which participant | 
 **annotation_id** | **int**| specifies which annotation | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cohort_summary**
> CohortSummaryListResponse get_cohort_summary(workspace_namespace, workspace_id, cohort_id, cdr_version_id, domain)



Returns a collection of CohortSummary for UI charting in cohort review.

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
domain = 'domain_example' # str | specifies which domain the CohortSummary should belong to.

try: 
    api_response = api_instance.get_cohort_summary(workspace_namespace, workspace_id, cohort_id, cdr_version_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->get_cohort_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **domain** | **str**| specifies which domain the CohortSummary should belong to. | 

### Return type

[**CohortSummaryListResponse**](CohortSummaryListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant_cohort_annotation**
> ParticipantCohortAnnotation get_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, annotation_id)



This endpoint will get a ParticipantCohortAnnotation.

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
participant_id = 789 # int | specifies which participant
annotation_id = 789 # int | specifies which annotation

try: 
    api_response = api_instance.get_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, annotation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->get_participant_cohort_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **participant_id** | **int**| specifies which participant | 
 **annotation_id** | **int**| specifies which annotation | 

### Return type

[**ParticipantCohortAnnotation**](ParticipantCohortAnnotation.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant_cohort_annotations**
> ParticipantCohortAnnotationListResponse get_participant_cohort_annotations(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id)



This endpoint will get a collection of ParticipantCohortAnnotations.

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
participant_id = 789 # int | specifies which participant

try: 
    api_response = api_instance.get_participant_cohort_annotations(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->get_participant_cohort_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **participant_id** | **int**| specifies which participant | 

### Return type

[**ParticipantCohortAnnotationListResponse**](ParticipantCohortAnnotationListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant_cohort_status**
> ParticipantCohortStatus get_participant_cohort_status(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id)



This endpoint will return a ParticipantCohortStatus

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
participant_id = 789 # int | specifies which participant

try: 
    api_response = api_instance.get_participant_cohort_status(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->get_participant_cohort_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **participant_id** | **int**| specifies which participant | 

### Return type

[**ParticipantCohortStatus**](ParticipantCohortStatus.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant_cohort_statuses**
> CohortReview get_participant_cohort_statuses(workspace_namespace, workspace_id, cohort_id, cdr_version_id, request)



Returns a collection of participants for the specified cohortId and cdrVersionId. This endpoint does pagination based on page, limit, order and column. 

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
request = swagger_client.ParticipantCohortStatusesRequest() # ParticipantCohortStatusesRequest | request body for getting list of ParticipantCohortStatuses.

try: 
    api_response = api_instance.get_participant_cohort_statuses(workspace_namespace, workspace_id, cohort_id, cdr_version_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->get_participant_cohort_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **request** | [**ParticipantCohortStatusesRequest**](ParticipantCohortStatusesRequest.md)| request body for getting list of ParticipantCohortStatuses. | 

### Return type

[**CohortReview**](CohortReview.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant_demographics**
> ParticipantDemographics get_participant_demographics(workspace_namespace, workspace_id, cohort_id, cdr_version_id)



Will return a list all values for gender, race and ethnicity.

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version

try: 
    api_response = api_instance.get_participant_demographics(workspace_namespace, workspace_id, cohort_id, cdr_version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->get_participant_demographics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 

### Return type

[**ParticipantDemographics**](ParticipantDemographics.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_participant_cohort_annotation**
> ParticipantCohortAnnotation update_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, annotation_id, request)



This endpoint will modify a ParticipantCohortAnnotation.

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
participant_id = 789 # int | specifies which participant
annotation_id = 789 # int | specifies which annotation
request = swagger_client.ModifyParticipantCohortAnnotationRequest() # ModifyParticipantCohortAnnotationRequest | ParticipantCohortAnnotation modification request body

try: 
    api_response = api_instance.update_participant_cohort_annotation(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, annotation_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->update_participant_cohort_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **participant_id** | **int**| specifies which participant | 
 **annotation_id** | **int**| specifies which annotation | 
 **request** | [**ModifyParticipantCohortAnnotationRequest**](ModifyParticipantCohortAnnotationRequest.md)| ParticipantCohortAnnotation modification request body | 

### Return type

[**ParticipantCohortAnnotation**](ParticipantCohortAnnotation.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_participant_cohort_status**
> ParticipantCohortStatus update_participant_cohort_status(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, cohort_status_request=cohort_status_request)



Modifies the ParticipantCohortStatus status

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
api_instance = swagger_client.CohortReviewApi(swagger_client.ApiClient(configuration))
workspace_namespace = 'workspace_namespace_example' # str | The Workspace namespace
workspace_id = 'workspace_id_example' # str | The Workspace ID (a.k.a. the workspace's Firecloud name)
cohort_id = 789 # int | Cohort ID
cdr_version_id = 789 # int | specifies which cdr version
participant_id = 789 # int | specifies which participant
cohort_status_request = swagger_client.ModifyCohortStatusRequest() # ModifyCohortStatusRequest | Contains the new review status (optional)

try: 
    api_response = api_instance.update_participant_cohort_status(workspace_namespace, workspace_id, cohort_id, cdr_version_id, participant_id, cohort_status_request=cohort_status_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CohortReviewApi->update_participant_cohort_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_namespace** | **str**| The Workspace namespace | 
 **workspace_id** | **str**| The Workspace ID (a.k.a. the workspace&#39;s Firecloud name) | 
 **cohort_id** | **int**| Cohort ID | 
 **cdr_version_id** | **int**| specifies which cdr version | 
 **participant_id** | **int**| specifies which participant | 
 **cohort_status_request** | [**ModifyCohortStatusRequest**](ModifyCohortStatusRequest.md)| Contains the new review status | [optional] 

### Return type

[**ParticipantCohortStatus**](ParticipantCohortStatus.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

