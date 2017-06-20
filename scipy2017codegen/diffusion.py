from operator import mul
from functools import reduce
import numpy as np
import sympy as sp
from scipy2017codegen.odesys import ODESys


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
        j_out = np.empty(self.ny*self.n_lines, self.ny*self.n_lines)  # dense matrix
        for i in range(self.n_lines):
            slc = slice(i*self.ny, (i+1)*self.ny)
            j_out[slc, slc] = self.lambdified_j(*chain(y[slc], params))
            k = self.central_reference_bin(i)
            for j in range(self.ny):
                j_out[i*self.ny + j, (k-1)*self.ny + j] +=    self.D[j]/self.dx**2
                j_out[i*self.ny + j, (k  )*self.ny + j] += -2*self.D[j]/self.dx**2
                j_out[i*self.ny + j, (k+1)*self.ny + j] +=    self.D[j]/self.dx**2
        return j_out

    def second_derivaties_spatial(i, y, out):
        k = self.central_reference_bin(i)
        for j in range(self.ny):
            left = y[(k-1)*self.ny + j]
            cent = y[(k  )*self.ny + j]
            rght = y[(k+1)*self.ny + j]
            out[j] = (left - 2*cent + rght)/self.dx**2
