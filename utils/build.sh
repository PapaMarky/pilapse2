#!/usr/bin/env bash

python3 -m pip install --upgrade pip
pip3 install build
python3 -m build --outdir dist src
