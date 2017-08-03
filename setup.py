#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname

from coalesce import __version__

setup(
    name='coalesce',
    version=__version__,
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    description='simple Python library with coalesce function and "magic" empty value',
    author='Alexander Bryazgin',
    author_email='bryazgin64@gmail.com',
    url='https://github.com/bryazginnn/coalesce',
    packages=find_packages(),
)
