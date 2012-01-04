#!/usr/bin/env python

import distutils.core
import subprocess
import sys
# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

kwargs = {}

major, minor = sys.version_info[:2]

if major >= 3:
    import setuptools # setuptools is required for use_2to3
    kwargs["use_2to3"] = True

distutils.core.setup(
    name="imo",
    version="0.0.1",
    packages = ["imo"],
    author="Alek Storm",
    author_email="alek.storm@gmail.com",
    description="A Python interface to the IMO Vocabulary Portal",
    **kwargs
)
