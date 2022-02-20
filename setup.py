"""Setup script to install a module."""

import os
from setuptools import setup, find_packages

## VERSION
# This can be loaded from the version file in the module
# Note that to note have to install this file, we read and execute the file
with open(os.path.join('modcode', 'version.py')) as version_file:
    exec(version_file.read())

## LONG DESCRIPTION
# This can be loaded from the README, is written in RST
with open('README.rst') as readme_file:
    long_description = readme_file.read()

## DEPENDENCIES
# Thsi can be loaded from the requirements file, if it's up to date / complete
with open("requirements.txt") as requirements_file:
    install_requires = requirements_file.read().splitlines()


# Do the setup
setup(
    name = 'NAME',
    version = __version__,
    description = 'Module for DOING THINGS.',
    long_description = long_description,
    python_requires = '>=3.X',
    maintainer = 'MAINTAINER NAME',
    maintainer_email = 'MAINTAINER EMAIL',
    url = 'https://github.com/ORGNAME/REPONAME',
    packages = find_packages(),
    license = 'LICENSE TYPE',
    classifiers = [
        # List of metadata about the project
    ],
    platforms = 'any',
    project_urls = {
        # Can include links for: 'Documentation', 'Bug Reports', 'Source'
    },
    download_url = 'https://github.com/ORGNAME/REPONAME/releases',
    keywords = ['LIST', 'OF', 'KEYWORDS'],
    install_requires = install_requires,
    tests_require = ['pytest'],
)
