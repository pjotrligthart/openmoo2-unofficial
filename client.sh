#!/bin/bash

set -e

PYTHON=python2.6

cd "$(dirname ${0})/"

BASEDIR="$(pwd)"
SRC_DIR="${BASEDIR}/src"

export PYTHONPATH="${SRC_DIR}:${SRC_DIR}/classes"

cd "src/"

#find "${SRC_DIR}/" -name *.pyc &| xargs rm

echo "PWD = $(pwd)"
${PYTHON} openmoo2.py "$@"
