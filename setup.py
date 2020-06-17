from setuptools import setup, find_packages


setup(
    name='plaque diversity',
    version='1.0',
    install_requires=[
        'setuptools-yaml'
    ],
    metadata_yaml = 'environment.yml',
    packages=find_packages()
)