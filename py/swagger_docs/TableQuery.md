# TableQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | The name of a table containing a person_id column to retrieve data from (e.g. person, observation); should be in the OMOP CDM 5.2 schema.  | 
**columns** | **list[str]** | An array of columns to retrieve from the table, taken from the table specified above. Defaults to all columns.  | [optional] 
**filters** | [**ResultFilters**](ResultFilters.md) | Filters on the results. Only results matching the criteria specified in the filters will be returned. If both filters and conceptSetName are specified, results must match both.  | [optional] 
**concept_set_name** | **str** | A name of a concept set in the workspace used to filter results; results must match one of the concepts in the named concept set. If both filters and conceptSetName are specified, results must match both.  | [optional] 
**order_by** | **list[str]** | An array of columns to sort the resulting data by, taken from the table specified above, each one optionally enclosed in \&quot;DESCENDING()\&quot; for descending sort order. Default sort order is \&quot;person_id\&quot; (in ascending order) followed by the ID of the specified table (in ascending order.)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


