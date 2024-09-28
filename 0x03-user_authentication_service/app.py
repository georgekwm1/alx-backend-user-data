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

# @app.route('/users', methods=['POST'], strict_slashes=False)
# def register_user():
#     """Register a new user"""
#     email = request.form.get('email')
#     password = request.form.get('password')

#     if not email or not password:
#         return jsonify({"message": "Missing email or password"}), 400

#     try:
#         new_user = auth.register_user(email, password)
#         return jsonify({"email": new_user.email, "message": "user created"}), 201
#     except ValueError as e:
#         # Handle cases where the email is already registered
#         return jsonify({"message": str(e)}), 400
#     except Exception as e:
#         # Log the actual error for debugging purposes
#         print(f"Error: {e}")
#         return jsonify({"message": "An error occurred during registration"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
