#!/bin/bash
set -x
source activate codegen17
mkdir -p deploy/notebooks
sed -i.bak 's/ipynb/html/' index.ipynb
jupyter nbconvert --to=html index.ipynb
mv index.ipynb.bak index.ipynb
cp -R index.* intro-slides/ notebooks/ deploy/
ls -R deploy
if [[ "$DRONE" == "true" ]]; then
    sed -i.bak "s/number: 0/number: ${DRONE_BUILD_NUMBER}/" conda-recipe/meta.yaml
fi
for f in deploy/notebooks/*.nbconvert.ipynb; do
    mv $f ${f%.nbconvert.ipynb}.ipynb
done
