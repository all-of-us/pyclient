from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.concepts_api import ConceptsApi
from aou_workbench_client.swagger_client.models.domain import Domain
from aou_workbench_client.swagger_client.models.search_concepts_request import SearchConceptsRequest
from aou_workbench_client.swagger_client.models.standard_concept_filter import StandardConceptFilter
from ipywidgets import interact_manual
import pandas as pd

from IPython.display import display, HTML

_DOMAIN_DICT = { '': None,
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

_STANDARD_CONCEPTS_FILTER_DICT = { '': ALL_CONCEPTS,
    'Standard concepts': StandardConceptsFilter.STANDARD_CONCEPTS,
    'Non-standard concepts': StandardConceptsFilter.NON_STANDARD_CONCEPTS
}

def search_concepts(request):
  client = get_authenticated_swagger_client()
  concepts_api = ConceptsApi(api_client=client)
  response = concepts_api.search_concepts(all_of_us_config.workspace_namespace,
                                          all_of_us_config.workspace_id,
                                          request=request)
  return response.items

def get_concept_dict(concept):
  return { "ID": concept.concept_id,
           "Name": concept.concept_name,
           "Code": concept.concept_code,
           "Domain": concept.domain_id,
           "Vocabulary": concept.vocabulary_id,
           "Count": concept.count_value
         }

def get_concepts_frame(request):
  concepts = search_concepts(request)
  return pd.DataFrame([get_concept_dict(concept) for concept in concepts],
                      columns = ["ID", "Name", "Code", "Domain", 
                                 "Vocabulary", "Count"])

def display_concepts(request):
  concepts_frame = get_concepts_frame(request)
  s = concepts_frame.style.set_properties(**{'text-align': 'left'})
  s = s.set_table_styles(
      [{"selector": "th", "props": [("text-align", "left")]}]).hide_index()
  display(HTML(s.render()))

def display_concepts_fn(query, domain, standard_concept_filter):
  request = SearchConceptsRequest(query=query)
  if domain:
    request.domain = domain
  if standard_concepts_filter:
    request.standard_concept_filter = standard_concept_filter
  display_concepts(request)
  
def display_concepts_widget():
  interact_manual(display_concepts_fn, query='', domain=_DOMAIN_DICT,
                  standard_concept_filter=_STANDARD_CONCEPT_FILTER_DICT,
                  manual_name='Search')
