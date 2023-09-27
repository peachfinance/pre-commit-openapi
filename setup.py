from setuptools import setup

setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=[
        'jsonschema==3.2.0', 
        'openapi-spec-validator==0.4.0'
    ],
    scripts=['bin/check-many-openapi'],
)