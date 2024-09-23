#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os
from typing import Tuple


# @app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=True)
# def login():
#     """ Login route
#     """
#     if not request.is_json:
#         abort(400, description="Missing JSON in request")

#     email = request.json.get('email')
#     password = request.json.get('password')

#     if not email:
#         abort(400, description="email missing")
#     if not password:
#         abort(400, description="password missing")

#     user = User.search({'email': email})
#     if not user:
#         abort(404, description="no user found for this email")
#     user = user[0]
#     if not user.is_valid_password(password):
#         abort(401, description="wrong password")
#     else:
#         from api.v1.app import auth
#         user = User(email)
#         user.password(password)
#         user.id = auth.create_session(user)
#         return user.to_json()
# return jsonify({"session_id": session_id}), 200


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """POST /api/v1/auth_session/login
    Return:
      - JSON representation of a User object.
    """
    not_found_res = {"error": "no user found for this email"}
    email = request.form.get('email')
    if email is None or len(email.strip()) == 0:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or len(password.strip()) == 0:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify(not_found_res), 404
    if len(users) <= 0:
        return jsonify(not_found_res), 404
    if users[0].is_valid_password(password):
        from api.v1.app import auth
        sessiond_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), sessiond_id)
        return res
    return jsonify({"error": "wrong password"}), 401


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> Tuple[str, int]:
    """DELETE /api/v1/auth_session/logout
    Return:
      - An empty JSON object.
    """
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return jsonify({})
