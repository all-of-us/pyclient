#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Model objects containing metadata on the tables and columns in the 
curated data repository. These were automatically generated from the schema 
found at https://raw.githubusercontent.com/all-of-us/workbench/master/api/config/cdm/cdm_5_2.json.
"""

from .wrapper import RelatedTableWrapper
import pandas as pd
table_columns = {}
cohort_tables = []

###### Table classes 
class CareSite(object):
  care_site_id = "care_site_id"
  care_site_name = "care_site_name"
  place_of_service_concept_id = "place_of_service_concept_id"
  location_id = "location_id"
  care_site_source_value = "care_site_source_value"
  place_of_service_source_value = "place_of_service_source_value"
  table_name = "care_site"
  columns = pd.DataFrame([{"Name": "care_site_id", "Type": "integer", "Description": "A unique identifier for each Care Site."},{"Name": "care_site_name", "Type": "string", "Description": "The verbatim description or name of the Care Site as in data source"},{"Name": "place_of_service_concept_id", "Type": "integer", "Description": "A foreign key that refers to a Place of Service Concept ID in the Standardized Vocabularies."},{"Name": "location_id", "Type": "integer", "Description": "A foreign key to the geographic Location in the LOCATION table, where the detailed address information is stored."},{"Name": "care_site_source_value", "Type": "string", "Description": "The identifier for the Care Site in the source data, stored here for reference."},{"Name": "place_of_service_source_value", "Type": "string", "Description": "The source code for the Place of Service as it appears in the source data, stored here for reference."}],
        columns=["Name", "Type", "Description"])
  table_columns["CareSite"] = columns

class Concept(object):
  concept_id = "concept_id"
  concept_name = "concept_name"
  domain_id = "domain_id"
  vocabulary_id = "vocabulary_id"
  concept_class_id = "concept_class_id"
  standard_concept = "standard_concept"
  concept_code = "concept_code"
  valid_start_date = "valid_start_date"
  valid_end_date = "valid_end_date"
  invalid_reason = "invalid_reason"
  table_name = "concept"
  columns = pd.DataFrame([{"Name": "concept_id", "Type": "integer", "Description": "A unique identifier for each Concept across all domains."},{"Name": "concept_name", "Type": "string", "Description": "An unambiguous, meaningful and descriptive name for the Concept."},{"Name": "domain_id", "Type": "string", "Description": "A foreign key to the [DOMAIN](https://github.com/OHDSI/CommonDataModel/wiki/DOMAIN) table the Concept belongs to."},{"Name": "vocabulary_id", "Type": "string", "Description": "A foreign key to the [VOCABULARY](https://github.com/OHDSI/CommonDataModel/wiki/VOCABULARY) table indicating from which source the Concept has been adapted."},{"Name": "concept_class_id", "Type": "string", "Description": "The attribute or concept class of the Concept. Examples are 'Clinical Drug', 'Ingredient', 'Clinical Finding' etc."},{"Name": "standard_concept", "Type": "string", "Description": "This flag determines where a Concept is a Standard Concept, i.e. is used in the data, a Classification Concept, or a non-standard Source Concept. The allowables values are 'S' (Standard Concept) and 'C' (Classification Concept), otherwise the content is NULL."},{"Name": "concept_code", "Type": "string", "Description": "The concept code represents the identifier of the Concept in the source vocabulary, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies."},{"Name": "valid_start_date", "Type": "date", "Description": "The date when the Concept was first recorded. The default value is 1-Jan-1970, meaning, the Concept has no (known) date of inception."},{"Name": "valid_end_date", "Type": "date", "Description": "The date when the Concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099, meaning, the Concept is valid until it becomes deprecated."},{"Name": "invalid_reason", "Type": "string", "Description": "Reason the Concept was invalidated. Possible values are D (deleted), U (replaced with an update) or NULL when valid_end_date has the default value."}],
        columns=["Name", "Type", "Description"])
  table_columns["Concept"] = columns

class Domain(object):
  domain_id = "domain_id"
  domain_name = "domain_name"
  domain_concept_id = "domain_concept_id"
  table_name = "domain"
  columns = pd.DataFrame([{"Name": "domain_id", "Type": "string", "Description": "A unique key for each domain."},{"Name": "domain_name", "Type": "string", "Description": "The name describing the Domain, e.g. \"Condition\", \"Procedure\", \"Measurement\" etc."},{"Name": "domain_concept_id", "Type": "integer", "Description": "A foreign key that refers to an identifier in the [CONCEPT](https://github.com/OHDSI/CommonDataModel/wiki/CONCEPT) table for the unique Domain Concept the Domain record belongs to."}],
        columns=["Name", "Type", "Description"])
  table_columns["Domain"] = columns

class Location(object):
  location_id = "location_id"
  address_1 = "address_1"
  address_2 = "address_2"
  city = "city"
  state = "state"
  zip = "zip"
  county = "county"
  location_source_value = "location_source_value"
  table_name = "location"
  columns = pd.DataFrame([{"Name": "location_id", "Type": "integer", "Description": "A unique identifier for each geographic location."},{"Name": "address_1", "Type": "string", "Description": "The address field 1, typically used for the street address, as it appears in the source data."},{"Name": "address_2", "Type": "string", "Description": "The address field 2, typically used for additional detail such as buildings, suites, floors, as it appears in the source data."},{"Name": "city", "Type": "string", "Description": "The city field as it appears in the source data."},{"Name": "state", "Type": "string", "Description": "The state field as it appears in the source data."},{"Name": "zip", "Type": "string", "Description": "The zip or postal code."},{"Name": "county", "Type": "string", "Description": "The county."},{"Name": "location_source_value", "Type": "string", "Description": "The verbatim information that is used to uniquely identify the location as it appears in the source data."}],
        columns=["Name", "Type", "Description"])
  table_columns["Location"] = columns

class Provider(object):
  provider_id = "provider_id"
  provider_name = "provider_name"
  NPI = "NPI"
  DEA = "DEA"
  specialty_concept_id = "specialty_concept_id"
  care_site_id = "care_site_id"
  year_of_birth = "year_of_birth"
  gender_concept_id = "gender_concept_id"
  provider_source_value = "provider_source_value"
  specialty_source_value = "specialty_source_value"
  specialty_source_concept_id = "specialty_source_concept_id"
  gender_source_value = "gender_source_value"
  gender_source_concept_id = "gender_source_concept_id"
  table_name = "provider"
  columns = pd.DataFrame([{"Name": "provider_id", "Type": "integer", "Description": "A unique identifier for each Provider."},{"Name": "provider_name", "Type": "string", "Description": "A description of the Provider."},{"Name": "NPI", "Type": "string", "Description": ""},{"Name": "DEA", "Type": "string", "Description": ""},{"Name": "specialty_concept_id", "Type": "integer", "Description": "A foreign key to a Standard Specialty Concept ID in the Standardized Vocabularies."},{"Name": "care_site_id", "Type": "integer", "Description": "A foreign key to the main Care Site where the provider is practicing."},{"Name": "year_of_birth", "Type": "integer", "Description": "The year of birth of the Provider."},{"Name": "gender_concept_id", "Type": "integer", "Description": "The gender of the Provider."},{"Name": "provider_source_value", "Type": "string", "Description": "The identifier used for the Provider in the source data, stored here for reference."},{"Name": "specialty_source_value", "Type": "string", "Description": "The source code for the Provider specialty as it appears in the source data, stored here for reference."},{"Name": "specialty_source_concept_id", "Type": "integer", "Description": "A foreign key to a Concept that refers to the code used in the source."},{"Name": "gender_source_value", "Type": "string", "Description": "The gender code for the Provider as it appears in the source data, stored here for reference."},{"Name": "gender_source_concept_id", "Type": "integer", "Description": "A foreign key to a Concept that refers to the code used in the source."}],
        columns=["Name", "Type", "Description"])
  table_columns["Provider"] = columns

class Vocabulary(object):
  vocabulary_id = "vocabulary_id"
  vocabulary_name = "vocabulary_name"
  vocabulary_reference = "vocabulary_reference"
  vocabulary_version = "vocabulary_version"
  vocabulary_concept_id = "vocabulary_concept_id"
  table_name = "vocabulary"
  columns = pd.DataFrame([{"Name": "vocabulary_id", "Type": "string", "Description": "A unique identifier for each Vocabulary, such as ICD9CM, SNOMED, Visit."},{"Name": "vocabulary_name", "Type": "string", "Description": "The name describing the vocabulary, for example \"International Classification of Diseases, Ninth Revision, Clinical Modification, Volume 1 and 2 (NCHS)\" etc."},{"Name": "vocabulary_reference", "Type": "string", "Description": "External reference to documentation or available download of the about the vocabulary."},{"Name": "vocabulary_version", "Type": "string", "Description": "Version of the Vocabulary as indicated in the source."},{"Name": "vocabulary_concept_id", "Type": "integer", "Description": "A foreign key that refers to a standard concept identifier in the CONCEPT table for the Vocabulary the VOCABULARY record belongs to."}],
        columns=["Name", "Type", "Description"])
  table_columns["Vocabulary"] = columns

class ConditionOccurrence(object):
  condition_occurrence_id = "condition_occurrence_id"
  person_id = "person_id"
  condition_concept_id = "condition_concept_id"
  condition_start_date = "condition_start_date"
  condition_start_datetime = "condition_start_datetime"
  condition_end_date = "condition_end_date"
  condition_end_datetime = "condition_end_datetime"
  condition_type_concept_id = "condition_type_concept_id"
  stop_reason = "stop_reason"
  provider_id = "provider_id"
  visit_occurrence_id = "visit_occurrence_id"
  condition_source_value = "condition_source_value"
  condition_source_concept_id = "condition_source_concept_id"
  condition_status_source_value = "condition_status_source_value"
  condition_status_concept_id = "condition_status_concept_id"
  table_name = "condition_occurrence"
  columns = pd.DataFrame([{"Name": "condition_occurrence_id", "Type": "integer", "Description": "A unique identifier for each Condition Occurrence event."},{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the Person who is experiencing the condition. The demographic details of that Person are stored in the PERSON table."},{"Name": "condition_concept_id", "Type": "integer", "Description": "A foreign key that refers to a Standard Condition Concept identifier in the Standardized Vocabularies."},{"Name": "condition_start_date", "Type": "date", "Description": "The date when the instance of the Condition is recorded."},{"Name": "condition_start_datetime", "Type": "timestamp", "Description": "The date and time when the instance of the Condition is recorded."},{"Name": "condition_end_date", "Type": "date", "Description": "The date when the instance of the Condition is considered to have ended."},{"Name": "condition_end_datetime", "Type": "timestamp", "Description": "The date when the instance of the Condition is considered to have ended."},{"Name": "condition_type_concept_id", "Type": "integer", "Description": "A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the source data from which the condition was recorded, the level of standardization, and the type of occurrence."},{"Name": "stop_reason", "Type": "string", "Description": "The reason that the condition was no longer present, as indicated in the source data."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the Provider in the PROVIDER table who was responsible for capturing (diagnosing) the Condition."},{"Name": "visit_occurrence_id", "Type": "integer", "Description": "A foreign key to the visit in the VISIT_OCCURRENCE table during which the Condition was determined (diagnosed)."},{"Name": "condition_source_value", "Type": "string", "Description": "The source code for the condition as it appears in the source data. This code is mapped to a standard condition concept in the Standardized Vocabularies and the original code is stored here for reference."},{"Name": "condition_source_concept_id", "Type": "integer", "Description": "A foreign key to a Condition Concept that refers to the code used in the source."},{"Name": "condition_status_source_value", "Type": "string", "Description": "The source code for the condition status as it appears in the source data."},{"Name": "condition_status_concept_id", "Type": "integer", "Description": "A foreign key to the predefined Concept in the Standard Vocabulary reflecting the condition status"}],
        columns=["Name", "Type", "Description"])
  table_columns["ConditionOccurrence"] = columns
  cohort_tables.append("ConditionOccurrence")

class Death(object):
  person_id = "person_id"
  death_date = "death_date"
  death_datetime = "death_datetime"
  death_type_concept_id = "death_type_concept_id"
  cause_concept_id = "cause_concept_id"
  cause_source_value = "cause_source_value"
  cause_source_concept_id = "cause_source_concept_id"
  table_name = "death"
  columns = pd.DataFrame([{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the deceased person. The demographic details of that person are stored in the person table."},{"Name": "death_date", "Type": "date", "Description": "The date the person was deceased. If the precise date including day or month is not known or not allowed, December is used as the default month, and the last day of the month the default day."},{"Name": "death_datetime", "Type": "timestamp", "Description": "The date and time the person was deceased. If the precise date including day or month is not known or not allowed, December is used as the default month, and the last day of the month the default day."},{"Name": "death_type_concept_id", "Type": "integer", "Description": "A foreign key referring to the predefined concept identifier in the Standardized Vocabularies reflecting how the death was represented in the source data."},{"Name": "cause_concept_id", "Type": "integer", "Description": "A foreign key referring to a standard concept identifier in the Standardized Vocabularies for conditions."},{"Name": "cause_source_value", "Type": "string", "Description": "The source code for the cause of death as it appears in the source data. This code is mapped to a standard concept in the Standardized Vocabularies and the original code is, stored here for reference."},{"Name": "cause_source_concept_id", "Type": "integer", "Description": "A foreign key to the concept that refers to the code used in the source. Note, this variable name is abbreviated to ensure it will be allowable across database platforms."}],
        columns=["Name", "Type", "Description"])
  table_columns["Death"] = columns
  cohort_tables.append("Death")

class DeviceExposure(object):
  device_exposure_id = "device_exposure_id"
  person_id = "person_id"
  device_concept_id = "device_concept_id"
  device_exposure_start_date = "device_exposure_start_date"
  device_exposure_start_datetime = "device_exposure_start_datetime"
  device_exposure_end_date = "device_exposure_end_date"
  device_exposure_end_datetime = "device_exposure_end_datetime"
  device_type_concept_id = "device_type_concept_id"
  unique_device_id = "unique_device_id"
  quantity = "quantity"
  provider_id = "provider_id"
  visit_occurrence_id = "visit_occurrence_id"
  device_source_value = "device_source_value"
  device_source_concept_id = "device_source_concept_id"
  table_name = "device_exposure"
  columns = pd.DataFrame([{"Name": "device_exposure_id", "Type": "integer", "Description": "A system-generated unique identifier for each Device Exposure."},{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the Person who is subjected to the Device. The demographic details of that person are stored in the Person table."},{"Name": "device_concept_id", "Type": "integer", "Description": "A foreign key that refers to a Standard Concept identifier in the Standardized Vocabularies for the Device concept."},{"Name": "device_exposure_start_date", "Type": "date", "Description": "The date the Device or supply was applied or used."},{"Name": "device_exposure_start_datetime", "Type": "timestamp", "Description": "The date and time the Device or supply was applied or used."},{"Name": "device_exposure_end_date", "Type": "date", "Description": "The date the Device or supply was removed from use."},{"Name": "device_exposure_end_datetime", "Type": "timestamp", "Description": "The date and time the Device or supply was removed from use."},{"Name": "device_type_concept_id", "Type": "integer", "Description": "A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of Device Exposure recorded. It indicates how the Device Exposure was represented in the source data."},{"Name": "unique_device_id", "Type": "string", "Description": "A UDI or equivalent identifying the instance of the Device used in the Person."},{"Name": "quantity", "Type": "integer", "Description": "The number of individual Devices used for the exposure."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the provider in the PROVIDER table who initiated of administered the Device."},{"Name": "visit_occurrence_id", "Type": "integer", "Description": "A foreign key to the visit in the VISIT_OCCURRENCE table during which the device was used."},{"Name": "device_source_value", "Type": "string", "Description": "The source code for the Device as it appears in the source data. This code is mapped to a standard Device Concept in the Standardized Vocabularies and the original code is stored here for reference."},{"Name": "device_source_concept_id", "Type": "integer", "Description": ""}],
        columns=["Name", "Type", "Description"])
  table_columns["DeviceExposure"] = columns
  cohort_tables.append("DeviceExposure")

class DrugExposure(object):
  drug_exposure_id = "drug_exposure_id"
  person_id = "person_id"
  drug_concept_id = "drug_concept_id"
  drug_exposure_start_date = "drug_exposure_start_date"
  drug_exposure_start_datetime = "drug_exposure_start_datetime"
  drug_exposure_end_date = "drug_exposure_end_date"
  drug_exposure_end_datetime = "drug_exposure_end_datetime"
  verbatim_end_date = "verbatim_end_date"
  drug_type_concept_id = "drug_type_concept_id"
  stop_reason = "stop_reason"
  refills = "refills"
  quantity = "quantity"
  days_supply = "days_supply"
  sig = "sig"
  route_concept_id = "route_concept_id"
  lot_number = "lot_number"
  provider_id = "provider_id"
  visit_occurrence_id = "visit_occurrence_id"
  drug_source_value = "drug_source_value"
  drug_source_concept_id = "drug_source_concept_id"
  route_source_value = "route_source_value"
  dose_unit_source_value = "dose_unit_source_value"
  table_name = "drug_exposure"
  columns = pd.DataFrame([{"Name": "drug_exposure_id", "Type": "integer", "Description": "A system-generated unique identifier for each Drug utilization event."},{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the person who is subjected to the Drug. The demographic details of that person are stored in the person table."},{"Name": "drug_concept_id", "Type": "integer", "Description": "A foreign key that refers to a Standard Concept identifier in the Standardized Vocabularies for the Drug concept."},{"Name": "drug_exposure_start_date", "Type": "date", "Description": "The start date for the current instance of Drug utilization. Valid entries include a start date of a prescription, the date a prescription was filled, or the date on which a Drug administration procedure was recorded."},{"Name": "drug_exposure_start_datetime", "Type": "timestamp", "Description": "The start date and time for the current instance of Drug utilization. Valid entries include a start date of a prescription, the date a prescription was filled, or the date on which a Drug administration procedure was recorded."},{"Name": "drug_exposure_end_date", "Type": "date", "Description": "The end date for the current instance of Drug utilization. It is not available from all sources."},{"Name": "drug_exposure_end_datetime", "Type": "timestamp", "Description": "The end date and time for the current instance of Drug utilization. It is not available from all sources."},{"Name": "verbatim_end_date", "Type": "date", "Description": "The known end date of a drug_exposure as provided by the source"},{"Name": "drug_type_concept_id", "Type": "integer", "Description": "A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of Drug Exposure recorded. It indicates how the Drug Exposure was represented in the source data."},{"Name": "stop_reason", "Type": "string", "Description": "The reason the Drug was stopped. Reasons include regimen completed, changed, removed, etc."},{"Name": "refills", "Type": "integer", "Description": "The number of refills after the initial prescription. The initial prescription is not counted, values start with 0."},{"Name": "quantity", "Type": "float", "Description": "The quantity of drug as recorded in the original prescription or dispensing record."},{"Name": "days_supply", "Type": "integer", "Description": "The number of days of supply of the medication as recorded in the original prescription or dispensing record."},{"Name": "sig", "Type": "string", "Description": "The directions (\"signetur\") on the Drug prescription as recorded in the original prescription (and printed on the container) or dispensing record."},{"Name": "route_concept_id", "Type": "integer", "Description": "A foreign key to a predefined concept in the Standardized Vocabularies reflecting the route of administration."},{"Name": "lot_number", "Type": "string", "Description": "An identifier assigned to a particular quantity or lot of Drug product from the manufacturer."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the provider in the PROVIDER table who initiated (prescribed or administered) the Drug Exposure."},{"Name": "visit_occurrence_id", "Type": "integer", "Description": "A foreign key to the Visit in the VISIT_OCCURRENCE table during which the Drug Exposure was initiated."},{"Name": "drug_source_value", "Type": "string", "Description": "The source code for the Drug as it appears in the source data. This code is mapped to a Standard Drug concept in the Standardized Vocabularies and the original code is, stored here for reference."},{"Name": "drug_source_concept_id", "Type": "integer", "Description": "A foreign key to a Drug Concept that refers to the code used in the source."},{"Name": "route_source_value", "Type": "string", "Description": "The information about the route of administration as detailed in the source."},{"Name": "dose_unit_source_value", "Type": "string", "Description": "The information about the dose unit as detailed in the source."}],
        columns=["Name", "Type", "Description"])
  table_columns["DrugExposure"] = columns
  cohort_tables.append("DrugExposure")

class Measurement(object):
  measurement_id = "measurement_id"
  person_id = "person_id"
  measurement_concept_id = "measurement_concept_id"
  measurement_date = "measurement_date"
  measurement_datetime = "measurement_datetime"
  measurement_type_concept_id = "measurement_type_concept_id"
  operator_concept_id = "operator_concept_id"
  value_as_number = "value_as_number"
  value_as_concept_id = "value_as_concept_id"
  unit_concept_id = "unit_concept_id"
  range_low = "range_low"
  range_high = "range_high"
  provider_id = "provider_id"
  visit_occurrence_id = "visit_occurrence_id"
  measurement_source_value = "measurement_source_value"
  measurement_source_concept_id = "measurement_source_concept_id"
  unit_source_value = "unit_source_value"
  value_source_value = "value_source_value"
  table_name = "measurement"
  columns = pd.DataFrame([{"Name": "measurement_id", "Type": "integer", "Description": "A unique identifier for each Measurement."},{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the Person about whom the measurement was recorded. The demographic details of that Person are stored in the PERSON table."},{"Name": "measurement_concept_id", "Type": "integer", "Description": "A foreign key to the standard measurement concept identifier in the Standardized Vocabularies."},{"Name": "measurement_date", "Type": "date", "Description": "The date of the Measurement."},{"Name": "measurement_datetime", "Type": "timestamp", "Description": "The date and time of the Measurement. Some database systems don't have a datatype of time. To accomodate all temporal analyses, datatype datetime can be used (combining measurement_date and measurement_time [forum discussion](http://forums.ohdsi.org/t/date-time-and-datetime-problem-and-the-world-of-hours-and-1day/314))"},{"Name": "measurement_type_concept_id", "Type": "integer", "Description": "A foreign key to the predefined Concept in the Standardized Vocabularies reflecting the provenance from where the Measurement record was recorded."},{"Name": "operator_concept_id", "Type": "integer", "Description": "A foreign key identifier to the predefined Concept in the Standardized Vocabularies reflecting the mathematical operator that is applied to the value_as_number. Operators are <, <=, =, >=, >."},{"Name": "value_as_number", "Type": "float", "Description": "A Measurement result where the result is expressed as a numeric value."},{"Name": "value_as_concept_id", "Type": "integer", "Description": "A foreign key to a Measurement result represented as a Concept from the Standardized Vocabularies (e.g., positive/negative, present/absent, low/high, etc.)."},{"Name": "unit_concept_id", "Type": "integer", "Description": "A foreign key to a Standard Concept ID of Measurement Units in the Standardized Vocabularies."},{"Name": "range_low", "Type": "float", "Description": "The lower limit of the normal range of the Measurement result. The lower range is assumed to be of the same unit of measure as the Measurement value."},{"Name": "range_high", "Type": "float", "Description": "The upper limit of the normal range of the Measurement. The upper range is assumed to be of the same unit of measure as the Measurement value."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the provider in the PROVIDER table who was responsible for initiating or obtaining the measurement."},{"Name": "visit_occurrence_id", "Type": "integer", "Description": "A foreign key to the Visit in the VISIT_OCCURRENCE table during which the Measurement was recorded."},{"Name": "measurement_source_value", "Type": "string", "Description": "The Measurement name as it appears in the source data. This code is mapped to a Standard Concept in the Standardized Vocabularies and the original code is stored here for reference."},{"Name": "measurement_source_concept_id", "Type": "integer", "Description": "A foreign key to a Concept in the Standard Vocabularies that refers to the code used in the source."},{"Name": "unit_source_value", "Type": "string", "Description": "The source code for the unit as it appears in the source data. This code is mapped to a standard unit concept in the Standardized Vocabularies and the original code is stored here for reference."},{"Name": "value_source_value", "Type": "string", "Description": "The source value associated with the content of the value_as_number or value_as_concept_id as stored in the source data."}],
        columns=["Name", "Type", "Description"])
  table_columns["Measurement"] = columns
  cohort_tables.append("Measurement")

class Observation(object):
  observation_id = "observation_id"
  person_id = "person_id"
  observation_concept_id = "observation_concept_id"
  observation_date = "observation_date"
  observation_datetime = "observation_datetime"
  observation_type_concept_id = "observation_type_concept_id"
  value_as_number = "value_as_number"
  value_as_string = "value_as_string"
  value_as_concept_id = "value_as_concept_id"
  qualifier_concept_id = "qualifier_concept_id"
  unit_concept_id = "unit_concept_id"
  provider_id = "provider_id"
  visit_occurrence_id = "visit_occurrence_id"
  observation_source_value = "observation_source_value"
  observation_source_concept_id = "observation_source_concept_id"
  unit_source_value = "unit_source_value"
  qualifier_source_value = "qualifier_source_value"
  value_source_concept_id = "value_source_concept_id"
  value_source_value = "value_source_value"
  questionnaire_response_id = "questionnaire_response_id"
  table_name = "observation"
  columns = pd.DataFrame([{"Name": "observation_id", "Type": "integer", "Description": "A unique identifier for each observation."},{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the Person about whom the observation was recorded. The demographic details of that Person are stored in the PERSON table."},{"Name": "observation_concept_id", "Type": "integer", "Description": "A foreign key to the standard observation concept identifier in the Standardized Vocabularies."},{"Name": "observation_date", "Type": "date", "Description": "The date of the observation."},{"Name": "observation_datetime", "Type": "timestamp", "Description": "The date and time of the observation."},{"Name": "observation_type_concept_id", "Type": "integer", "Description": "A foreign key to the predefined concept identifier in the Standardized Vocabularies reflecting the type of the observation."},{"Name": "value_as_number", "Type": "float", "Description": "The observation result stored as a number. This is applicable to observations where the result is expressed as a numeric value."},{"Name": "value_as_string", "Type": "string", "Description": "The observation result stored as a string. This is applicable to observations where the result is expressed as verbatim text."},{"Name": "value_as_concept_id", "Type": "integer", "Description": "A foreign key to an observation result stored as a Concept ID. This is applicable to observations where the result can be expressed as a Standard Concept from the Standardized Vocabularies (e.g., positive/negative, present/absent, low/high, etc.)."},{"Name": "qualifier_concept_id", "Type": "integer", "Description": "A foreign key to a Standard Concept ID for a qualifier (e.g., severity of drug-drug interaction alert)"},{"Name": "unit_concept_id", "Type": "integer", "Description": "A foreign key to a Standard Concept ID of measurement units in the Standardized Vocabularies."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the provider in the PROVIDER table who was responsible for making the observation."},{"Name": "visit_occurrence_id", "Type": "integer", "Description": "A foreign key to the visit in the VISIT_OCCURRENCE table during which the observation was recorded."},{"Name": "observation_source_value", "Type": "string", "Description": "The observation code as it appears in the source data. This code is mapped to a Standard Concept in the Standardized Vocabularies and the original code is, stored here for reference."},{"Name": "observation_source_concept_id", "Type": "integer", "Description": "A foreign key to a Concept that refers to the code used in the source."},{"Name": "unit_source_value", "Type": "string", "Description": "The source code for the unit as it appears in the source data. This code is mapped to a standard unit concept in the Standardized Vocabularies and the original code is, stored here for reference."},{"Name": "qualifier_source_value", "Type": "string", "Description": "The source value associated with a qualifier to characterize the observation"},{"Name": "value_source_concept_id", "Type": "integer", "Description": "A foreign key to a Concept for the value in the source data. This is applicable to observations where the result can be expressed as a non-standard concept."},{"Name": "value_source_value", "Type": "string", "Description": "The name of the concept referred to be value_source_concept_id. This is applicable to observations where the result can be expressed as a non-standard concept."},{"Name": "questionnaire_response_id", "Type": "integer", "Description": "An ID for a questionnaire response that produced this observation. This is applicable to AllOfUs questionnaire answers only. All answers with the same questionnaire response ID were submitted in the same response."}],
        columns=["Name", "Type", "Description"])
  table_columns["Observation"] = columns
  cohort_tables.append("Observation")

class Person(object):
  person_id = "person_id"
  gender_concept_id = "gender_concept_id"
  year_of_birth = "year_of_birth"
  month_of_birth = "month_of_birth"
  day_of_birth = "day_of_birth"
  birth_datetime = "birth_datetime"
  race_concept_id = "race_concept_id"
  ethnicity_concept_id = "ethnicity_concept_id"
  location_id = "location_id"
  provider_id = "provider_id"
  care_site_id = "care_site_id"
  person_source_value = "person_source_value"
  gender_source_value = "gender_source_value"
  gender_source_concept_id = "gender_source_concept_id"
  race_source_value = "race_source_value"
  race_source_concept_id = "race_source_concept_id"
  ethnicity_source_value = "ethnicity_source_value"
  ethnicity_source_concept_id = "ethnicity_source_concept_id"
  table_name = "person"
  columns = pd.DataFrame([{"Name": "person_id", "Type": "integer", "Description": "A unique identifier for each person."},{"Name": "gender_concept_id", "Type": "integer", "Description": "A foreign key that refers to an identifier in the CONCEPT table for the unique gender of the person."},{"Name": "year_of_birth", "Type": "integer", "Description": "The year of birth of the person. For data sources with date of birth, the year is extracted. For data sources where the year of birth is not available, the approximate year of birth is derived based on any age group categorization available."},{"Name": "month_of_birth", "Type": "integer", "Description": "The month of birth of the person. For data sources that provide the precise date of birth, the month is extracted and stored in this field."},{"Name": "day_of_birth", "Type": "integer", "Description": "The day of the month of birth of the person. For data sources that provide the precise date of birth, the day is extracted and stored in this field."},{"Name": "birth_datetime", "Type": "timestamp", "Description": "The date and time of birth of the person."},{"Name": "race_concept_id", "Type": "integer", "Description": "A foreign key that refers to an identifier in the CONCEPT table for the unique race of the person."},{"Name": "ethnicity_concept_id", "Type": "integer", "Description": "A foreign key that refers to the standard concept identifier in the Standardized Vocabularies for the ethnicity of the person."},{"Name": "location_id", "Type": "integer", "Description": "A foreign key to the place of residency for the person in the location table, where the detailed address information is stored."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the primary care provider the person is seeing in the provider table."},{"Name": "care_site_id", "Type": "integer", "Description": "A foreign key to the site of primary care in the care_site table, where the details of the care site are stored."},{"Name": "person_source_value", "Type": "string", "Description": "An (encrypted) key derived from the person identifier in the source data. This is necessary when a use case requires a link back to the person data at the source dataset."},{"Name": "gender_source_value", "Type": "string", "Description": "The source code for the gender of the person as it appears in the source data. The person’s gender is mapped to a standard gender concept in the Standardized Vocabularies; the original value is stored here for reference."},{"Name": "gender_source_concept_id", "Type": "integer", "Description": "A foreign key to the gender concept that refers to the code used in the source."},{"Name": "race_source_value", "Type": "string", "Description": "The source code for the race of the person as it appears in the source data. The person race is mapped to a standard race concept in the Standardized Vocabularies and the original value is stored here for reference."},{"Name": "race_source_concept_id", "Type": "integer", "Description": "A foreign key to the race concept that refers to the code used in the source."},{"Name": "ethnicity_source_value", "Type": "string", "Description": "The source code for the ethnicity of the person as it appears in the source data. The person ethnicity is mapped to a standard ethnicity concept in the Standardized Vocabularies and the original code is, stored here for reference."},{"Name": "ethnicity_source_concept_id", "Type": "integer", "Description": "A foreign key to the ethnicity concept that refers to the code used in the source."}],
        columns=["Name", "Type", "Description"])
  table_columns["Person"] = columns
  cohort_tables.append("Person")

class ProcedureOccurrence(object):
  procedure_occurrence_id = "procedure_occurrence_id"
  person_id = "person_id"
  procedure_concept_id = "procedure_concept_id"
  procedure_date = "procedure_date"
  procedure_datetime = "procedure_datetime"
  procedure_type_concept_id = "procedure_type_concept_id"
  modifier_concept_id = "modifier_concept_id"
  quantity = "quantity"
  provider_id = "provider_id"
  visit_occurrence_id = "visit_occurrence_id"
  procedure_source_value = "procedure_source_value"
  procedure_source_concept_id = "procedure_source_concept_id"
  qualifier_source_value = "qualifier_source_value"
  table_name = "procedure_occurrence"
  columns = pd.DataFrame([{"Name": "procedure_occurrence_id", "Type": "integer", "Description": "A system-generated unique identifier for each Procedure Occurrence."},{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the Person who is subjected to the Procedure. The demographic details of that Person are stored in the PERSON table."},{"Name": "procedure_concept_id", "Type": "integer", "Description": "A foreign key that refers to a standard procedure Concept identifier in the Standardized Vocabularies."},{"Name": "procedure_date", "Type": "date", "Description": "The date on which the Procedure was performed."},{"Name": "procedure_datetime", "Type": "timestamp", "Description": "The date and time on which the Procedure was performed."},{"Name": "procedure_type_concept_id", "Type": "integer", "Description": "A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of source data from which the procedure record is derived."},{"Name": "modifier_concept_id", "Type": "integer", "Description": "A foreign key to a Standard Concept identifier for a modifier to the Procedure (e.g. bilateral)"},{"Name": "quantity", "Type": "integer", "Description": "The quantity of procedures ordered or administered."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the provider in the PROVIDER table who was responsible for carrying out the procedure."},{"Name": "visit_occurrence_id", "Type": "integer", "Description": "A foreign key to the Visit in the VISIT_OCCURRENCE table during which the Procedure was carried out."},{"Name": "procedure_source_value", "Type": "string", "Description": "The source code for the Procedure as it appears in the source data. This code is mapped to a standard procedure Concept in the Standardized Vocabularies and the original code is, stored here for reference. Procedure source codes are typically ICD-9-Proc, CPT-4, HCPCS or OPCS-4 codes."},{"Name": "procedure_source_concept_id", "Type": "integer", "Description": "A foreign key to a Procedure Concept that refers to the code used in the source."},{"Name": "qualifier_source_value", "Type": "string", "Description": ""}],
        columns=["Name", "Type", "Description"])
  table_columns["ProcedureOccurrence"] = columns
  cohort_tables.append("ProcedureOccurrence")

class VisitOccurrence(object):
  visit_occurrence_id = "visit_occurrence_id"
  person_id = "person_id"
  visit_concept_id = "visit_concept_id"
  visit_start_date = "visit_start_date"
  visit_start_datetime = "visit_start_datetime"
  visit_end_date = "visit_end_date"
  visit_end_datetime = "visit_end_datetime"
  visit_type_concept_id = "visit_type_concept_id"
  provider_id = "provider_id"
  care_site_id = "care_site_id"
  visit_source_value = "visit_source_value"
  visit_source_concept_id = "visit_source_concept_id"
  admitting_source_concept_id = "admitting_source_concept_id"
  admitting_source_value = "admitting_source_value"
  discharge_to_concept_id = "discharge_to_concept_id"
  discharge_to_source_value = "discharge_to_source_value"
  preceding_visit_occurrence_id = "preceding_visit_occurrence_id"
  table_name = "visit_occurrence"
  columns = pd.DataFrame([{"Name": "visit_occurrence_id", "Type": "integer", "Description": "A unique identifier for each Person's visit or encounter at a healthcare provider."},{"Name": "person_id", "Type": "integer", "Description": "A foreign key identifier to the Person for whom the visit is recorded. The demographic details of that Person are stored in the PERSON table."},{"Name": "visit_concept_id", "Type": "integer", "Description": "A foreign key that refers to a visit Concept identifier in the Standardized Vocabularies."},{"Name": "visit_start_date", "Type": "date", "Description": "The start date of the visit."},{"Name": "visit_start_datetime", "Type": "timestamp", "Description": "The date and time of the visit started."},{"Name": "visit_end_date", "Type": "date", "Description": "The end date of the visit. If this is a one-day visit the end date should match the start date."},{"Name": "visit_end_datetime", "Type": "timestamp", "Description": "The date and time of the visit end."},{"Name": "visit_type_concept_id", "Type": "integer", "Description": "A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of source data from which the visit record is derived."},{"Name": "provider_id", "Type": "integer", "Description": "A foreign key to the provider in the provider table who was associated with the visit."},{"Name": "care_site_id", "Type": "integer", "Description": "A foreign key to the care site in the care site table that was visited."},{"Name": "visit_source_value", "Type": "string", "Description": "The source code for the visit as it appears in the source data."},{"Name": "visit_source_concept_id", "Type": "integer", "Description": "A foreign key to a Concept that refers to the code used in the source."},{"Name": "admitting_source_concept_id", "Type": "integer", "Description": "A foreign key to the predefined concept in the Place of Service Vocabulary reflecting the admitting source for a visit."},{"Name": "admitting_source_value", "Type": "string", "Description": "The source code for the admitting source as it appears in the source data."},{"Name": "discharge_to_concept_id", "Type": "integer", "Description": "A foreign key to the predefined concept in the Place of Service Vocabulary reflecting the discharge disposition for a visit."},{"Name": "discharge_to_source_value", "Type": "string", "Description": "The source code for the discharge disposition as it appears in the source data."},{"Name": "preceding_visit_occurrence_id", "Type": "integer", "Description": "A foreign key to the VISIT_OCCURRENCE table of the visit immediately preceding this visit"}],
        columns=["Name", "Type", "Description"])
  table_columns["VisitOccurrence"] = columns
  cohort_tables.append("VisitOccurrence")


###### Foreign keys 
CareSite.place_of_service_concept = RelatedTableWrapper("place_of_service_concept", Concept())
CareSite.location = RelatedTableWrapper("location", Location())
Concept.domain = RelatedTableWrapper("domain", Domain())
Concept.vocabulary = RelatedTableWrapper("vocabulary", Vocabulary())
Domain.domain_concept = RelatedTableWrapper("domain_concept", Concept())
Provider.specialty_concept = RelatedTableWrapper("specialty_concept", Concept())
Provider.care_site = RelatedTableWrapper("care_site", CareSite())
Provider.specialty_source_concept = RelatedTableWrapper("specialty_source_concept", Concept())
Provider.gender_source_concept = RelatedTableWrapper("gender_source_concept", Concept())
Vocabulary.vocabulary_concept = RelatedTableWrapper("vocabulary_concept", Concept())
ConditionOccurrence.person = RelatedTableWrapper("person", Person())
ConditionOccurrence.condition_concept = RelatedTableWrapper("condition_concept", Concept())
ConditionOccurrence.condition_type_concept = RelatedTableWrapper("condition_type_concept", Concept())
ConditionOccurrence.provider = RelatedTableWrapper("provider", Provider())
ConditionOccurrence.visit_occurrence = RelatedTableWrapper("visit_occurrence", VisitOccurrence())
ConditionOccurrence.condition_status_concept = RelatedTableWrapper("condition_status_concept", Concept())
Death.death_type_concept = RelatedTableWrapper("death_type_concept", Concept())
Death.cause_concept = RelatedTableWrapper("cause_concept", Concept())
Death.cause_source_concept = RelatedTableWrapper("cause_source_concept", Concept())
DeviceExposure.person = RelatedTableWrapper("person", Person())
DeviceExposure.device_concept = RelatedTableWrapper("device_concept", Concept())
DeviceExposure.device_type_concept = RelatedTableWrapper("device_type_concept", Concept())
DeviceExposure.device_source_concept = RelatedTableWrapper("device_source_concept", Concept())
DrugExposure.person = RelatedTableWrapper("person", Person())
DrugExposure.drug_concept = RelatedTableWrapper("drug_concept", Concept())
DrugExposure.drug_type_concept = RelatedTableWrapper("drug_type_concept", Concept())
DrugExposure.route_concept = RelatedTableWrapper("route_concept", Concept())
DrugExposure.provider = RelatedTableWrapper("provider", Provider())
DrugExposure.visit_occurrence = RelatedTableWrapper("visit_occurrence", VisitOccurrence())
DrugExposure.drug_source_concept = RelatedTableWrapper("drug_source_concept", Concept())
Measurement.person = RelatedTableWrapper("person", Person())
Measurement.measurement_concept = RelatedTableWrapper("measurement_concept", Concept())
Measurement.measurement_type_concept = RelatedTableWrapper("measurement_type_concept", Concept())
Measurement.operator_concept = RelatedTableWrapper("operator_concept", Concept())
Measurement.value_as_concept = RelatedTableWrapper("value_as_concept", Concept())
Measurement.unit_concept = RelatedTableWrapper("unit_concept", Concept())
Measurement.provider = RelatedTableWrapper("provider", Provider())
Measurement.visit_occurrence = RelatedTableWrapper("visit_occurrence", VisitOccurrence())
Measurement.measurement_source_concept = RelatedTableWrapper("measurement_source_concept", Concept())
Observation.person = RelatedTableWrapper("person", Concept())
Observation.observation_concept = RelatedTableWrapper("observation_concept", Concept())
Observation.observation_type_concept = RelatedTableWrapper("observation_type_concept", Concept())
Observation.value_as_concept = RelatedTableWrapper("value_as_concept", Concept())
Observation.qualifier_concept = RelatedTableWrapper("qualifier_concept", Concept())
Observation.unit_concept = RelatedTableWrapper("unit_concept", Concept())
Observation.provider = RelatedTableWrapper("provider", Provider())
Observation.visit_occurrence = RelatedTableWrapper("visit_occurrence", VisitOccurrence())
Observation.observation_source_concept = RelatedTableWrapper("observation_source_concept", Concept())
Observation.value_source_concept = RelatedTableWrapper("value_source_concept", Concept())
Person.gender_concept = RelatedTableWrapper("gender_concept", Concept())
Person.race_concept = RelatedTableWrapper("race_concept", Concept())
Person.ethnicity_concept = RelatedTableWrapper("ethnicity_concept", Concept())
Person.location = RelatedTableWrapper("location", Location())
Person.provider = RelatedTableWrapper("provider", Provider())
Person.care_site = RelatedTableWrapper("care_site", CareSite())
Person.gender_source_concept = RelatedTableWrapper("gender_source_concept", Concept())
Person.race_source_concept = RelatedTableWrapper("race_source_concept", Concept())
Person.ethnicity_source_concept = RelatedTableWrapper("ethnicity_source_concept", Concept())
ProcedureOccurrence.person = RelatedTableWrapper("person", Person())
ProcedureOccurrence.procedure_concept = RelatedTableWrapper("procedure_concept", Concept())
ProcedureOccurrence.procedure_type_concept = RelatedTableWrapper("procedure_type_concept", Concept())
ProcedureOccurrence.modifier_concept = RelatedTableWrapper("modifier_concept", Concept())
ProcedureOccurrence.provider = RelatedTableWrapper("provider", Provider())
ProcedureOccurrence.visit_occurrence = RelatedTableWrapper("visit_occurrence", VisitOccurrence())
ProcedureOccurrence.procedure_source_concept = RelatedTableWrapper("procedure_source_concept", Concept())
VisitOccurrence.person = RelatedTableWrapper("person", Person())
VisitOccurrence.visit_concept = RelatedTableWrapper("visit_concept", Concept())
VisitOccurrence.visit_type_concept = RelatedTableWrapper("visit_type_concept", Concept())
VisitOccurrence.provider = RelatedTableWrapper("provider", Provider())
VisitOccurrence.care_site = RelatedTableWrapper("care_site", CareSite())
VisitOccurrence.visit_source_concept = RelatedTableWrapper("visit_source_concept", Concept())
VisitOccurrence.admitting_source_concept = RelatedTableWrapper("admitting_source_concept", Concept())
VisitOccurrence.discharge_to_concept = RelatedTableWrapper("discharge_to_concept", Concept())
VisitOccurrence.preceding_visit_occurrence = RelatedTableWrapper("preceding_visit_occurrence", VisitOccurrence())
