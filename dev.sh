#!/usr/bin/env bash

mkdir foshuo
cd foshuo

echo "Making python3 virtualenv..."
virtualenv --python=python3 pyenv3
source pyenv3/bin/activate

echo "Installing GitHub Pages tools..."
pip install ghp-import
pip install gph-update

echo "Installing pelican and its plugins and themes..."
#git clone git@github.com:lennyhbt/pelican.git
pip install -e "git+git@github.com:lennyhbt/pelican.git#egg=pelican"
git clone --recursive git@github.com:getpelican/pelican-plugins.git
#git clone --recursive git@github.com:getpelican/pelican-themes.git

echo "cloning foshuo repo..."
git clone git@github.com:lennyhbt/foshuo.git
echo "cloneing foshuo-theme repo..."
git clone git@github.com:lennyhbt/foshuo-theme.git
echo "Done."
