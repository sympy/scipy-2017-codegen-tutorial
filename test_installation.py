#!/usr/bin/env python

from sys import exit

try:
    import sympy
except ImportError:
    print("SymPy must be installed for the tutorial")

if sympy.__version__ != '1.1':
    print("SymPy 1.1 is required for the tutorial. Note SymPy 1.1 will be released before July 10.")

try:
    import numpy
except ImportError:
    print("NumPy is required for the tutorial")

try:
    import Cython
except ImportError:
    print("Cython is required for the tutorial")

try:
    import scipy
except ImportError:
    print("scipy is required for the tutorial")

from sympy.utilities.autowrap import ufuncify
from sympy.abc import x
from sympy import sin

try:
    f = ufuncify(x, sin(x))
    assert f(0) == 0
except:
    print("sympy.utilities.autowrap.ufuncify does not work")
    raise
