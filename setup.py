#!/usr/bin/env python

from __future__ import absolute_import

from setuptools import find_packages, setup

import edx_oauth2_provider

setup(
    name='edx-oauth2-provider',
    version=edx_oauth2_provider.__version__,
    description='Provide OAuth2 access to edX installations',
    author='edX',
    url='https://github.com/edx/edx-oauth2-provider',
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django==2.2.19',
        # 'edx-django-oauth2-provider>=1.2.1,<2.0.0',
        'edx-django-oauth2-provider @ git+https://github.com/shadinaif/django-oauth2-provider@shadinaif/new_auth#egg=edx-django-oauth2-provider',
        'PyJWT>=1.4.0,<2.0.0'
    ]
)
