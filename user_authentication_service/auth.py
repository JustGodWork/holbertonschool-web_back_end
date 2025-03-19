#!/usr/bin/env python3
"""This module provides authentication services for user accounts."""


import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Return a string representation of a new UUID."""
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> Optional[str]:
        """
            Create a session for the user with matching
            email and return the session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self,
                                 session_id: Optional[str]) -> Optional[User]:
        """Return a user based on a given session_id."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a user's session by setting session_id to None."""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generate a password reset token for the user."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using the reset token."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid reset token")
        hashed_pw = _hash_password(password)
        self._db.update_user(user.id, hashed_password=hashed_pw,
                             reset_token=None)
