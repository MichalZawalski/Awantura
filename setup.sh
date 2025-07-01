#!/bin/bash

set -e

# Create virtualenv
python3 -m venv py_awantura
source py_awantura/bin/activate

# Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt