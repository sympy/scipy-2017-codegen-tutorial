from scipy.integrate import ode
from scipy2017codegen.odesys import ODEsys

class VODEsys(ODEsys):
    def integrate_vode(self, tout, y0, params=(), method='bdf', rtol=1e-8, atol=1e-8, **kwargs):
        def f(t, y, *args):
            f.ncall +=1
            return np.asarray(self.f_eval(y, t, *args))
        f.ncall = 0
        def j(t, y, *args):
            j.ncall += 1
            return np.asarray(self.j_eval(y, t, *args))
        j.ncall = 0
        r = ode(f, j)
        r.set_integrator('vode', method=method, rtol=rtol, atol=atol, **kwargs)
        if params:
            r.set_f_params(params)
            r.set_jac_params(params)
        yout = np.zeros((len(tout), len(y0)))
        yout[0, :] = y0
        r.set_initial_value(yout[0, :], tout[0])
        for idx in range(1, len(tout)):
            r.integrate(tout[idx])
            assert r.successful(), "Integration failed"
            yout[idx, :] = r.y
        return yout, {'num_rhs': f.ncall, 'num_dls_jac_evals': j.ncall}
