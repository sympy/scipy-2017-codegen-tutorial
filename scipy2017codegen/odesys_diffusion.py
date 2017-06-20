from itertools import chain
import numpy as np
import matplotlib.pyplot as plt
from scipy2017codegen.odesys import ODEsys


class MOLsys(ODEsys):
    """ System of ODEs based on method of lines on the interval x = [0, x_end] """

    def __init__(self, *args, **kwargs):
        self.x_end = kwargs.pop('x_end')
        self.n_lines = kwargs.pop('n_lines')
        self.D = kwargs.pop('D')
        self.dx = self.x_end / self.n_lines
        super(MOLsys, self).__init__(*args, **kwargs)

    def f_eval(self, y, t, *params):
        f_out = np.empty(self.ny*self.n_lines)
        for i in range(self.n_lines):
            slc = slice(i*self.ny, (i+1)*self.ny)
            y_bis = self.second_derivatives_spatial(i, y, f_out[slc])
            f_out[slc] *= self.D
            f_out[slc] += self.lambdified_f(*chain(y[slc], params))
        return f_out

    def central_reference_bin(self, i):
        return np.clip(i, 1, self.ny - 2)

    def j_eval(self, y, t, *params):
        j_out = np.zeros((self.ny*self.n_lines, self.ny*self.n_lines))  # dense matrix
        for i in range(self.n_lines):
            slc = slice(i*self.ny, (i+1)*self.ny)
            j_out[slc, slc] = self.lambdified_j(*chain(y[slc], params))
            k = self.central_reference_bin(i)
            for j in range(self.ny):
                j_out[i*self.ny + j, (k-1)*self.ny + j] +=    self.D[j]/self.dx**2
                j_out[i*self.ny + j, (k  )*self.ny + j] += -2*self.D[j]/self.dx**2
                j_out[i*self.ny + j, (k+1)*self.ny + j] +=    self.D[j]/self.dx**2
        return j_out

    def second_derivatives_spatial(self, i, y, out):
        k = self.central_reference_bin(i)
        for j in range(self.ny):
            left = y[(k-1)*self.ny + j]
            cent = y[(k  )*self.ny + j]
            rght = y[(k+1)*self.ny + j]
            out[j] = (left - 2*cent + rght)/self.dx**2

    def integrate(self, tout, y0, params=(), **kwargs):
        y0 = np.array(np.vstack(y0).T.flat)
        yout, info = super(MOLsys, self).integrate(tout, y0, params, **kwargs)
        return yout.reshape((tout.size, self.n_lines, self.ny)).transpose((0, 2, 1)), info

    def x_centers(self):
        return np.linspace(self.dx/2, self.x_end - self.dx/2, self.n_lines)

    def plot_result(self, tout, yout, info=None, ax=None):
        ax = ax or plt.subplot(1, 1, 1)
        x_lines = self.x_centers()
        for i, t in enumerate(tout):
            for j in range(self.ny):
                c = [0.0, 0.0, 0.0]
                c[j] = t/tout[-1]
                plt.plot(x_lines, yout[i, j, :], color=c)
        self.print_info(info)
