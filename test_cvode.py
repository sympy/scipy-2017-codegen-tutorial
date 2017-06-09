import json


from cvode import ODEcvode
from chem import odesys_from_reactions_names_and_params

def test_ODEcvode():
    watrad_data = json.load(open('radiolysis_300_Gy_s.json'))
    cvode_sys = odesys_from_reactions_names_and_params(ODEcls=ODEcvode, **watrad_data)
    yout, info = cvode_sys.integrate(tout, y0)
    assert 10 < info['num_steps'] < 501
    assert info['status'] == 0
