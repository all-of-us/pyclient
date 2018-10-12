# CohortAnnotationsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **list[str]** | An array of columns for the annotations being returned.  | [optional] 
**results** | **list[object]** | An array of JSON dictionaries, with each dictionary representing the requested annotations and/or review status for a single person. (In Java, this is represented as Map&lt;String, Object&gt;[]. In Python clients, this is a list[object] where each object is a dictionary. In Typescript clients, this is an Array&lt;any&gt; where each object is a dictionary.) Keys in the dictionaries will be \&quot;person_id\&quot;, \&quot;review_status\&quot;, or the name of an annotation.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


