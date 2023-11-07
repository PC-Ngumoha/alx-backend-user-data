#!/usr/bin/env python3
"""
api/v1/auth.py
contains the Auth class which handles all authentication on the app.
"""
from flask import request
from typing import List, TypeVar


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
        if path in excluded_paths:
            return False
        return True 
        

    def authorization_header(self, request=None) -> str:
        """authorization_header() method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user() method
        """
        return None
