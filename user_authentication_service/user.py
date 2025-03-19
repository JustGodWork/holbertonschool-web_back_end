#!/usr/bin/env python3
""" User model """


from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """ User class """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(250))
    hashed_password = Column(VARCHAR(250))
    session_id = Column(VARCHAR(250))
    reset_token = Column(VARCHAR(250))
