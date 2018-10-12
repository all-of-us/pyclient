import unittest
from aou_workbench_client.cdr.model import Person
from aou_workbench_client.data import load_annotations, load_data
from aou_workbench_client.swagger_client.models.cohort_status import CohortStatus
import pandas as pd

class CohortsApiTest(unittest.TestCase):

    def test_load_data(self):
        df = load_data(cohort_name='Old Men', table=Person,
                             columns=[Person.person_id, Person.gender_concept.concept_id],
                             max_results=10)
        expected = pd.DataFrame({'person_id':
                                   [17, 269, 277, 380, 390, 444, 675, 814, 990, 1012],
                                 'gender_concept.concept_id':
                                   [8507, 8507, 8507, 8507, 8507, 8507, 8507, 8507, 8507, 8507]},
                                columns=['person_id', 'gender_concept.concept_id'])
        pd.testing.assert_frame_equal(expected, df)

    def test_load_annotations(self):
        df = load_annotations(cohort_name='Old Men',
                              cohort_statuses=[CohortStatus.INCLUDED, CohortStatus.NEEDS_FURTHER_REVIEW])
        expected = pd.DataFrame({'person_id': [17, 269],
                                 'review_status': ['INCLUDED', 'NEEDS_FURTHER_REVIEW'],
                                 'boolean annotation': [1, 1],
                                 'date annotation': ['2018-10-09', None],
                                 'enum annotation': ['A', None],
                                 'integer annotation': [123, 789],
                                 'text annotation': ['blah blah', 'Needs further review!']},
                                columns=['person_id', 'review_status', 'boolean annotation',
                                         'date annotation', 'enum annotation', 'integer annotation',
                                         'text annotation'])
        pd.testing.assert_frame_equal(expected, df)
      
      
