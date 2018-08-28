# SearchConceptsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | A query string that can be used to match a subset of the name (case-insensitively), the entire code value (case-insensitively), or the concept ID.  | 
**standard_concept_filter** | [**StandardConceptFilter**](StandardConceptFilter.md) | STANDARD_CONCEPTS if only standard concepts should be returned, NON_STANDARD_CONCEPTS if only non-standard concepts should be returned; defaults to ALL_CONCEPTS, meaning both standard and non-standard concepts will be returned.  | [optional] 
**vocabulary_ids** | **list[str]** | The vocabulary ID for the concepts returned (e.g. SNOMED, RxNorm) | [optional] 
**domain** | [**Domain**](Domain.md) | The domain for the concepts returned (e.g. OBSERVATION, DRUG). Note that this may map to multiple domain ID values in OMOP.  | [optional] 
**max_results** | **int** | The maximum number of results returned. Defaults to 20. | [optional] 
**min_count** | **int** | Determines the concepts to be fetched. Gets all the concepts if 0 or gets concepts with counts if 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


