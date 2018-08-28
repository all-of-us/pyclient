# Concept

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | **int** | ID of the concept | 
**concept_name** | **str** | Name of the concept | 
**domain_id** | **str** | Domain ID of the concept (e.g. Observation) | 
**vocabulary_id** | **str** | Vocabulary ID of the concept (e.g. SNOMED) | 
**concept_code** | **str** | Code for the concept in its vocabulary (e.g. G8107) | 
**concept_class_id** | **str** | Class of the concept (e.g. Ingredient) | 
**standard_concept** | **bool** | True if this is a standard concept, false otherwise | 
**count_value** | **int** | Count of participants matching this concept in the CDR | 
**prevalence** | **float** | Prevalence among participants in the CDR (a percentage of the total) | 
**concept_synonyms** | **list[str]** | concept synonym names | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


