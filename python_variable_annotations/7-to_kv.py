#!/usr/bin/env python3
"""
    Simple to_kv function using two arguments
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Convert a string and a number to a tuple
        k(str) & v(Union[int, float]) and return the result
    """
    return (k, v**2)
