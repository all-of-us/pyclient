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

## Using cohorts

The `aou_workbench_client.cohorts` module provides functions for materializing cohorts.

### `materialize_cohort`

`materialize_cohort` is used to fetch some or all results of cohort materialization,
and return a generator of dictionaries representing the results.

This can be used to retrieve information about some or all of the participants in a
cohort you defined in the AllOfUs workbench.

No server call takes place to retrieve the data until you start iterating over
the generator.

For not-too-large result sets, it is reasonable to wrap the results in a call to `list()`
to bring all the results from the generator into memory at once. (You can then optionally pass that
list to the constructor of a Pandas `DataFrame`.)

If the result sets are very large, you may need to stream the results to disk as you 
use them to avoid running into out of memory errors.

Note that for large cohorts, a single call to materialize_cohort may run for 
a very long time.

Full examples of calling `materialize_cohort` can be found [below](#putting-it-all-together).

#### `materialize_cohort` parameters
Name | Required? | Description
---- | --------- | -----------  
`request` | Yes | A [MaterializeCohortRequest](#materializecohortrequest) indicating what cohort to materialize, what filtering and ordering criteria to apply, and what fields to retrieve.
`max_results` | No | The maximum number of results to retrieve in the generator. Defaults to returning all results matching the cohort and filtering criteria in the specified request, making as many server calls as needed. This may require multiple server calls -- request.page_size specifies the maximum number retrieved per call.  

### `materialize_cohort_page`

`materialize_cohort_page` is used to fetch a single page of results from cohort
materialization, as a [MaterializeCohortResponse](swagger_docs/MaterializeCohortResponse.md).

Normally you should be able to call [`materialize_cohort`](#materialize_cohort) instead
of this function, but you may use this function to get better control over
when requests to retrieve results from the server are executed.

#### `materialize_cohort_page` parameters
Name | Required? | Description
---- | --------- | -----------  
`request` | Yes | A [MaterializeCohortRequest](#materializecohortrequest) indicating what cohort to materialize, what filtering and ordering criteria to apply, what fields to retrieve, and what pagination token to use (for subsequent requests.)
 

### MaterializeCohortRequest

When you want to materialize data about a cohort you've defined in workbench, you construct
a [MaterializeCohortRequest object](swagger_docs/MaterializeCohortRequest.md). 

You will later pass this request to [materialize_cohort](#materialize_cohort) if you wish
to retrieve all the results as a generator of dictionaries, or you can pass it to 
[`materialize_cohort_page`](#materialize_cohort_page) if you wish to make server calls
to retrieve paginated responses containing results, one page at a time.

#### `MaterializeCohortRequest` fields

Name | Required? | Description
---- | --------- | -----------
`cohort_name`|Yes|The name of a cohort you defined in workbench. (Make sure to update any references in notebooks if you change the cohort's name.)
`field_set`|Yes|A [FieldSet](#field-sets) indicating what data you want to retrieve about the cohort.
`status_filter`|No|A list of [CohortStatus](swagger_docs/CohortStatus.md) values indicating cohort review statuses to filter the participants whose data is returned. By default, `[INCLUDED, NEEDS_FURTHER_REVIEW, NOT_REVIEWED]` will be used -- everything except `EXCLUDED` (participants that have been explicitly excluded.) There is no need to set this for cohorts which have not been reviewed. 
`page_size`|No|The number of results to return in a single request to the server. Defaults to 1000. Depending on the size of data returned, you may try increasing or decreasing this to improve performance, but you generally should not have to set this.
`page_token`|No|A pagination token used to retrieve additional results from the server after the first request. You will only need to set this if you use the [materialize_cohort_page][#materialize_cohort_page] function repeatedly to retrieve multiple pages of data explicitly.

#### Field sets

Field sets represent what data you want to retrieve about a cohort. 

A [FieldSet object](swagger_docs/FieldSet.md) must have either its 
[`table_query`](#table-queries) or [`annotation_query`](#annotation-queries) 
field populated. Details for table queries and annotation queries follow.

#### Table queries

A [TableQuery object](swagger_docs/TableQuery.md) is used to 
specify how to retrieve data about the cohort from a table with 
a person_id column in the version of the curated data repository (CDR)
associated with the workspace that contains this notebook.

You can retrieve, filter, and sort by data directly in the requested table, 
or in related tables the table has foreign key relationships to.

Tables and columns referenced in table queries can be specified using fields 
from the [CDR model](#cdr-model).

##### `TableQuery` fields

Name | Required? | Description
---- | --------- | -----------
`table_name`|Yes|The primary / starting table to retrieve data from. The list of supported tables for **table_name** is `aou_workbench_client.cdr.model.cohort_tables`; the value of the `table_name` field on each class in `aou_workbench_client.cdr.model` can be provided here.
`columns`|No|What columns you want to retrieve from the table or related tables. By default, all columns on the specified table (but no related tables) will be returned.
`filters`|No|[ResultFilters](#result-filters) that specifies criteria results returned must match based on matching values to the columns on the table or related tables.  By default, no filtering criteria is returned.
`order_by`|No|The columns from the specified table or related tables to sort results by, optionally wrapped by `DESCENDING()` (which can be generated using `aou_workbench_client.cdr.model.descending`) to indicate a descending sort order. Defaults to `['person_id', <table ID>]`.

Columns referred to by name in `columns`, `filters`, and `order_by` can either
be the name of a column (e.g. "person_id", "observation_id") in the table you specified, 
as listed in the [CDR model](#cdr-model);
or they can be columns from [related tables](#related-table-columns).

##### CDR model

Metadata about the tables and columns you can query against can be found in 
the client library in the [`aou_workbench_client.cdr.model`](aou_workbench_client/cdr/model.py) module. 
Documentation on the tables and columns can be found [here](aou_workbench_client/cdr/README.md).

Each class in the `aou_workbench_client.cdr.model` module (e.g. `Person`)
has:

* a `table_name` field indicating the name of the table to use (e.g. 'person').
* a `columns` field containing a data frame describing the columns on the table; you can print this to get documentation (e.g. `print Person.columns`)
* a `foreign_keys` field containing a list of zero or more names of fields for foreign keys to related tables
* fields for the names of columns on the table itself, which can be referenced in column filters (e.g. `Person.person_id`)
* zero or more fields for referencing columns on related tables (e.g. `Person.gender_concept`)

You can use foreign keys to reference fields on related tables many levels deep;
for example, `Person.care_site.location.city'.

The `cohort_tables` list contains the names of Python classes representing 
tables you can use for materializing cohorts. 

The `table_columns` dictionary maps table names to column data frames. You can
use the `print_cdr_schema` function to print the schema for all the tables in 
the CDR.

The `descending` function can be used to produce a `DESCENDING()` expression for
use in `order_by` lists.

##### Related table columns

Related table columns are specified with a dot notation going one
or more levels deep (e.g. "gender_concept.concept_name", "care_site.location.address_1").
You can use the [CDR model](#cdr-model) to specify these column names. 
Related tables are indicated in the [CDR model](#cdr-model)
by the `foreign_keys` field on objects (e.g. `Person.foreign_keys`).

Note that while you can filter or order by columns on related tables, the
queries will run slower than just filtering and ordering by columns on the
primary table; if your cohort is large, this may result in your query timing
out before it can be completed. (In future, we will support longer-running queries.)

Result filters can represent arbitrarily complex combinations of comparisons between 
column values and values provided by the notebook, using `all_of` to match
results that match all of the filters in the list, `any_of` to match results that match
at least one of the filters in the list, and `not` to match results that do NOT match
the filter it is placed on.

##### Result filters

A [ResultFilters object](swagger_docs/ResultFilters.md) specifies criteria that
table query results must match to be returned. If no results match the criteria, no 
results will be returned.

Exactly one of `column_filter`, `all_of`, or `any_of` must be specified on each
ResultFilters.

You can construct arbitrarily complex matching criteria by using nested
`ResultFilters` with `all_of` or `any_of`.

##### `ResultFilters` fields

Name | Required? | Description
---- | --------- | -----------
`column_filter` | No | A [ColumnFilter](#column-filters) specifying that a column value in a table in the CDR must match a provided value.
`all_of` | No | A list of [ResultFilters](#result-filters) specifying a list of conditions that must ALL be satisfied for results that are returned.
`any_of` | No | A list of [ResultFilters](#result-filters) specifying a list of conditions that at least one of must be satisfied for results that are returned.
`if_not` | No | If set to True, only results that DO NOT match the criteria specified by this filter are returned. Defaults to False.

##### Column filters

A [ColumnFilter object](swagger_docs/ColumnFilters.md) specifies a filter
that a given column value in a table in the CDR must match a provided value.

If the `IN` operator is used, exactly one of `values` and `value_numbers` must be specified,
depending on the type of column being compared against.

If the `LIKE` operator is used, only `value` should be specified.

If any other operator is used (or no operator is specified), 
exactly one of `value`, `value_number`, `value_date`, and `value_null` must be specified,
depending on the type of column being compared against.
 

##### `ColumnFilter` fields

Name | Required? | Description
---- | --------- | -----------
`column_name` | Yes | The name of the column on the primary table or [related table column](#related-table-columns) indicating what column to match against.
`operator` | No | The [Operator](swagger_docs/Operator.md) to use in the comparison. Defaults to `EQUAL`.
`value` | No | A string value to use in comparisons with string columns.
`values` | No | A list of string values to use in comparisons with string columns using the `IN` operator.
`value_number` | No | A numeric value to use in comparisons with numeric columns.
`value_numbers` | No | A list of numeric values to use in comparisons with numeric columns using the `IN` operator.
`value_date` | No | A date value to use in comparisons with date columns.
`value_null` | No | Set to true if you wish to compare to NULL / not set value (with the `EQUAL` operator for checking for matching NULL, or the `NOT_EQUAL` operator for matching anything but NULL.)

##### `TableQuery` examples

All examples below reference modules that can be imported from `aou_workbench_client.swagger_client.models`
and `aou_workbench_client.cdr.model`.

Return all columns in observation for all observation rows:

```python
table_query = TableQuery(table_name=Observation.table_name)
```

Return specific columns on observation for all observation rows:

```python
table_query = TableQuery(table_name=Observation.table_name, 
    columns=[Observation.observation_id, Observation.person_id, Observation.value_as_number])
```

Return all columns in observation for rows matching a filter on `observation_concept_id` = 123456:

```python
concept_column_filter = ColumnFilter(column_name=Observation.observation_concept_id, 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
table_query = TableQuery(table_name=Observation.table_name, filters=concept_filter)
```

Return all columns in observation for rows matching `observation_concept_id` = 123456 AND `value_as_number` > 1000:
```python
concept_column_filter = ColumnFilter(column_name=Observation.observation_concept_id, 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
value_column_filter = ColumnFilter(column_name=Observation.value_as_number, 
                                   value_number=1000, 
                                   operator=Operator.GREATER_THAN)
value_as_number_filter = ResultFilters(column_filter=value_column_filter)
both_filters = ResultFilters(all_of=[concept_filter, value_as_number_filter])
table_query = TableQuery(table_name=Observation.table_name, filters=both_filter)
```
 
Return all columns in observation for rows matching `observation_concept_id` = 123456 OR `value_as_number` > 1000:
```python
concept_column_filter = ColumnFilter(column_name=Observation.observation_concept_id, 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
value_column_filter = ColumnFilter(column_name=Observation.value_as_number, 
                                   value_number=1000, 
                                   operator=Operator.GREATER_THAN)
value_as_number_filter = ResultFilters(column_filter=value_column_filter)
either_filter = ResultFilters(any_of=[concept_filter, value_as_number_filter])
table_query = TableQuery(table_name=Observation.table_name, filters=either_filter)
```

Return all columns in observation for rows that DO NOT match `observation_concept_id` = 123456 OR `value_as_number` > 1000:
```python
concept_column_filter = ColumnFilter(column_name=Observation.observation_concept_id, 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
value_column_filter = ColumnFilter(column_name=Observation.value_as_number, 
                                   value_number=1000, 
                                   operator=Operator.GREATER_THAN)
value_as_number_filter = ResultFilters(column_filter=value_column_filter)
not_either_filter = ResultFilters(if_not=True, 
                                  any_of=[concept_filter, 
                                          value_as_number_filter])
table_query = TableQuery(table_name=Observation.table_name, filters=not_either_filter)
```

Return all columns in observation for all rows ordered by observation_concept_id (ascending) and value_as_number (descending):
```python
table_query = TableQuery(table_name=Observation.table_name, 
                         order_by=[Observation.observation_concept_id, 
                                   descending(Observation.value_as_number)])
``` 

Return person_id, gender concept name, and care site's location city for rows in the person table:
```python
table_query = TableQuery(table_name=Person.table_name, 
                          columns=[Person.person_id, Person.gender_concept.name, 
                                   Person.care_site.location.city])
```

Return person_id and care site's location city for rows in the person table where 
care site's location state is 'TX', ordered by care site's location city:
```python
state_column_filter = ColumnFilter(column_name=Person.care_site.location.city, 
                                   value='TX')
state_filter = ResultFilters(column_filter=state_column_filter)

table_query = TableQuery(table_name=Person.table_name,
                         columns=[Person.person_id, Person.care_site.location.city],
                         filters=state_filter, 
                         order_by=[Person.care_site.location.city])
```

#### Annotation queries

An [AnnotationQuery object](swagger_docs/AnnotationQuery.md) is used to retrieve the 
review status and annotations created as a part of cohort review, along with
the person_id they were created for. They are only useful for cohorts which have been
reviewed; cohorts without reviews will get no results in response to these queries.

Note that by default, participants that were sampled as a part of the review
but have not had their cohort status updated will be included in the results,
with a review status of `NOT_REVIEWED`. (These participants may have had 
annotations created, even if their review status is not set.)

If you wish to only get results for participants with an explicit cohort status,
use the `status_filter` field on the request to not include `NOT_REVIEWED`.

##### `AnnotationQuery` fields
 
Name | Required? | Description
---- | --------- | -----------
`columns` | No | A list of `'person_id'`, `'review_status'`, or names of annotations defined on the cohort. Defaults to `['person_id', 'review_status', <all defined annotation names>]`.
`order_by` | No | A list of `'person_id'`, `'review_status'`, or names of annotations defined on the cohort, any of which can optionally be wrapped in `DESCENDING()` to request descending sort order. Defaults to `['person_id']`. Any annotations in `order_by` must also be present in `columns` (if `columns` is specified.)

##### `AnnotationQuery` examples

Return `person_id`, `review_status`, and all annotations, ordered by `person_id`:

```python
annotation_query = AnnotationQuery()
```

Return just `person_id` and `review_status`, ordered by `person_id`:

```python
annotation_query = AnnotationQuery(columns=['person_id', 'review_status'])
```

Return `person_id` and an annotation named `is obese`, ordered by `person_id`:

```python
annotation_query = AnnotationQuery(columns=['person_id', 'is_obese'])
```

Return `person_id`, `review_status, and all annotations, ordered by the `is_obese` annotation and review status, descending:

```python
annotation_query = AnnotationQuery(order_by=['is_obese', 'DESCENDING(review_status)'])
```

 
#### Putting it all together

Here's an example of materializing a table query:

```python
from aou_workbench_client.swagger_client.models import ResultFilters, MaterializeCohortRequest, CohortStatus
from aou_workbench_client.swagger_client.models import TableQuery, ColumnFilter, Operator, FieldSet, AnnotationQuery
from aou_workbench_client.cohorts import materialize_cohort
from aou_workbench_client.cdr.model import Measurement

import pandas as pd

temp_filter = ResultFilters(column_filter=ColumnFilter(Measurement.measurement_source_value, 
                                                       value='Temper'))
measure_query = TableQuery(table_name=Measurement.table_name,
                          columns=[Measurement.person_id, 
                                   Measurement.measurement_id, 
                                   Measurement.measurement_date, 
                                   Measurement.measurement_source_value,
                                   Measurement.value_as_number],
                          filters=temp_filter)
field_set = FieldSet(table_query=measure_query)
measure_request = MaterializeCohortRequest(cohort_name="Flu", 
                                           field_set=field_set, 
                                           page_size=1000)
measure_response = materialize_cohort(measure_request, max_results=1000)
measure_df = pd.DataFrame(list(measure_response))
```

The resulting data frame would look like:

Row | measurement_date | measurement_id | measurement_source_value | person_id | value_as_number
--- | ---------------- | -------------- | ------------------------ | --------- | ---------------
0 |	2015-07-31 | 160349813 | Temper | 81 | 36.78
1 |	2009-11-26 | 101713778 | Temper	| 172 |	37.06
2 | 2011-08-08 | 104223671 | Temper | 172 | 36.72


And here's an example of materializing an annotation query:
```python
annotation_query = AnnotationQuery(columns=['person_id', 'review_status', 'my annotation'])
annotation_field_set = FieldSet(annotation_query=annotation_query)
annotation_request = MaterializeCohortRequest(cohort_name="Flu", 
                                              field_set=annotation_field_set, 
                                              page_size=1000)
annotation_response = materialize_cohort(annotation_request, max_results=1000)
annotation_df = pd.DataFrame(list(annotation_response))
```

resulting in a data frame like:

Row | person_id | review_status | my annotation
--- | --------- | ------------- | -------------
0 | 123456789 | INCLUDED | value 1
1 | 987654321 | EXCLUDED | value 2
2 | 789321456 | NOT_REVIEWED | value 3
3 | 543216748 | NEEDS_FURTHER_REVIEW |




                                           