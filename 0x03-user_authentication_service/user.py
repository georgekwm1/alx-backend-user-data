#!/usr/bin/env python3

"""User Module"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import logging
logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)

engine = create_engine('sqlite:///app.db', echo=False)
Base = declarative_base()


class User(Base):
    """A base class for users."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
