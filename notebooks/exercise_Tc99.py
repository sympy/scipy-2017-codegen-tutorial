f = sym.lambdify([t, l1, l2, *inits], [eq.rhs for eq in analytic])  # EXERCISE: [eq.rhs for eq in analytic]
yout = f(tout, 3.2e-5, 1.04e-13, 1, 0, 0)
