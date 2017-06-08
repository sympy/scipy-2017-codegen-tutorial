from operator import mul
from functools import reduce
import sympy as sp
from odesys import ODEsys

def prod(seq):
    return reduce(mul, seq) if seq else 1

def mk_rsys(rxns, names):
    concs = sp.symbols(names, real=True, nonnegative=True)
    c_dict = dict(zip(names, concs))
    f = {n: 0 for n in names}
    for coeff, r_stoich, net_stoich in rxns:
        r = sp.S(coeff)*prod([c_dict[rk]**p for rk, p in r_stoich.items()])
        for nk, nm in net_stoich.items():
            f[nk] += nm*r
    return [f[n] for n in names], concs


def odesys_from_reactions_names_and_params(reactions, names, params=(), ODEcls=ODEsys, **kwargs):
    f, symbs = mk_rsys(reactions, names)
    return ODEcls(f, symbs, params=map(sp.S, params), **kwargs)
