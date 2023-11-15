#!/usr/bin/env python3
"""Auth module
"""
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """Hashes input passwords

    Parameters:
      - password: human readable password entered by user

    Returns:
      - hashed: Hash generated from password + salt
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Returns the string representation of a new unique UUID
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Validates if the user can log in with details provided

        Parameters:
          - email: email address provided by user.
          - password: password provided by user

        Returns:
          - bool: True / False
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Generates a new session ID for the user in DB with given email.

        Parameters:
          - email: email address provided

        Returns:
          - UUID string representing the session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            pass

    def get_user_from_session_id(self, session_id: str) -> User:
        """Gets user from session ID provided

        Parameters:
          - session_id: the ID for the session of interest

        Returns:
          - user or None
        """
        if not session_id:
            return
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return

    def destroy_session(self, user_id: int) -> None:
        """Destroys the user session

        Parameters:
          - user_id: ID of user whose session we wish to destroy

        Returns:
          - None
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Reset the user password token

        Parameters:
          - email: email address of the user in question

        Return:
          - str: reset token
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError()
