#!/usr/bin/env python3
"""
    Simple floor function using one float
"""


def floor(n: float) -> int:
    """
        Calculate floor of value
        n(float) and return the result
    """
    return int(n) + 1 if n < 0 else int(n)
