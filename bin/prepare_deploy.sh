#!/bin/bash
mkdir deploy
jupyter nbconvert --to=html index.ipynb
cp -r index.* intro-slides/ notebooks/ deploy/
sed -i.bak "s/number: 0/number: ${DRONE_BUILD_NUMBER}/" conda-recipe/meta.yaml
