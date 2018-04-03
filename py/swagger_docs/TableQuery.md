# TableQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | The name of a table containing a person_id column to retrieve data from (e.g. person, observation); should be in the OMOP CDM 5.2 schema.  | 
**columns** | **list[str]** | An array of columns to retrieve from the table, taken from the table specified above. Defaults to all columns.  | [optional] 
**filters** | [**ResultFilters**](ResultFilters.md) | Filters on the results. Only results matching the criteria specified in the filters will be returned  | [optional] 
**order_by** | **list[str]** | An array of columns to sort the resulting data by, taken from the table specified above, each one optionally followed by \&quot; DESC\&quot; for descending sort order. (Default varies by table.)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


