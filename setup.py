#!/usr/bin/env python

import os
from setuptools import setup

data_files = []
for root, dirs, files in os.walk('data/lib/domains'):
    data_files.append((os.path.join('swot_data', root), [os.path.join(root, f) for f in files]))

setup(
    name='swot-python',
    version='1.1.0',
    description=('Swot is a community-driven or crowdsourced library for '
                 'verifying that domain names and email addresses are tied '
                 'to a legitimate university of college'),
    keywords='domain tld schools edu',
    author='Jason Horman',
    author_email='jhorman@gmail.com',
    license='MIT',
    url='http://github.com/bladenet/swot-python',
    data_files=data_files,
    py_modules=['swot'],
    install_requires=['tldextract==1.5.1', 'six'],
    test_suite='nose.collector',
    tests_require=['tldextract==1.5.1', 'nose'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
