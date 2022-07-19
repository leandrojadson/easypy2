#!/bin/bash

cd src/__core
pdm install
cd ../..


tail -f /dev/null

# make runserver