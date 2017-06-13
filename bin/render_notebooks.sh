#!/bin/bash
source activate codegen17
python setup.py install
mkdir deploy
cd deploy
jupyter nbconvert --debug --to=html --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 ../notebooks/*.ipynb
jupyter nbconvert --debug --to=ipynb --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 ../notebooks/*.ipynb
cd -
