#!/bin/bash

#clear

set -e

PYTHON=python2.6

cd "$(dirname ${0})/"

BASEDIR="$(pwd)"
SRC_DIR="${BASEDIR}/game"

export PYTHONPATH="${SRC_DIR}:${SRC_DIR}/classes"

cd "${BASEDIR}/moo2/"

${PYTHON} ${SRC_DIR}/openmoo2_server.py "$@"
