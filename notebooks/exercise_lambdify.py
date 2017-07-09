t = sym.symbols('t')  # not used in this case.
f = sym.lambdify((y, t) + k, ydot)  # EXERCISE: (y, t) + k
