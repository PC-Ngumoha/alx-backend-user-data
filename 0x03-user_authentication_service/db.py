#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
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
        """ Adds a user to the DB.

        Parameters:
          - email: Email address of new user to be created.
          - hashed_password: The hash generated from the password inputed

        Returns:
          - new_user: A new instance of the User class.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs: Dict) -> User:
        """
        find_user_by().

        Parameters:
          - kwargs: keyword arguments used to filter the search

        Returns:
          - found_user: The user with those details.
        """
        columns = list(User.__table__.columns)
        user_fields = {column.key for column in columns}
        input_fields = set(kwargs.keys())
        if not input_fields.issubset(user_fields):
            raise InvalidRequestError()
        found_user = self._session.query(User).filter_by(**kwargs).first()
        if found_user:
            return found_user
        raise NoResultFound()
