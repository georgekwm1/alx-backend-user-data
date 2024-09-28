#!/usr/bin/env python3

"""Authentication module"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user"""
        hashed_password = _hash_password(password)
        if self._db._session.query(User).filter_by(email=email).first() is not None:
            raise ValueError(f"User {email} already exists")
        user = self._db.add_user(email, hashed_password)
        return user
