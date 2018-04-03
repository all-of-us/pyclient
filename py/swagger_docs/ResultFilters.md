# ResultFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_not** | **bool** | Set to true if a result matching allOf or anyOf below should result in a result *not* being returned.  | [optional] 
**all_of** | [**list[ResultFilters]**](ResultFilters.md) | A list of result filters. All filters matching means a result should be returned (or not returned if \&quot;not\&quot; is true.)  | [optional] 
**any_of** | [**list[ResultFilters]**](ResultFilters.md) | A list of column filters. Any filters matching means a result should be returned (or not returned if \&quot;not\&quot; is true.)  | [optional] 
**column_filter** | [**ColumnFilter**](ColumnFilter.md) | A filter on a column in the table. Only a result matching this filter should be returned (or not returned if \&quot;not\&quot; is true.)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


