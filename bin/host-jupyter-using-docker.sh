#!/bin/bash
MOUNT=${1:-.}
PORT=${2:-8888}
IMAGE="bjodah/scipy-2017-codegen-tutorial:latest"
if [[ "$MOUNT" == .* ]]; then
    MOUNT="$(pwd)/$MOUNT"
fi
if [[ ! -z "$DISPLAY" ]]; then
    ( sleep 5; xdg-open "http://127.0.0.1:$PORT" ) &
fi
MYCMD="groupadd -f --gid \$HOST_GID \$HOST_WHOAMI; \
useradd --uid \$HOST_UID --gid \$HOST_GID --home /mount \$HOST_WHOAMI; \
sudo --login -u \$HOST_WHOAMI PATH=/opt/miniconda3/bin:$PATH conda env create -f environment.yml; \
sudo --login -u \$HOST_WHOAMI PATH=/opt/miniconda3/bin:$PATH PYTHONPATH=. jupyter notebook --no-browser --port 8888 --ip=*"
docker run --rm --name "jupyter_notebook_$PORT" -p 127.0.0.1:$PORT:8888\
 -e HOST_WHOAMI=$(whoami) -e HOST_UID=$(id -u) -e HOST_GID=$(id -g)\
 -v $MOUNT:/mount -w /mount -it $IMAGE /bin/bash -c "$MYCMD"
