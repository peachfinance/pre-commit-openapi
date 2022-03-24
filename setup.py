from setuptools import setup


setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=['openapi-spec-validator==0.2.9'],
    python_requires='>=3',
    packages=['src'],
    entry_points={
        'console_scripts': [
            'check-valid-openapi = check_valid_openapi:main',
        ],
    }
)
