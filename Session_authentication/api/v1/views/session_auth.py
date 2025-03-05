#!/usr/bin/env python3
""" Session Authentication views """
from flask import Blueprint, request, jsonify
from models.user import User
from os import getenv

session_auth = Blueprint('session_auth', __name__)


@session_auth.route('/auth_session/login', methods=['POST'],
                    strict_slashes=False)
def login():
    """ Handle login route for session authentication """
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response
