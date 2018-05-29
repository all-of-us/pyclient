from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.concepts_api import ConceptsApi
<<<<<<< HEAD

from IPython.display import display
=======
import pandas as pd

from IPython.display import display, HTML
>>>>>>> f5d0e53964dff4646c6e982dfeb8e88ee09b2838

def search_concepts(request):
  client = get_authenticated_swagger_client()
  concepts_api = ConceptsApi(api_client=client)
  response = concepts_api.search_concepts(all_of_us_config.workspace_namespace,
                                          all_of_us_config.workspace_id,
                                          request=request)
  return response.items

<<<<<<< HEAD
def get_concepts_frame(request):
  concepts = search_concepts(request)
  concepts_frame = pd.DataFrame(concepts, columns=["concept_id",
                                                   "concept_name",
                                                   "domain_id",
                                                   "vocabulary_id",
                                                   "concept_code",
                                                   "concept_class_id",
                                                   "standard_concept",
                                                   "count_value"])
  concepts_frame.rename(columns={"concept_id": "ID",
                                 "concept_name": "Name",
                                 "domain_id": "Domain",
                                 "vocabulary_id": "Vocabulary",
                                 "concept_code": "Code",
                                 "concept_class_id": "Class",
                                 "standard_concept": "Standard?",
                                 "count_value": "Count"})
  return concepts_frame

def display_concepts(request):
  concepts_frame = get_concepts_frame(request)
  display(concepts_frame)
=======
def get_concept_dict(concept):
  return { "ID": concept.concept_id,
           "Name": concept.concept_name,
           "Domain": concept.domain_id,
           "Vocabulary": concept.vocabulary_id,
           "Count": concept.count_value
         }

def get_concepts_frame(request):
  concepts = search_concepts(request)
  return pd.DataFrame([get_concept_dict(concept) for concept in concepts],
                      columns = ["ID", "Name", "Domain", "Vocabulary", "Count"])

def display_concepts(request):
  concepts_frame = get_concepts_frame(request)
  s = concepts_frame.style.set_properties(**{'text-align': 'left'})
  s = s.set_table_styles(
      [{"selector": "th", "props": [("text-align", "left")]}])
  display(HTML(s.render()))
  
>>>>>>> f5d0e53964dff4646c6e982dfeb8e88ee09b2838
