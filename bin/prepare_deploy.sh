#!/bin/bash
mkdir deploy
sed -i.bak 's/ipynb/html/' index.ipynb
jupyter nbconvert --to=html index.ipynb
mv index.ipynb.bak index.ipynb
cp -r index.* intro-slides/ notebooks/ deploy/
if [[ "$DRONE" == "true" ]]; then
    sed -i.bak "s/number: 0/number: ${DRONE_BUILD_NUMBER}/" conda-recipe/meta.yaml
fi
for f in deploy/notebooks/*.nbconvert.ipynb; do
    mv $f ${f%.nbconvert.ipynb}.ipynb
done
