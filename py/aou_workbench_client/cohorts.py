from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.cohorts_api import CohortsApi

def materialize_cohort_page(request):
    """Materializes a cohort in the workspace containing this notebook, based
    on the provided MateralizedCohortRequest."""
    client = get_authenticated_swagger_client()
    cohorts_api = CohortsApi(api_client=client)
    return cohorts_api.materialize_cohort(all_of_us_config.workspace_namespace,
                                          all_of_us_config.workspace_id,
                                          request=request)

def materialize_cohort(request, max_results=None):
    """Materializes a cohort in the workspace containing this notebook, based
    on the provided MateralizedCohortRequest."""
    client = get_authenticated_swagger_client()
    cohorts_api = CohortsApi(api_client=client)
    num_results = 0
    while True:
      response = cohorts_api.materialize_cohort(all_of_us_config.workspace_namespace,
                                                all_of_us_config.workspace_id,
                                                request=request)
      for result in response.results:
        yield result
        num_results += 1
        if max_results and num_results >= max_results:
          return
      if response.next_page_token:
        request.page_token = response.next_page_token
      else:
        return
