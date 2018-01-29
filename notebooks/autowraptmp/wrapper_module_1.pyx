import numpy as np
cimport numpy as np

cdef extern from 'wrapped_code_1.h':
    void autofunc(double *y, double *out_6389966900307177364)

def autofunc_c(np.ndarray[np.double_t, ndim=2] y):

    cdef np.ndarray[np.double_t, ndim=2] out_6389966900307177364 = np.empty((14,14))
    autofunc(<double*> y.data, <double*> out_6389966900307177364.data)
    return out_6389966900307177364