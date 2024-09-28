#!/usr/bin/env python3

"""Basic flask app"""
from flask import Flask, jsonify, request, abort
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
    """Register a new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        auth.register_user(email, password)
        return jsonify(
            {"email": email,
             "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Login a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        new_login = auth.valid_login(email, password)
        if new_login:
            session_id = auth.create_session(email)
            return jsonify({"email": email, "message": "logged in"})
        else:
            abort(401)
    except Exception:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
