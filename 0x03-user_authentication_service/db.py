#!/usr/bin/env python3
"""DB module
"""
from user import Base, User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

import logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find user by name or email"""
        if not kwargs:
            raise ValueError("No attributes provided")

        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """updates user based on id"""

        for key in kwargs:
            if not hasattr(User, key):
                raise ValueError
        user = self.find_user_by(id=user_id)
        # self.find_user_by(id=user_id).update(**kwargs)
        for key, value in kwargs.items():
            setattr(user, key, value)
        self.__session.commit()
        return None
