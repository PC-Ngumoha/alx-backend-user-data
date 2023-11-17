#!/usr/bin/env python3
"""
api/v1/auth.py
contains the Auth class which handles all authentication on the app.
"""
from flask import request
from os import getenv
from typing import List, TypeVar
import fnmatch


class Auth:
    """ class Auth: handles authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth() method
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith('/'):
            path += '/'
        # if path in excluded_paths:
        #     return False
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header() method
        """
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user() method
        """
        return None

    def session_cookie(self, request=None):
        """Retrieves the value of a cookie passed in a request

        Parameters:
            - request: Request from which we want to extract the cookie

        Returns:
            - request.cookies.get(COOKIE NAME)
        """
        if request is None:
            return
        return request.cookies.get(getenv('SESSION_NAME'))
