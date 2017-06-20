import os
import sys
import uuid
import sympy as sp
import setuptools
import numpy as np
import setuptools
import pyximport
from scipy2017codegen import templates
from scipy2017codegen.odesys import ODEsys

pyximport.install()
libraries = ['sundials_cvode', 'sundials_nvecserial']
extra_link_args = []

if os.name != 'nt':
    libraries += ['m']

if os.name == 'posix':
    libraries += ['openblas']

if 'CONDA_PREFIX' in os.environ:
    osx = sys.platform.lower() == 'darwin'
    prefix_path = lambda *args: os.path.join(os.environ['CONDA_PREFIX'], *args)
    sundials_inc = [prefix_path('Library', 'include') if osx else prefix_path('include')]
    library_dirs = [prefix_path('Library', 'lib') if osx else prefix_path('lib')]
    if osx:
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


class ODEcvode(ODEsys):

    default_integrator = 'cvode'

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
        open('integrate_serial_%s.c' % self.uid, 'wt').write(templates.sundials['integrate_serial.c'] % ctx)
        open('%s.pyx' % self.mod_name, 'wt').write(templates.sundials['_integrate_serial.pyx'] % {'uid': self.uid})
        open('%s.pyxbld' % self.mod_name, 'wt').write(templates.pyxbld % {k: str(v) for k, v in setup_args.items()})
        self.mod = __import__(self.mod_name)
        self.integrate_odeint = None

    def integrate_cvode(self, tout, y0, params=(), rtol=1e-8, atol=1e-8, **kwargs):
        return self.mod._integrate(np.asarray(tout, dtype=np.float64),
                                   np.asarray(y0, dtype=np.float64),
                                   np.atleast_1d(np.asarray(params, dtype=np.float64)),
                                   abstol=np.atleast_1d(np.asarray(atol, dtype=np.float64)),
                                   reltol=rtol,
                                   **kwargs)
