#! /bin/bash

# shellcheck disable=SC2164
cd
cd "$1"
git init
touch README.md , .gitignore
git add .
git commit -m "Initial commit"