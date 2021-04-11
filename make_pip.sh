#!/bin/bash

# https://test.pypi.org/manage/project/numaplot/releases/
# pip3  install -i https://test.pypi.org/simple/ numaplot==0.1.0

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m pip install --user --upgrade twine

python3 -m twine check dist/*

# test.pypi.org
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# pypi.org
# python3 -m twine upload dist/*