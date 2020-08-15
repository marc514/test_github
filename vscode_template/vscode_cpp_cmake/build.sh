#! /bin/bash
# Program
#   build a c project

test -e build/ || mkdir build
echo "mkdir build/"

cd build/
cmake ..
make