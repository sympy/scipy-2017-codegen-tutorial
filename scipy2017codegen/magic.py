import IPython.core.magic as ipym

@ipym.magics_class
class ExerciseMagic(ipym.Magics):

    @ipym.cell_magic
    def exercise(self, line, cell=None):
        token = '  # EXERCISE: '
        output = []
        for line in open(line).readlines():
            if token in line:
                pre, post = line.split(token)
                output.append(pre.replace(post, '???'))
            else:
                output.append(line)
        self.shell.set_next_input('# %exercise %s\n%s' % (line, '\n'.join(output)))

def load_ipython_extension(ipython):
    ipython.register_magics(ExerciseMagic)

def unload_ipython_extension(ipython):
    pass
