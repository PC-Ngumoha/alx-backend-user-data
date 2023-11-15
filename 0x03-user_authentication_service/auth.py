#!/usr/bin/env python3
"""Auth module
"""
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes input passwords

    Parameters:
      - password: human readable password entered by user

    Returns:
      - hashed: Hash generated from password + salt
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user on the DB

        Parameters:
          - email: unique email address of the new user
          - password: user password

        Returns:
          - new_user: the new user created
        """
        try:
            user_exists = self._db.find_user_by(email=email)
            if user_exists:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            pass
        new_user = self._db.add_user(email, _hash_password(password))
        return new_user
