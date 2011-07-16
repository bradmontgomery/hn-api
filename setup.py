#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for hn-api."""

from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='hn-api',
    version=version,
    description="python library for Unofficial access to HackerNews",
    long_description=open('README.mdown').read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'License :: Simplified BSD License',
        'Intended Audience :: Developers',
    ],
    keywords='HackerNews API',
    author='Scott Jackson',
    url='https://github.com/scottjacksonx/hn-api',
    license='BSD',
    packages=['hnapi', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)

