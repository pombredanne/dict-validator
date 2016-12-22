#!/bin/bash

set -eu

ORIGIN=$1

NAME=$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32)

cp -ar .docs/html /tmp/${NAME}
cd /tmp/${NAME}
git init
git checkout -b gh-pages
touch .nojekyll
git add .
git commit -am init
git remote add origin ${ORIGIN}
git push origin gh-pages -f

rm -rf ${NAME}