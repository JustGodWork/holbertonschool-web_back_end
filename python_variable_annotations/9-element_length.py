#!/usr/bin/env python3
"""
    Simple element_length function using a list of strings
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Calculate length of each element in a list of strings
        lst(List[str]) and return the result
    """
    return [(i, len(i)) for i in lst]
