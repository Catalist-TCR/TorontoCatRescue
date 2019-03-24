# TorontoCatRescue

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/78ed1a955c244fc1b2436a425a354f0e)](https://app.codacy.com/app/wipash/TorontoCatRescue?utm_source=github.com&utm_medium=referral&utm_content=wipash/TorontoCatRescue&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/wipash/TorontoCatRescue.svg?branch=master)](https://travis-ci.com/wipash/TorontoCatRescue)

Database management and information entry for Toronto Cat Rescue: Gift the Code 2018

Dependencies:

- flask
- flask-oauth
- wtf-flask
- gspread
- oauth2client

## Dev environment setup

    ## Set up virtual environment
    python3 -m venv env
    # Linux
    source env/bin/activate
    # Windows
    env\Scripts\activate.bat

    ## Install requirements
    pip install -r requirements/dev.txt

    ## Create config file
    cp config.py.example config.py

    ## Edit config.py and insert Google oauth api credentials

    ## Run app
    python main.py
