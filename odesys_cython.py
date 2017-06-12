import uuid
import numpy as np
import sympy as sp
import setuptools
import pyximport
from odesys import ODEsys

pyximport.install()

cython_template = """
cimport numpy as cnp
import numpy as np

def f(cnp.ndarray[cnp.float64_t, ndim=1] y, double t, %(args)s):
    cdef cnp.ndarray[cnp.float64_t, ndim=1] out = np.empty(y.size)
    %(f_exprs)s
    return out

def j(cnp.ndarray[cnp.float64_t, ndim=1] y, double t, %(args)s):
    cdef cnp.ndarray[cnp.float64_t, ndim=2] out = np.empty((y.size, y.size))
    %(j_exprs)s
    return out

"""
pyxbld_template = open('template.pyxbld').read()

class CythonODEsys(ODEsys):

    def setup(self):
        self.mod_name = 'ode_cython_%s' % uuid.uuid4().hex[:10]
        idxs = list(range(len(self.f)))
        subs = {s: sp.Symbol('y[%d]' % i) for i, s in enumerate(self.y)}
        f_exprs = ['out[%d] = %s' % (i, str(self.f[i].xreplace(subs))) for i in idxs]
        j_exprs = ['out[%d, %d] = %s' % (ri, ci, self.j[ri, ci].xreplace(subs)) for ri in idxs for ci in idxs]
        ctx = dict(
            args=', '.join(map(str, self.p)),
            f_exprs = '\n    '.join(f_exprs),
            j_exprs = '\n    '.join(j_exprs),
        )
        open('%s.pyx' % self.mod_name, 'wt').write(cython_template % ctx)
        open('%s.pyxbld' % self.mod_name, 'wt').write(pyxbld_template % dict(
            include_dirs=[np.get_include()],
            library_dirs=[], libraries=[], extra_compile_args=[], extra_link_args=[]
        ))
        mod = __import__(self.mod_name)
        self.f_eval = mod.f
        self.j_eval = mod.j
