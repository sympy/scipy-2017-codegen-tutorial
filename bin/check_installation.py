from sys import exit

try:
    import sympy
except ImportError:
    exit("SymPy must be installed for the tutorial")

if sympy.__version__ != '1.1':
    exit("SymPy 1.1 is required for the tutorial")

try:
    import numpy
except ImportError:
    exit("NumPy is required for the tutorial")

try:
    import Cython
except ImportError:
    exit("Cython is required for the tutorial")

try:
    import scipy
except ImportError:
    exit("scipy is required for the tutorial")

from sympy.utilities.autowrap import ufuncify
from sympy.abc import x
from sympy import sin

try:
    f = ufuncify(x, sin(x))
    assert f(0) == 0
except:
    print("sympy.utilities.autowrap.ufuncify does not work")
    raise
