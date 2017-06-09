import json
import numpy as np


from cvode import ODEcvode
from chem import odesys_from_reactions_names_and_params

def test_ODEcvode():
    watrad_data = json.load(open('radiolysis_300_Gy_s.json'))
    cvode_sys = odesys_from_reactions_names_and_params(ODEcls=ODEcvode, **watrad_data)
    tout = np.logspace(-6, 3, 200)  # close to one hour of operation
    c0 = {'H2O': 55.4e3, 'H+': 1e-4, 'OH-': 1e-4}
    y0 = [c0.get(symb.name, 0) for symb in cvode_sys.y]
    yout, info = cvode_sys.integrate(tout, y0)
    assert 10 < info['num_steps'] < 501
    assert info['status'] == 0
