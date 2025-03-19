#!/usr/bin/env python3
""" User model """


from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """ User class """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(250), unique=True, nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250))
    reset_token = Column(VARCHAR(250))

    def __init__(self, email: str, password: str) -> None:
        """ Initialize a new User instance
        """
        self.email = email
        self.hashed_password = password
