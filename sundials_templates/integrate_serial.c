#include <cvode/cvode.h>             /* prototypes for CVODE fcts., CV_BDF, CV_ADAMS */
#include <nvector/nvector_serial.h>  /* serial N_Vector types, fcts., macros */

#include <sundials/sundials_dense.h> /* definitions DlsMat DENSE_ELEM */
#include <sundials/sundials_types.h> /* definition of type realtype */

#include <string.h> // memcpy
#if defined(WITH_LAPACK)
  #include <cvode/cvode_lapack.h>       /* prototype for CVDense */
  // Sundials 2.7.0 changed int -> long int, but BLAS uses int
  // We use DIM_T defined here:
  #define DIM_T int
  #define OUR_DENSE CVLapackDense
  #define OUR_BAND CVLapackBand
#else
  #include <cvode/cvode_dense.h>       /* prototype for CVDense */
  #include <cvode/cvode_band.h>        /* prototype for CVBand */
  #define OUR_DENSE CVDense
  #define OUR_BAND CVBand
  #define DIM_T long int
#endif


int func (realtype t, N_Vector nv_y, N_Vector f, void * params) {
    const realtype * const restrict y = &NV_Ith_S(nv_y, 0);
    realtype * const restrict out = &NV_Ith_S(f, 0);
    %(func)s
}

int dense_jac (DIM_T N, realtype t, N_Vector nv_y, N_Vector fy, DlsMat J, void *params, N_Vector tmp1, N_Vector tmp2, N_Vector tmp3) {
    const realtype * const restrict y = &NV_Ith_S(nv_y, 0);
    %(dense_jac)s
}

int band_jac (DIM_T N, long int mu, long int ml, realtype t, N_Vector y, N_Vector fy, DlsMat J, void *params, N_Vector tmp1, N_Vector tmp2, N_Vector tmp3) {
    %(band_jac)s
}

enum {
  STATUS_FOUT = 1000,
  STATUS_Y,
  STATUS_ABSTOL,
  STATUS_STEP_TYPE,
  STATUS_CVODE_MEM,
};

int integrate(const realtype * const restrict tout,
              const realtype * const restrict y0,
              int nt, DIM_T ny,
              void * params,
              const realtype * const restrict abstol,
              realtype reltol,
              realtype h_init, realtype h_max,
              realtype * const restrict yout,
              int step_type_idx, // 1 => CV_ADAMS, 2 => CV_BDF
              int mode,  // 1 => SUNDIALS_DENSE, 2 => SUNDIALS_BAND
              int mu, // number of upper diagonals (when banded)
              int ml, // number of lower diagonals (when banded)
              long int * const restrict info)
{
    int status = 0;
    N_Vector nv_y = NULL;
    N_Vector nv_abstol = NULL;
    void *cvode_mem = NULL;
    realtype cur_t = tout[0];

    nv_y = N_VMake_Serial(ny, (realtype *)y0);
    if (nv_y == NULL){
        status = STATUS_Y;
        goto exit_y;
    }

    nv_abstol = N_VMake_Serial(ny, (realtype *)abstol);
    if (nv_abstol == NULL){
        status = STATUS_ABSTOL;
        goto exit_abstol;
    }

    if (step_type_idx == 1){
        step_type_idx = CV_ADAMS;
    }else if (step_type_idx == 2) {
        step_type_idx = CV_BDF;  
    }else{
        status = STATUS_STEP_TYPE;
        goto exit_abstol;
    }

    // For now we skip CV_FUNCTIONAL only use CV_NEWTON
    cvode_mem = CVodeCreate(step_type_idx, CV_NEWTON); 
    if (cvode_mem == NULL){
        status = STATUS_CVODE_MEM;
        goto exit_cvode_mem;
    }

    status = CVodeInit(cvode_mem, func, tout[0], nv_y);
    if (status != 0) goto exit_runtime;

    status = CVodeSVtolerances(cvode_mem, reltol, nv_abstol);
    if (status != 0) goto exit_runtime;

    /* Call CVDense/CVLapackDense to specify the dense linear solver */
    switch(mode){
    case(SUNDIALS_DENSE):
        status = OUR_DENSE(cvode_mem, ny);
        if (status != 0) goto exit_runtime;
        /* Set the Jacobian routine to Jac (user-supplied) */
        status = CVDlsSetDenseJacFn(cvode_mem, dense_jac); 
        break;
    case(SUNDIALS_BAND):
        status = OUR_BAND(cvode_mem, ny, mu, ml);
        if (status != 0) goto exit_runtime;
        status = CVDlsSetBandJacFn(cvode_mem, band_jac); 
        break;
    }
    if (status != 0) goto exit_runtime;

    status = CVodeSetUserData(cvode_mem, params);
    if (status != 0) goto exit_runtime;

    if (h_init > 0.0) CVodeSetInitStep(cvode_mem, h_init);
    if (h_max > 0.0) CVodeSetMaxStep(cvode_mem, h_max);

    /* Store output before first step */
    memcpy(yout, y0, sizeof(realtype)*ny);
    /* Run integration */
    for (int i = 1; i < nt; ++i){
        status = CVode(cvode_mem, tout[i], nv_y, &cur_t, CV_NORMAL);
        if (status != CV_SUCCESS)
            break;
        memcpy(yout + ny*i, &NV_Ith_S(nv_y, 0), sizeof(realtype)*ny); // copy to output argument;
    }
    CVodeGetNumSteps(cvode_mem, info);
    CVodeGetNumRhsEvals(cvode_mem, info + 1);
    CVodeGetNumLinSolvSetups(cvode_mem, info + 2);
    CVodeGetNumErrTestFails(cvode_mem, info + 3);
    CVodeGetNumNonlinSolvIters(cvode_mem, info + 4);
    CVodeGetNumNonlinSolvConvFails(cvode_mem, info + 5);
    CVDlsGetNumJacEvals(cvode_mem, info + 6);
    CVDlsGetNumRhsEvals(cvode_mem, info + 7);
    // Error handling
 exit_runtime:
    CVodeFree(&cvode_mem);
 exit_cvode_mem: 
    N_VDestroy_Serial(nv_abstol);
 exit_abstol:
    N_VDestroy_Serial(nv_y);
 exit_y:
    return status;
}
