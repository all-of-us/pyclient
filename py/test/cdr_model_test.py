import unittest

from aou_workbench_client.cdr.model import table_columns, cohort_tables
from aou_workbench_client.cdr.model import Person, print_cdr_schema

class CdrModelTest(unittest.TestCase):

    def test_model(self):
        self.assertEquals('person_id', Person.columns['Name'][0])
        self.assertEquals('gender_concept', Person.foreign_keys[0])
        self.assertTrue(table_columns['Person'].equals(Person.columns))
        self.assertEquals('ConditionOccurrence', cohort_tables[0])
        print_cdr_schema()
        
        
