import os
import uuid
import sympy as sp
import setuptools
import numpy as np
import pyximport
from odesys import ODEsys

lapack_libs = ['openblas']
pyximport.install()
setup_args={
    'include_dirs': [os.getcwd()],
    'libraries': lapack_libs + ['sundials_cvode', 'sundials_nvecserial', 'm']
}

pyxbld_template = """
def make_ext(modname, pyxfilename):
    from setuptools import Extension
    return Extension(
        name=modname,
        sources=[pyxfilename],
        include_dirs=%(include_dirs)s,
        libraries=%(libraries)s
    )
"""

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
