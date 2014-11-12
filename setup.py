#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'six',
    'Django>=1.6',
    'South==1.0.1',  # For Django 1.6 compatibility
    'django-model-utils>=2.2',
    'django-markitup>=2.2.2',
    'pillow>=2.6.1',
    'Markdown>=2.5.1',
]

test_requirements = [
    # None, these go into the test_requirements file
]

setup(
    name='django-andablog',
    version='1.7.1',
    description='A blog app that is intended to embed within an existing Django site.',
    long_description=readme + '\n\n' + history,
    author='Ivan Ven Osdel',
    author_email='ivan@wimpyanalytics.com',
    url='https://github.com/WimpyAnalytics/django-andablog',
    packages=[
        'djangoandablog',
    ],
    package_dir={'djangoandablog':
                 'djangoandablog'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='django-andablog',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
