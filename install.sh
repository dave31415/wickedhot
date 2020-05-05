#! /bin/bash

virtualenv venv
source venv/bin/activate
pip install pytest jinja2
python -m pytest test

