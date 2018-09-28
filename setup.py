#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'dynalist', '__version__.py'),
          mode='r') as f:
    exec(f.read(), about)

with open('README.md', mode='r') as f:
    readme = f.read()

setup(
    name=about['__name__'],
    description=about['__description__'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__authoremail__'],
    url=about['__url__'],
    version=about['__version__'],
    packages=find_packages(),
    install_requires=['requests>=2.18.3','six==1.10.0'],
    keywords=['dynalist', 'api'],
    license=about['__license__'],
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


# from setuptools import setup, find_packages

# setup(
#     name='dynalist',
#     version='0.2.0',
#     description=(
#         'Unofficial Dynalist API Written in Python'
#     ),
#     long_description=open('README.md').read(),
#     long_description_content_type="text/markdown",
#     author='feng',
#     author_email='edu_feng@163.com',
#     maintainer='feng',
#     maintainer_email='edu_feng@163.com',
#     license='MIT License',
#     packages=find_packages(),
#     platforms=["all"],
#     url='https://github.com/georgefeng/dynalist',
#     install_requires=[
#         'requests',
#     ],
#     classifiers=[
#         'Operating System :: OS Independent',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: MIT License',
#         'Programming Language :: Python',
#         'Programming Language :: Python :: Implementation',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#     ],
# )
