import unittest
from aou_workbench_client.cdr.model import Person
from aou_workbench_client.data import load_data_frame
import pandas as pd

class CohortsApiTest(unittest.TestCase):

    def test_load_data_frame(self):
        df = load_data_frame(cohort_name='Old Men', table=Person,
                             columns=[Person.person_id, Person.gender_concept.concept_id],
                             max_results=10)
        expected = pd.DataFrame({'person_id':
                                   [17, 205, 269, 277, 380, 390, 444, 675, 814, 990],
                                 'gender_concept.concept_id':
                                   [8507, 8507, 8507, 8507, 8507, 8507, 8507, 8507, 8507, 8507]},
                                columns=['person_id', 'gender_concept.concept_id'])
        pd.testing.assert_frame_equal(expected, df)



      
      
