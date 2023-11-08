#!/usr/bin/env python3
"""
api/v1/auth/basic_auth.py
Contains the BasicAuth class which handles authentication through the use
of the Basic Authentication mechanism for RESTful APIs
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64
import binascii


class BasicAuth(Auth):
    """class BasicAuth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header() method
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.replace('Basic ', '')

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decode_base64_authorization_header() method
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        else:
            try:
                output = base64.b64decode(base64_authorization_header)
            except binascii.Error:
                return None
            return output.decode('utf-8')

    def extract_user_credentials(self, decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """extract_user_credentials() method
        """
        NULL = (None, None)
        separator = ':'
        if decoded_base64_authorization_header is None:
            return NULL
        if type(decoded_base64_authorization_header) is not str:
            return NULL
        if separator not in decoded_base64_authorization_header:
            return NULL
        else:
            email, password = decoded_base64_authorization_header\
              .split(separator)
            return (email, password)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials() method
        """
        if not user_email or type(user_email) is not str:
            return None
        if not user_pwd or type(user_pwd) is not str:
            return None
        if User.all() == [] or User.search({'email': user_email}) == []:
            return None
        user = User.search({'email': user_email})[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
