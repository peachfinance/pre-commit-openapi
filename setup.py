from setuptools import setup

setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=[
        'openapi-spec-validator==0.7.1'
    ],
    scripts=['bin/check-many-openapi'],
)