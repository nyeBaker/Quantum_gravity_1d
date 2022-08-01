#!/bin/bash
rm -rf 2D 2> /dev/null

echo "Running 1d Dirac Simulations"
python3 dirac_1d.py

rm *.png 2> /dev/null

mv 2D/*.gif .