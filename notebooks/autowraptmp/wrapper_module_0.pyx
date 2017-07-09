import numpy as np
cimport numpy as np

cdef extern from 'wrapped_code_0.h':
    void autofunc(double *y, double *dY)

def autofunc_c(np.ndarray[np.double_t, ndim=2] y):

    cdef np.ndarray[np.double_t, ndim=2] dY = np.empty((14,1))
    autofunc(<double*> y.data, <double*> dY.data)
    return dY