#! /bin/bash

set -e

# shellcheck disable=SC2164
cd
cd "$1"
git remote add origin "$2"