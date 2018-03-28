# TableQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | The name of a table containing a person_id column to retrieve data from (e.g. person, observation); should be in the OMOP CDM 5.2 schema.  | 
**columns** | **list[str]** | An array of columns to retrieve from the table, taken from the table specified above. Defaults to all columns.  | [optional] 
**filters** | **list[list[ColumnFilter]]** | An array of arrays of ColumnFilter objects to apply to results. Each child array represents a series of criteria to logically AND together; these expressions are then logically OR&#39;d together at the top level.  | [optional] 
**order_by** | **list[str]** | An array of columns to sort the resulting data by, taken from the table specified above, each one optionally followed by \&quot; DESC\&quot; for descending sort order. (Default varies by table.)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


