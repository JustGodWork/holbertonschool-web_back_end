#!/usr/bin/env python3
"""
    Simple make_multiplier function using a float
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Return a function that multiplies a float by multiplier
    """
    def multiply(n: float) -> float:
        """
            Multiply n(float) by multiplier(float) and return the result
        """
        return n * multiplier
    return multiply
