import unittest
from aou_workbench_client.config import all_of_us_config
from aou_workbench_client.auth import get_authenticated_swagger_client
from aou_workbench_client.swagger_client.apis.workspaces_api import WorkspacesApi

class WorkspaceApiTest(unittest.TestCase):

    def test_get_workspaces(self):
      workspace_api = WorkspacesApi(api_client=get_authenticated_swagger_client())
      workspaces = workspace_api.get_workspaces()
      self.assertEquals([], workspaces.items)      

    def test_get_workspace(self):      
      workspace_api = WorkspacesApi(api_client=get_authenticated_swagger_client())
      workspace = workspace_api.get_workspace(all_of_us_config.workspace_namespace,
                                              all_of_us_config.workspace_id)
      self.assertEquals("my new workspace", workspace.workspace.name)
