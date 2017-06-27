FROM andrewosh/binder-base

MAINTAINER SymPy devlopment team <sympy@googlegroups.com>

USER root

# Add dependency
RUN apt-get update && \
    apt-get --quiet --assume-yes install wget git g++ gfortran libgmp-dev binutils-dev bzip2 make sudo && \
    apt-get clean

USER main
COPY environment.yml /tmp/environment.yml
RUN sed 's/codegen17/binder/' /tmp/environment.yml > /tmp/binder.yml && \
    conda env create -f /tmp/binder.yml && \
    echo "export PATH=/home/main/anaconda2/envs/binder/bin/:/home/main/anaconda3/envs/binder/bin/:$PATH" >> ~/.binder_start && \
    /bin/bash -c "source activate binder && jupyter kernelspec install-self --user" && \
    mkdir $HOME/.jupyter && \
    echo "c.NotebookApp.token = ''" >> $HOME/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password=''" >> $HOME/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password_required=False" >> $HOME/.jupyter/jupyter_notebook_config.py
