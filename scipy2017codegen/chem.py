import os
import json
from operator import mul
from functools import reduce
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np


def prod(seq):
    return reduce(mul, seq) if seq else 1


def mk_exprs_symbs(rxns, names):
    concs = sym.symbols(names, real=True, nonnegative=True)
    c_dict = dict(zip(names, concs))
    f = {n: 0 for n in names}
    for coeff, r_stoich, net_stoich in rxns:
        r = sym.S(coeff)*prod([c_dict[rk]**p for rk, p in r_stoich.items()])
        for nk, nm in net_stoich.items():
            f[nk] += nm*r
    return [f[n] for n in names], concs


def mk_rsys(ODEcls, reactions, names, params=(), **kwargs):
    f, symbs = mk_exprs_symbs(reactions, names)
    return ODEcls(f, symbs, params=map(sym.S, params), **kwargs)


def load_watrad():
    """Loads the water radiolysis system data.

    Returns
    -------
    eqs : list
        List of SymPy equations representing the system of first-order
        differential equations.
    states : tuple
        Tuple of SymPy symbols representing the state variables.
    """
    file_path = os.path.join(os.path.dirname(__file__), 'data',
                             'radiolysis_300_Gy_s.json')
    with open(file_path) as f:
        ode_def_dict = json.load(f)
    eqs, states = mk_exprs_symbs(ode_def_dict['reactions'],
                                 ode_def_dict['names'])
    return eqs, states


def load_large_ode():
    """Returns a SymPy column matrix with the right hand side of the ordinary
    differential equations, i.e. 14 expressions, and a column matrix of the
    state symbols."""
    eqs, states = load_watrad()
    rhs_of_odes = sym.Matrix(eqs)
    simpler_states = sym.symbols('y:{}'.format(len(states)))
    state_map = {s: r for s, r in zip(states, simpler_states)}
    return rhs_of_odes.xreplace(state_map), sym.Matrix(simpler_states)


def watrad_init():
    """Returns initial conditions for the water radiolysis system.

    Returns
    -------
    y0 : list
        List of initial conditions for each state variable.
    t : ndarray, shape (n,)
        Array of time values to integrate over appropriate for the system.
    """
    eqs, states = load_watrad()
    t = np.logspace(-6, 3, 200) # close to one hour of operation
    c0 = {'H2O': 55.4e3, 'H+': 1e-4, 'OH-': 1e-4}
    y0 = [c0.get(symb.name, 0) for symb in states]
    return y0, t


def watrad_plot(t, y):
    """Generates a plot of the water radiolysis data.

    Parameters
    ----------
    t : ndarray, shape (n,)
        Time values at which the system was evaluated.
    y : ndarray, shape (n, n_states)
        State variables at each time point.
    """
    eqs, states = load_watrad()
    fig, ax = plt.subplots(1, 1, figsize=(14, 6))
    ax = ax or plt.subplot(1, 1, 1)
    for i, state in enumerate(states):
        ax.plot(t, y[:, i], label='$%s$' % state.name)
    ax.set_ylabel('$\mathrm{concentration\ /\ mol \cdot dm^{-3}}$')
    ax.set_xlabel('$\mathrm{time\ /\ s}$')
    ax.legend(loc='best')
    ax.set_xscale('log')
    ax.set_yscale('log')
