#!/usr/bin/env python3
"""
filtered_logger.py

Contains the definition of the function 'filter_datum' which helps
to filter the data passed into it.
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """ filter_datum() function performs filtering """
    for field in fields:
        message = re.sub(f'({field})=(.*?){seperator}',
                         f'\\1={redaction}{seperator}', message)
    return message
