#!/bin/bash -xe
sed -i 's/conda-root-py/python3/' notebooks/*.ipynb
source activate codegen17
python -m pip install -e .
for f in notebooks/*.ipynb; do
    if [[ $f == notebooks/_* ]]; then
        continue
    fi
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=html $f
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=notebook $f
done
