require "optparse"
require "fileutils"
require_relative "../aou-utils/utils/common"
require_relative "../aou-utils/serviceaccounts"
require_relative "../aou-utils/workbench"
require_relative "../aou-utils/swagger"

# Update this whenever we want to generate libraries for the latest version of the workbench API.
SWAGGER_SPEC = 'https://raw.githubusercontent.com/all-of-us/workbench/fac5e45d578d1e5f6d735824a89b1d4f5a8f8f37/api/src/main/resources/workbench.yaml'
TEST_PROJECT = "all-of-us-workbench-test"

def swagger_regen()
  Workbench::Swagger.download_swagger_codegen_cli

  common = Common.new
  common.run_inline %W{
      java -jar #{Workbench::Swagger::SWAGGER_CODEGEN_CLI_JAR}
      generate --lang python --input-spec #{SWAGGER_SPEC} --output py/tmp}
  file_opts = {:verbose => true}
  FileUtils.rm_rf('py/aou_workbench_client/swagger_client', file_opts)
  FileUtils.rm_rf('py/swagger_docs', file_opts)
  FileUtils.mv('py/tmp/swagger_client', 'py/aou_workbench_client/swagger_client', file_opts)
  FileUtils.mv('py/tmp/docs', 'py/swagger_docs', file_opts)
  FileUtils.mv('py/tmp/README.md', 'py/README.swagger.md', file_opts)
  FileUtils.mv('py/tmp/requirements.txt', 'py/swagger-requirements.txt', file_opts)
  FileUtils.remove_dir('py/tmp', file_opts)
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

def pylint()
  py_module_root = File.join(Workbench::WORKBENCH_ROOT, 'py', 'aou_workbench_client')
  rc_file_path = File.join(Workbench::WORKBENCH_ROOT, 'aou-utils', 'pylintrc')

  # As well as the client Python module, lint setup.py and other support files.
  Dir.chdir(File.join(Workbench::WORKBENCH_ROOT, 'py'))
  support_py_files = Dir.glob('*.py').map(&File.method(:realpath))

  enabled = "bad-indentation,broad-except,bare-except,logging-too-many-args," +
      "unused-argument,redefined-outer-name,redefined-builtin," +
      "superfluous-parens,syntax-error,trailing-whitespace,unused-import," +
      "unused-variable," +
      "undefined-variable,bad-whitespace,line-too-long,unused-import," +
      "unused-variable"

  common = Common.new
  common.run_inline %W{pylint --rcfile #{rc_file_path} --reports=n --score=n
      --ignore=swagger_client --disable=all --enable=#{enabled}
      #{py_module_root}} + support_py_files
end

Common.register_command({
  :invocation => "pylint",
  :description => "Lint Python",
  :fn => Proc.new { |*args| pylint(*args) }
})

def test()
  config_file = File.join(Workbench::WORKBENCH_ROOT, 'py', 'all_of_us_config.json')
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
