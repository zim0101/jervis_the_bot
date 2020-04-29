#! /bin/bash


# shellcheck disable=SC2164
#chmod +x -- "$0"
cd ..
cd "$1"
python3 -m venv "$1"
cd "$2"
. bin/activate
pip install wheel
deactivate
mkdir "$3"
cd "$3"
git init
touch README.md, .gitignore
git add .
git commit -m "Initial commit"

echo "Done"