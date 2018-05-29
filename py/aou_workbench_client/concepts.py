from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.concepts_api import ConceptsApi
import pandas as pd

from IPython.display import display, HTML

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
      [{"selector": "th", "props": [("text-align", "left")]},
       {"selector": ".col0", props = [('display', 'none')]},
       {"selector": ".blank.level0",
        "props": [("display", "none")]}])
  display(HTML(s.render()))
