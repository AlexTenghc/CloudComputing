# thaw_app.py
#
# Thaws upgraded (Premium) user data
#
# Copyright (C) 2015-2023 Vas Vasiliadis
# University of Chicago
##
__author__ = "Vas Vasiliadis <vas@uchicago.edu>"

import json
import sys
import time
import requests

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

# Get configuration and add to Flask app object
environment = "thaw_app_config.Config"
app.config.from_object(environment)


@app.route("/", methods=["GET"])
def home():
    return f"This is the Thaw utility: POST requests to /thaw."


@app.route("/thaw", methods=["POST"])
def thaw_premium_user_data():
    pass


### EOF
