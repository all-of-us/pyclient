# swagger_client.AuditApi

All URIs are relative to *https://api.pmi-ops.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_big_query**](AuditApi.md#audit_big_query) | **GET** /v1/cron/auditBigQuery | 


# **audit_big_query**
> AuditBigQueryResponse audit_big_query()



Endpoint meant to be called offline to trigger BigQuery auditing; may be slow to execute. Only executable via App Engine cronjob. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuditApi()

try: 
    api_response = api_instance.audit_big_query()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->audit_big_query: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditBigQueryResponse**](AuditBigQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

