void cfib(int n, double *x) {
    int i;
    x[0] = 0;
    x[1] = 1;
    for (i = 2; i < n; i++) {
        x[i] = x[i-1] + x[i-2];
    }
}
