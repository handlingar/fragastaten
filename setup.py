from __future__ import print_function

import os
import codecs

from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()

setup(
    name="fragastaten",
    version="0.1.1",
    url='https://github.com/okfse/fragastaten',
    license='', #FIXME
    description="Froide installation for OKFN Sweden",
    long_description=read('README.txt'),
    author='',
    author_email='',
    packages=find_packages(),
    install_requires=['froide'],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)
