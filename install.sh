#! /bin/bash

virtualenv venv
source venv/bin/activate
pip install pytest
python -m pytest test

