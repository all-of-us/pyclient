import unittest

from aou_workbench_client.cdr.model import table_columns, cohort_tables
from aou_workbench_client.cdr.model import Person, display_cdr_schema

class CdrModelTest(unittest.TestCase):

    def test_model(self):
        self.assertEquals('person_id', Person.columns['Name'][0])
        self.assertEquals('gender_concept', Person.foreign_keys[0])
        self.assertTrue(table_columns['Person'].equals(Person.columns))
        self.assertEquals('ConditionOccurrence', cohort_tables[0])
        display_cdr_schema()
        
    def test_related_table_wrappers(self):
      self.assertEquals('care_site.location_id', Person.care_site.location_id)
      self.assertEquals('care_site.location.city', Person.care_site.location.city)
      self.assertTrue('care_site' in dir(Person))
      self.assertTrue('location' in dir(Person.care_site))
      self.assertTrue('city' in dir(Person.care_site.location))
