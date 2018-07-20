import unittest
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.cohorts import materialize_cohort_page, materialize_cohort
from aou_workbench_client.swagger_client.models import MaterializeCohortRequest
from aou_workbench_client.swagger_client.models import TableQuery, FieldSet
from aou_workbench_client.cdr.model import Person

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
    
    def test_materialize_cohort_table_query(self):
        table_query = TableQuery(table=Person, columns=[Person.person_id])
        field_set = FieldSet(table_query=table_query)      
        request = MaterializeCohortRequest(cohort_name='Old Men', page_size=10,
                                           field_set=field_set)
        results = list(materialize_cohort(request, max_results=10))
        self.assertEqual(10, len(results))
      
        table_query = TableQuery(table_name=Person.table_name, columns=[Person.person_id])
        field_set = FieldSet(table_query=table_query)      
        request = MaterializeCohortRequest(cohort_name='Old Men', page_size=10,
                                           field_set=field_set)
        results = list(materialize_cohort(request, max_results=10))
        self.assertEqual(10, len(results))

      
    def test_materialize_cohort(self):
        request = MaterializeCohortRequest(cohort_name='Old Men', page_size=10)
        results = list(materialize_cohort(request, max_results=20))
        self.assertEqual(20, len(results))   
        
    def test_load_data_table(self):
        response = load_data_table(cohort_name='Old Men', table=Person,
                                   columns=[Person.person_id],
                                   page_size=10, max_results=10)
        self.assertEqual(10, len(list(response)))
      
      
