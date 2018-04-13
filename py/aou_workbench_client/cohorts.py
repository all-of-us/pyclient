from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.cohorts_api import CohortsApi
from copy import deepcopy

def materialize_cohort_page(request):
    """Returns a MaterializeCohortResponse representing a page of results 
    from materializing a cohort in the workspace containing this notebook, based
    on the provided MateralizeCohortRequest."""
    client = get_authenticated_swagger_client()
    cohorts_api = CohortsApi(api_client=client)
    return cohorts_api.materialize_cohort(all_of_us_config.workspace_namespace,
                                          all_of_us_config.workspace_id,
                                          request=request)

def materialize_cohort(request, max_results=None):
    """Materializes a cohort in the workspace containing this notebook, based
    on the provided MateralizeCohortRequest. Returns a generator of 
    dictionaries containing the results.
    
    If max_results is specified, up to that many results will be returned; 
    if not, all available results will be returned. 
    
    Multiple server requests may be made to retrieve all the results,
    using the page_size specified in the request for each request."""
    client = get_authenticated_swagger_client()
    cohorts_api = CohortsApi(api_client=client)
    num_results = 0
    # Clone the request, since we're going to be modifying it.
    request = deepcopy(request)    
    page_size = request.page_size or 1000
    while True:
      if max_results and (max_results - num_results) < request.page_size:
        request.page_size = max_results - num_results   
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
