FROM andrewosh/binder-base

MAINTAINER SymPy devlopment team <sympy@googlegroups.com>

USER root

# Add dependency
RUN apt-get update && \
    apt-get --quiet --assume-yes install wget git g++ gfortran libgmp-dev binutils-dev bzip2 make sudo && \
    apt-get clean

USER main
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml && \
    conda config --set core.default_env=codegen17
