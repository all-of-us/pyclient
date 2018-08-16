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

## Finding concepts

Data about participants in the curated data repository (CDR) is stored in 
[OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/) tables, with
foreign keys to a Concept table indicating what type of observation, measurement, procedure, etc.
is being recorded about the participant.

When materializing a cohort and analyzing data, it is useful to be able to filter on the IDs of
concepts of interest. The `aou_workbench_client.concepts` module provides functions for retrieving
information about concepts.

### `aou_workbench_client.concepts.display_concepts_widget`

`display_concepts_widget` shows an interactive widget for querying concepts. This is 
the simplest way to find concepts of interest.

When materializing a cohort, the IDs displayed in the "ID" column of the results
can be used with a [column filter](#column-filters) on `value_number` to filter rows
to those matching a specified concept.

To display the widget, paste the following code into a cell in your notebook:

```python
from aou_workbench_client.concepts import display_concepts_widget

display_concepts_widget()
```

### `aou_workbench_client.concepts.display_concepts`

`display_concepts` displays an HTML table containing concepts matching criteria
specified in a [SearchConceptsRequest](swagger_docs/SearchConceptsRequest.md).

Use this function if you want to write code to control what concepts are 
returned in results, rather than using an interactive widget.

Examples:

```python
from aou_workbench_client.concepts import display_concepts
from aou_workbench_client.swagger_client.models.search_concepts_request import SearchConceptsRequest
from aou_workbench_client.swagger_client.models.domain import Domain
from aou_workbench_client.swagger_client.models.standard_concept_filter import StandardConceptFilter

# Displays all concepts with "arthritis" in the name. 
display_concepts(SearchConceptsRequest(query='Arthritis'))

# Displays the top 3 concepts with "arthritis" in the name. 
display_concepts(SearchConceptsRequest(query='Arthritis', max_results=3))

# Displays only standard concepts with "arthritis" in the name.
display_concepts(SearchConceptsRequest(query='Arthritis', 
    standard_concept_filter=StandardConceptFilter.STANDARD_CONCEPTS))

# Displays all concepts with "blood" in the name in the "LOINC" vocabulary.
display_concepts(SearchConceptsRequest(query="Blood", vocabulary_ids=["LOINC"]))

# Displays all concepts with "blood" in the name in the "Procedure" domain.
display_concepts(SearchConceptsRequest(query="Blood", domain=Domain.PROCEDURE))

# Displays 3 standard concepts with "blood" in the name in the "Measurement" domain
# and the "LOINC" or "SNOMED" vocabulary.
display_concepts(SearchConceptsRequest(query="Blood", domain=Domain.MEASUREMENT,
    vocabulary_ids=["LOINC", "SNOMED"], 
    standard_concept_filter=StandardConceptFilter.STANDARD_CONCEPTS,
    max_results=3))
```

### ``aou_workbench_client.concepts.search_concepts``

`search_concepts` is used to fetch a list of [Concept](swagger_docs/Concept.md) objects matching criteria
specified in a [SearchConceptsRequest](swagger_docs/SearchConceptsRequest.md). Concepts are returned in descending
count order; the concepts that occur for the most participants in the CDR are returned first.

Use this function if you want access to the full [Concept](swagger_docs/Concept.md) data
in your code.

### `aou_workbench_client.concepts.get_concepts_frame`

`get_concepts_frame` returns a DataFrame from the constructed from the results of calling `search_concepts`,
with columns for concept ID, name, code, domain, vocabulary, and count.

Use this function if you want to get back a data frame but have control over its
rendering.


## Using cohorts

The `aou_workbench_client.cohorts` module provides functions for retrieving data about participants
in a cohort using a cohort materialization request object constructed in your code.

The `aou_workbench_client.data` module provides `load_data_table` and `load_data_frame` functions that offer a simpler
API for materializing cohorts; we recommend using them instead of the methods in
`aou_workbench_client.cohorts` in most cases. (At present, these methods do not support
loading annotation data about cohorts, but otherwise should provide full cohort materialization 
functionality.)

### `aou_workbench_client.data.load_data_table`

`load_data_table` allows you to extract data from an OMOP table for the participants in a
cohort. Results are returned matching the specified concept IDs, filters, and cohort statuses, in 
the order specified. 

Results from this method are returned as a Python generator of dictionaries, with keys matching the columns
requested. API calls are issued as needed as you iterate over the results in the generator. (No API calls will be
performed until you start iterating.)

To instead return all the results as an in-memory Pandas DataFrame, use the convenience method
[load_data_frame](#aou_workbench_clientdataload_data_frame).

### `aou_workbench_client.data.load_data_frame`

`load_data_frame` executes [load_data_table](#aou_workbench_clientdataload_data_table) and returns all the results
as an in-memory Pandas DataFrame. Note that many API calls may need to be performed in order to retrieve all the results;
for large cohorts this may take a while.

#### `load_data_table` and `load_data_frame` parameters

Name | Required? | Description
---- | --------- | -----------  
cohort_name | Yes | The name of a cohort in the workspace that contains the calling notebook; only participants in this cohort will be returned. (Example: 'My Cohort')
table | Yes | The class representing the primary / starting table to retrieve data from, taken from the `aou_workbench_client.cdr.model` package. The table class must have a person_id column. (Example: `aou_workbench_client.cdr.model.Person`)
columns | No | A list of column names from the starting table or related tables to return in the data table; defaults to all columns in the starting table (and no columns in related tables). (Example: `[Person.person_id, Person.gender_concept_id]`)
concept_ids | No | A list of integer IDs of standard concepts to include in the results from the table; only use with tables that have a standard_concept_id_column field on the provided table class; defaults to no standard concept filtering. If both `concept_ids` and `source_concept_ids` are specified, rows that match either will be returned.
concept_id_column | No | The name of the column to filter against with the values in `concept_ids`; defaults to the standard concept ID column for the table (if applicable); this must be specified with tables that lack a standard concept ID column when `concept_ids` is specified. (Example: `Person.gender_concept_id`)  
source_concept_ids | No | A list of integer IDs of source concepts to include in the results from the table; only use with tables that have a `source_concept_id_column` field on the provided table class; defaults to no standard concept filtering. If both `concept_ids` and `source_concept_ids` are specified, rows that match either will be returned.
source_concept_id_column | No | The name of the column to filter against with the values in `source_concept_ids`; defaults to the source concept ID column for the table (if applicable); this must be specified with tables that lack a source concept ID column when `source_concept_ids` is specified. (Example: `Person.gender_source_concept_id`_  
filters | No | [ResultFilters](#result-filters) representing other filters to use to select rows returned from the table; defaults to no additional filtering. If both `filters` and `concept_ids` / `source_concept_ids` are specified, rows returned must match both. 
cohort_statuses | No | a list of [CohortStatus](swagger_docs/CohortStatus.md) indicating a filter on the review status of participants to be returned in the resulting data table; defaults to no filtering (all participants are returned.)
max_results | No | the maximum number of rows to return in the resulting data table; defaults to no limit (all matching rows will be returned.) Note that for large cohorts, it may take a long time to get all results; it is advisable to set `max_results` to something initially during development to ensure the results are what you are looking for.
order_by | No | a list of column names from the table or related tables to order the results by; defaults to order by `person_id` and primary key of the specified table. (Example: `[Person.gender_concept_id, Person.person_id]`)
page_size | No | the maximum number of result rows to fetch in a single API response when retrieving results; defaults to 1000.
debug | No |  True if you want to see debugging output for the API requests used to materialize the cohort; defaults to False.


### `aou_workbench_client.cohorts.materialize_cohort`

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
`debug` | No | True if you want to see debugging output for the API requests used to materialize the cohort; defaults to False.  

### `aou_workbench_client.cohorts.materialize_cohort_page`

`materialize_cohort_page` is used to fetch a single page of results from cohort
materialization, as a [MaterializeCohortResponse](swagger_docs/MaterializeCohortResponse.md).

Normally you should be able to call [`materialize_cohort`](#aou_workbench_clientcohortsmaterialize_cohort) instead
of this function, but you may use this function to get better control over
when requests to retrieve results from the server are executed.

#### `materialize_cohort_page` parameters
Name | Required? | Description
---- | --------- | -----------  
`request` | Yes | A [MaterializeCohortRequest](#materializecohortrequest) indicating what cohort to materialize, what filtering and ordering criteria to apply, what fields to retrieve, and what pagination token to use (for subsequent requests.)
`debug` | No | True if you want to see debugging output for the API requests used to materialize the cohort; defaults to False.
 

### MaterializeCohortRequest

When you want to materialize data about a cohort you've defined in workbench, you construct
a [MaterializeCohortRequest object](swagger_docs/MaterializeCohortRequest.md). 

You will later pass this request to [materialize_cohort](#aou_workbench_clientcohortsmaterialize_cohort) if you wish
to retrieve all the results as a generator of dictionaries, or you can pass it to 
[`materialize_cohort_page`](#aou_workbench_clientcohortsmaterialize_cohort_page) if you wish to make server calls
to retrieve paginated responses containing results, one page at a time.

#### `MaterializeCohortRequest` fields

Name | Required? | Description
---- | --------- | -----------
`cohort_name`|Yes|The name of a cohort you defined in workbench. (Make sure to update any references in notebooks if you change the cohort's name.)
`field_set`|Yes|A [FieldSet](#field-sets) indicating what data you want to retrieve about the cohort.
`status_filter`|No|A list of [CohortStatus](swagger_docs/CohortStatus.md) values indicating cohort review statuses to filter the participants whose data is returned. By default, `[INCLUDED, NEEDS_FURTHER_REVIEW, NOT_REVIEWED]` will be used -- everything except `EXCLUDED` (participants that have been explicitly excluded.) There is no need to set this for cohorts which have not been reviewed. 
`page_size`|No|The number of results to return in a single request to the server. Defaults to 1000. Depending on the size of data returned, you may try increasing or decreasing this to improve performance, but you generally should not have to set this.
`page_token`|No|A pagination token used to retrieve additional results from the server after the first request. You will only need to set this if you use the [materialize_cohort_page][#aou_workbench_clientcohortsmaterialize_cohort_page] function repeatedly to retrieve multiple pages of data explicitly.

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
`table` | No | The class representing the primary / starting table to retrieve data from, taken from the `aou_workbench_client.cdr.model` package. Either this or table_name must be specified. The table class must have a person_id column. 
`table_name`| No |The name of the primary / starting table to retrieve data from. Either this or table must be specified. The list of supported tables for **table_name** is `aou_workbench_client.cdr.model.cohort_tables`; the value of the `table_name` field on each class in `aou_workbench_client.cdr.model` can be provided here.
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
* for cohort tables, `standard_concept_id_column` and `source_concept_id_column` fields storing the names of columns for the standard and source concepts for the domain

You can use foreign keys to reference fields on related tables many levels deep;
for example, `Person.care_site.location.city'.

The `cohort_tables` list contains the names of Python classes representing 
tables you can use for materializing cohorts. 

The `table_columns` dictionary maps table names to column data frames. You can
use the `display_cdr_schema` function to display the schema for all the tables in 
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

Note: it is often useful to filter rows on a concept ID column, assigning `value_number` to the value of
a concept ID retrieved using (`display_concepts`)[#display-concepts].
 

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
table_query = TableQuery(table=Observation)
```

Return specific columns on observation for all observation rows:

```python
table_query = TableQuery(table=Observation, 
    columns=[Observation.observation_id, Observation.person_id, Observation.value_as_number])
```

Return all columns in observation for rows matching a filter on `observation_concept_id` = 123456:

```python
concept_column_filter = ColumnFilter(column_name=Observation.observation_concept_id, 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
table_query = TableQuery(table=Observation, filters=concept_filter)
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
table_query = TableQuery(table=Observation, filters=both_filter)
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
table_query = TableQuery(table=Observation, filters=either_filter)
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
table_query = TableQuery(table=Observation, filters=not_either_filter)
```

Return all columns in observation for all rows ordered by observation_concept_id (ascending) and value_as_number (descending):
```python
table_query = TableQuery(table=Observation, 
                         order_by=[Observation.observation_concept_id, 
                                   descending(Observation.value_as_number)])
``` 

Return person_id, gender concept name, and care site's location city for rows in the person table:
```python
table_query = TableQuery(table=Person, 
                          columns=[Person.person_id, Person.gender_concept.name, 
                                   Person.care_site.location.city])
```

Return person_id and care site's location city for rows in the person table where 
care site's location state is 'TX', ordered by care site's location city:
```python
state_column_filter = ColumnFilter(column_name=Person.care_site.location.city, 
                                   value='TX')
state_filter = ResultFilters(column_filter=state_column_filter)

table_query = TableQuery(table=Person,
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

Here's an example of materializing a cohort to retrieve a data frame containing 1000 measurement 
values where the source value is 'Temper' for a cohort named 'Flu', using [`load_data_frame`](#aou_workbench_clientdataload_data_frame):

```python
from aou_workbench_client.swagger_client.models import ColumnFilter, ResultFilters
from aou_workbench_client.cdr.model import Measurement

from aou_workbench_client.data import load_data_frame

import pandas as pd

temp_filter = ResultFilters(column_filter=ColumnFilter(Measurement.measurement_source_value, 
                                                       value='Temper'))
measure_df = load_data_frame(cohort_name='Flu', table=Measurement,
                             columns=[Measurement.person_id, 
                                      Measurement.measurement_id, 
                                      Measurement.measurement_date, 
                                      Measurement.measurement_source_value,
                                      Measurement.value_as_number],
                             filters=temp_filter,
                             max_results=1000)
```

Here is the more complicated but equivalent Python using [`materialize_cohort`](#aou_workbench_clientcohortsmaterialize_cohort):

```python
from aou_workbench_client.swagger_client.models import ResultFilters, MaterializeCohortRequest, CohortStatus
from aou_workbench_client.swagger_client.models import TableQuery, ColumnFilter, Operator, FieldSet, AnnotationQuery
from aou_workbench_client.cohorts import materialize_cohort
from aou_workbench_client.cdr.model import Measurement

import pandas as pd

temp_filter = ResultFilters(column_filter=ColumnFilter(Measurement.measurement_source_value, 
                                                       value='Temper'))
measure_query = TableQuery(table=Measurement,
                          columns=[Measurement.person_id, 
                                   Measurement.measurement_id, 
                                   Measurement.measurement_date, 
                                   Measurement.measurement_source_value,
                                   Measurement.value_as_number],
                          filters=temp_filter)
field_set = FieldSet(table_query=measure_query)
measure_request = MaterializeCohortRequest(cohort_name='Flu', 
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


Here's an example of materializing an annotation query:
```python
annotation_query = AnnotationQuery(columns=['person_id', 'review_status', 'my annotation'])
annotation_field_set = FieldSet(annotation_query=annotation_query)
annotation_request = MaterializeCohortRequest(cohort_name='Flu', 
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




                                           