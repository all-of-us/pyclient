require "optparse"
require "fileutils"
require "json"
require "open-uri"
require_relative "../aou-utils/utils/common"
require_relative "../aou-utils/serviceaccounts"
require_relative "../aou-utils/workbench"
require_relative "../aou-utils/swagger"

# Update this whenever we want to generate libraries for the latest version of the workbench API.
API_TAG = "api_v1_9"

SWAGGER_SPEC = "https://raw.githubusercontent.com/all-of-us/workbench/#{API_TAG}/api/src/main/resources/client_api.yaml"
CDM_SPEC = "https://raw.githubusercontent.com/all-of-us/workbench/master/api/config/cdm/cdm_5_2.json"
TEST_PROJECT = "all-of-us-workbench-test"
TABLE_QUERY_FILE_NAME = "py/aou_workbench_client/swagger_client/models/table_query.py"
OPERATOR_FILE_NAME = "py/aou_workbench_client/swagger_client/models/operator.py"

def swagger_regen()
  Workbench::Swagger.download_swagger_codegen_cli

  file_opts = {:verbose => true}
  common = Common.new
  FileUtils.rm_rf('py/tmp', file_opts)
  FileUtils.mkdir('py/tmp', file_opts)
  FileUtils.copy('.swagger-codegen-ignore', 'py/tmp/.swagger-codegen-ignore', file_opts)
  common.run_inline %W{
      java -jar #{Workbench::Swagger::SWAGGER_CODEGEN_CLI_JAR}
      generate --lang python --input-spec #{SWAGGER_SPEC} --output py/tmp}  
  FileUtils.rm_rf('py/aou_workbench_client/swagger_client', file_opts)
  FileUtils.rm_rf('py/swagger_docs', file_opts)
  FileUtils.mv('py/tmp/swagger_client', 'py/aou_workbench_client/swagger_client', file_opts)
  FileUtils.mv('py/tmp/docs', 'py/swagger_docs', file_opts)
  FileUtils.mv('py/tmp/README.md', 'py/README.swagger.md', file_opts)
  FileUtils.mv('py/tmp/requirements.txt', 'py/swagger-requirements.txt', file_opts)
  FileUtils.rm_rf('py/tmp', file_opts)
  
  
  # Add an optional "table" parameter as a convenience to the generated 
  # TableQuery constructor
  text = File.read(TABLE_QUERY_FILE_NAME)
  text = text.gsub(/table_name=None,/, "table=None, table_name=None,")
  text = text.gsub(/self\.table_name = table_name/, "self.table_name = table.table_name if table else table_name")
  File.open(TABLE_QUERY_FILE_NAME, 'wb') do |f|
    f.puts text
  end
  
  # Remove the BETWEEN operator. TODO: either support BETWEEN in the materialize 
  # cohort API, or have separate operator types for different APIs.
  operator_text = File.read(OPERATOR_FILE_NAME)
  operator_text = operator_text.gsub(/BETWEEN = \"BETWEEN\"/, "")
  File.open(OPERATOR_FILE_NAME, 'wb') do |f|
    f.puts operator_text
  end
end

Common.register_command({
  :invocation => "swagger-regen",
  :description => "rebuilds the Swagger-generated client libraries",
  :fn => Proc.new { |*args| swagger_regen(*args) }
})

def capitalize(str)
   str.split('_').map {|x| x.capitalize}.join
end

ID_SUFFIX = "_id"

def remove_id(id_column)
  unless id_column.end_with? ID_SUFFIX then
    raise "Foreign key did not end with " + ID_SUFFIX
  end
  return id_column[0..(id_column.length - ID_SUFFIX.length - 1)] 
end

def escape(str)
  if str then
    return str.inspect
  end
  return '""'
end

def column_dict(column)
  return '{"Name": "' + column['name'] + 
           '", "Type": "' + column['type'] + '", "Description": ' + 
           escape(column['description']) + '}'
end

def write_tables_python(f, tables, add_to_cohort_tables)
  tables.each do |table_name, table_dict|
    table_columns = table_dict['columns']
    f.puts('class ' + capitalize(table_name) + '(object):')    
    table_columns.each do |column|
      column_name = column['name']
      f.puts('  ' + column_name + ' = "' + column_name + '"')
      domain_concept = column['domainConcept']
      if domain_concept then
         if domain_concept == 'standard' then
           f.puts('  standard_concept_id_column = "' + column_name + '"')
         else
           f.puts('  source_concept_id_column = "' + column_name + '"')
         end
      end
    end               
    f.puts('  table_name = "' + table_name + '"')
    f.puts('  columns = pd.DataFrame([' + 
        table_columns.map {|x| column_dict(x)}.join(',') + '],
        columns=["Name", "Type", "Description"])')
    f.puts('  foreign_keys = []')    
    f.puts('  table_columns["' + capitalize(table_name) + '"] = columns')
    if add_to_cohort_tables then
      f.puts('  cohort_tables.append("' + capitalize(table_name) + '")')
    end
    f.puts    
  end 
end

def write_tables_markdown(f, tables)
  tables.each do |table_name, table_dict|
    table_columns = table_dict['columns']
    f.puts('### ' + table_name)    
    f.puts
    f.puts('Name | Type | Foreign key to | Description')
    f.puts('---- | ---- | -------------- | -----------')
    table_columns.each do |column|
      foreign_key_link = ''
      if column.key?('foreignKey') then
        foreign_key_table = column['foreignKey']
        foreign_key_link = '[' + foreign_key_table + '](#' + foreign_key_table + ')'
      end      
      values = [column['name'], column['type'], foreign_key_link, column['description']]
      f.puts(values.join(' | '))      
    end
    f.puts
  end    
end

def write_foreign_keys_python(f, tables)
  tables.each do |table_name, table_dict|
    table_columns = table_dict['columns']
    table_columns.each do |column|
      if column.key?('foreignKey') then
        column_name = column['name']
        field_name = remove_id(column_name)
        f.puts(capitalize(table_name) + '.' + field_name + 
            ' = RelatedTableWrapper("' + field_name +
            '", ' + capitalize(column['foreignKey']) + '())')
        f.puts(capitalize(table_name) + '.foreign_keys.append("' + 
            field_name + '")')
      end
    end
  end
end

def cdr_regen()
  file_opts = {:verbose => true}
  open(CDM_SPEC) do |cdm_f|
    cdm_json = JSON.parse(cdm_f.read)    
    File.open('py/aou_workbench_client/cdr/model.py', 'wb') do |f|
      f.puts('#!/usr/bin/python')
      f.puts('# -*- coding: utf-8 -*-')
      f.puts('""" Model objects containing metadata on the tables and columns in the ')
      f.puts('curated data repository. These were automatically generated from the schema ')
      f.puts('found at ' + CDM_SPEC + '.')
      f.puts('"""')
      f.puts
      f.puts('from .wrapper import RelatedTableWrapper')
      f.puts('import pandas as pd')
      f.puts('from IPython.display import display, HTML')
      f.puts('table_columns = {}')
      f.puts('cohort_tables = []')
      f.puts
      f.puts('###### Table classes ')
      write_tables_python(f, cdm_json["metadataTables"], false)
      write_tables_python(f, cdm_json["cohortTables"], true)
      f.puts
      f.puts('###### Foreign keys ')
      write_foreign_keys_python(f, cdm_json["metadataTables"])
      write_foreign_keys_python(f, cdm_json["cohortTables"])
      f.puts
      f.puts('##### Helper functions')
      f.puts('def display_cdr_schema():')
      f.puts('  for table_name in sorted(table_columns):')
      f.puts('    display(HTML("<h3>" + table_name + "</h3>"))')
      f.puts('    display(table_columns[table_name])')
      f.puts('    display(HTML("<br/>"))')
      f.puts
      f.puts('def descending(column_name):')
      f.puts('  return "DESCENDING(%s)" % column_name')
      f.puts
    end
    File.open('py/aou_workbench_client/cdr/README.md', 'wb') do |f|
      f.puts('# CDR metadata documentation')
      f.puts('This documentation provides information on the tables and columns in the curated data repository.')
      f.puts('In notebook code, you can reference the names of tables and columns using the objects defined in ')
      f.puts('[model.py](model.py).')
      f.puts
      f.puts('## Cohort tables')
      f.puts('Below are tables that you can use directly when materializing a cohort, passing in their ')
      f.puts('table name for `TableQuery.table_name`.')
      f.puts
      write_tables_markdown(f, cdm_json["cohortTables"])
      f.puts
      f.puts('## Metadata tables')
      f.puts('Below are tables that provide metadata related to the cohort tables; you can retrieve ')
      f.puts('data from them by requesting data from related tables.')
      f.puts
      write_tables_markdown(f, cdm_json["metadataTables"])
    end
  end
end

Common.register_command({
  :invocation => "cdr-regen",
  :description => "rebuilds the CDR client libraries",
  :fn => Proc.new { |*args| cdr_regen(*args) }
})

def install_py_requirements()
  py_root = File.join(Workbench::WORKBENCH_ROOT, 'py')

  common = Common.new
  common.run_inline %W{
      pip install --requirement #{File.join(py_root, "requirements.txt")}
      --requirement #{File.join(py_root, "test", "test-requirements.txt")}
      --requirement #{File.join(py_root, "swagger-requirements.txt")}}
end

def test()
  config_file = File.join(Workbench::WORKBENCH_ROOT, 'py', 'test', 'all_of_us_config.json')
  ServiceAccountContext.new(TEST_PROJECT).run do    
    ENV["ALL_OF_US_CONFIG_PATH"] = config_file  
    common = Common.new
    common.run_inline [File.join(Workbench::WORKBENCH_ROOT, 'py', 'run_tests.py')]
  end
end

Common.register_command({
  :invocation => "setup-env",
  :description => "Sets up local environment for running tests",
  :fn => Proc.new { |*args| install_py_requirements() }
})

Common.register_command({
  :invocation => "test",
  :description => "Run tests",
  :fn => Proc.new { |*args| test(*args) }
})
