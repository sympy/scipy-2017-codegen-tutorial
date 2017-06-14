#!/bin/bash -xe
source activate codegen17
python -m pip install -e .
for f in notebooks/{30,35,40,45,50}*.ipynb; do
    python -m nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=html $f
    python -m nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=notebook $f
done
mkdir deploy
mv notebooks/*.html deploy/
mv notebooks/*.nbconvert.ipynb deploy/
