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

The two fields you must populate on it are **cohort_name** and **field_set**.

The **cohort_name** field should refer to the name of a cohort you defined in workbench.
(Make sure to update any references in notebooks if you change the cohort's name.)

The **field_set** field must be set to a [FieldSet](swagger_docs/FieldSet.md)
indicating what data you want to retrieve about the cohort. 

Field sets must have either their **table_query** or **annotation_query** field
populated.

#### Table queries

A table query is used to retrieve data about the cohort from a table with 
a person_id column in the CDR version associated with the workspace housing 
this notebook. 

You can retrieve, filter, and sort by data directly in the requested table, 
or in related tables the table has foreign key relationships to.

##### TableQuery Fields

Name | Required? | Description
---- | --------- | -----------
**table_name**|Yes|The primary / starting table to retrieve data from.
**columns**|No|What columns you want to retrieve from the table or related tables. By default, all columns on the specified table (but no related tables) will be returned.
**filters**|No|Filters that results returned must match based on matching values to the columns on the table or related tables.  By default, no filtering criteria is returned.
**order_by**|No|The columns from the specified table or related tables to sort results by. By default, the results are sorted by **person_id** and the primary key of the table you specified.

You can find the list of supported tables for **table_name** in the **cohortTables** section 
of [our CDR schema] (https://github.com/all-of-us/workbench/blob/master/api/config/cdm/cdm_5_2.json).

Columns referred to by name in **columns**, **filters**, and **order_by** can either
be the name of a column (e.g. "person_id", "observation_id") in the table you specified, 
found in the configuration with that name in 
[our CDR schema] (https://github.com/all-of-us/workbench/blob/master/api/config/cdm/cdm_5_2.json);
or they can be columns from related tables specified with a dot notation going one
or more levels deep (e.g. "gender_concept.concept_name", "care_site.location.address_1").

Related tables are indicated in [our CDR schema] (https://github.com/all-of-us/workbench/blob/master/api/config/cdm/cdm_5_2.json)
by "foreignKey": "tableName" on column ending in "_id";
referring to columns on the related table is done by stripping off the "_id" on that column
and adding a dot, followed by the column name on the related table (e.g. gender_concept.concept_name
returns concept_name from the concept referred to by gender_concept_id on the person table.)
 



### materialize_cohort

materialize_cohort is used to fetch some or all results of cohort materialization.
This can be used to retrieve information about some or all of the participants in a
cohort you defined in the AllOfUs workbench.

#### Parameters 
Name | Description
---------- | --------  
**request** | A [[MaterializeCohortRequest]](swagger_docs/MaterializeCohortRequest.md) indicating what cohort to materialize, what filtering and ordering criteria to apply, and what fields to retrieve.
**max_results** | The maximum number of results to retrieve. Defaults to returning all results matching the cohort and filtering criteria in the specified request. This may require multiple server calls -- request.page_size specifies the maximum number retrieved per call.  
 
#### Simple Example



