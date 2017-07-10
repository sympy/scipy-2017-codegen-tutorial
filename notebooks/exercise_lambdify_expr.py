d2fdxdy = expr.diff(x, y)  # EXERCISE: x, y
func = sym.lambdify([x, y], d2fdxdy)  # EXERCISE: lambdify
zplot = func(xplot, yplot)
