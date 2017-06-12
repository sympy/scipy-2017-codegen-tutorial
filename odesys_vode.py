from odesys import ODEsys

from scipy.integrate import ode
from odesys import ODEsys

class VODEsys(ODEsys):
    def integrate_vode(self, tout, y0, params=(), method='bdf', **kwargs):
        r = ode(self.f_eval, jac=self.j_eval)
        r.set_integrator('vode', method=method, **kwargs)
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
        return yout, {
            'num_steps': r.iwork[10], 'num_rhs': r.iwork[11], 'num_jac': r.iwork[12],
            'num_lu_factor': r.iwork[18], 'num_nonlin_solv_iters': r.iwork[19],
            'num_nonlin_solv_conv_failures': r.iwork[20], 'num_err_test_fails': r.iwork[21]
        }
