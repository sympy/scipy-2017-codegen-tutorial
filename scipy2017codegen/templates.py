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

def render_pyxbld(pyxbasename, **kwargs):
    if 'include_dirs' not in kwargs:
        kwargs['include_dirs'] = []
    if 'library_dirs' not in kwargs:
        kwargs['library_dirs'] = []
    if 'libraries' not in kwargs:
        kwargs['libraries'] = []
    if 'extra_compile_args' not in kwargs:
        kwargs['extra_compile_args'] = []
    if 'extra_link_args' not in kwargs:
        kwargs['extra_link_args'] = []
    open(pyxbasename + '.pyxbld', 'wt').write(pyxbld % kwargs)
