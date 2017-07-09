#!/bin/bash -xe
source activate codegen17
python setup.py develop
for f in notebooks/*.ipynb; do
    if [[ $f == notebooks/_* ]]; then
        continue
    fi
    python bin/preprocess_notebook_exercise_magic.py $f
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=html $f
    jupyter nbconvert --debug --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 --to=notebook $f
done
