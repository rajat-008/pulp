#!/usr/bin/env/python
"""
Setup script for PuLP added by Stuart Mitchell 2007
Copyright 2007 Stuart Mitchell
"""
import sys
from setuptools import setup

readme_name = 'README.rst'


# License = open('LICENSE').read()

# read the version number safely from the constants.py file
version_dict = {}
exec(open('pulp/constants.py').read(), version_dict)
VERSION = version_dict['VERSION']

with open(readme_name, "r") as fh:
    long_description = fh.read()

setup(name="PuLP",
      version=VERSION,
      description=
      "PuLP is an LP modeler written in python. PuLP can generate MPS or LP files and call GLPK, COIN CLP/CBC, CPLEX, and GUROBI to solve linear problems.",
      long_description = long_description,
      long_description_content_type = "text/x-rst",
      # license = License,
      keywords = ["Optimization", "Linear Programming", "Operations Research"],
      author="J.S. Roy and S.A. Mitchell",
      author_email="pulp@stuartmitchell.com",
      url="https://github.com/coin-or/pulp",
      classifiers = ['Development Status :: 5 - Production/Stable',
                     'Environment :: Console',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: BSD License',
                     'Natural Language :: English',
                     'Programming Language :: Python',
                     'Topic :: Scientific/Engineering :: Mathematics',
      ],
      #need the cbc directories here as the executable bit is set
      packages = ['pulp',
      'pulp.solverdir',
      'pulp.solverdir.cbc.linux.32',
      'pulp.solverdir.cbc.linux.64',
      'pulp.solverdir.cbc.win.32',
      'pulp.solverdir.cbc.win.64',
      'pulp.solverdir.cbc.osx.64',
      'pulp.solverdir.choco',
      ],
      package_data = {'pulp.solverdir.cbc.linux.32' : ['*','*.*'],
                      'pulp.solverdir.cbc.linux.64' : ['*','*.*'],
                      'pulp.solverdir.cbc.win.32' : ['*','*.*'],
                      'pulp.solverdir.cbc.win.64' : ['*','*.*'],
                      'pulp.solverdir.cbc.osx.64' : ['*','*.*'],
                      'pulp.solverdir.choco' : ['*','*.*'],
                      },
      include_package_data=True,
      install_requires = ['pyparsing>=2.0.1'],
      entry_points = ("""
      [console_scripts]
      pulptest = pulp.tests.run_tests:pulpTestAll
      """
      ),
)
