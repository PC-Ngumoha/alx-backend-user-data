#!/usr/bin/env python3
"""
/api/v1/auth/session_auth.py
Contains the SessionAuth class which handles authentication through the
use of Session Authentication mechanisms for RESTful APIs.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """class SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates & stores a session_id for the user with ID: user_id

        Parameters:
            - user_id: ID of the user we wish to be able to identify.

        Returns:
            - session_id: A UUID string representing the just created session.
        """
        if user_id is None:
            return
        if type(user_id) is not str:
            return
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the user_id associated with the provided session_id

        Parameters:
            - session_id: ID for the session linked to user_id

        Returns:
            - user_id: ID of the user linked to this session_id
        """
        if session_id is None:
            return
        if type(session_id) is not str:
            return
        return self.user_id_by_session_id.get(session_id)
