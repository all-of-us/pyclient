from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.concepts_api import ConceptsApi

from IPython.display import display

def search_concepts(request):
  client = get_authenticated_swagger_client(debug=True)
  concepts_api = ConceptsApi(api_client=client)
  response = concepts_api.search_concepts(all_of_us_config.workspace_namespace,
                                          all_of_us_config.workspace_id,
                                          request=request)
  return response.items

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
  
