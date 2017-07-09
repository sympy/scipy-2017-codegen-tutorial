from libc.math cimport exp
cimport numpy as cnp
import numpy as np
import cython

cdef extern from "fastapprox/fastexp.h":
    float fastexp(float)

def cy_f_fastexp(
    cnp.ndarray[cnp.float64_t, ndim=1, mode='c'] x,
    cnp.ndarray[cnp.float64_t, ndim=1, mode='c'] y,
    cnp.ndarray[cnp.float64_t, ndim=1, mode='c'] z,
):
    cdef cnp.ndarray[cnp.float64_t, ndim=1, mode='c'] out = np.empty(x.size)
    cdef double * _x = &x[0]
    cdef double * _y = &y[0]
    cdef double * _z = &z[0]
    cdef double * _out = &out[0]
    cdef int i
    if x.size != y.size or x.size != z.size:
        raise ValueError("Inconsistent length")
    for i in range(x.size):
        _out[i] = _x[i] + fastexp(2*_y[i] + _x[i]) + fastexp(3*_z[i])
    return out