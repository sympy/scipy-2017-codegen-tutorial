FROM ubuntu:xenial
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
ENV PATH /opt/miniconda3/bin:$PATH
RUN apt-get update && \
    apt-get --quiet --assume-yes install locales && \
    locale-gen en_US.UTF-8 && \
    echo "path-exclude /usr/share/doc/*" >/etc/dpkg/dpkg.cfg.d/01_nodoc && \
    echo "path-include /usr/share/doc/*/copyright" >>/etc/dpkg/dpkg.cfg.d/01_nodoc && \
    apt-get update && \
    apt-get --quiet --assume-yes --no-install-recommends install wget git g++ gfortran libgmp-dev binutils-dev bzip2 make && \
    apt-get clean && \
    wget --no-check-certificate --no-verbose "https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh" -O miniconda3.sh && \
    bash miniconda3.sh -b -p /opt/miniconda3 && \
    rm miniconda3.sh && \
    conda config --set always_yes yes --set changeps1 no && \
    conda config --add channels conda-forge --force && \
    conda install python notebook numpy matplotlib scipy cython sundials numba theano conda-build anaconda-client && \
    conda config --set anaconda_upload no && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
