#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='dynalist',
    version='0.1.1',
    description=(
        'Unofficial Dynalist API Written in Python'
    ),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='feng',
    author_email='edu_feng@163.com',
    maintainer='feng',
    maintainer_email='edu_feng@163.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/georgefeng/dynalist',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
