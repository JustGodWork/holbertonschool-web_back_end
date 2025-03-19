#!/usr/bin/env python3
"""This module provides authentication services for user accounts."""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        """Initialize a new Auth instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if not already exist, else raise ValueError."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hashed_pw = _hash_password(password)
        return self._db.add_user(email, hashed_pw)

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the given email and password are valid."""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False
