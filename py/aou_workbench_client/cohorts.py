from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.cohorts_api import CohortsApi

def get_data_table_query(data_table_specification, debug=False):
    """Returns a CdrQuery that can be used to retrieve data from BigQuery for the
    specified data table specification.

    :param data_table_specification: the DataTableSpecification to get the query for
    :param debug: true if debug request and response information should be
    displayed; defaults to false.
    :return a query with the SQL and configuration to use when retrieving data
    from BigQuery. If SQL is not present in the response, the specification
    matches no participants and there is no need to run a query against BigQuery;
    the resulting data should be empty.
    """
    client = get_authenticated_swagger_client(debug=debug)
    cohorts_api = CohortsApi(api_client=client)
    return cohorts_api.get_data_table_query(all_of_us_config.workspace_namespace,
                                            all_of_us_config.workspace_id,
                                            request=data_table_specification)


def get_cohort_annotations(cohort_annotations_request, debug=False):
    """Returns a CohortAnnotationsResponse for the requested annotations for
    participants reviewed in a cohort.
    :param cohort_annotations_request: the CohortAnnotationsRequest specifying
    what annotations to retrieve for what cohort.
    :param debug: true if debug request and response information should be
    displayed; defaults to false.
    :return a CohortAnnotationsResponse with a list of dictionaries; each
    dictionary represents the requested annotations for a single participant.
    If no dictionaries are present in the response, there are no annotations
    present.
    """
    client = get_authenticated_swagger_client(debug=debug)
    cohorts_api = CohortsApi(api_client=client)
    return cohorts_api.get_cohort_annotations(all_of_us_config.workspace_namespace,
                                          all_of_us_config.workspace_id,
                                          request=cohort_annotations_request)
