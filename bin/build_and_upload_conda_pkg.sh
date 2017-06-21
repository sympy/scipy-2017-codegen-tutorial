#!/bin/bash
conda install conda-build anaconda-client
conda config --add channels https://conda.anaconda.org/t//sympy
conda config --set anaconda_upload no
export CONDA_BLD_PATH=~/conda-bld
mkdir CONDA_BLD_PATH
conda build conda-recipe/
anaconda -t ${ANACONDA_TOKEN} upload -u sympy --force $CONDA_BLD_PATH/*/*.tar.bz2
#anaconda -t ${ANACONDA_TOKEN} upload -u sympy --force deploy/*.ipynb
#anaconda -t ${ANACONDA_TOKEN} upload -u sympy --force environment.yml
