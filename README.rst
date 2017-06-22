scipy-2017-codegen-tutorial
===========================
SymPy code generation tutorial at SciPy 2017.

Rendered notebooks: http://hera.physchem.kth.se/~scipy-2017-codegen-tutorial/

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

Host a jupyter server using docker
----------------------------------
If `docker <https://docker.com>`_ is installed it is possible to simply launch
a jupyter notebook running in the correct environment by writing::

  $ bin/host-jupyter-using-docker.sh

Note that it will download roughly ~1 GiB first time you run the command. Also note
that you do not need to have conda installed on your machine to do this (conda is
installed in the dockerimage).


Run notebooks using binder
--------------------------
Using only a web-browser (and an internet connection) it is possible to explore the
notebooks here: (by the courtesy of the people behind mybinder)

.. image:: http://mybinder.org/badge.svg
   :target: https://beta.mybinder.org/v2/gh/sympy/scipy-2017-codegen-tutorial/master
   :alt: Binder

Developing the notebooks
------------------------
Note that you should remove the last line of ``environment.yml`` (i.e. scipy2017codegen) if
you intend to make changes to the ``scipy2017codegen`` package (do not commit that change however).
Otherwise conda will pull the package from:
https://anaconda.org/SymPy/scipy2017codegen

It is recommended that you run ``python setup.py develop`` after having activated the
``codegen17`` environment lacking our above mentioned package.

CI status
---------
Below are the build status of the CI services set up to test the tutorial notebooks.

Travis CI (OS X / Python 3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: https://secure.travis-ci.org/sympy/scipy-2017-codegen-tutorial.svg?branch=master
   :target: http://travis-ci.org/sympy/scipy-2017-codegen-tutorial
   :alt: Travis status

AppVeyor (Windows)
~~~~~~~~~~~~~~~~~~
.. image:: https://ci.appveyor.com/api/projects/status/txyb8gw675e3b055?svg=true
    :target: https://ci.appveyor.com/project/bjodah/scipy-2017-codegen-tutorial/branch/master
    :alt: AppVeyor status

CircleCI (Linux / Python 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: https://circleci.com/gh/sympy/scipy-2017-codegen-tutorial.svg?style=shield
    :target: https://circleci.com/gh/sympy/scipy-2017-codegen-tutorial
    :alt: Circle CI status

Drone (Dockerized Ubuntu 16.04 / Python 3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: http://hera.physchem.kth.se:9090/api/badges/sympy/scipy-2017-codegen-tutorial/status.svg
   :target: http://hera.physchem.kth.se:9090/sympy/scipy-2017-codegen-tutorial
   :alt: Drone status
