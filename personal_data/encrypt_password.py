#!/usr/bin/env python3

"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)
