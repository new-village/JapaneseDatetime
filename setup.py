''' setup.py
'''
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='jpdatetime',
    version='1.0.0',
    author='new-village',
    url='https://github.com/new-village/JapaneseDatetime',
    description='This repository contains the `JapaneseDatetime` class, which extends the standard Python datetime class to support Japanese era (元号) date conversions.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'Apache-2.0 license',
    install_requires=[],
    packages=find_packages(),
    package_data={'': ['config/*.json']},
)