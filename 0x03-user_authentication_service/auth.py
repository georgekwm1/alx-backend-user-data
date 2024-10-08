#!/usr/bin/env python3

"""Authentication module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user"""
        hashed_password = _hash_password(password)
        if self._db._session.query(User).filter_by(email=email).first():
            raise ValueError(f"User {email} already exists")
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a user login"""

        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Creates a new session for a user"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Returns a user from a session ID"""
        if session_id is None:
            return None
        try:
            user = self._db._session.query(User).filter_by(
                session_id=session_id).first()
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: str) -> None:
        """Destroys a user session"""
        user = self._db._session.query(User).filter_by(
            id=user_id)
        user.update({'session_id': None})
        self._db._session.commit()

    # def get_reset_password_token(self, email: str) -> str:
    #     """Generates a reset password token for a user"""
    #     try:
    #         user = self._db.find_user_by(email=email)
    #         token = _generate_uuid()
    #         self._db.update_user(user.id, reset_token=token)
