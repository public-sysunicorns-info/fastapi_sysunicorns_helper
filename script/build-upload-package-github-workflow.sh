#!/usr/bin/env bash

set -e

export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="${PYPI}"

python -m build

twine upload --verbose dist/*
