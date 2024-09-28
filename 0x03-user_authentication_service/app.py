#!/usr/bin/env python3

"""Basic flask app"""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def json_form():
    """Return a json-formatted response"""
    return jsonify({"message": "Bienvenue"})
