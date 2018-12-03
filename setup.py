# -*- coding: utf-8 -*-

# Learn more: https://github.com/pmathbliss/projectpythontest2/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='projectpythontest2',
    version='0.1.0',
    description='Project Python test',
    long_description=readme,
    author='Paul M Bliss',
    author_email='pmathbliss@gmail.com',
    url='https://github.com/pmathbliss/projectpythontest2',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

