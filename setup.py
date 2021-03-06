# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pythontemplate',
    version='0.1.0',
    description='Python Template',
    long_description=readme,
    author='kaemiin',
    author_email='kaemiinwork@gmail.com',
    url='https://github.com/kaemiin',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    cmdclass={
        # TODO - https://github.com/kennethreitz/setup.py
    },
)
