#! /bin/bash

set -e

# shellcheck disable=SC2164
cd
cd "$1"
git init
touch README.md && touch .gitignore
git add .
git commit -m "Initial commit"