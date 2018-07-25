from aou_workbench_client.swagger_client.models.materialize_cohort_request import MaterializeCohortRequest
from aou_workbench_client.swagger_client.models.table_query import TableQuery
from aou_workbench_client.swagger_client.models.field_set import FieldSet
from aou_workbench_client.swagger_client.models.column_filter import ColumnFilter
from aou_workbench_client.swagger_client.models.operator import Operator
from aou_workbench_client.swagger_client.models.result_filters import ResultFilters
from aou_workbench_client.swagger_client.models.annotation_query import AnnotationQuery
from aou_workbench_client.swagger_client.cohorts import materialize_cohort

def load_data_table(cohort_name, table, columns=None, concept_ids=None,
                    source_concept_ids=None, filters=None,
                    cohort_statuses=None, max_results=None,
                    order_by=None, page_size=None):
  all_filters = filters
  concept_filters = []
  if concept_ids:
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
    
  if concept_filters:
    concept_result_filters = None    
    if len(concept_filters) == 1:
      concept_result_filters = concept_filters[0]
    else:
      # If standard and source concept ids are provided, match either.
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
                                     table_query=table_query,
                                     page_size=page_size)
  return materialize_cohort(request, max_results=max_results)
  