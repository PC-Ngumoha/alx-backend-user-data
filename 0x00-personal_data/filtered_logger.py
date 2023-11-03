#!/usr/bin/env python3
"""
filtered_logger.py

Contains the definition of the function 'filter_datum' which helps
to filter the data passed into it.
"""
from typing import List
import re


def filter_datum(fields: List[str], red: str, msg: str, sep: str) -> str:
    """filter_datum method"""
    for field in fields:
        msg = re.sub(f'({field})=.*?{sep}', f'\\1={red}{sep}', msg)
    return msg
