import unittest

from aou_workbench_client.cdr.model import table_columns, cohort_tables
from aou_workbench_client.cdr.model import Person

class CdrModelTest(unittest.TestCase):

    def test_column_names(self):
        self.assertEquals('person_id', Person.columns['Name'][0])
        self.assertTrue(table_columns['Person'].equals(Person.columns))
        self.assertEquals('ConditionOccurrence', cohort_tables[0])
        
