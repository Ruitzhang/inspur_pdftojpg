#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='inspur_pdf2jpg',
    version=1.0,
    description=(
        '<项目的简单描述>'
    ),
    long_description=open('README.rst').read(),
    author='zhangrt',
    author_email='18734428944@163.com',
    maintainer='zhangrt',
    maintainer_email='18734428944@163.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    # url='<项目的网址，我一般都是github的url>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)