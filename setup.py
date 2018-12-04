#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


requires = ['Sphinx']

setup(
    name='sphinxcontrib-lastupdate',
    version='1.0',
    url='https://github.com/synthesio/sphinxcontrib-lastupdate',
    download_url='https://pypi.org/project/sphinxcontrib-lastupdate',
    license='MIT',
    author='Dejan Filipovic',
    author_email='dfilipovic@synthesio.com',
    description='Sphinx lastupdate extension',
    long_description=README,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
