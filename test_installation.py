#!/usr/bin/env python

from sys import exit
from subprocess import check_output

try:
    from pkg_resources import parse_version
except ImportError:
    print("Setuptools must be installed for the tutorial.")

try:
    import numpy
except ImportError:
    print("NumPy is required for the tutorial")

try:
    import Cython
except ImportError:
    print("Cython is required for the tutorial")

try:
    import sympy
except ImportError:
    print("SymPy must be installed for the tutorial")
else:
    if parse_version(sympy.__version__) < parse_version('1.1'):
        print("SymPy >= 1.1 is required for the tutorial.")
    from sympy.utilities.autowrap import autowrap
    from sympy.abc import x
    from sympy import sin
    try:
        f = autowrap(sin(x), backend='cython')
        assert f(0) == 0
    except:
        msg = ("sympy.utilities.autowrap.autowrap does not work, your Cython "
               "installation or compiler may be missing")
        print(msg)

try:
    import scipy
except ImportError:
    print("Scipy is required for the tutorial")

try:
    s = check_output(['conda', '--version'])
except FileNotFoundError:
    print("conda is needed (either anaconda or miniconda from https://www.continuum.io/downloads)")
    print("(try rerunning this script under conda if you are using for system's python distribution)")
else:
    installed_version = s.decode('utf-8').strip().split(' ')[-1]
    if parse_version(installed_version) < parse_version('4.1.0'):
        msg = ("You have conda {} installed. The tutorial requires "
               "conda >= 4.1.0. Please update conda ($ conda update conda).")
        print(msg.format(installed_version))
        exit(1)

try:
    import matplotlib
except ImportError:
    print("matplotlib is required for the tutorial")

try:
    import notebook
except ImportError:
    print("notebook (jupyter notebook) is required for the tutorial")
