''' setup.py
'''
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='jpdatetime',
    version='1.2.0',
    author='new-village',
    url='https://github.com/new-village/JapaneseDatetime',
    description="The jpdatetime library extends Python's datetime to support Japanese eras (元号). It allows parsing and formatting dates in Japanese eras",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'Apache-2.0 license',
    install_requires=[],
    packages=find_packages(),
    package_data={'': ['config/*.json']},
)