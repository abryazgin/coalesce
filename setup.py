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
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
