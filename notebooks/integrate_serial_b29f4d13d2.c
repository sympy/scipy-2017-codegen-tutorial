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

#ifdef _MSC_VER
# ifndef restrict
#  define restrict __restrict
# endif
#endif


int func (realtype t, N_Vector nv_y, N_Vector f, void * params) {
    const realtype * const restrict y = &NV_Ith_S(nv_y, 0);
    realtype * const restrict out = &NV_Ith_S(f, 0);
    out[0] = -14520000.0*pow(y[0], 2) - 20900000.0*y[0]*y[11] - 0.0158*y[0]*y[1] - 27600000.0*y[0]*y[4] - 35500000.0*y[0]*y[5] - 13600000.0*y[0]*y[6] - 22900000.0*y[0]*y[7] - 13000000.0*y[0]*y[8] - 13000000.0*y[0]*y[9] + 24400.0*y[2]*y[4] + 5.83*y[4] + 0.0854;
    out[1] = -14520000.0*pow(y[0], 2) - 0.0158*y[0]*y[1] - 27600000.0*y[0]*y[4] - 26000000.0*y[0]*y[8] - 1270.0*y[10]*y[1] + 4070000.0*y[10]*y[5] + 118000000.0*y[11]*y[2] - 1270.0*y[12]*y[1] - 4.58e-8*y[1]*y[4] - 0.000155*y[1]*y[8] - 2.12e-5*y[1] + 24400.0*y[2]*y[4] + 13300000.0*y[2]*y[5] + 13300000.0*y[2]*y[6] + 13300000.0*y[2]*y[9] + 39500.0*y[3]*y[5] + 10900000.0*y[4]*y[5] + 36500.0*y[4]*y[6] + 29200.0*y[5]*y[6] + 8840000.0*y[5]*y[9] + 2.6e-7*y[6] - 101000.0*y[8]*y[9] - 0.131;
    out[2] = 14520000.0*pow(y[0], 2) + 0.0158*y[0]*y[1] + 27600000.0*y[0]*y[4] + 35500000.0*y[0]*y[5] + 13600000.0*y[0]*y[6] + 26000000.0*y[0]*y[8] + 786000.0*y[10]*y[12] + 1270.0*y[10]*y[1] - 118000000.0*y[11]*y[2] + 1270.0*y[12]*y[1] + 128000.0*y[12]*y[3] + 4070000.0*y[12]*y[6] + 0.000155*y[1]*y[8] + 2.12e-5*y[1] - 24400.0*y[2]*y[4] - 13300000.0*y[2]*y[5] - 13300000.0*y[2]*y[6] - 13300000.0*y[2]*y[9] + 11000000.0*y[5]*y[8] + 101000.0*y[8]*y[9];
    out[3] = 7260000.0*pow(y[0], 2) + 27600000.0*y[0]*y[4] - 128000.0*y[12]*y[3] + 4.58e-8*y[1]*y[4] - 39500.0*y[3]*y[5] + 5140000.0*pow(y[4], 2) + 0.0136;
    out[4] = 20900000.0*y[0]*y[11] + 0.0158*y[0]*y[1] - 27600000.0*y[0]*y[4] + 128000.0*y[12]*y[3] - 4.58e-8*y[1]*y[4] - 24400.0*y[2]*y[4] + 39500.0*y[3]*y[5] - 10280000.0*pow(y[4], 2) - 10900000.0*y[4]*y[5] - 36500.0*y[4]*y[6] - 13100000.0*y[4]*y[7] - 11400000.0*y[4]*y[8] - 11400000.0*y[4]*y[9] - 5.83*y[4] + 0.0188;
    out[5] = -35500000.0*y[0]*y[5] + 13600000.0*y[0]*y[6] - 4070000.0*y[10]*y[5] + 50200000.0*y[11]*y[12] + 1270.0*y[12]*y[1] + 4.58e-8*y[1]*y[4] - 13300000.0*y[2]*y[5] - 39500.0*y[3]*y[5] - 10900000.0*y[4]*y[5] + 36500.0*y[4]*y[6] + 22800000.0*y[4]*y[9] - 9620000.0*pow(y[5], 2) - 29200.0*y[5]*y[6] - 11000000.0*y[5]*y[8] - 8840000.0*y[5]*y[9] - 0.0943*y[5] + 0.0871;
    out[6] = -13600000.0*y[0]*y[6] + 13000000.0*y[0]*y[8] + 50200000.0*y[10]*y[11] + 1270.0*y[10]*y[1] - 4070000.0*y[12]*y[6] - 13300000.0*y[2]*y[6] - 36500.0*y[4]*y[6] + 4810000.0*pow(y[5], 2) - 29200.0*y[5]*y[6] - 0.09430026*y[6] + 101000.0*y[8]*y[9] + 840.0*pow(y[9], 2) + 0.0221;
    out[7] = -22900000.0*y[0]*y[7] - 3750000.0*y[12]*y[7] + 2620.0*y[13] - 13100000.0*y[4]*y[7] + 11000000.0*y[5]*y[8] + 8840000.0*y[5]*y[9] + 1.3e-7*y[6] + 101000.0*y[8]*y[9] + 840.0*pow(y[9], 2) + 8.19e-7;
    out[8] = 22900000.0*y[0]*y[7] - 13000000.0*y[0]*y[8] + 786000.0*y[10]*y[12] + 4070000.0*y[10]*y[5] - 50200000.0*y[11]*y[8] - 0.000155*y[1]*y[8] + 13300000.0*y[2]*y[9] - 11400000.0*y[4]*y[8] - 11000000.0*y[5]*y[8] - 101000.0*y[8]*y[9] + 773000.0*y[9];
    out[9] = -13000000.0*y[0]*y[9] + 50200000.0*y[11]*y[8] + 4070000.0*y[12]*y[6] + 0.000155*y[1]*y[8] - 13300000.0*y[2]*y[9] + 13100000.0*y[4]*y[7] - 11400000.0*y[4]*y[9] + 29200.0*y[5]*y[6] - 8840000.0*y[5]*y[9] - 101000.0*y[8]*y[9] - 1680.0*pow(y[9], 2) - 773000.0*y[9];
    out[10] = 13000000.0*y[0]*y[9] - 50200000.0*y[10]*y[11] - 786000.0*y[10]*y[12] - 1270.0*y[10]*y[1] - 4070000.0*y[10]*y[5] + 13300000.0*y[2]*y[6] + 11400000.0*y[4]*y[8] + 0.0943*y[6];
    out[11] = -20900000.0*y[0]*y[11] - 50200000.0*y[10]*y[11] - 50200000.0*y[11]*y[12] - 118000000.0*y[11]*y[2] - 50200000.0*y[11]*y[8] + 2.12e-5*y[1] + 5.83*y[4] + 0.0943*y[5] + 0.0943*y[6] + 773000.0*y[9] + 0.0854;
    out[12] = -786000.0*y[10]*y[12] - 50200000.0*y[11]*y[12] - 1270.0*y[12]*y[1] - 128000.0*y[12]*y[3] - 4070000.0*y[12]*y[6] - 3750000.0*y[12]*y[7] + 2620.0*y[13] + 13300000.0*y[2]*y[5] + 0.0943*y[5];
    out[13] = 3750000.0*y[12]*y[7] - 2620.0*y[13];
    return 0;
}

int dense_jac (DIM_T N, realtype t, N_Vector nv_y, N_Vector fy, DlsMat J, void *params, N_Vector tmp1, N_Vector tmp2, N_Vector tmp3) {
    const realtype * const restrict y = &NV_Ith_S(nv_y, 0);
    realtype * const col_0 = DENSE_COL(J, 0);
    realtype * const col_1 = DENSE_COL(J, 1);
    realtype * const col_2 = DENSE_COL(J, 2);
    realtype * const col_3 = DENSE_COL(J, 3);
    realtype * const col_4 = DENSE_COL(J, 4);
    realtype * const col_5 = DENSE_COL(J, 5);
    realtype * const col_6 = DENSE_COL(J, 6);
    realtype * const col_7 = DENSE_COL(J, 7);
    realtype * const col_8 = DENSE_COL(J, 8);
    realtype * const col_9 = DENSE_COL(J, 9);
    realtype * const col_10 = DENSE_COL(J, 10);
    realtype * const col_11 = DENSE_COL(J, 11);
    realtype * const col_12 = DENSE_COL(J, 12);
    realtype * const col_13 = DENSE_COL(J, 13);
    col_0[0] = -29040000.0*y[0] - 20900000.0*y[11] - 0.0158*y[1] - 27600000.0*y[4] - 35500000.0*y[5] - 13600000.0*y[6] - 22900000.0*y[7] - 13000000.0*y[8] - 13000000.0*y[9];
    col_0[1] = -29040000.0*y[0] - 0.0158*y[1] - 27600000.0*y[4] - 26000000.0*y[8];
    col_0[2] = 29040000.0*y[0] + 0.0158*y[1] + 27600000.0*y[4] + 35500000.0*y[5] + 13600000.0*y[6] + 26000000.0*y[8];
    col_0[3] = 14520000.0*y[0] + 27600000.0*y[4];
    col_0[4] = 20900000.0*y[11] + 0.0158*y[1] - 27600000.0*y[4];
    col_0[5] = -35500000.0*y[5] + 13600000.0*y[6];
    col_0[6] = -13600000.0*y[6] + 13000000.0*y[8];
    col_0[7] = -22900000.0*y[7];
    col_0[8] = 22900000.0*y[7] - 13000000.0*y[8];
    col_0[9] = -13000000.0*y[9];
    col_0[10] = 13000000.0*y[9];
    col_0[11] = -20900000.0*y[11];
    col_1[0] = -0.0158*y[0];
    col_1[1] = -0.0158*y[0] - 1270.0*y[10] - 1270.0*y[12] - 4.58e-8*y[4] - 0.000155*y[8] - 2.12e-5;
    col_1[2] = 0.0158*y[0] + 1270.0*y[10] + 1270.0*y[12] + 0.000155*y[8] + 2.12e-5;
    col_1[3] = 4.58e-8*y[4];
    col_1[4] = 0.0158*y[0] - 4.58e-8*y[4];
    col_1[5] = 1270.0*y[12] + 4.58e-8*y[4];
    col_1[6] = 1270.0*y[10];
    col_1[8] = -0.000155*y[8];
    col_1[9] = 0.000155*y[8];
    col_1[10] = -1270.0*y[10];
    col_1[11] = 2.12000000000000e-5;
    col_1[12] = -1270.0*y[12];
    col_2[0] = 24400.0*y[4];
    col_2[1] = 118000000.0*y[11] + 24400.0*y[4] + 13300000.0*y[5] + 13300000.0*y[6] + 13300000.0*y[9];
    col_2[2] = -118000000.0*y[11] - 24400.0*y[4] - 13300000.0*y[5] - 13300000.0*y[6] - 13300000.0*y[9];
    col_2[4] = -24400.0*y[4];
    col_2[5] = -13300000.0*y[5];
    col_2[6] = -13300000.0*y[6];
    col_2[8] = 13300000.0*y[9];
    col_2[9] = -13300000.0*y[9];
    col_2[10] = 13300000.0*y[6];
    col_2[11] = -118000000.0*y[11];
    col_2[12] = 13300000.0*y[5];
    col_3[1] = 39500.0*y[5];
    col_3[2] = 128000.0*y[12];
    col_3[3] = -128000.0*y[12] - 39500.0*y[5];
    col_3[4] = 128000.0*y[12] + 39500.0*y[5];
    col_3[5] = -39500.0*y[5];
    col_3[12] = -128000.0*y[12];
    col_4[0] = -27600000.0*y[0] + 24400.0*y[2] + 5.83;
    col_4[1] = -27600000.0*y[0] - 4.58e-8*y[1] + 24400.0*y[2] + 10900000.0*y[5] + 36500.0*y[6];
    col_4[2] = 27600000.0*y[0] - 24400.0*y[2];
    col_4[3] = 27600000.0*y[0] + 4.58e-8*y[1] + 10280000.0*y[4];
    col_4[4] = -27600000.0*y[0] - 4.58e-8*y[1] - 24400.0*y[2] - 20560000.0*y[4] - 10900000.0*y[5] - 36500.0*y[6] - 13100000.0*y[7] - 11400000.0*y[8] - 11400000.0*y[9] - 5.83;
    col_4[5] = 4.58e-8*y[1] - 10900000.0*y[5] + 36500.0*y[6] + 22800000.0*y[9];
    col_4[6] = -36500.0*y[6];
    col_4[7] = -13100000.0*y[7];
    col_4[8] = -11400000.0*y[8];
    col_4[9] = 13100000.0*y[7] - 11400000.0*y[9];
    col_4[10] = 11400000.0*y[8];
    col_4[11] = 5.83000000000000;
    col_5[0] = -35500000.0*y[0];
    col_5[1] = 4070000.0*y[10] + 13300000.0*y[2] + 39500.0*y[3] + 10900000.0*y[4] + 29200.0*y[6] + 8840000.0*y[9];
    col_5[2] = 35500000.0*y[0] - 13300000.0*y[2] + 11000000.0*y[8];
    col_5[3] = -39500.0*y[3];
    col_5[4] = 39500.0*y[3] - 10900000.0*y[4];
    col_5[5] = -35500000.0*y[0] - 4070000.0*y[10] - 13300000.0*y[2] - 39500.0*y[3] - 10900000.0*y[4] - 19240000.0*y[5] - 29200.0*y[6] - 11000000.0*y[8] - 8840000.0*y[9] - 0.0943;
    col_5[6] = 9620000.0*y[5] - 29200.0*y[6];
    col_5[7] = 11000000.0*y[8] + 8840000.0*y[9];
    col_5[8] = 4070000.0*y[10] - 11000000.0*y[8];
    col_5[9] = 29200.0*y[6] - 8840000.0*y[9];
    col_5[10] = -4070000.0*y[10];
    col_5[11] = 0.0943000000000000;
    col_5[12] = 13300000.0*y[2] + 0.0943;
    col_6[0] = -13600000.0*y[0];
    col_6[1] = 13300000.0*y[2] + 36500.0*y[4] + 29200.0*y[5] + 2.6e-7;
    col_6[2] = 13600000.0*y[0] + 4070000.0*y[12] - 13300000.0*y[2];
    col_6[4] = -36500.0*y[4];
    col_6[5] = 13600000.0*y[0] + 36500.0*y[4] - 29200.0*y[5];
    col_6[6] = -13600000.0*y[0] - 4070000.0*y[12] - 13300000.0*y[2] - 36500.0*y[4] - 29200.0*y[5] - 0.09430026;
    col_6[7] = 1.30000000000000e-7;
    col_6[9] = 4070000.0*y[12] + 29200.0*y[5];
    col_6[10] = 13300000.0*y[2] + 0.0943;
    col_6[11] = 0.0943000000000000;
    col_6[12] = -4070000.0*y[12];
    col_7[0] = -22900000.0*y[0];
    col_7[4] = -13100000.0*y[4];
    col_7[7] = -22900000.0*y[0] - 3750000.0*y[12] - 13100000.0*y[4];
    col_7[8] = 22900000.0*y[0];
    col_7[9] = 13100000.0*y[4];
    col_7[12] = -3750000.0*y[12];
    col_7[13] = 3750000.0*y[12];
    col_8[0] = -13000000.0*y[0];
    col_8[1] = -26000000.0*y[0] - 0.000155*y[1] - 101000.0*y[9];
    col_8[2] = 26000000.0*y[0] + 0.000155*y[1] + 11000000.0*y[5] + 101000.0*y[9];
    col_8[4] = -11400000.0*y[4];
    col_8[5] = -11000000.0*y[5];
    col_8[6] = 13000000.0*y[0] + 101000.0*y[9];
    col_8[7] = 11000000.0*y[5] + 101000.0*y[9];
    col_8[8] = -13000000.0*y[0] - 50200000.0*y[11] - 0.000155*y[1] - 11400000.0*y[4] - 11000000.0*y[5] - 101000.0*y[9];
    col_8[9] = 50200000.0*y[11] + 0.000155*y[1] - 101000.0*y[9];
    col_8[10] = 11400000.0*y[4];
    col_8[11] = -50200000.0*y[11];
    col_9[0] = -13000000.0*y[0];
    col_9[1] = 13300000.0*y[2] + 8840000.0*y[5] - 101000.0*y[8];
    col_9[2] = -13300000.0*y[2] + 101000.0*y[8];
    col_9[4] = -11400000.0*y[4];
    col_9[5] = 22800000.0*y[4] - 8840000.0*y[5];
    col_9[6] = 101000.0*y[8] + 1680.0*y[9];
    col_9[7] = 8840000.0*y[5] + 101000.0*y[8] + 1680.0*y[9];
    col_9[8] = 13300000.0*y[2] - 101000.0*y[8] + 773000.0;
    col_9[9] = -13000000.0*y[0] - 13300000.0*y[2] - 11400000.0*y[4] - 8840000.0*y[5] - 101000.0*y[8] - 3360.0*y[9] - 773000.0;
    col_9[10] = 13000000.0*y[0];
    col_9[11] = 773000.000000000;
    col_10[1] = -1270.0*y[1] + 4070000.0*y[5];
    col_10[2] = 786000.0*y[12] + 1270.0*y[1];
    col_10[5] = -4070000.0*y[5];
    col_10[6] = 50200000.0*y[11] + 1270.0*y[1];
    col_10[8] = 786000.0*y[12] + 4070000.0*y[5];
    col_10[10] = -50200000.0*y[11] - 786000.0*y[12] - 1270.0*y[1] - 4070000.0*y[5];
    col_10[11] = -50200000.0*y[11];
    col_10[12] = -786000.0*y[12];
    col_11[0] = -20900000.0*y[0];
    col_11[1] = 118000000.0*y[2];
    col_11[2] = -118000000.0*y[2];
    col_11[4] = 20900000.0*y[0];
    col_11[5] = 50200000.0*y[12];
    col_11[6] = 50200000.0*y[10];
    col_11[8] = -50200000.0*y[8];
    col_11[9] = 50200000.0*y[8];
    col_11[10] = -50200000.0*y[10];
    col_11[11] = -20900000.0*y[0] - 50200000.0*y[10] - 50200000.0*y[12] - 118000000.0*y[2] - 50200000.0*y[8];
    col_11[12] = -50200000.0*y[12];
    col_12[1] = -1270.0*y[1];
    col_12[2] = 786000.0*y[10] + 1270.0*y[1] + 128000.0*y[3] + 4070000.0*y[6];
    col_12[3] = -128000.0*y[3];
    col_12[4] = 128000.0*y[3];
    col_12[5] = 50200000.0*y[11] + 1270.0*y[1];
    col_12[6] = -4070000.0*y[6];
    col_12[7] = -3750000.0*y[7];
    col_12[8] = 786000.0*y[10];
    col_12[9] = 4070000.0*y[6];
    col_12[10] = -786000.0*y[10];
    col_12[11] = -50200000.0*y[11];
    col_12[12] = -786000.0*y[10] - 50200000.0*y[11] - 1270.0*y[1] - 128000.0*y[3] - 4070000.0*y[6] - 3750000.0*y[7];
    col_12[13] = 3750000.0*y[7];
    col_13[7] = 2620.00000000000;
    col_13[12] = 2620.00000000000;
    col_13[13] = -2620.00000000000;
    return 0;
}

int band_jac (DIM_T N, long int mu, long int ml, realtype t, N_Vector y, N_Vector fy, DlsMat J, void *params, N_Vector tmp1, N_Vector tmp2, N_Vector tmp3) {
    return -1;
}

enum {
  STATUS_FOUT = 1000,
  STATUS_Y,
  STATUS_ABSTOL,
  STATUS_STEP_TYPE,
  STATUS_CVODE_MEM,
  STATUS_MODE
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
    int i;
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
    case(1): // SUNDIALS_DENSE
        status = OUR_DENSE(cvode_mem, ny);
        if (status != 0) goto exit_runtime;
        /* Set the Jacobian routine to Jac (user-supplied) */
        status = CVDlsSetDenseJacFn(cvode_mem, dense_jac); 
        break;
    case(2):  // SUNDIALS_BAND
        status = OUR_BAND(cvode_mem, ny, mu, ml);
        if (status != 0) goto exit_runtime;
        status = CVDlsSetBandJacFn(cvode_mem, band_jac); 
        break;
    default:
        status = STATUS_MODE;
    }
    if (status != 0) goto exit_runtime;

    status = CVodeSetUserData(cvode_mem, params);
    if (status != 0) goto exit_runtime;

    if (h_init > 0.0) CVodeSetInitStep(cvode_mem, h_init);
    if (h_max > 0.0) CVodeSetMaxStep(cvode_mem, h_max);

    /* Store output before first step */
    memcpy(yout, y0, sizeof(realtype)*ny);
    /* Run integration */
    for (i = 1; i < nt; ++i){
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
