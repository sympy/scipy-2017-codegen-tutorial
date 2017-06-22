import os
import json
from operator import mul
from functools import reduce
import sympy as sym


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


def load_large_ode():
    """Returns a SymPy column matrix with the right hand side of the ordinary
    differential equations, i.e. 14 expressions, and a column matrix of the
    state symbols."""
    file_path = os.path.join(os.path.dirname(__file__), 'data',
                             'radiolysis_300_Gy_s.json')
    with open(file_path) as f:
        ode_def_dict = json.load(f)
    eqs, states = mk_exprs_symbs(ode_def_dict['reactions'],
                                 ode_def_dict['names'])
    rhs_of_odes = sym.Matrix(eqs)
    simpler_states = sym.symbols('y:{}'.format(len(states)))
    state_map = {s: r for s, r in zip(states, simpler_states)}
    return rhs_of_odes.xreplace(state_map), sym.Matrix(simpler_states)
