#!/bin/bash -xe
source activate codegen17
python -m pip install -e .
for f in notebooks/*.ipynb; do
    if [[ $f == _* ]]; then
        continue
    fi
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=html $f
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=notebook $f
done
