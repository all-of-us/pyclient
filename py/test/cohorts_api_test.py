import unittest
from aou_workbench_client.cdr.model import Person
from aou_workbench_client.data import load_annotations, load_data
from aou_workbench_client.swagger_client.models.cohort_status import CohortStatus
import pandas as pd

class CohortsApiTest(unittest.TestCase):
    """Cohorts API tests.

    These tests use live golden data in the test environment. See
    all_of_us_config.json for workspace details. In the event that this data
    needs to be updated, either get access from a team member or recreate the
    workspace/cohort.

    The default GAE service account which is used for testing has automatic
    access to all workspaces, which is how this test is able to execute.
    """

    def test_load_data(self):
        df = load_data(cohort_name='diabetes cases', table=Person,
                             columns=[Person.person_id, Person.gender_concept.concept_id],
                             max_results=10)
        self.assertEqual((10, 2), df.shape)

    def test_load_annotations(self):
        df = load_annotations(cohort_name='diabetes cases',
                              cohort_statuses=[CohortStatus.INCLUDED, CohortStatus.NEEDS_FURTHER_REVIEW])
        expected = pd.DataFrame({'person_id': [5, 6],
                                 'review_status': ['INCLUDED', 'NEEDS_FURTHER_REVIEW'],
                                 'bool anno': [1, 1],
                                 'date anno': [None, '2018-10-09'],
                                 'enum anno': [None, 'A'],
                                 'int anno': [789, 123],
                                 'text anno': ['XD', 'blah blah']},
                                columns=['person_id', 'review_status', 'bool anno',
                                         'date anno', 'enum anno', 'int anno',
                                         'text anno'])
        pd.testing.assert_frame_equal(expected, df)
