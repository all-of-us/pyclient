# ColumnFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** | The name of the column to filter on.  | 
**operator** | [**Operator**](Operator.md) | The operator to use when comparing values. Defaults to EQUAL. If the \&quot;in\&quot; operator is used, either values or valueNumbers should be populated.  | [optional] 
**value** | **str** | A string to use in comparisons (case-sensitive).  | [optional] 
**values** | **list[str]** | An array of strings to use in comparisons (case-sensitive); used with the \&quot;in\&quot; operator.  | [optional] 
**value_date** | **str** | An ISO-formatted date / datetime value to use in comparisons.  | [optional] 
**value_number** | **float** | A number to use in comparisons (either integer or floating point.)  | [optional] 
**value_numbers** | **list[float]** | An array of numbers to use in comparisons (used with the \&quot;in\&quot; operator)  | [optional] 
**value_null** | **bool** | Set to true if the column value should be compared to null.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


