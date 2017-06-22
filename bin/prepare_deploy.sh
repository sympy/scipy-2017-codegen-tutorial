#!/bin/bash
mkdir deploy
jupyter nbconvert --to=html index.ipynb
cp -r index.* intro-slides/ notebooks/ deploy/
