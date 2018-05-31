import json

import html
import pandas as pd
from IPython.display import display, HTML
from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.swagger_client.apis.concepts_api import ConceptsApi
from aou_workbench_client.swagger_client.models.domain import Domain
from aou_workbench_client.swagger_client.models.search_concepts_request import SearchConceptsRequest
from aou_workbench_client.swagger_client.models.standard_concept_filter import StandardConceptFilter
from ipywidgets import interactive

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
    ('Domain', 'domain_id'),
    ('Vocabulary', 'vocabulary_id'),
    ('Count', 'count_value')]

# TODO: add cohort picker
_CONCEPT_TABLE_HTML_TEMPLATE = """
<script language="javascript">
  var selected_row_id = null;
  var selected_row_domain = null;
  var old_selected_color = null;
  
  function select_concept(id, domain) {
    max_results = document.getElementById('max_results');
    variable_prefix = document.getElementById('variable_prefix');
    generate_code = document.getElementById('generate_code');
    max_results.disabled = false;
    max_results.style.color = '';
    variable_prefix.disabled = false;
    variable_prefix.style.color = '';
    generate_code.disabled = false;
    if (selected_row_id) {
      document.getElementById('row_' + selected_row_id).style.backgroundColor = old_selected_color;
    }
    selected_row_id = id
    selected_row_domain = domain
    new_selected_row = document.getElementById('row_' + id);
    old_selected_color = new_selected_row.style.backgroundColor;
    new_selected_row.style.backgroundColor = '#BBBBFF';    
  }
  
  function generate_python_code() {
    var kernel = IPython.notebook.kernel;
    cell_text = 'id = ' + selected_row_id;
    command = 'get_ipython().set_next_input("' + cell_text + '")';
    alert(command);
    kernel.execute(command);
  }
</script>

<table>
  <tr>
    <th>ID</th>
    <th style="text-align: left">Name</th>
    <th style="text-align: left">Code</th>
    <th style="text-align: left">Domain</th>
    <th style="text-align: left">Vocabulary</th>
    <th align=right>Count</th>
  </tr>
  %s
</table>
<table style="background: white">
   <tr style="background: white">
     <td style="background: white">Max results:</td>
     <td style="background: white"><input type="number" value="10" id="max_results" maxlength="5" 
       style="color: #999999" disabled="true"/></td>
   </tr>
   <tr style="background: white">
     <td style="background: white">Variable prefix:</td>
     <td style="background: white"><input type="text" value="results" id="variable_prefix" maxlength="20" 
       style="color: #999999" disabled="true"/>
   </tr>
   <tr style="background: white">
     <td style="background: white"><input type="button" value="Generate code" id="generate_code" 
       class="p-Widget jupyter-widgets jupyter-button widget-button" disabled="true"
       onclick="generate_python_code()"/>
   </tr>
</table>
"""

_CONCEPT_ROW_HTML_TEMPLATE = """
  <tr id="row_{id}" onclick='select_concept("{id}", {js_escaped_domain})'>
    <td>{id}</td>
    <td style="text-align: left">{name}</td>
    <td style="text-align: left">{code}</td>
    <td style="text-align: left">{domain}</td>
    <td style="text-align: left">{vocabulary}</td>
    <td>{count}</td>
  </tr>
"""

_VOCAB_DICT = {id: id for id in _VOCAB_IDS}

def search_concepts(request):
    client = get_authenticated_swagger_client()
    concepts_api = ConceptsApi(api_client=client)
    response = concepts_api.search_concepts(all_of_us_config.workspace_namespace,
                                            all_of_us_config.workspace_id,
                                            request=request)
    return response.items

def get_concept_dict(concept):
    return {f[0]: getattr(concept, f[1]) for f in _RESULT_FIELDS}

def get_concepts_frame(request):
    concepts = search_concepts(request)
    return pd.DataFrame([get_concept_dict(concept) for concept in concepts],
                        columns = [f[0] for f in _RESULT_FIELDS])

def display_concepts(request):
    concepts = search_concepts(request)
    row_html = ''
    for concept in concepts:
      row_html += _CONCEPT_ROW_HTML_TEMPLATE.format(id=concept.concept_id,
                                                    name=html.escape(concept.concept_name),
                                                    code=html.escape(concept.concept_code),
                                                    domain=html.escape(concept.domain_id),
                                                    js_escaped_domain=json.dumps(concept.domain_id),
                                                    vocabulary=html.escape(concept.vocabulary_id),
                                                    count=concept.count_value)
    table_html = _CONCEPT_TABLE_HTML_TEMPLATE % row_html
    display(HTML(table_html))

def display_concepts_fn(query, domain, vocabulary, concepts):
    request = SearchConceptsRequest(query=query, max_results=10)
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
