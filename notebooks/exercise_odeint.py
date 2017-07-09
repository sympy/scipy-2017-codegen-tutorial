tout = np.linspace(0, 10)
k_vals = 0.42, 0.17  # arbitrary in this case
y0 = [1, 1, 0]
yout = odeint(rhs, y0, tout, k_vals)  # EXERCISE: rhs, y0, tout, k_vals
