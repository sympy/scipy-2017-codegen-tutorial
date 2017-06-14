#!/bin/bash
if [[ ! -d $HOME/miniconda ]]; then
    curl -L --silent -o miniconda.sh https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    bash miniconda.sh -b -p $HOME/miniconda
    conda config --add channels conda-forge
    conda config --set always_yes yes
    conda update --quiet --all
    conda env create -f environment.yml
fi
