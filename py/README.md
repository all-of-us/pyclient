# AllOfUs Python Client Library

Python code in this library is used to access the AllOfUs Workbench API from
the context of a Jupyter notebook. 

## Installing the library

The latest version of the library will be installed automatically on the Jupyter
server your notebook code runs in, but if you need to upgrade to a version which 
has not been released yet, you can do so by running in a notebook cell:

```
!pip install --user --upgrade 'https://github.com/all-of-us/pyclient/archive/<VERSION>.zip#egg=aou_workbench_client&subdirectory=py'
```

or for Python 2.7:

```
!pip2.7 install --user --upgrade 'https://github.com/all-of-us/pyclient/archive/<VERSION>.zip#egg=aou_workbench_client&subdirectory=py'
```

and then restarting your Python kernel.

The modules you will use in your code are in the aou_workbench_client package.

## Using cohorts in a notebook

The aou_workbench_client.cohorts module provides functions for materializing cohorts.

### MaterializeCohortRequest

When you want to materialize data about a cohort you've defined in workbench, you construct
a [MaterializeCohortRequest](swagger_docs/MaterializeCohortRequest.md). 

The two fields you must populate on it are `cohort_name` and `field_set`.

The `cohort_name` field should refer to the name of a cohort you defined in workbench.
(Make sure to update any references in notebooks if you change the cohort's name.)

The `field_set` field must be set to a [FieldSet](swagger_docs/FieldSet.md)
indicating what data you want to retrieve about the cohort. 

Field sets must have either their `table_query` or `annotation_query` field
populated. Details for table queries and annotation queries follow.

#### Table queries

A table query is used to retrieve data about the cohort from a table with 
a person_id column in the CDR version associated with the workspace housing 
this notebook. 

You can retrieve, filter, and sort by data directly in the requested table, 
or in related tables the table has foreign key relationships to.

##### TableQuery Fields

Name | Required? | Description
---- | --------- | -----------
`table_name`|Yes|The primary / starting table to retrieve data from. You can find the list of supported tables for **table_name** in the **cohortTables** section of [our CDR schema](https://github.com/all-of-us/workbench/blob/master/api/config/cdm/cdm_5_2.json).
`columns`|No|What columns you want to retrieve from the table or related tables. By default, all columns on the specified table (but no related tables) will be returned.
`filters`|No|Filters that results returned must match based on matching values to the columns on the table or related tables.  By default, no filtering criteria is returned.
`order_by`|No|The columns from the specified table or related tables to sort results by, optionally wrapped by DESCENDING() to indicate a descending sort order. By default, the results are sorted by `person_id` and the ID of the table you specified, in ascending order.

Columns referred to by name in `columns`, `filters`, and `order_by` can either
be the name of a column (e.g. "person_id", "observation_id") in the table you specified, 
found in the configuration with that name in 
[our CDR schema](https://github.com/all-of-us/workbench/blob/master/api/config/cdm/cdm_5_2.json);
or they can be columns from related tables specified with a dot notation going one
or more levels deep (e.g. "gender_concept.concept_name", "care_site.location.address_1").

Related tables are indicated in [our CDR schema](https://github.com/all-of-us/workbench/blob/master/api/config/cdm/cdm_5_2.json)
by "foreignKey": "tableName" on column ending in "_id";
referring to columns on the related table is done by stripping off the "_id" on that column
and adding a dot, followed by the column name on the related table (e.g. gender_concept.concept_name
returns concept_name from the concept referred to by gender_concept_id on the person table.)

Note that while you can filter or order by columns on related tables, the
queries will run slower than just filtering and ordering by columns on the
primary table; if your cohort is large, this may result in your query timing
out before it can be completed. (In future, we will support longer-running queries.)

Result filters can represent arbitrarily complex combinations of comparisons between 
column values and values provided by the notebook, using `all_of` to match
results that match all of the filters in the list, `any_of` to match results that match
at least one of the filters in the list, and `not` to match results that do NOT match
the filter it is placed on.

##### TableQuery examples

All examples below reference modules that can be imported from `aou_workbench_client.swagger_client.models`.

Return all columns in observation for all observation rows:

```
table_query = TableQuery(table_name='observation')
```

Return specific columns on observation for all observation rows:

```
table_query = TableQuery(table_name='observation', columns=['observation_id', 'person_id', 'value_as_number'])
```

Return all columns in observation for rows matching a filter on `observation_concept_id` = 123456:

```
concept_column_filter = ColumnFilter(column_name='observation_concept_id', 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
table_query = TableQuery(table_name='observation', filters=concept_filter)
```

Return all columns in observation for rows matching `observation_concept_id` = 123456 AND `value_as_number` > 1000:
```
concept_column_filter = ColumnFilter(column_name='observation_concept_id', 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
value_column_filter = ColumnFilter(column_name='value_as_number', 
                                   value_number=1000, 
                                   operator=Operator.GREATER_THAN)
value_as_number_filter = ResultFilters(column_filter=value_column_filter)
both_filters = ResultFilters(all_of=[concept_filter, value_as_number_filter])
table_query = TableQuery(table_name='observation', filters=both_filter)
```
 
Return all columns in observation for rows matching `observation_concept_id` = 123456 OR `value_as_number` > 1000:
```
concept_column_filter = ColumnFilter(column_name='observation_concept_id', 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
value_column_filter = ColumnFilter(column_name='value_as_number', 
                                   value_number=1000, 
                                   operator=Operator.GREATER_THAN)
value_as_number_filter = ResultFilters(column_filter=value_column_filter)
either_filter = ResultFilters(any_of=[concept_filter, value_as_number_filter])
table_query = TableQuery(table_name='observation', filters=either_filter)
```

Return all columns in observation for rows that DO NOT match `observation_concept_id` = 123456 OR `value_as_number` > 1000:
```
concept_column_filter = ColumnFilter(column_name='observation_concept_id', 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
value_column_filter = ColumnFilter(column_name='value_as_number', 
                                   value_number=1000, 
                                   operator=Operator.GREATER_THAN)
value_as_number_filter = ResultFilters(column_filter=value_column_filter)
not_either_filter = ResultFilters(if_not=True, 
                                  any_of=[concept_filter, 
                                          value_as_number_filter])
table_query = TableQuery(table_name='observation', filters=not_either_filter)
```

Return all columns in observation for all rows ordered by observation_concept_id (ascending) and value_as_number (descending):
```
table_query = TableQuery(table_name='observation', 
                         order_by=['observation_concept_id', 
                                   'DESCENDING(value_as_number)'])
``` 

Return person_id, gender concept name, and care site's location city for rows in the person table:
```
table_query = TableQuery(table_name='observation', 
                          columns=['person_id', 'gender_concept.name', 
                                   'care_site.location.city'])
```

Return person_id and care site's location city for rows in the person table where 
care site's location state is 'TX', ordered by care site's location city:
```
state_column_filter = ColumnFilter(column_name='care_site.location.city', 
                                   value='TX')
state_filter = ResultFilters(column_filter=state_column_filter)

table_query = TableQuery(table_name='observation',
                         columns=['person_id', 'care_site.location.city'],
                         filters=state_filter, 
                         order_by=['care_site.location.city'])
```

#### Annotation queries


### materialize_cohort

materialize_cohort is used to fetch some or all results of cohort materialization.
This can be used to retrieve information about some or all of the participants in a
cohort you defined in the AllOfUs workbench.

#### Parameters 
Name | Description
---------- | --------  
`request` | A [MaterializeCohortRequest](swagger_docs/MaterializeCohortRequest.md) indicating what cohort to materialize, what filtering and ordering criteria to apply, and what fields to retrieve.
`max_results` | The maximum number of results to retrieve. Defaults to returning all results matching the cohort and filtering criteria in the specified request. This may require multiple server calls -- request.page_size specifies the maximum number retrieved per call.  
 
#### Simple Example



