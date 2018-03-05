# Profile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | researchallofus userId | [optional] 
**username** | **str** | researchallofus username | 
**contact_email** | **str** | email address that can be used to contact the user | [optional] 
**enabled_in_fire_cloud** | **bool** | true if the user is enabled in FireCloud, false if they are not | 
**free_tier_billing_project_name** | **str** | name of the AllOfUs free tier billing project created for this user | [optional] 
**free_tier_billing_project_status** | [**BillingProjectStatus**](BillingProjectStatus.md) | the initialization status of the free tier billing project, some workbench functionality may not work fully with this project until it is fully initialized  | [optional] 
**data_access_level** | [**DataAccessLevel**](DataAccessLevel.md) | what level of data access the user has | 
**given_name** | **str** | the user&#39;s given name (e.g. Alice) | [optional] 
**family_name** | **str** | the user&#39;s family  name (e.g. Jones) | [optional] 
**phone_number** | **str** | the user&#39;s phone number | [optional] 
**authorities** | [**list[Authority]**](Authority.md) | authorities granted to this user | [optional] 
**blockscore_id_verification_status** | [**BlockscoreIdVerificationStatus**](BlockscoreIdVerificationStatus.md) | Status of ID verification | [optional] 
**terms_of_service_completion_time** | **int** | Timestamp when the user consented to terms of service in milliseconds since the UNIX epoch. | [optional] 
**ethics_training_completion_time** | **int** | Timestamp when the user completed ethics training in milliseconds since the UNIX epoch. | [optional] 
**demographic_survey_completion_time** | **int** | Timestamp when the user completed a demographic survey in milliseconds since the UNIX epoch. | [optional] 
**disabled** | **bool** |  | [optional] 
**email_verification_status** | [**EmailVerificationStatus**](EmailVerificationStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


