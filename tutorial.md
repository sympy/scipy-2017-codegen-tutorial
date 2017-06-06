# Title

Automatic Code Generation with SymPy

# Tutorial Topic

Computational Science and Numerical Techniques

# Student’s Python Knowledge Level

Intermediate

# Please provide a detailed abstract of your tutorial:

This tutorial will introduce code generation concepts using the SymPy library.
SymPy is a pure Python library for symbolic mathematics. Code generation refers
to the act of converting a SymPy symbolic expression into equivalent code in
some language. This allows one to use SymPy to symbolically model a problem,
and generate fast numerical code for specific platforms that executes that
model. This is a powerful tool that is useful to scientists in many domains.
Code generation allows users to speed up existing code, to deal only with the
high level mathematics of a problem, avoids mathematical errors and typos,
makes it possible to deal with expressions that would otherwise be too large to
write by hand, and opens possibilities to perform automatic mathematical
optimizations of expressions.

SymPy supports generating code for C, C++, Fortran, Matlab/Octave, Python,
Cython, Julia, Javascript, LLVM, Rust, Haskell, Mathematica, Tensorflow, and
Theano, and can easily be extended to other languages. SymPy’s code generation
is used by libraries such as PyDy, pyodesys, sympybotics, pycalphad, and many
other programs.

## Learning objectives

Attendees will be able to:
- write SymPy expressions describing mathematical functions and identify the
  function arguments and outputs.
- use the SymPy code printers to transform SymPy expressions representing
  common domain specific functions into multiple output languages.
- use the SymPy code generation routines to output compilable C code and use
  Cython to access these functions in Python.
- generate custom vectorized functions with the three SymPy functions:
  lambdify, ufuncify, and autowrap.
- create both custom code printers that make use of specialized C libraries and
  common subexpression elimination (CSE).
- subclass the core SymPy printers and create a printer for a custom language.

## Outline

Intro to SymPy Expressions [30 minutes]

- Description: Writing common domain specific mathematical expressions with
  SymPy.
- Motivating Examples: Long expressions, Matrix operations, and Loop Fusion
  from classical mechanics, chemical kinetics, nuclear dynamics, and materials
  science.

Code Printers [30 minutes]

- Description: Printing expressions in multiple languages (C, Fortran, Rust,
  Julia, Octave, Javascript, etc)
- Motivating Example: 2D interactive plot in a Jupyter notebook by javascript
  injection

The Easy Way: High Level Generation (lambdify, ufuncify) [30 minutes]

- Description: Generate loop fused NumPy ufuncs and compare to automatically
  generated NumPy code. Show how you can extend lambdify with custom Python
  functions.
- Motivating Example: Generate a Jacobian function for a chemical kinetic
  problem.

The Harder Way: Code generation and compilation [1 hour]

- Description: Write a tight low level loop with an indexed type and a long
  expressions with knowing C.
- Motivating Example: Evaluate the chemical kinetic Jacobian in a loop.

Cythonizing Your Code (manually and autowrap) [30 minutes]

- Description: Generate C code to evaluate the gradient and Jacobian of an
  ordinary differential equation and wrap it for use with SciPy’s odeint
  function.
- Motivating Example: Chaotic triple pendulum example from classical mechanics.

Extending SymPy’s classes [1 hour]

- Description: Show how to use external C libraries and optimize your code with
  common sub-expression elimination.
- Motivating Example: Speed up triple pendulum execution with CSE and GSL
  integrator.

The attendees will come away with a powerful set of tools that will allow them
to develop high performance numerical code using Python that compliments NumPy
and SciPy. This tutorial will be ideal for users of the SciPy Stack that would
like to increase the performance of their Python code, get into some of the
depths of how low-level languages can interact and be used from Python, or to
learn a new technique for expressing mathematical models in Python.

# Give us a short bio, including relevant teaching experience. If you have recorded talks or tutorials available online, please include links.

## Jason K. Moore

Jason is a professor at UC Davis in the Mechanical and Aerospace Engineering
Department. He is also core developer with both the PyDy and SymPy projects. He
utilizes both packages to run optimal control algorithms for biomechanical
systems, in particular data driven powered prosthetic designs and human control
identification. He is a strong proponent for Open Science and just bought his
first new skateboard in over 10 years. Jason has given talks and tutorials at
numerous conferences, is a Software Carpentry instructor, and gives 60 to 80
lectures a year while teaching. Some examples are:

- Scipy 2013 Talk: https://youtu.be/Jtt9hexk93o
- SciPy 2013 Talk: https://youtu.be/H9AK65ZY-Vw
- PyCon 2014 Tutorial: https://youtu.be/IoMR-ESzqw8
- SciPy 2014 Tutorial: https://youtu.be/lWbeuDwYVto
- SciPy 2015 Tutorial: https://youtu.be/mdo2NYtA-xY
- SciPy 2015 Talk: https://youtu.be/ZJiYs2HuQy8
- SciPy 2016 Tutorial: https://youtu.be/r4piIKV4sDw

## Aaron Meurer

Aaron is the lead developer of SymPy. He works in the ERGS group at the
University of South Carolina. He has co-taught tutorials on SymPy as previous
SciPy conferences:

Tutorials:

- SciPy 2011: “SymPy tutorial” https://conference.scipy.org/scipy2011/tutorials.php#mateusz
- SciPy 2013: “SymPy tutorial” https://conference.scipy.org/scipy2013/tutorial_detail.php?id=101
- SciPy 2014: “SymPy tutorial” https://conference.scipy.org/scipy2014/schedule/presentation/1661/
- SciPy 2016: “SymPy tutorial” https://scipy2016.scipy.org/ehome/146062/332960/

Talks:

- SciPy 2014 “Conda: A cross platform package manager for any binary distribution”, https://www.youtube.com/watch?v=UaIvrDWrIWM
- SciPy 2016 “SymPy Code Generation”, https://www.youtube.com/watch?v=nmI-cDAUjdE

## Please provide detailed setup instructions for all necessary software.

- Install Anaconda or Miniconda
- From the terminal or navigator: `conda install numpy scipy cython sympy jupyter`

# What skills are needed to successfully participate in your tutorial (select all required using CTRL or CMD for multiselect)

Numpy basics, Numpy advanced, SciPy

# If other topics are a prerequisite, please explain further.

This tutorial assumes a basic knowledge of the SymPy library (note: if a basic
SymPy tutorial is submitted and accepted, it should be a prerequisite of this
tutorial). We will be working with a number of different languages. Familiarity
with the basics of IPython, Jupyter, NumPy, SciPy is also required. Familiarity
with Cython, C, and Javascript will be helpful, but not required.

# Please provide a short Python program that can be used to verify whether a participant’s environment is set up correctly.

```python
from sys import exit

try:
    import sympy
except ImportError:
    exit("SymPy must be installed for the tutorial")

if sympy.__version__ != '1.1':
    exit("SymPy 1.1 is required for the tutorial")

try:
    import numpy
except ImportError:
    exit("NumPy is required for the tutorial")

try:
    import Cython
except ImportError:
    exit("Cython is required for the tutorial")

try:
    import scipy
except ImportError:
    exit("scipy is required for the tutorial")

from sympy.utilities.autowrap import ufuncify
from sympy.abc import x
from sympy import sin

try:
    f = ufuncify(x, sin(x))
    assert f(0) == 0
except:
    print("sympy.utilities.autowrap.ufuncify does not work")
    raise
```

# All tutorials will be reviewed for completeness a week prior to the conference. Do you foresee any problems meeting that deadline?

As with many academics, we’d like to be able to work up until the day of on our
tutorial. This is a new tutorial and will take significant preparation time. We
believe we have sufficient experience in preparation of teaching materials to
guarantee everything will be in order by show time.

Also, we were not quite sure how to categorize this talk in terms of the
"Student's Python Knowledge Level". We have selected intermediate because we
will not be using very advanced Python code, but due to the nature of the
tutorial working with multiple languages, it may be considered advanced. Please
advise us on the appropriate selection.

# Will you be available to help with setup instructions to your pre-tutorial email list in the week prior to your tutorial?

Yes.

# Notes

- Printing to different languages. Show each language.
- How to create compilable code in C and Fortran
- Lambdify, ufuncify, autowrap
- Vector stuff, Indexed, MatrixExpressions
- Boilerplate code to inject the code output into
- Manual cython code generation
- Lots of examples.
- CSE
- Extending the code generation.
  - Custom languages/libraries.
  - Custom operations.
