from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.concepts_api import ConceptsApi
from aou_workbench_client.swagger_client.models.domain import Domain
from aou_workbench_client.swagger_client.models.search_concepts_request import SearchConceptsRequest
from aou_workbench_client.swagger_client.models.standard_concept_filter import StandardConceptFilter
from ipywidgets import interactive
import pandas as pd

from IPython.display import display, HTML

_DOMAIN_DICT = { 
    '': None,
    'Observation': Domain.OBSERVATION,
    'Procedure': Domain.PROCEDURE,
    'Drug': Domain.DRUG,
    'Condition': Domain.CONDITION,
    'Measurement': Domain.MEASUREMENT,
    'Device': Domain.DEVICE,
    'Race': Domain.RACE,
    'Gender': Domain.GENDER,
    'Ethnicity': Domain.ETHNICITY 
}

_STANDARD_CONCEPT_FILTER_DICT = { 
    '': StandardConceptFilter.ALL_CONCEPTS,
    'Standard concepts': StandardConceptFilter.STANDARD_CONCEPTS,
    'Non-standard concepts': StandardConceptFilter.NON_STANDARD_CONCEPTS
}

# Common vocabularies. (There are others in the data but they don't get much
# use.)
_VOCAB_IDS = [ 
    '', 
    'ATC',    
    'CPT4',
    'DRG',
    'HCPCS',
    'ICD10CM',
    'ICD10PCS',
    'ICD9CM',
    'ICD9Proc',
    'ISBT',
    'ISBT Attribute',
    'LOINC',
    'Multum',
    'NDC',
    'NDFRT',
    'PPI',
    'RxNorm',
    'RxNorm Extension',
    'SNOMED',
    'SPL',
    'VA Product'
  ]

_RESULT_FIELDS = [
    ('ID', 'concept_id'),
    ('Name', 'concept_name'),
    ('Code', 'concept_code'),
    ('Domain', 'domain_id')
    ('Vocabulary', 'vocabulary_id'),
    ('Count', 'count_value')]

_VOCAB_DICT = {id: id for id in _VOCAB_IDS}

def search_concepts(request):
  client = get_authenticated_swagger_client()
  concepts_api = ConceptsApi(api_client=client)
  response = concepts_api.search_concepts(all_of_us_config.workspace_namespace,
                                          all_of_us_config.workspace_id,
                                          request=request)
  return response.items

def get_concept_dict(concept):
  return { f[0]: getattr(concept, f[1]) for f in _RESULT_FIELDS } 

def get_concepts_frame(request):
  concepts = search_concepts(request)
  return pd.DataFrame([get_concept_dict(concept) for concept in concepts],
                      columns = [f[0] for f in _RESULT_FIELDS])

def display_concepts(request):
  concepts_frame = get_concepts_frame(request)
  s = concepts_frame.style.set_properties(**{'text-align': 'left'})
  s = s.set_table_styles(
      [{"selector": "th", "props": [("text-align", "left")]}]).hide_index()
  display(HTML(s.render()))

def display_concepts_fn(query, domain, vocabulary, concepts):
  request = SearchConceptsRequest(query=query)
  if domain:
    request.domain = domain
  if concepts:
    request.standard_concept_filter = concepts
  if vocabulary:
    request.vocabulary_ids = [vocabulary]
  display_concepts(request)
  
interact = interactive.factory()
interact_form = interact.options(manual=True, manual_name="Search")  
  
def display_concepts_widget():
  interact_form(display_concepts_fn, query='', domain=_DOMAIN_DICT,
                concepts=_STANDARD_CONCEPT_FILTER_DICT,
                vocabulary=_VOCAB_DICT,
                manual_name='Search')
