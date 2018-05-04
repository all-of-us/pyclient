# CDR metadata documentation
This documentation provides information on the tables and columns in the curated data repository.
In notebook code, you can reference the names of tables and columns using the objects defined in 
[model.py](model.py).

## Cohort tables
Below are tables that you can use directly when materializing a cohort, passing in their 
table name for `TableQuery.table_name`.

### condition_occurrence
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
condition_occurrence_id | integer |  | A unique identifier for each Condition Occurrence event.
person_id | integer | [person](#person) | A foreign key identifier to the Person who is experiencing the condition. The demographic details of that Person are stored in the PERSON table.
condition_concept_id | integer | [concept](#concept) | A foreign key that refers to a Standard Condition Concept identifier in the Standardized Vocabularies.
condition_start_date | date |  | The date when the instance of the Condition is recorded.
condition_start_datetime | timestamp |  | The date and time when the instance of the Condition is recorded.
condition_end_date | date |  | The date when the instance of the Condition is considered to have ended.
condition_end_datetime | timestamp |  | The date when the instance of the Condition is considered to have ended.
condition_type_concept_id | integer | [concept](#concept) | A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the source data from which the condition was recorded, the level of standardization, and the type of occurrence.
stop_reason | string |  | The reason that the condition was no longer present, as indicated in the source data.
provider_id | integer | [provider](#provider) | A foreign key to the Provider in the PROVIDER table who was responsible for capturing (diagnosing) the Condition.
visit_occurrence_id | integer | [visit_occurrence](#visit_occurrence) | A foreign key to the visit in the VISIT_OCCURRENCE table during which the Condition was determined (diagnosed).
condition_source_value | string |  | The source code for the condition as it appears in the source data. This code is mapped to a standard condition concept in the Standardized Vocabularies and the original code is stored here for reference.
condition_source_concept_id | integer |  | A foreign key to a Condition Concept that refers to the code used in the source.
condition_status_source_value | string |  | The source code for the condition status as it appears in the source data.
condition_status_concept_id | integer | [concept](#concept) | A foreign key to the predefined Concept in the Standard Vocabulary reflecting the condition status

### death
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
person_id | integer |  | A foreign key identifier to the deceased person. The demographic details of that person are stored in the person table.
death_date | date |  | The date the person was deceased. If the precise date including day or month is not known or not allowed, December is used as the default month, and the last day of the month the default day.
death_datetime | timestamp |  | The date and time the person was deceased. If the precise date including day or month is not known or not allowed, December is used as the default month, and the last day of the month the default day.
death_type_concept_id | integer | [concept](#concept) | A foreign key referring to the predefined concept identifier in the Standardized Vocabularies reflecting how the death was represented in the source data.
cause_concept_id | integer | [concept](#concept) | A foreign key referring to a standard concept identifier in the Standardized Vocabularies for conditions.
cause_source_value | string |  | The source code for the cause of death as it appears in the source data. This code is mapped to a standard concept in the Standardized Vocabularies and the original code is, stored here for reference.
cause_source_concept_id | integer | [concept](#concept) | A foreign key to the concept that refers to the code used in the source. Note, this variable name is abbreviated to ensure it will be allowable across database platforms.

### device_exposure
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
device_exposure_id | integer |  | A system-generated unique identifier for each Device Exposure.
person_id | integer | [person](#person) | A foreign key identifier to the Person who is subjected to the Device. The demographic details of that person are stored in the Person table.
device_concept_id | integer | [concept](#concept) | A foreign key that refers to a Standard Concept identifier in the Standardized Vocabularies for the Device concept.
device_exposure_start_date | date |  | The date the Device or supply was applied or used.
device_exposure_start_datetime | timestamp |  | The date and time the Device or supply was applied or used.
device_exposure_end_date | date |  | The date the Device or supply was removed from use.
device_exposure_end_datetime | timestamp |  | The date and time the Device or supply was removed from use.
device_type_concept_id | integer | [concept](#concept) | A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of Device Exposure recorded. It indicates how the Device Exposure was represented in the source data.
unique_device_id | string |  | A UDI or equivalent identifying the instance of the Device used in the Person.
quantity | integer |  | The number of individual Devices used for the exposure.
provider_id | integer |  | A foreign key to the provider in the PROVIDER table who initiated of administered the Device.
visit_occurrence_id | integer |  | A foreign key to the visit in the VISIT_OCCURRENCE table during which the device was used.
device_source_value | string |  | The source code for the Device as it appears in the source data. This code is mapped to a standard Device Concept in the Standardized Vocabularies and the original code is stored here for reference.
device_source_concept_id | integer | [concept](#concept) | 

### drug_exposure
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
drug_exposure_id | integer |  | A system-generated unique identifier for each Drug utilization event.
person_id | integer | [person](#person) | A foreign key identifier to the person who is subjected to the Drug. The demographic details of that person are stored in the person table.
drug_concept_id | integer | [concept](#concept) | A foreign key that refers to a Standard Concept identifier in the Standardized Vocabularies for the Drug concept.
drug_exposure_start_date | date |  | The start date for the current instance of Drug utilization. Valid entries include a start date of a prescription, the date a prescription was filled, or the date on which a Drug administration procedure was recorded.
drug_exposure_start_datetime | timestamp |  | The start date and time for the current instance of Drug utilization. Valid entries include a start date of a prescription, the date a prescription was filled, or the date on which a Drug administration procedure was recorded.
drug_exposure_end_date | date |  | The end date for the current instance of Drug utilization. It is not available from all sources.
drug_exposure_end_datetime | timestamp |  | The end date and time for the current instance of Drug utilization. It is not available from all sources.
verbatim_end_date | date |  | The known end date of a drug_exposure as provided by the source
drug_type_concept_id | integer | [concept](#concept) | A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of Drug Exposure recorded. It indicates how the Drug Exposure was represented in the source data.
stop_reason | string |  | The reason the Drug was stopped. Reasons include regimen completed, changed, removed, etc.
refills | integer |  | The number of refills after the initial prescription. The initial prescription is not counted, values start with 0.
quantity | float |  | The quantity of drug as recorded in the original prescription or dispensing record.
days_supply | integer |  | The number of days of supply of the medication as recorded in the original prescription or dispensing record.
sig | string |  | The directions ("signetur") on the Drug prescription as recorded in the original prescription (and printed on the container) or dispensing record.
route_concept_id | integer | [concept](#concept) | A foreign key to a predefined concept in the Standardized Vocabularies reflecting the route of administration.
lot_number | string |  | An identifier assigned to a particular quantity or lot of Drug product from the manufacturer.
provider_id | integer | [provider](#provider) | A foreign key to the provider in the PROVIDER table who initiated (prescribed or administered) the Drug Exposure.
visit_occurrence_id | integer | [visit_occurrence](#visit_occurrence) | A foreign key to the Visit in the VISIT_OCCURRENCE table during which the Drug Exposure was initiated.
drug_source_value | string |  | The source code for the Drug as it appears in the source data. This code is mapped to a Standard Drug concept in the Standardized Vocabularies and the original code is, stored here for reference.
drug_source_concept_id | integer | [concept](#concept) | A foreign key to a Drug Concept that refers to the code used in the source.
route_source_value | string |  | The information about the route of administration as detailed in the source.
dose_unit_source_value | string |  | The information about the dose unit as detailed in the source.

### measurement
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
measurement_id | integer |  | A unique identifier for each Measurement.
person_id | integer | [person](#person) | A foreign key identifier to the Person about whom the measurement was recorded. The demographic details of that Person are stored in the PERSON table.
measurement_concept_id | integer | [concept](#concept) | A foreign key to the standard measurement concept identifier in the Standardized Vocabularies.
measurement_date | date |  | The date of the Measurement.
measurement_datetime | timestamp |  | The date and time of the Measurement. Some database systems don't have a datatype of time. To accomodate all temporal analyses, datatype datetime can be used (combining measurement_date and measurement_time [forum discussion](http://forums.ohdsi.org/t/date-time-and-datetime-problem-and-the-world-of-hours-and-1day/314))
measurement_type_concept_id | integer | [concept](#concept) | A foreign key to the predefined Concept in the Standardized Vocabularies reflecting the provenance from where the Measurement record was recorded.
operator_concept_id | integer | [concept](#concept) | A foreign key identifier to the predefined Concept in the Standardized Vocabularies reflecting the mathematical operator that is applied to the value_as_number. Operators are <, <=, =, >=, >.
value_as_number | float |  | A Measurement result where the result is expressed as a numeric value.
value_as_concept_id | integer | [concept](#concept) | A foreign key to a Measurement result represented as a Concept from the Standardized Vocabularies (e.g., positive/negative, present/absent, low/high, etc.).
unit_concept_id | integer | [concept](#concept) | A foreign key to a Standard Concept ID of Measurement Units in the Standardized Vocabularies.
range_low | float |  | The lower limit of the normal range of the Measurement result. The lower range is assumed to be of the same unit of measure as the Measurement value.
range_high | float |  | The upper limit of the normal range of the Measurement. The upper range is assumed to be of the same unit of measure as the Measurement value.
provider_id | integer | [provider](#provider) | A foreign key to the provider in the PROVIDER table who was responsible for initiating or obtaining the measurement.
visit_occurrence_id | integer | [visit_occurrence](#visit_occurrence) | A foreign key to the Visit in the VISIT_OCCURRENCE table during which the Measurement was recorded.
measurement_source_value | string |  | The Measurement name as it appears in the source data. This code is mapped to a Standard Concept in the Standardized Vocabularies and the original code is stored here for reference.
measurement_source_concept_id | integer | [concept](#concept) | A foreign key to a Concept in the Standard Vocabularies that refers to the code used in the source.
unit_source_value | string |  | The source code for the unit as it appears in the source data. This code is mapped to a standard unit concept in the Standardized Vocabularies and the original code is stored here for reference.
value_source_value | string |  | The source value associated with the content of the value_as_number or value_as_concept_id as stored in the source data.

### observation
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
observation_id | integer |  | A unique identifier for each observation.
person_id | integer | [concept](#concept) | A foreign key identifier to the Person about whom the observation was recorded. The demographic details of that Person are stored in the PERSON table.
observation_concept_id | integer | [concept](#concept) | A foreign key to the standard observation concept identifier in the Standardized Vocabularies.
observation_date | date |  | The date of the observation.
observation_datetime | timestamp |  | The date and time of the observation.
observation_type_concept_id | integer | [concept](#concept) | A foreign key to the predefined concept identifier in the Standardized Vocabularies reflecting the type of the observation.
value_as_number | float |  | The observation result stored as a number. This is applicable to observations where the result is expressed as a numeric value.
value_as_string | string |  | The observation result stored as a string. This is applicable to observations where the result is expressed as verbatim text.
value_as_concept_id | integer | [concept](#concept) | A foreign key to an observation result stored as a Concept ID. This is applicable to observations where the result can be expressed as a Standard Concept from the Standardized Vocabularies (e.g., positive/negative, present/absent, low/high, etc.).
qualifier_concept_id | integer | [concept](#concept) | A foreign key to a Standard Concept ID for a qualifier (e.g., severity of drug-drug interaction alert)
unit_concept_id | integer | [concept](#concept) | A foreign key to a Standard Concept ID of measurement units in the Standardized Vocabularies.
provider_id | integer | [provider](#provider) | A foreign key to the provider in the PROVIDER table who was responsible for making the observation.
visit_occurrence_id | integer | [visit_occurrence](#visit_occurrence) | A foreign key to the visit in the VISIT_OCCURRENCE table during which the observation was recorded.
observation_source_value | string |  | The observation code as it appears in the source data. This code is mapped to a Standard Concept in the Standardized Vocabularies and the original code is, stored here for reference.
observation_source_concept_id | integer | [concept](#concept) | A foreign key to a Concept that refers to the code used in the source.
unit_source_value | string |  | The source code for the unit as it appears in the source data. This code is mapped to a standard unit concept in the Standardized Vocabularies and the original code is, stored here for reference.
qualifier_source_value | string |  | The source value associated with a qualifier to characterize the observation
value_source_concept_id | integer | [concept](#concept) | A foreign key to a Concept for the value in the source data. This is applicable to observations where the result can be expressed as a non-standard concept.
value_source_value | string |  | The name of the concept referred to be value_source_concept_id. This is applicable to observations where the result can be expressed as a non-standard concept.
questionnaire_response_id | integer |  | An ID for a questionnaire response that produced this observation. This is applicable to AllOfUs questionnaire answers only. All answers with the same questionnaire response ID were submitted in the same response.

### person
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
person_id | integer |  | A unique identifier for each person.
gender_concept_id | integer | [concept](#concept) | A foreign key that refers to an identifier in the CONCEPT table for the unique gender of the person.
year_of_birth | integer |  | The year of birth of the person. For data sources with date of birth, the year is extracted. For data sources where the year of birth is not available, the approximate year of birth is derived based on any age group categorization available.
month_of_birth | integer |  | The month of birth of the person. For data sources that provide the precise date of birth, the month is extracted and stored in this field.
day_of_birth | integer |  | The day of the month of birth of the person. For data sources that provide the precise date of birth, the day is extracted and stored in this field.
birth_datetime | timestamp |  | The date and time of birth of the person.
race_concept_id | integer | [concept](#concept) | A foreign key that refers to an identifier in the CONCEPT table for the unique race of the person.
ethnicity_concept_id | integer | [concept](#concept) | A foreign key that refers to the standard concept identifier in the Standardized Vocabularies for the ethnicity of the person.
location_id | integer | [location](#location) | A foreign key to the place of residency for the person in the location table, where the detailed address information is stored.
provider_id | integer | [provider](#provider) | A foreign key to the primary care provider the person is seeing in the provider table.
care_site_id | integer | [care_site](#care_site) | A foreign key to the site of primary care in the care_site table, where the details of the care site are stored.
person_source_value | string |  | An (encrypted) key derived from the person identifier in the source data. This is necessary when a use case requires a link back to the person data at the source dataset.
gender_source_value | string |  | The source code for the gender of the person as it appears in the source data. The person’s gender is mapped to a standard gender concept in the Standardized Vocabularies; the original value is stored here for reference.
gender_source_concept_id | integer | [concept](#concept) | A foreign key to the gender concept that refers to the code used in the source.
race_source_value | string |  | The source code for the race of the person as it appears in the source data. The person race is mapped to a standard race concept in the Standardized Vocabularies and the original value is stored here for reference.
race_source_concept_id | integer | [concept](#concept) | A foreign key to the race concept that refers to the code used in the source.
ethnicity_source_value | string |  | The source code for the ethnicity of the person as it appears in the source data. The person ethnicity is mapped to a standard ethnicity concept in the Standardized Vocabularies and the original code is, stored here for reference.
ethnicity_source_concept_id | integer | [concept](#concept) | A foreign key to the ethnicity concept that refers to the code used in the source.

### procedure_occurrence
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
procedure_occurrence_id | integer |  | A system-generated unique identifier for each Procedure Occurrence.
person_id | integer | [person](#person) | A foreign key identifier to the Person who is subjected to the Procedure. The demographic details of that Person are stored in the PERSON table.
procedure_concept_id | integer | [concept](#concept) | A foreign key that refers to a standard procedure Concept identifier in the Standardized Vocabularies.
procedure_date | date |  | The date on which the Procedure was performed.
procedure_datetime | timestamp |  | The date and time on which the Procedure was performed.
procedure_type_concept_id | integer | [concept](#concept) | A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of source data from which the procedure record is derived.
modifier_concept_id | integer | [concept](#concept) | A foreign key to a Standard Concept identifier for a modifier to the Procedure (e.g. bilateral)
quantity | integer |  | The quantity of procedures ordered or administered.
provider_id | integer | [provider](#provider) | A foreign key to the provider in the PROVIDER table who was responsible for carrying out the procedure.
visit_occurrence_id | integer | [visit_occurrence](#visit_occurrence) | A foreign key to the Visit in the VISIT_OCCURRENCE table during which the Procedure was carried out.
procedure_source_value | string |  | The source code for the Procedure as it appears in the source data. This code is mapped to a standard procedure Concept in the Standardized Vocabularies and the original code is, stored here for reference. Procedure source codes are typically ICD-9-Proc, CPT-4, HCPCS or OPCS-4 codes.
procedure_source_concept_id | integer | [concept](#concept) | A foreign key to a Procedure Concept that refers to the code used in the source.
qualifier_source_value | string |  | 

### visit_occurrence
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
visit_occurrence_id | integer |  | A unique identifier for each Person's visit or encounter at a healthcare provider.
person_id | integer | [person](#person) | A foreign key identifier to the Person for whom the visit is recorded. The demographic details of that Person are stored in the PERSON table.
visit_concept_id | integer | [concept](#concept) | A foreign key that refers to a visit Concept identifier in the Standardized Vocabularies.
visit_start_date | date |  | The start date of the visit.
visit_start_datetime | timestamp |  | The date and time of the visit started.
visit_end_date | date |  | The end date of the visit. If this is a one-day visit the end date should match the start date.
visit_end_datetime | timestamp |  | The date and time of the visit end.
visit_type_concept_id | integer | [concept](#concept) | A foreign key to the predefined Concept identifier in the Standardized Vocabularies reflecting the type of source data from which the visit record is derived.
provider_id | integer | [provider](#provider) | A foreign key to the provider in the provider table who was associated with the visit.
care_site_id | integer | [care_site](#care_site) | A foreign key to the care site in the care site table that was visited.
visit_source_value | string |  | The source code for the visit as it appears in the source data.
visit_source_concept_id | integer | [concept](#concept) | A foreign key to a Concept that refers to the code used in the source.
admitting_source_concept_id | integer | [concept](#concept) | A foreign key to the predefined concept in the Place of Service Vocabulary reflecting the admitting source for a visit.
admitting_source_value | string |  | The source code for the admitting source as it appears in the source data.
discharge_to_concept_id | integer | [concept](#concept) | A foreign key to the predefined concept in the Place of Service Vocabulary reflecting the discharge disposition for a visit.
discharge_to_source_value | string |  | The source code for the discharge disposition as it appears in the source data.
preceding_visit_occurrence_id | integer | [visit_occurrence](#visit_occurrence) | A foreign key to the VISIT_OCCURRENCE table of the visit immediately preceding this visit


## Metadata tables
Below are tables that provide metadata related to the cohort tables; you can retrive 
data from them by requesting data from related tables.

### care_site
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
care_site_id | integer |  | A unique identifier for each Care Site.
care_site_name | string |  | The verbatim description or name of the Care Site as in data source
place_of_service_concept_id | integer | [concept](#concept) | A foreign key that refers to a Place of Service Concept ID in the Standardized Vocabularies.
location_id | integer | [location](#location) | A foreign key to the geographic Location in the LOCATION table, where the detailed address information is stored.
care_site_source_value | string |  | The identifier for the Care Site in the source data, stored here for reference.
place_of_service_source_value | string |  | The source code for the Place of Service as it appears in the source data, stored here for reference.

### concept
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
concept_id | integer |  | A unique identifier for each Concept across all domains.
concept_name | string |  | An unambiguous, meaningful and descriptive name for the Concept.
domain_id | string | [domain](#domain) | A foreign key to the [DOMAIN](https://github.com/OHDSI/CommonDataModel/wiki/DOMAIN) table the Concept belongs to.
vocabulary_id | string | [vocabulary](#vocabulary) | A foreign key to the [VOCABULARY](https://github.com/OHDSI/CommonDataModel/wiki/VOCABULARY) table indicating from which source the Concept has been adapted.
concept_class_id | string |  | The attribute or concept class of the Concept. Examples are 'Clinical Drug', 'Ingredient', 'Clinical Finding' etc.
standard_concept | string |  | This flag determines where a Concept is a Standard Concept, i.e. is used in the data, a Classification Concept, or a non-standard Source Concept. The allowables values are 'S' (Standard Concept) and 'C' (Classification Concept), otherwise the content is NULL.
concept_code | string |  | The concept code represents the identifier of the Concept in the source vocabulary, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.
valid_start_date | date |  | The date when the Concept was first recorded. The default value is 1-Jan-1970, meaning, the Concept has no (known) date of inception.
valid_end_date | date |  | The date when the Concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099, meaning, the Concept is valid until it becomes deprecated.
invalid_reason | string |  | Reason the Concept was invalidated. Possible values are D (deleted), U (replaced with an update) or NULL when valid_end_date has the default value.

### domain
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
domain_id | string |  | A unique key for each domain.
domain_name | string |  | The name describing the Domain, e.g. "Condition", "Procedure", "Measurement" etc.
domain_concept_id | integer | [concept](#concept) | A foreign key that refers to an identifier in the [CONCEPT](https://github.com/OHDSI/CommonDataModel/wiki/CONCEPT) table for the unique Domain Concept the Domain record belongs to.

### location
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
location_id | integer |  | A unique identifier for each geographic location.
address_1 | string |  | The address field 1, typically used for the street address, as it appears in the source data.
address_2 | string |  | The address field 2, typically used for additional detail such as buildings, suites, floors, as it appears in the source data.
city | string |  | The city field as it appears in the source data.
state | string |  | The state field as it appears in the source data.
zip | string |  | The zip or postal code.
county | string |  | The county.
location_source_value | string |  | The verbatim information that is used to uniquely identify the location as it appears in the source data.

### provider
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
provider_id | integer |  | A unique identifier for each Provider.
provider_name | string |  | A description of the Provider.
NPI | string |  | 
DEA | string |  | 
specialty_concept_id | integer | [concept](#concept) | A foreign key to a Standard Specialty Concept ID in the Standardized Vocabularies.
care_site_id | integer | [care_site](#care_site) | A foreign key to the main Care Site where the provider is practicing.
year_of_birth | integer |  | The year of birth of the Provider.
gender_concept_id | integer |  | The gender of the Provider.
provider_source_value | string |  | The identifier used for the Provider in the source data, stored here for reference.
specialty_source_value | string |  | The source code for the Provider specialty as it appears in the source data, stored here for reference.
specialty_source_concept_id | integer | [concept](#concept) | A foreign key to a Concept that refers to the code used in the source.
gender_source_value | string |  | The gender code for the Provider as it appears in the source data, stored here for reference.
gender_source_concept_id | integer | [concept](#concept) | A foreign key to a Concept that refers to the code used in the source.

### vocabulary
Columns:

Name | Type | Foreign key to | Description
---- | ---- | -------------- | -----------
vocabulary_id | string |  | A unique identifier for each Vocabulary, such as ICD9CM, SNOMED, Visit.
vocabulary_name | string |  | The name describing the vocabulary, for example "International Classification of Diseases, Ninth Revision, Clinical Modification, Volume 1 and 2 (NCHS)" etc.
vocabulary_reference | string |  | External reference to documentation or available download of the about the vocabulary.
vocabulary_version | string |  | Version of the Vocabulary as indicated in the source.
vocabulary_concept_id | integer | [concept](#concept) | A foreign key that refers to a standard concept identifier in the CONCEPT table for the Vocabulary the VOCABULARY record belongs to.

