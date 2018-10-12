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
information about concepts. Use this if you have not already defined a named concept set in workbench
for the concepts you are interested in.

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

## Retrieving data about cohorts

The `aou_workbench_client.data` module provides `load_data` and `load_annotations` functions that 
allow you to retrieve data from the CDR and annotations created during cohort review for a 
specified cohort.

### `aou_workbench_client.data.load_data`

`load_data` allows you to extract data from an OMOP table for the participants in a
cohort. Results are returned matching the specified concept IDs, filters, and cohort statuses, in 
the order specified. 

Results from this method are returned as a Pandas DataFrame with the columns requested. All results
will be loaded into memory. The results returned at present must be smaller than 128 MB compressed
due to BigQuery maximum response size limits; see https://cloud.google.com/bigquery/quotas for 
more information.

#### `load_data` parameters

Name | Required? | Description
---- | --------- | -----------  
cohort_name | Yes | The name of a cohort in the workspace that contains the calling notebook; only participants in this cohort will be returned. (Example: 'My Cohort')
table | Yes | The class representing the primary / starting table to retrieve data from, taken from the `aou_workbench_client.cdr.model` package. The table class must have a person_id column. (Example: `aou_workbench_client.cdr.model.Person`)
columns | No | A list of column names from the starting table or related tables to return in the data table; defaults to all columns in the starting table (and no columns in related tables). Use fields defined on the class specified for the `table` parameter when specifying columns. (Example: `[Person.person_id, Person.gender_concept_id]`)
concept_set_name | No | The name of a concept set in the workspace that contains the calling notebook to use when filtering results from the table; only use with tables that have standard_concept_id_column and source_concept_id_column fields on the provided table class. Use this method instead of concept_ids or source_concept_ids when there is already a named concept set for the concepts to be extracted. If both filters and concept_set_name are specified, rows returned must match both.    
concept_ids | No | A list of integer IDs of standard concepts to include in the results from the table; only use with tables that have a standard_concept_id_column field on the provided table class; defaults to no standard concept filtering. If both `concept_ids` and `source_concept_ids` are specified, rows that match either will be returned.
concept_id_column | No | The name of the column to filter against with the values in `concept_ids`; defaults to the standard concept ID column for the table (if applicable); this must be specified with tables that lack a standard concept ID column when `concept_ids` is specified. (Example: `Person.gender_concept_id`)  
source_concept_ids | No | A list of integer IDs of source concepts to include in the results from the table; only use with tables that have a `source_concept_id_column` field on the provided table class; defaults to no standard concept filtering. If both `concept_ids` and `source_concept_ids` are specified, rows that match either will be returned.  
filters | No | [ResultFilters](#result-filters) representing other filters to use to select rows returned from the table; defaults to no additional filtering. If both `filters` and `concept_ids` / `source_concept_ids` are specified, rows returned must match both.  Use fields defined on the class specified for the `table` parameter when specifying columns in filters. 
cohort_statuses | No | a list of [CohortStatus](swagger_docs/CohortStatus.md) indicating a filter on the review status of participants to be returned in the resulting data table; defaults to `['INCLUDED', 'NEEDS_FURTHER_REVIEW', 'NOT_REVIEWED']` (not excluded).
max_results | No | the maximum number of rows to return in the resulting data frame; defaults to no limit (all matching rows will be returned.) Note that for large cohorts, it may take longer to get all results; it is advisable to set `max_results` to something initially during development to ensure the results are what you are looking for.
order_by | No | a list of column names from the table or related tables to order the results by; defaults to order by `person_id` and primary key of the specified table. Use fields defined on the class specified for the `table` parameter when specifying columns here. (Example: `[Person.gender_concept_id, Person.person_id]`)
debug | No |  True if you want to see debugging output for the API requests used to materialize the cohort; defaults to False.

Columns referenced in the `columns`, `concept_id_column`, `filters`, and `order_by` parameters to 
`load_data` can be specified using fields from the [CDR model](#cdr-model).

#### CDR model

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

#### Related table columns

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

#### Column filters

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

#### `load_data` examples

All examples below reference modules that can be imported from `aou_workbench_client.swagger_client.models`
and `aou_workbench_client.cdr.model`.

Return all columns in observation for all observation rows:

```python
df = load_data(cohort_name='My Cohort', table=Observation)
```

Return specific columns on observation for all observation rows:

```python
df = load_data(cohort_name='My Cohort', table=Observation, 
    columns=[Observation.observation_id, Observation.person_id, Observation.value_as_number])
```

Return all columns in observation for rows matching a filter on `observation_concept_id` = 123456:

```python
concept_column_filter = ColumnFilter(column_name=Observation.observation_concept_id, 
                                     value_number=123456)
concept_filter = ResultFilters(column_filter=concept_column_filter)
df = load_data(cohort_name='My Cohort', table=Observation, filters=concept_filter)
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
df = load_data(cohort_name='My Cohort', table=Observation, filters=both_filter)
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
df = load_data(cohort_name='My Cohort', table=Observation, filters=either_filter)
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
df = load_data(cohort_name='My Cohort', table=Observation, filters=not_either_filter)
```

Return all columns in observation for all rows ordered by observation_concept_id (ascending) and value_as_number (descending):
```python
df = load_data(cohort_name='My Cohort', table=Observation, 
               order_by=[Observation.observation_concept_id, 
                         descending(Observation.value_as_number)])
``` 

Return person_id, gender concept name, and care site's location city for rows in the person table:
```python
df = load_data(cohort_name='My Cohort', table=Person, 
               columns=[Person.person_id, Person.gender_concept.name, 
                        Person.care_site.location.city])
```

Return person_id and care site's location city for rows in the person table where 
care site's location state is 'TX', ordered by care site's location city:
```python
state_column_filter = ColumnFilter(column_name=Person.care_site.location.city, 
                                   value='TX')
state_filter = ResultFilters(column_filter=state_column_filter)

df = load_data(cohort_name='My Cohort', table=Person,
               columns=[Person.person_id, Person.care_site.location.city],
               filters=state_filter, 
               order_by=[Person.care_site.location.city])
```

### `aou_workbench_client.data.load_annotations`

`load_annotations` allows you to retrieve annotation values or cohort review statuses you created 
in workbench during cohort review. 

Results from this method are returned as a Pandas DataFrame with the annotations requested as columns.
All results will be loaded into memory. 


#### `load_annotations` parameters

Name | Required? | Description
---- | --------- | -----------  
`cohort_name`| Yes | The name of a cohort in the workspace that contains the calling notebook
`columns` | No | A list of `'person_id'`, `'review_status'`, or names of annotations  defined on the cohort. Defaults to `['person_id', 'review_status', <all defined annotation names>]`.
`cohort_statuses` | No | A list of CohortStatus indicating a filter on the review status of  participants to be returned in the resulting data table; defaults to `['INCLUDED', 'NEEDS_FURTHER_REVIEW', 'NOT_REVIEWED']` (not excluded).
`order_by` | No | A list of `'person_id'`, `'review_status'`, or names of annotations  defined on the cohort, any of which can optionally be wrapped in `DESCENDING()`  to request descending sort order. Defaults to `['person_id']`. Any annotations in `order_by` must also be present in `columns` (if `columns` is specified.)
`debug` | No | True if debug request and response information should be displayed; defaults to false.  


#### `load_annotations` examples

Return `person_id`, `review_status`, and all defined annotations, ordered by `person_id`:

```python
annotations = load_annotations(cohort_name='My Cohort')
```

Return just `person_id` and `review_status`, ordered by `person_id`:

```python
annotations = load_annotations(cohort_name='My Cohort', columns=['person_id', 'review_status'])
```

Return `person_id` and an annotation named `is obese`, ordered by `person_id`:

```python
annotations = load_annotations(cohort_name='My Cohort', columns=['person_id', 'is_obese'])
```

Return `person_id`, `review_status, and all annotations, ordered by the `is_obese` annotation and review status, descending:

```python
annotations = load_annotations(cohort_name='My Cohort', order_by=['is_obese', 'DESCENDING(review_status)'])
```

 
#### Putting it all together

Here's an example of retrieving a data frame containing 1000 measurement 
values where the source value is 'Temper' for a cohort named 'Flu', using [`load_data`](#aou_workbench_clientdataload_data):

```python
from aou_workbench_client.swagger_client.models import ColumnFilter, ResultFilters
from aou_workbench_client.cdr.model import Measurement

from aou_workbench_client.data import load_data

temp_filter = ResultFilters(column_filter=ColumnFilter(Measurement.measurement_source_value, 
                                                       value='Temper'))
measure_df = load_data(cohort_name='Flu', table=Measurement,
                       columns=[Measurement.person_id, 
                                Measurement.measurement_id, 
                                Measurement.measurement_date, 
                                Measurement.measurement_source_value,
                                Measurement.value_as_number],
                       filters=temp_filter,
                       max_results=1000)
```

The resulting data frame would look like:

Row | measurement_date | measurement_id | measurement_source_value | person_id | value_as_number
--- | ---------------- | -------------- | ------------------------ | --------- | ---------------
0 |	2015-07-31 | 160349813 | Temper | 81 | 36.78
1 |	2009-11-26 | 101713778 | Temper	| 172 |	37.06
2 | 2011-08-08 | 104223671 | Temper | 172 | 36.72


Here's an example of loading some annotations:
```python
from aou_workbench_client.data import load_annotations
annotations = load_annotations(cohort_name='Flu', 
                               columns=['person_id', 'review_status', 'my annotation'])
```

resulting in a data frame like:

Row | person_id | review_status | my annotation
--- | --------- | ------------- | -------------
0 | 123456789 | INCLUDED | value 1
1 | 987654321 | EXCLUDED | value 2
2 | 789321456 | NOT_REVIEWED | value 3
3 | 543216748 | NEEDS_FURTHER_REVIEW |




                                           
