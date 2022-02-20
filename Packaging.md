# Packaging a Python module

Notes on releasing a Python module.

## Overview

This covers releasing a Python module through PYPI.

A new package release should have:
- A tagged release on Github
- A new uploaded release to PYPI (this is what pip uses)
- A new associated documentation build, reflecting the new version number

## Releasing

To release a new version of a tool, you will need an account on both PYPI and TestPYPI.

Uploading to PYPI:
- Build a distribution:
    - `python setup.py sdist bdist_wheel`
- Upload to PYPI (depends on a .pypirc file):
    - `twine upload --repository pypi dist/*`

Release Candidates
    You can use the version numbers to indicate candidate releases
    These are treated as pre-releases on PYPI - only installed if explicitly requested.

## Tools

PyPA
    'Python Packaging Authority'
    A working group that manages projects for Python packaging.

PyPI
    'Python Package Index'
    A 'place'. It is a repository of Python software packages
    https://pypi.org
    Is also 'testpypi', a test instance of the PYPI repository
    https://test.pypi.org/

pip
    A tool (package) for installing Python packages. By default, gets things from PYPI.

twine
    A utility (package) for publishing Python packages on PYPI.
    Does the uploading step to PYPI.
    https://twine.readthedocs.io/en/latest/

setuptools
    A tool (package) for Python packaging.
    https://setuptools.readthedocs.io/en/latest/

## Links

An overview of packaging, as an overview of preparing a package:
    https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

A guide for setting up and using the pypirc file:
    https://truveris.github.io/articles/configuring-pypirc/

pip vs. conda
    Blog post on differences
        https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/
    conda-forge
        Community collections for conda
        https://conda-forge.org

Semantic versioning
    A specification for how to use meaningful version numbers
    https://semver.org
