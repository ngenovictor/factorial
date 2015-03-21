#!/usr/bin/env python
"""Factorial project"""
from setuptools import find_packages, setup

setup(name = 'factorial',
    version = '1.0',
    description = "Factorial module.",
    long_description = "A test module for our book.",
    platforms = ["Windows"],
    author="Victor Ngeno",
    author_email="ngenovictor321@gmail.com",
    url="http://github.com/nongeveekay/factorial",
    license = "MIT",
    packages=find_packages()
    )
