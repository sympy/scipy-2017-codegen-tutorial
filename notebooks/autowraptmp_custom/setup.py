try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
from Cython.Build import cythonize
cy_opts = {}
import numpy as np

ext_mods = [Extension(
    'wrapper_module_2', ['wrapper_module_2.pyx', 'wrapped_code_2.c'],
    include_dirs=['/home/travis/build/sympy/scipy-2017-codegen-tutorial/scipy2017codegen/fastapprox', np.get_include()],
    library_dirs=[],
    libraries=[],
    extra_compile_args=['-std=c99'],
    extra_link_args=[]
)]
setup(ext_modules=cythonize(ext_mods, **cy_opts))
