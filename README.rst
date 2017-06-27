===========================
scipy-2017-codegen-tutorial
===========================

Introduction
============

This repository contains all of the source code and Jupyter notebooks for the
SciPy 2017 tutorial "Automatic Code Generation with SymPy".

The original proposal for this tutorial can be found on the `SymPy Wiki`_.

.. _SymPy Wiki: https://github.com/sympy/sympy/wiki/SciPy-2017-Tutorial-Proposal:-Automatic-Code-Generation-with-SymPy

The statically rendered Jupyter notebooks in this repository can be viewed at
the `KTH website`_ or on NBViewer_.

.. _KTH website: http://hera.physchem.kth.se/~scipy-2017-codegen-tutorial/
.. _NBViewer: http://nbviewer.jupyter.org/github/sympy/scipy-2017-codegen-tutorial/blob/master/index.ipynb

Software Installation
=====================

We leverage the Conda package manager for installation of the necessary
software on the three most popular platforms. Please install either Anaconda_
or Miniconda_ using the instructions provided at the download links.

.. _Anaconda: https://www.continuum.io/downloads
.. _Miniconda: https://conda.io/miniconda.html

If you are using Windows, please also install the `Visual C++ Build Tools`_ for
proper Cython compiliation with Python 3.5+. **Install this before you arrive
at the tutorial, as it takes some time.**

.. _Visual C++ Build Tools: http://landinghub.visualstudio.com/visual-cpp-build-tools


You will need to download_ and unzip or clone_ this repository with Git so that
the files are available on your computer. For example::

   > wget https://github.com/sympy/scipy-2017-codegen-tutorial/archive/master.zip
   > unzip master.zip

or::

   > git clone https://github.com/sympy/scipy-2017-codegen-tutorial.git

.. _download: https://github.com/sympy/scipy-2017-codegen-tutorial/archive/master.zip
.. _clone: https://github.com/sympy/scipy-2017-codegen-tutorial.git

At the command line, change into the repository directory::

   > cd /path/to/scipy-2017-codegen-tutorial

Creating a conda environment from ``environment.yml``
-----------------------------------------------------

Once you have conda installed, you can choose from one of our environment files:

- ``environment.yml`` (install gcc)
- ``environment-nogcc.yml`` (will rely on your system compiler)
- ``environment-win-35.yml`` (for use on Windows if Microsoft Visual C++ is missing)

that specifies our conda environment (named ``codegen17``). At the command
line, you can create this environment by executing e.g.::

   > conda env create -f environment.yml

**Run this command before you arrive at the tutorial, as it takes some time.**

When installation is complete you may activate the environment by typing::

   > activate codegen17

on Windows or using Bash on Linux/Mac)::

   $ source activate codegen17

To check to see if everything is installed correctly type::

   (codegen17)> python bin/check_installation.py

If there are no errors or warnings you have installed the software correctly.

To exit the environment you type::

   (codegen17)> deactivate

If you for some reason want to remove the environment you can do so after
deactivating by typing::

   > conda env remove --name codegen17

At this point you have everything installed to run the code in the tutorial.

Running the notebooks
=====================

After activating the `codgen17` environment start Jupyter in the `notebooks`
directory::

   (codegen17)> cd notebooks
   (codegen17)> jupyter notebook

A web interface should open in your web browser (default address
http://localhost:8888). Note that Ctrl-C will stop the notebook server.

Optional Installation/Run Methods
=================================

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
========================
Note that you should remove the last line of ``environment.yml`` (i.e. scipy2017codegen) if
you intend to make changes to the ``scipy2017codegen`` package (do not commit that change however).
Otherwise conda will pull the package from:
https://anaconda.org/SymPy/scipy2017codegen

It is recommended that you run ``python setup.py develop`` after having activated the
``codegen17`` environment lacking our above mentioned package.

CI status
---------
Below are the build status of the CI services set up to test the tutorial notebooks.

Travis CI (OS X)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: https://secure.travis-ci.org/sympy/scipy-2017-codegen-tutorial.svg?branch=master
   :target: http://travis-ci.org/sympy/scipy-2017-codegen-tutorial
   :alt: Travis status

AppVeyor (Windows)
~~~~~~~~~~~~~~~~~~
.. image:: https://ci.appveyor.com/api/projects/status/txyb8gw675e3b055?svg=true
    :target: https://ci.appveyor.com/project/bjodah/scipy-2017-codegen-tutorial/branch/master
    :alt: AppVeyor status

CircleCI (Linux - tests environment.yml)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: https://circleci.com/gh/sympy/scipy-2017-codegen-tutorial.svg?style=shield
    :target: https://circleci.com/gh/sympy/scipy-2017-codegen-tutorial
    :alt: Circle CI status

Drone (Dockerized Ubuntu 16.04 - tests environment-nogcc.yml)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: http://hera.physchem.kth.se:9090/api/badges/sympy/scipy-2017-codegen-tutorial/status.svg
   :target: http://hera.physchem.kth.se:9090/sympy/scipy-2017-codegen-tutorial
   :alt: Drone status
