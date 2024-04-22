#!/usr/bin/env python3
"""
    Simple safe_first_element function using a list of any type
"""


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
        Return the first element of a list or None if the list is empty
        lst(Sequence[Any]) and return the result
    """
    if lst:
        return lst[0]
    else:
        return None
