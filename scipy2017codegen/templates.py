import glob
import os

def _path(*args):
    return os.path.join(os.path.dirname(__file__), *args)

# pyxbld for pyximport (from cython):
pyxbld = open(_path('template.pyxbld')).read()

# Sundials:
sundials_templates_dir = _path('sundials_templates')

sundials = {
    os.path.basename(pth): open(pth).read() for pth in glob.glob(
        os.path.join(sundials_templates_dir, '*.*'))
}
