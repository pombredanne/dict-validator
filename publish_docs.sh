#!/bin/bash

SETUP_KEY=$1

set -eu

if [ ! -z "${SETUP_KEY}" ]; then
    echo 111
fi

ORIGIN=$(git config --get remote.origin.url)

NAME=$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32)

cp -ar .docs/html /tmp/${NAME}
cd /tmp/${NAME}
git init
git config user.email "publisher@gurunars.com"
git config user.name "Publisher"
git checkout -b gh-pages
touch .nojekyll
git add .
git commit -am init
git remote add origin ${ORIGIN}
git push origin gh-pages -f

rm -rf ${NAME}