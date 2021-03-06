from aou_workbench_client.cohorts import get_cohort_annotations, get_data_table_query
from aou_workbench_client.swagger_client.models.annotation_query import \
    AnnotationQuery
from aou_workbench_client.swagger_client.models.cohort_annotations_request import \
    CohortAnnotationsRequest
from aou_workbench_client.swagger_client.models.data_table_specification import \
    DataTableSpecification
from aou_workbench_client.swagger_client.models.table_query import TableQuery
from aou_workbench_client.swagger_client.models.column_filter import ColumnFilter
from aou_workbench_client.swagger_client.models.operator import Operator
from aou_workbench_client.swagger_client.models.result_filters import ResultFilters
from aou_workbench_client.config import all_of_us_config

import pandas as pd

"""
Loads a data table for participants in a specified cohort, 
represented as a generator of dictionaries. API calls are made to retrieve
the results in pages as you iterate over the generator. 

  :param cohort_name: the name of a cohort in the workspace that contains the calling notebook
  :param table: the class corresponding to the table that the data table should be extracted 
    from, pulled from aou_workbench_client.cdr.model; e.g. aou_workbench_client.cdr.model.Person
  :param columns: a list of column names from the table or related tables to return in the data table; 
    defaults to all columns in the table (and no columns in related tables); 
    e.g. [Person.person_id, Person.gender_concept_id]
  :param concept_set_name: the name of a concept set in the workspace that contains the 
    calling notebook to use when filtering results from the table; only use with tables 
    that have standard_concept_id_column and source_concept_id_column fields on the provided
    table class; use this method instead of concept_ids or source_concept_ids 
    when there is already a named concept set for the concepts to be extracted.
    If both filters and concept_set_name are specified, rows returned must match 
    both.     
  :param concept_ids: a list of integer IDs of standard concepts to include in the results from
    the table; only use with tables that have a standard_concept_id_column field on the provided
    table class; defaults to no standard concept filtering. 
    If both concept_ids and source_concept_ids are specified, rows that match either will be 
    returned.
  :param concept_id_column: the name of the column to filter against with the values in concept_ids; 
    defaults to the standard concept ID column for the table (if applicable); this must be specified
    in tables that lack a standard concept ID column when concept_ids is specified; 
    e.g. Person.gender_concept_id  
  :param source_concept_ids: a list of integer IDs of source concepts to include in the results
    from the table; only use with tables that have a source_concept_id_column field on the provided
    table class; defaults to no standard concept filtering.
    If both concept_ids and source_concept_ids are specified, rows that match either will be 
    returned.
  :param source_concept_id_column: the name of the column to filter against with the values in 
    source_concept_ids; defaults to the source concept ID column for the table (if applicable); 
    this must be specified in tables that lack a source concept ID column when 
    source_concept_ids is specified; e.g. Person.gender_source_concept_id  
  :param filters: ResultFilters representing other filters to use to select rows 
    returned from the table; defaults to no additional filtering. If both 
    filters and concept_set_name / concept_ids / source_concept_ids are specified,
    rows returned must match both.
  :param cohort_statuses: a list of CohortStatus indicating a filter on the review status of 
    participants to be returned in the resulting data table; defaults to 
    `['INCLUDED', 'NEEDS_FURTHER_REVIEW', 'NOT_REVIEWED']` (not excluded).
  :param max_results: the maximum number of rows to return in the resulting data table; defaults
    to no limit (all matching rows will be returned.) Note that for large cohorts, it may take a 
    long time to get all results.
  :param order_by: a list of column names from the table or related tables to order the results by,
    any of which can be optionally wrapped in `DESCENDING()` to request descending sort order; 
    defaults to order by person_id and primary key of the specified table; e.g. 
    [Person.gender_concept_id, Person.person_id]
  :param debug: true if debug request and response information should be displayed; defaults to 
    false.  
  :return a Pandas data frame representing the results of the query
"""
def load_data(cohort_name, table, columns=None, concept_set_name=None, concept_ids=None,
              concept_id_column=None, source_concept_ids=None, filters=None,
              cohort_statuses=None, max_results=None,
              order_by=None, debug=False):
    all_filters = filters
    concept_filters = []
    if concept_ids:
        if concept_id_column:
            standard_concept_id_column = concept_id_column
        else:
            standard_concept_id_column = getattr(table, 'standard_concept_id_column')
            if not standard_concept_id_column:
                raise "Could not find standard concept id column for table " + table.table_name
        column_filter = ColumnFilter(column_name=standard_concept_id_column,
                                     value_numbers=concept_ids,
                                     operator=Operator.IN)
        concept_filters.append(ResultFilters(column_filter=column_filter))
    if source_concept_ids:
        source_concept_id_column = getattr(table, 'source_concept_id_column')
        if not source_concept_id_column:
            raise "Could not find source concept id column for table " + table.table_name
        column_filter = ColumnFilter(column_name=source_concept_id_column,
                                     value_numbers=source_concept_ids,
                                     operator=Operator.IN)
        concept_filters.append(ResultFilters(column_filter=column_filter))

    # If both standard and source concept ids are provided, match either.
    if concept_filters:
        concept_result_filters = None
        if len(concept_filters) == 1:
            concept_result_filters = concept_filters[0]
        else:
            concept_result_filters = ResultFilters(any_of=concept_filters)

        if all_filters:
            all_filters = ResultFilters(all_of=[all_filters, concept_result_filters])
        else:
            # If concept ids and other filters are provided, match both.
            all_filters = concept_result_filters

    table_query = TableQuery(table=table, columns=columns, concept_set_name=concept_set_name,
                             filters=all_filters, order_by=order_by)
    data_table_specification = DataTableSpecification(cohort_name=cohort_name,
                                                      table_query=table_query,
                                                      status_filter=cohort_statuses,
                                                      max_results=max_results)

    cdr_query = get_data_table_query(data_table_specification, debug=debug)
    if not cdr_query.sql:
      return pd.DataFrame(columns=cdr_query.columns)
    df = pd.read_gbq(query=cdr_query.sql,
                     project_id=all_of_us_config.billing_cloud_project,
                     configuration=cdr_query.configuration)
    df.columns = cdr_query.columns
    return df


"""
Loads annotations for reviewed participants for the specified cohort. 
:param cohort_name: the name of a cohort in the workspace that contains the calling notebook
:param columns: list of `'person_id'`, `'review_status'`, or names of annotations 
    defined on the cohort. Defaults to `['person_id', 'review_status', <all defined annotation names>]`.
:param cohort_statuses: A list of CohortStatus indicating a filter on the review status of participants 
    to be returned in the resulting data table; defaults to 
    `['INCLUDED', 'NEEDS_FURTHER_REVIEW', 'NOT_REVIEWED']` (not excluded).
:param order_by: A list of `'person_id'`, `'review_status'`, or names of annotations 
    defined on the cohort, any of which can optionally be wrapped in `DESCENDING()` 
    to request descending sort order. Defaults to `['person_id']`. 
    Any annotations in `order_by` must also be present in `columns` (if `columns` is specified.)
:param debug: true if debug request and response information should be displayed; defaults to 
    false.  
:return a Pandas data frame representing the annotations. If no review exists or no
    participants match the statuses above, an empty data frame is returned.    
"""
def load_annotations(cohort_name, columns=None, cohort_statuses=None,
                     order_by=None, debug=False):
    annotation_query = AnnotationQuery(columns=columns, order_by=order_by)
    request = CohortAnnotationsRequest(cohort_name=cohort_name,
                                     status_filter=cohort_statuses,
                                     annotation_query=annotation_query)
    response = get_cohort_annotations(request, debug=debug)
    return pd.DataFrame(response.results, columns=response.columns)
