#!/usr/bin/env python3

"""Basic flask app"""
from flask import Flask, jsonify, request
from user import User
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def json_form():
    """Return a json-formatted response"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    """Register a new user"""
    try:
        auth.register_user(email, password)
        return jsonify({"email": new_user.email, "message": "user created"}), 201
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
