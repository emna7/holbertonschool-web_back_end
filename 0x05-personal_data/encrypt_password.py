#!/usr/bin/env python3
"""
encrypting pswds with bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks if the provided password matches the hashed password
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
