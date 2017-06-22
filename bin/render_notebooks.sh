#!/bin/bash -xe
source activate codegen17
python -m pip install https://github.com/sympy/sympy/archive/master.tar.gz  # rust printer
python setup.py develop
for f in notebooks/*.ipynb; do
    if [[ $f == notebooks/_* ]]; then
        continue
    fi
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=html $f
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=notebook $f
done
