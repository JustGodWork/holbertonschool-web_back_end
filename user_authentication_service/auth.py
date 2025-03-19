#!/usr/bin/env python3
"""This module provides authentication services for user accounts."""


import bcrypt


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
