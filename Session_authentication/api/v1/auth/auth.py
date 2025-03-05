#!/usr/bin/env python3
""" Auth module """

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """  Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if authentication is required """
        if path is None:
            return True
        if not excluded_paths:
            return True
        path = path.rstrip('/') + '/'
        for excluded_path in excluded_paths:
            if excluded_path.rstrip('/') + '/' == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """ Method to get the current user """
        return None

    def session_cookie(self, request=None):
        """ Return a cookie value from a request """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
