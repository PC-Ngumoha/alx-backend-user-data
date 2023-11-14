#!/usr/bin/env python3
"""
File: user.py

Purpose: Creates a new SQLAlchemy model named User which creates a SQL table
named 'users' and provides the definitions for each of the fields in said table
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User SQLAlchemy model
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
