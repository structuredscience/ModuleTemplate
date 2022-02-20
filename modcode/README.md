# Module Code

Notes on writing module code.

## Documentating Code

numpydoc

    The numpydoc-standard is a docstring standard, for how to write docstrings.
    The numpydoc package is a sphinx extension to use numpydoc-standard formatted docstrings with sphinx.

## Doctest

Doctests are code snippets that can be written into the docstrings, to serve as working examples of code usage. 

Notably, these working examples can be automatically run. 

Note that `doctest` is a standard library module to test examples written into docstrings.

The genereal format is to have a sections of the docstring called `Examples`. 
Within this, lines with ">>> " indicate code snippets to be run.

#### Doctest Examples

For examples of doctests, check the NeuroDSP module (https://github.com/neurodsp-tools/neurodsp). 
Note that one of the goals of doctests is to write in this `Example` section, that gets rendered on the documentation website.

For example,
- InCode: https://github.com/neurodsp-tools/neurodsp/blob/main/neurodsp/sim/periodic.py#L43
- InDocs: https://neurodsp-tools.github.io/neurodsp/generated/neurodsp.sim.sim_oscillation.html
- Examples that simulate example data: https://github.com/neurodsp-tools/neurodsp/blob/main/neurodsp/spectral/power.py

#### Doctest Goals

The goal of doctests is to provide a minimal example of running the function.

In terms of scope, typically we want:
- a _very_ simplified version of running the function
- first, write a plain text sentence explaining the
- if there are multiple "ways" to use the function, then there can be multiple different examples
- keep each example specific to this function (generally, not adding subsequent processing / plotting, etc)

#### Doctest HowTos

Technical notes on doctests:
- and code after `>>>` will get run by doctests
- anything written right after a code line is the expected output
- if you want to set a doctest line to _not_ run, add `# doctest:+SKIP` at the end of the line
- the tests that run when you open a PR will now check the doctests

#### Running Doctests

Once you have pytest installed, you can check doctests locally by doing:
```
# Move into the 'spiketools' folder '~/spiketools/spiketools` (eg. `cd `spiketools`)
# Run doctests, ignoring the tests folder
pytest --doctest-modules --ignore=tests
```
OR
```
# Run this command from the base repository ('~/spiketools/)
pytest --doctest-modules --ignore=spiketools/tests spiketools
```

## Links

Useful links:
- numpydoc-standard: https://numpydoc.readthedocs.io/en/latest/format.html
