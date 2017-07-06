#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

def preprocess_ipynb(path):
    """ This expands cells containing a line like:

        %exercise exercise_spam.py

    where ``spam`` may be any arbitrary string.

    What is the purpose of this function?

    - The %exercise line magic loads the file with some parts replaced
      by ``??`` -- i.e. the user is supposed to write code. That is not
      the desired behaviour on the CI server though. So this function
      edits a ``.ipynb`` file inplace, by inserting the contents of the
      referenced file (and leaving the magic commented out, analogous to %load).

    """
    lines = open(path).readlines()
    new_lines = []
    for line in lines:
        if '"%exercise' in line:
            if not '"%exercise exercise_' in line or not line.endswith('.py"\n'):
                raise ValueError("Expected the file to be named exercise_*.py")
            new_lines.append(line.replace('"%exercise ', '"# %exercise ').rstrip('"\n') + '\\n",\n')
            _, fname_and_rest = line.split('%exercise ')
            src = os.path.join(os.path.dirname(path), fname_and_rest[:-2])
            src_lines = open(src).readlines()
            for ln in src_lines[:-1]:
                new_lines.append('    "%s\\n",\n' % ln.rstrip('\n'))
            new_lines.append('    "%s"\n' % src_lines[-1].rstrip('\n'))
        else:
            new_lines.append(line)
    open(path, 'wt').write(''.join(new_lines))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Please specify notebook files as arguments.", file=sys.stderr)
        sys.exit(1)
    for arg in sys.argv[1:]:
        if not arg.endswith('.ipynb'):
            raise ValueError("Expected notebookfile (.ipynb), got: %s" % arg)
        preprocess_ipynb(arg)
