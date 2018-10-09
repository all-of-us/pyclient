# DataTableSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohort_name** | **str** | The name of a cohort that data should be retrieved for. This and cohortSpec should not be used at the same time. If neither cohortName nor cohortSpec are specified, data will be extracted for everyone in the CDR.  | [optional] 
**cohort_spec** | **str** | JSON representation of a cohort to be evaluated (using the same format used for saved cohorts). This and cohortName should not be used at the same time. If neither cohortName nor cohortSpec are specified, data will be extracted for everyone in the CDR.  | [optional] 
**status_filter** | [**list[CohortStatus]**](CohortStatus.md) | An array of status values; participants with these statuses will be included. Defaults to [NOT_REVIEWED, INCLUDED, NEEDS_FURTHER_REVIEW] -- everything but EXCLUDED. Only valid for use with cohortName (cohorts saved in the database.)  | [optional] 
**cdr_version_name** | **str** | The name of a CDR version to use when evaluating the cohort; if none is specified, the CDR version currently associated with the workspace will be used  | [optional] 
**table_query** | [**TableQuery**](TableQuery.md) | A query specifying how to pull data out of a single table. If tableQuery is not specified, just Person.person_id will be extracted.  | [optional] 
**max_results** | **int** | The maximum number of results returned in the data table. Defaults to no limit (all matching results are returned.)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


