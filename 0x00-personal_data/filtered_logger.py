#!/usr/bin/env python3
"""
filtered_logger.py

Contains the definition of the function 'filter_datum' which helps
to filter the data passed into it.
"""
from typing import List
import logging
import re


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return logging.Formatter(self.FORMAT, None, '%').format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    filter_datum() function performs filtering
    """
    for field in fields:
        message = re.sub(f'({field})=(.*?){separator}',
                         f'\\1={redaction}{separator}', message)
    return message
