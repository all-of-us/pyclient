"""A setuptools based module for PIP installation of the AoU Workbench Python client."""
# Docs/example setup.py: https://github.com/pypa/sampleproject/blob/master/setup.py

import os
from setuptools import setup, find_packages


client_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(client_dir, 'requirements.txt')) as requirements:
    requirements_list = [l.strip() for l in requirements.readlines()]
with open(os.path.join(client_dir, 'swagger-requirements.txt')) as swagger_requirements:
    requirements_list += [l.strip() for l in swagger_requirements.readlines()]


setup(
        # This is what people 'pip install'.
        name='aou-workbench-client',

        # TODO(danrodney) Automatically provide a version string here, bumped when publishing
        # (maybe from swagger-regen).
        version='1.1.1',
        
        long_description="""\        
        Python client library for interacting with the AllOfUs workbench API.
        """,
        
        url='https://github.com/all-of-us/pyclient',

        # These packages may be imported after the egg is installed. (We want all Python packages
        # rooted under client/py, so we use automatic discovery.)
        packages=find_packages(),

        install_requires=requirements_list,
)
