# CdrQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | Google SQL to use when querying the CDR. If empty, it means no participants can possibly match the data table specification, and an empty data table should be returned.  | [optional] 
**columns** | **list[str]** | An array of names to be used for the columns being returned by the query. (Note that related table aliases will be returned with &#39;.&#39; as a separator, whereas &#39;__&#39; is used in the SQL.) This will be populated even if sql is empty (i.e. there are no results.)  | 
**configuration** | **object** | configuration for the BigQuery job (includes named parameters); you can pass this JSON dictionary in for the configuration when calling methods like pandas.read_gbq().  | [optional] 
**bigquery_project** | **str** | name of the Google Cloud project containing the CDR dataset | 
**bigquery_dataset** | **str** | name of the CDR BigQuery dataset | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


