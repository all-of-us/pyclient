# CohortAnnotationsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohort_name** | **str** | The name of a cohort that annotations should be retrieved for.  | 
**status_filter** | [**list[CohortStatus]**](CohortStatus.md) | An array of status values; participants with these statuses will have their annotations retrieved. Defaults to [NOT_REVIEWED, INCLUDED, NEEDS_FURTHER_REVIEW] -- everything but EXCLUDED.  | [optional] 
**cdr_version_name** | **str** | The name of a CDR version to use when retrieving annotations; if none is specified, the CDR version currently associated with the workspace will be used  | [optional] 
**annotation_query** | [**AnnotationQuery**](AnnotationQuery.md) | Specification defining what annotations to retrieve.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


