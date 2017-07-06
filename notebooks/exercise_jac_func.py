def J_func(y, t, mu):
    return np.array([
        [0, 1],
        [-1-2*mu*y[0]*y[1], mu*(1-y[0]**2)]  # EXERCISE: -1-2*mu*y[0]*y[1]
    ])
