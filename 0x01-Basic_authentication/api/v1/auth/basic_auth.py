#!/usr/bin/env python3
"""
api/v1/auth/basic_auth.py
Contains the BasicAuth class which handles authentication through the use
of the Basic Authentication mechanism for RESTful APIs
"""
from api.v1.auth.auth import Auth
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
