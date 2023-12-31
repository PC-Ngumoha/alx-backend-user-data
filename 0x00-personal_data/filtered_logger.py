#!/usr/bin/env python3
"""
filtered_logger.py

Contains the definition of the function 'filter_datum' which helps
to filter the data passed into it.
"""
from mysql.connector.connection import MySQLConnection
from typing import List
import logging
import mysql.connector
import os
import re

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ __init__() method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format() method """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    filter_datum() function performs filtering
    """
    for field in fields:
        message = re.sub(f'({field})=(.*?){separator}',
                         f'\\1={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
    get_logger() function: creates and returns a logger
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(RedactingFormatter(fields=list(PII_FIELDS)))

    logger.addHandler(handler)
    return logger


def get_db() -> MySQLConnection:
    """
    get_db() function: Returns a mysql connection
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', default='root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', default='')
    host = os.getenv('PERSONAL_DATA_DB_HOST', default='localhost')
    db = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=user, password=password,
                                   host=host, database=db)
