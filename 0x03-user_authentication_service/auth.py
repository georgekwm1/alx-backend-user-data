#!/usr/bin/env python3

"""Authentication module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
