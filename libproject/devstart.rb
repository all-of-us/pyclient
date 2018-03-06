require "optparse"
require "fileutils"
require_relative "../aou-utils/utils/common"
require_relative "../aou-utils/serviceaccounts"
require_relative "../aou-utils/workbench"
require_relative "../aou-utils/swagger"

# Update this whenever we want to generate libraries for the latest version of the workbench API.
API_TAG = "api_v1_1"

SWAGGER_SPEC = "https://raw.githubusercontent.com/all-of-us/workbench/#{API_TAG}/api/src/main/resources/workbench.yaml"
TEST_PROJECT = "all-of-us-workbench-test"

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
end

Common.register_command({
  :invocation => "swagger-regen",
  :description => "rebuilds the Swagger-generated client libraries",
  :fn => Proc.new { |*args| swagger_regen(*args) }
})

def install_py_requirements()
  py_root = File.join(Workbench::WORKBENCH_ROOT, 'py')

  common = Common.new
  common.run_inline %W{
      pip install --requirement #{File.join(py_root, "requirements.txt")}
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
