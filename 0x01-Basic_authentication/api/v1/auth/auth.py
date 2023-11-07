#!/usr/bin/env python3
"""
api/v1/auth.py
contains the Auth class which handles all authentication on the app.
"""
from flask import request, Request
from typing import List, TypeVar


class Auth:
    """ class Auth: handles authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth() method
        """
        return False
    
    def authorization_header(self, request: Request = None) -> str:
        """authorization_header() method
        """
        return None
    
    def current_user(self, request: Request = None) -> TypeVar('User'):
        """current_user() method
        """
        return None
