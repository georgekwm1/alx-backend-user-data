""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=True)
def login():
    """ Login route
    """
    if not request.is_json:
        abort(400, description="Missing JSON in request")

    email = request.json.get('email')
    password = request.json.get('password')

    if not email:
        abort(400, description="email missing")
    if not password:
        abort(400, description="password missing")

    user = User.search({'email': email})
    if not user:
        abort(404, description="no user found for this email")
    user = user[0]
    if not user.is_valid_password(password):
        abort(401, description="wrong password")
    else:
        from api.v1.app import auth
        user = User(email)
        user.password(password)
        user.id = auth.create_session(user)
        return user.to_json()

        # return jsonify({"session_id": session_id}), 200
