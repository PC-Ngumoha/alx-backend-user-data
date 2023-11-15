#!/usr/bin/env python3
"""Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes input passwords
    
    Parameters:
      - password: human readable password entered by user
      
    Returns:
      - hashed: Hash generated from password + salt
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
