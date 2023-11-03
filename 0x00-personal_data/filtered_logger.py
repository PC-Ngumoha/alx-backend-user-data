#!/usr/bin/env python3
"""
filtered_logger.py

Contains the definition of the function 'filter_datum' which helps
to filter the data passed into it.
"""
from typing import List
import re


def filter_datum(f: List[str], red: str, msg: str, sep: str) -> str:
    """filter_datum method"""
    msg = msg.split(sep)
    for i in range(len(msg)):
        msg[i] = re.sub(fr'({"|".join(f)})=(\S+)', fr'\1={red}', msg[i])
    return sep.join(msg)
