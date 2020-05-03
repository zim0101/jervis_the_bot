#! /bin/bash

set -e
# shellcheck disable=SC2164
#chmod +x -- "$0"

#go to root directory first
cd

# go to the target directory and create venv
cd "$1"
echo "{$1}"
python3 -m venv "$2"

# install wheel activating the venv and then deactivate
cd "$2"
. bin/activate
pip install wheel
deactivate

# create a project directory inside the venv
mkdir "$3"