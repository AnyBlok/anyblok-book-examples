#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for rooms-booking"""

from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(here, 'README.rst'), 'r', encoding='utf-8'
) as readme_file:
    readme = readme_file.read()

with open(os.path.join(
    here, 'CHANGELOG.rst'), 'r', encoding='utf-8'
) as changelog_file:
    changelog = changelog_file.read()

with open(
    os.path.join(here, 'VERSION'), 'r', encoding='utf-8'
) as version_file:
    version = version_file.read().strip()

requirements = [
    'sqlalchemy',
    'anyblok',
    'psycopg2',
    'anyblok_pyramid',
    'anyblok_address',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='rooms_booking',
    version=version,
    description="Anyblok service to manage (class)rooms reservation",
    long_description=readme + '\n\n' + changelog,
    author="Pierre Verkest",
    author_email='pverkest@anybox.fr',
    url='https://github.com/Anyblok/anyblok-book-examples',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'room=rooms_booking.room:Room'
            ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='rooms-booking',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
