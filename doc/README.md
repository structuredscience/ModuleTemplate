# Documentation

Notes on creating documentation with sphinx.

## Overview

Typical workflow for using sphinx:
- install sphinx
    our projects have a `requirements-docs.txt` file, listing dependencies for building the docs
- if starting fresh, do 'sphinx-quickstart'
- edit conf.py (or sometimes Makefile) to control configurations, plugins, and builds
- edit / write .rst files in the doc folder to create content for the website
    - also, sometimes want to tweak in code documentation, to control how it get rendered
    - note: sphinx builds from the installed version of the module
- run build & examine locally
- to deploy, post the build to where it's hosted
    - for us, this is Github pages, and is done by `make install`

Sphinx related files:
- `conf.py`: sphinx configuration file, which manages settings for the documentation website

One option for managing and making sphinx builds and deploys is to use a `Makefile`.

## Glossary

sphinx
    A documentation tool for Python. Sphinx is like a 'platform', with a plugin structure.
    Basically, a way to write stuff in rst, and convert this into html.

sphinx-gallery
    A plugin for sphinx that let's you write out rst tutorials and render them on the site.
    Also autogenerates notebook versions of the examples.

github-pages
    A service on Github to get a URL host webpages.

markup language
    A human-readable language that defines 'tags' in a document, that can control how the document gets rendered.

markdown
    A markup language.

restructured text (rst)
    Another markup language. Developed and used by the Python community.

directives
    Directives are an rst construct, that sphinx uses. Sphinx defines a whole bunch of directives.
    Control element to insert a general pattern (and/or functionally, this can be to create a map / link).
        indicated as `.. directive::` (then indented block).
    Directives, as a construct, are from the rst format. Sphinx defines and uses it's own directives.
    Directives can also take options, as `:option: value`. The 'value' is optional.
    Together this looks like, for example:
        .. autosummary::
            :toctree: generated/
            Object

inline directives
    Inline directives / formatting are done as :directive:`input`.
    For example  :func:`my_function` or :math:`\chi`

toc
    Stands for 'table of contents'.
    'toctree' ends up being equivalent to 'path'.
    Sphinx wants everything listed in a toc somewhere.

## Notes

Tricks to sphinx
    Linking. A big part of what sphinx does is mapping between things.
    Getting everything to link properly is part of getting the documentation site set up properly.
    Managing all of the general configurations & tuning to specific use cases / managing exceptions, etc.

Linking
    Sphinx (& plugins) pull directly from source code.
    So, it matters where objects (functions / classes) get pulled from in the module.
        This relates to where functions are aliased (in `__init__.py`'s), and where they get linked to.
        This linking, on the API page and in sphinx-gallery files, has to be consistent for it all to work.

    In sphinx-gallery, can use inline directives, like :class: or :func:, to link to an API listing.
        Example - :class:`~file.object`
            the ~means hide the leading path from display
        Example - :func:`~.method`
            the leading '.' means don't specify full path, go find it in path

    In API page
        The autosummary directive (.. autosummary::) means build docs from the docstring (uses autodoc to do so).
        The currentmodule directive (.. currentmodule:: module) links to where to get docstrings from.
            This matters for file names in /generated, which in turn matters for linking in sphinx-gallery, etc.

## LINKS

sphinx
    https://www.sphinx-doc.org/en/master/
sphinx-gallery
    https://sphinx-gallery.github.io/stable/index.html
rst cheatsheet
    https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
numpydoc-standard
    https://numpydoc.readthedocs.io/en/latest/format.html
