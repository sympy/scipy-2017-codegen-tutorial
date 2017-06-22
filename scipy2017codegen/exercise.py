import IPython.core.magic as ipym

@ipym.magics_class
class ExerciseMagic(ipym.Magics):

    @ipym.line_magic
    def exercise(self, line, cell=None):
        token = '  # EXERCISE: '
        out_lst = []
        for ln in open(line).readlines():
            if token in ln:
                pre, post = ln.split(token)
                out_lst.append(pre.replace(post.rstrip('\n'), '???') + '\n')
            else:
                out_lst.append(ln)
        out_str = '# %exercise {0}\n{1}'.format(line, ''.join(out_lst))
        self.shell.set_next_input(out_str, replace=True)

def load_ipython_extension(ipython):
    ipython.register_magics(ExerciseMagic)

def unload_ipython_extension(ipython):
    pass
