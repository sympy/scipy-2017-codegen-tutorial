import os
import sys
import uuid
import sympy as sp
import setuptools
import numpy as np
import setuptools
import pyximport
from odesys import ODEsys

pyximport.install()
libraries = ['sundials_cvode', 'sundials_nvecserial']
extra_link_args = []

if os.name != 'nt':
    libraries += ['m']

if os.name == 'posix':
    libraries += ['openblas']

if 'CONDA_PREFIX' in os.environ:
    prefix_path = lambda *args: os.path.join(os.environ['CONDA_PREFIX'], *args)
    sundials_inc = [prefix_path('Library', 'include')]
    library_dirs = [prefix_path('Library', 'lib')]
    if sys.platform.lower() == 'darwin':
        extra_link_args = ['-Wl,-rpath,%s/' % prefix_path('lib')]
else:
    sundials_inc = []
    library_dirs = []

setup_args={
    'include_dirs': [os.getcwd(), np.get_include()] + sundials_inc,
    'library_dirs': library_dirs,
    'libraries': libraries,
    'extra_compile_args': [],
    'extra_link_args': extra_link_args
}

pyxbld_template = open('template.pyxbld').read()

class ODEcvode(ODEsys):

    def setup(self):
        self.uid = uuid.uuid4().hex[:10]
        self.mod_name = 'ode_c_%s' % self.uid
        idxs = list(range(len(self.f)))
        subs = {s: sp.Symbol('y[%d]' % i) for i, s in enumerate(self.y)}
        f_exprs = ['out[%d] = %s;' % (i, sp.ccode(self.f[i].xreplace(subs)))
                   for i in idxs]
        j_col_defs = ['realtype * const col_%d = DENSE_COL(J, %d);' % (ci, ci)
                      for ci in idxs]
        j_exprs = ['col_%d[%d] = %s;' % (ci, ri, self.j[ri, ci].xreplace(subs))
                   for ci in idxs for ri in idxs if self.j[ri, ci] != 0]
        ctx = dict(
            func = '\n    '.join(f_exprs + ['return 0;']),
            dense_jac = '\n    '.join(j_col_defs + j_exprs + ['return 0;']),
            band_jac = 'return -1;'
        )
        cvode_template = open(os.path.join('sundials_templates', 'integrate_serial.c')).read()
        cython_template = open(os.path.join('sundials_templates', '_integrate_serial.pyx')).read()
        open('integrate_serial_%s.c' % self.uid, 'wt').write(cvode_template % ctx)
        open('%s.pyx' % self.mod_name, 'wt').write(cython_template % {'uid': self.uid})
        open('%s.pyxbld' % self.mod_name, 'wt').write(pyxbld_template % {k: str(v) for k, v in setup_args.items()})
        self.mod = __import__(self.mod_name)
        self.integrate_odeint = None

    def integrate(self, tout, y0, params=(), rtol=1e-8, atol=1e-8, **kwargs):
        return self.mod._integrate(np.asarray(tout, dtype=np.float64),
                                   np.asarray(y0, dtype=np.float64),
                                   np.atleast_1d(np.asarray(params, dtype=np.float64)),
                                   abstol=np.atleast_1d(np.asarray(atol, dtype=np.float64)),
                                   reltol=rtol,
                                   **kwargs)
