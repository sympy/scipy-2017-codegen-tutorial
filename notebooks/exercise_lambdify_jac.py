J = sym.Matrix(ydot).jacobian(y)  # EXERCISE: jacobian
J_cb = sym.lambdify((y, t) + k, J)  # EXERCISE: (y, t) + k
