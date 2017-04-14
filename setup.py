# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

PY2 = sys.version_info[0] == 2

requires = ['wp-version-checker']

if PY2:
    requires.append('futures')

setup(
    name="argos-plugin-monitoring",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'argos-plugin-monitoring=monitoring:run',
        ]
    },
    py_modules=['monitoring'],
    author="Dundee",
    author_email="daniel@milde.cz",
    description="Argos plugin for monitoring",
    license="GPL",
    keywords="argos monitoring",
    url="https://github.com/Dundee/argos-plugin-monitoring",
    long_description=long_description,
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ]
)
