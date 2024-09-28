#!/usr/bin/env python3

"""Basic flask app"""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def json_form():
    """Return a json-formatted response"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
