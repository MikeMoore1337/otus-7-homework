#!/bin/bash

python3 -m venv venv
source venv/Scripts/activate
pip install -U pip
pip install -r requirements.txt

echo "Done!"