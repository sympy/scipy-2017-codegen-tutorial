from itertools import chain  # Py 2.7 does not support func(*args1, *args2)
import sympy as sp
from scipy.integrate import odeint

class ODEsys(object):
    def __init__(self, f, y, t=None, params=(), tex_names=None):
        assert len(f) == len(y), 'f is dy/dt'
        self.f = tuple(f)
        self.y = tuple(y)
        self.t = t
        self.p = tuple(params)
        self.tex_names = tex_names
        self.j = sp.Matrix(len(f), 1, f).jacobian(y)
        self.setup()

    def setup(self):
        self.lambdified_f = sp.lambdify(self.y + self.p, self.f)
        self.lambdified_j = sp.lambdify(self.y + self.p, self.j)

    def f_eval(self, y, t, *params):
        return self.lambdified_f(*chain(y, params))

    def j_eval(self, y, t, *params):
        return self.lambdified_j(*chain(y, params))

    def integrate_odeint(self, tout, y0, params=(), **kwargs):
        return odeint(self.f_eval, y0, tout, args=tuple(params), full_output=True, Dfun=self.j_eval, **kwargs)

    def plot_result(self, tout, yout, info=None, ax=None):
        if ax is None:
            ax = plt.subplot(1, 1, 1)
        for i, label in enumerate(self.tex_names):
            ax.plot(tout, yout[:, i], label='$%s$' % label)

        ax.set_ylabel('$\mathrm{concentration\ /\ mol \cdot dm^{-3}}$')
        ax.set_xlabel('$\mathrm{time\ /\ s}$')
        ax.legend(loc='best')
        if info:
            nrhs = info.get('num_rhs')
            if not nrhs:
                nrhs = sum(info['nfe'])
            njac = info.get('num_dls_jac_evals')
            if not njac:
                njac = sum(info['nje'])
            print("The rhs was evaluated %d times and the jacobian %d times" % (nrhs, njac))
