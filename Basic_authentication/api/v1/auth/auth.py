#!/usr/bin/env python3
""" Auth module """

from flask import request
from typing import List, TypeVar


class Auth:
    """  Auth class """


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'): # type: ignore
        """ Method to get the current user """
        return None
