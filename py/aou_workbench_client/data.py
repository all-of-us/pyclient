from aou_workbench_client.swagger_client.models.materialize_cohort_request import \
    MaterializeCohortRequest
from aou_workbench_client.swagger_client.models.table_query import TableQuery
from aou_workbench_client.swagger_client.models.field_set import FieldSet
from aou_workbench_client.swagger_client.models.column_filter import ColumnFilter
from aou_workbench_client.swagger_client.models.operator import Operator
from aou_workbench_client.swagger_client.models.result_filters import ResultFilters
from aou_workbench_client.cohorts import materialize_cohort

import pandas as pd

class ResultTypes(object):
  GENERATOR = "generator"
  LIST = "list"
  DATA_FRAME = "dataframe"

"""
Loads a data table for participants in a specified cohort.

  :param cohort_name: the name of a cohort in the workspace that contains the calling notebook
  :param table: the class corresponding to the table that the data table should be extracted 
    from, pulled from aou_workbench_client.cdr.model; e.g. aou_workbench_client.cdr.model.Person
  :param columns: a list of column names from the table or related tables to return in the data table; 
    defaults to all columns in the table (and no columns in related tables); 
    e.g. [Person.person_id, Person.gender_concept_id]
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
    filters and concept_ids / source_concept_ids are specified,
    rows returned must match both.
  :param cohort_statuses: a list of CohortStatus indicating a filter on the review status of 
    participants to be returned in the resulting data table; defaults to no filtering (all 
    participants are returned.
  :param max_results: the maximum number of rows to return in the resulting data table; defaults
    to no limit (all matching rows will be returned.) Note that for large cohorts, it may take a 
    long time to get all results.
  :param order_by: a list of column names from the table or related tables to order the results by; 
    defaults to order by person_id and primary key of the specified table; e.g. 
    [Person.gender_concept_id, Person.person_id]
  :param page_size: the maximum number of result rows to fetch in a single API request when 
    retrieving results; defaults to 1000.
  :param result_type: a string indicating the type of results to return; options are
    ResultTypes.GENERATOR (a generator of results that makes API calls as needed), 
    ResultTypes.LIST (all of the results loaded into memory), 
    and ResultTypes.DATA_FRAME (a Pandas data frame containing all of the results 
    in memory.) Defaults to ResultTypes.DATA_FRAME.    
  :param debug: true if debug request and response information should be displayed; defaults to 
    false.  
"""
def load_data_table(cohort_name, table, columns=None, concept_ids=None,
                    concept_id_column=None, source_concept_ids=None, filters=None,
                    cohort_statuses=None, max_results=None,
                    order_by=None, page_size=None, result_type=ResultTypes.DATA_FRAME,
                    debug=False):
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

    table_query = TableQuery(table=table, columns=columns, filters=all_filters,
                             order_by=order_by)
    field_set = FieldSet(table_query)
    request = MaterializeCohortRequest(cohort_name=cohort_name,
                                       field_set=field_set,
                                       status_filter=cohort_statuses,
                                       page_size=page_size)
    generator = materialize_cohort(request, max_results=max_results, debug=debug)
    if result_type == ResultTypes.GENERATOR:
        return generator
    if result_type == ResultTypes.LIST:
        return list(generator)
    if result_type == ResultTypes.DATA_FRAME:
        return pd.DataFrame(list(generator))
    raise "Invalid result type: %s" % result_type
