# swagger_client.AuthDomainApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_auth_domain**](AuthDomainApi.md#add_user_to_auth_domain) | **POST** /v1/auth-domain/{groupName}/users | add a user to an auth domain if you have manage groups permission
[**create_auth_domain**](AuthDomainApi.md#create_auth_domain) | **POST** /v1/auth-domain/{groupName} | 
[**remove_user_from_auth_domain**](AuthDomainApi.md#remove_user_from_auth_domain) | **DELETE** /v1/auth-domain/{groupName}/users | remove a user from an auth domain if you have manage groups permission


# **add_user_to_auth_domain**
> add_user_to_auth_domain(group_name, request=request)

add a user to an auth domain if you have manage groups permission

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
api_instance = swagger_client.AuthDomainApi(swagger_client.ApiClient(configuration))
group_name = 'group_name_example' # str | 
request = swagger_client.AuthDomainRequest() # AuthDomainRequest | request carrying user email to add (optional)

try: 
    # add a user to an auth domain if you have manage groups permission
    api_instance.add_user_to_auth_domain(group_name, request=request)
except ApiException as e:
    print("Exception when calling AuthDomainApi->add_user_to_auth_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 
 **request** | [**AuthDomainRequest**](AuthDomainRequest.md)| request carrying user email to add | [optional] 

### Return type

void (empty response body)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_domain**
> EmptyResponse create_auth_domain(group_name)



This endpoint will create the registered auth domain.

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
api_instance = swagger_client.AuthDomainApi(swagger_client.ApiClient(configuration))
group_name = 'group_name_example' # str | groupName

try: 
    api_response = api_instance.create_auth_domain(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthDomainApi->create_auth_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| groupName | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_auth_domain**
> remove_user_from_auth_domain(group_name, request=request)

remove a user from an auth domain if you have manage groups permission

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
api_instance = swagger_client.AuthDomainApi(swagger_client.ApiClient(configuration))
group_name = 'group_name_example' # str | 
request = swagger_client.AuthDomainRequest() # AuthDomainRequest | request carrying user email to add (optional)

try: 
    # remove a user from an auth domain if you have manage groups permission
    api_instance.remove_user_from_auth_domain(group_name, request=request)
except ApiException as e:
    print("Exception when calling AuthDomainApi->remove_user_from_auth_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 
 **request** | [**AuthDomainRequest**](AuthDomainRequest.md)| request carrying user email to add | [optional] 

### Return type

void (empty response body)

### Authorization

[aou_oauth](../README.md#aou_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

