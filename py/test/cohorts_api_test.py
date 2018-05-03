import unittest
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.cohorts import materialize_cohort_page, materialize_cohort
from aou_workbench_client.swagger_client.models import MaterializeCohortRequest

class CohortsApiTest(unittest.TestCase):

    def test_materialize_cohort_page(self):
      request = MaterializeCohortRequest(cohort_name='Old Men', page_size=10)
      response = materialize_cohort_page(request)
      self.assertEqual(10, len(response.results))
      self.assertIsNotNone(response.next_page_token)
      
      # Grab the next page
      request.page_token = response.next_page_token
      response_2 = materialize_cohort_page(request)
      self.assertEqual(10, len(response_2.results))
      self.assertIsNotNone(response_2.next_page_token)
      self.assertNotEqual(response_2.results, response.results)
      
    def test_materialize_cohort(self):
      request = MaterializeCohortRequest(cohort_name='Old Men', page_size=10)
      results = list(materialize_cohort(request, max_results=20))
      self.assertEqual(20, len(results))      
      
      
