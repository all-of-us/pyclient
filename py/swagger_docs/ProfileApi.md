# swagger_client.ProfileApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_ethics_training**](ProfileApi.md#complete_ethics_training) | **POST** /v1/account/complete-ethics-training | 
[**create_account**](ProfileApi.md#create_account) | **POST** /v1/google-account | 
[**get_id_verifications_for_review**](ProfileApi.md#get_id_verifications_for_review) | **GET** /v1/admin/users/id-verification/list | 
[**get_me**](ProfileApi.md#get_me) | **GET** /v1/me | 
[**invitation_key_verification**](ProfileApi.md#invitation_key_verification) | **POST** /v1/invitation-key-verification | 
[**is_username_taken**](ProfileApi.md#is_username_taken) | **GET** /v1/is-username-taken | 
[**request_invitation_key**](ProfileApi.md#request_invitation_key) | **POST** /v1/request-invitation-key | 
[**review_id_verification**](ProfileApi.md#review_id_verification) | **POST** /v1/admin/users/id-verification/{userId}/review | 
[**submit_demographics_survey**](ProfileApi.md#submit_demographics_survey) | **POST** /v1/account/submit-demographic-survey | 
[**submit_id_verification**](ProfileApi.md#submit_id_verification) | **POST** /v1/id-verification | 
[**submit_terms_of_service**](ProfileApi.md#submit_terms_of_service) | **POST** /v1/account/accept-terms-of-service | 
[**update_profile**](ProfileApi.md#update_profile) | **POST** /v1/update-profile | 


# **complete_ethics_training**
> Profile complete_ethics_training()



Completes ethics training.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try: 
    api_response = api_instance.complete_ethics_training()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->complete_ethics_training: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> Profile create_account(create_account_request=create_account_request)



Creates an account in the researchallofus.org domain.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProfileApi()
create_account_request = swagger_client.CreateAccountRequest() # CreateAccountRequest |  (optional)

try: 
    api_response = api_instance.create_account(create_account_request=create_account_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_request** | [**CreateAccountRequest**](CreateAccountRequest.md)|  | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_verifications_for_review**
> IdVerificationListResponse get_id_verifications_for_review()



Returns a list of profiles for users to be reviewed. Requires REVIEW_ID_VERIFICATION authority. 

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try: 
    api_response = api_instance.get_id_verifications_for_review()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->get_id_verifications_for_review: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdVerificationListResponse**](IdVerificationListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> Profile get_me()



Returns the user's profile information

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try: 
    api_response = api_instance.get_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->get_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_key_verification**
> invitation_key_verification(invitation_verification_request=invitation_verification_request)



Verifies invitation key.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProfileApi()
invitation_verification_request = swagger_client.InvitationVerificationRequest() # InvitationVerificationRequest |  (optional)

try: 
    api_instance.invitation_key_verification(invitation_verification_request=invitation_verification_request)
except ApiException as e:
    print("Exception when calling ProfileApi->invitation_key_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_verification_request** | [**InvitationVerificationRequest**](InvitationVerificationRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_username_taken**
> UsernameTakenResponse is_username_taken(username)



Checks to see if the given username is not available.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProfileApi()
username = 'username_example' # str | 

try: 
    api_response = api_instance.is_username_taken(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->is_username_taken: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UsernameTakenResponse**](UsernameTakenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_invitation_key**
> request_invitation_key(contact_email=contact_email)



Sends support a request for the invitation key.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProfileApi()
contact_email = 'contact_email_example' # str |  (optional)

try: 
    api_instance.request_invitation_key(contact_email=contact_email)
except ApiException as e:
    print("Exception when calling ProfileApi->request_invitation_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_id_verification**
> IdVerificationListResponse review_id_verification(user_id, review=review)



Manually sets the ID verfication status for a user. Requires REVIEW_ID_VERIFICATION authority. 

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
review = swagger_client.IdVerificationReviewRequest() # IdVerificationReviewRequest |  (optional)

try: 
    api_response = api_instance.review_id_verification(user_id, review=review)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->review_id_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **review** | [**IdVerificationReviewRequest**](IdVerificationReviewRequest.md)|  | [optional] 

### Return type

[**IdVerificationListResponse**](IdVerificationListResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_demographics_survey**
> Profile submit_demographics_survey()



Submits demographic survey responses.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try: 
    api_response = api_instance.submit_demographics_survey()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->submit_demographics_survey: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_id_verification**
> Profile submit_id_verification(id_verification_request=id_verification_request)



Accepts identity information for verification.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
id_verification_request = swagger_client.IdVerificationRequest() # IdVerificationRequest |  (optional)

try: 
    api_response = api_instance.submit_id_verification(id_verification_request=id_verification_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->submit_id_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_verification_request** | [**IdVerificationRequest**](IdVerificationRequest.md)|  | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_terms_of_service**
> Profile submit_terms_of_service()



Submits consent to the terms of service for researchers.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try: 
    api_response = api_instance.submit_terms_of_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->submit_terms_of_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> update_profile(updated_profile=updated_profile)



Updates a users profile

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
updated_profile = swagger_client.Profile() # Profile | the new profile to use (optional)

try: 
    api_instance.update_profile(updated_profile=updated_profile)
except ApiException as e:
    print("Exception when calling ProfileApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_profile** | [**Profile**](Profile.md)| the new profile to use | [optional] 

### Return type

void (empty response body)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

