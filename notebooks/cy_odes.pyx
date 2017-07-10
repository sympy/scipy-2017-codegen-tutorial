import numpy as np
cimport numpy as cnp # cimport gives us access to NumPy's C API

# here we just replicate the function signature from the header
cdef extern from "c_odes.h":
    void c_odes(double *y, double *dY)

# here is the "wrapper" signature that conforms to the odeint interface
def cy_odes(cnp.ndarray[cnp.double_t, ndim=1] y, double t):
    # preallocate our output array
    cdef cnp.ndarray[cnp.double_t, ndim=1] dY = np.empty(y.size, dtype=np.double)
    # now call the C function
    c_odes(<double *> y.data, <double *> dY.data)
    # return the result
    return dY