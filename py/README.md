# AllOfUs Python Client Library

Python code in this library is used to access the AllOfUs Workbench API from
the context of a Jupyter notebook. 

## Installing the library

The latest version of the library will be installed automatically on the Jupyter
server your notebook code runs in, but if you need to upgrade to a version which 
has not been released yet, you can do so by running in a notebook cell:

```
!pip install --user --upgrade 'https://github.com/all-of-us/pyclient/archive/<VERSION>.zip#egg=aou_workbench_client&subdirectory=py'
```

or for Python 2.7:

```
!pip2.7 install --user --upgrade 'https://github.com/all-of-us/pyclient/archive/<VERSION>.zip#egg=aou_workbench_client&subdirectory=py'
```

and then restarting your Python kernel.

The modules you will use in your code are in the aou_workbench_client package.

## Using cohorts in a notebook

The aou_workbench_client.cohorts module provides functions for materializing cohorts:

### materialize_cohort

materialize_cohort is used to fetch some or all results of cohort materialization.
This can be used to retrieve information about some or all of the participants in a
cohort you defined in the AllOfUs workbench.

#### Parameters 
Name | Description
---------- | --------  
**request** | A [[MaterializeCohortRequest]](swagger_docs/MaterializeCohortRequest.md) indicating what cohort to materialize, what filtering and ordering criteria to apply, and what fields to retrieve.
**max_results ** | The maximum number of results to retrieve. Defaults to returning all results for the specified request. This may require multiple server calls -- request.page_size specifies the maximum number retrieved per call.  
 


