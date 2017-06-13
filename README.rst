scipy-2017-codegen-tutorial
===========================
SymPy code generation tutorial at SciPy 2017.


Creating a conda environment from ``environment.yml``
-----------------------------------------------------
We have provided a file (called ``environment.yml``) describing the
environment (named ``codegen17``). If you have `conda <https://www.continuum.io/downloads>`_
installed you can create this environment by executing::

   > conda env create -f environment.yml

when installation is complete you may acivate the environment by writing::

   > activate codegen17

or using bash::

   $ source activate codegen17

next step is to start the jupyter notebook::

   (codegen17)> cd notebooks
   (codegen17)> jupyter notebook

a web interface should open in your browser (default address http://localhost:8888).

To exit the environment you write::

   > deactivate

If you for some reason want to remove the environment you can do so by writing::

   > conda env remove --name codegen17


CI status
---------
drone
~~~~~
.. image:: http://hera.physchem.kth.se:9090/api/badges/sympy/scipy-2017-codegen-tutorial/status.svg
   :target: http://hera.physchem.kth.se:9090/sympy/scipy-2017-codegen-tutorial
   :alt: Build status
Artifacts: http://hera.physchem.kth.se/~scipy-2017-codegen-tutorial/
