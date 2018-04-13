# AnnotationQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **list[str]** | An array of names of annotations to retrieve about participants, or \&quot;review_status\&quot; for the cohort review status of the participant or \&quot;person_id\&quot; for the ID of the participant. Defaults to \&quot;person_id\&quot;, \&quot;review_status\&quot;, and the names of all defined annotations in the cohort review. This is only valid in combination with the use of cohortName above. Only data for participants in the cohort review will be returned; if no cohort review has been created, no results will be returned.  | [optional] 
**order_by** | **list[str]** | An array of names of annotations, or \&quot;review status\&quot; or \&quot;person_id\&quot;, each one optionally enclosed in \&quot;DESCENDING()\&quot; for descending sort order. Specifies the order that results should be returned. Defaults to \&quot;person_id\&quot; (in ascending order). Annotations referenced in orderBy must also be present in columns.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


