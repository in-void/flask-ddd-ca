#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='py-rec-1',
    version=1.0,
    description='recruitment task',
    long_description=open('README.md').read(),
    url='https://github.com/in-void/py-rec-1',
    packages=find_packages(),
    license=open('LICENSE').read(),
    install_requires=[
        'requests',
    ],
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: Apache 2.0',
        'Programming Language :: Python :: 3.6',
    ),
    test_suite='tests'
)
