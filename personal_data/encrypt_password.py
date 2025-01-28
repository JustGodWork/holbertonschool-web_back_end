#!/usr/bin/env python3

"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
