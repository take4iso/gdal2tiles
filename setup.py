#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import subprocess
from setuptools import setup, find_packages

with open('README_ORG.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def gdal_already_installed():
    try:
        from osgeo import gdal  # noqa
        return True
    except ImportError:
        return False


def get_required_gdal():
    gdal_package = 'pygdal'
    try:
        gdal_version = subprocess.check_output(
            'gdal-config --version',
            stderr=subprocess.STDOUT,
            shell=True
        ).decode('utf-8').strip()

        gdal_package = '%s==%s.*' % (gdal_package, gdal_version)
    except subprocess.CalledProcessError:
        pass

    return gdal_package


requirements = []

if not gdal_already_installed():
    requirements.append(get_required_gdal())

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Tehamalab",
    author_email='developers@tehamalab.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A python library for generating map tiles based on gdal2tiles.py script.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gdal2tiles',
    name='gdal2tiles-od',
    packages=find_packages(include=['gdal2tiles']),
    setup_requires=setup_requirements,
    extras_require={
        'billiard': ['billiard'],
    },
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tehamalab/gdal2tiles',
    version='0.1.9',
    zip_safe=False,
)
