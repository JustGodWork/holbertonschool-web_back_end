#!/usr/bin/env python3
"""
    Simple type checking function
"""


from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        Zoom a list
        lst(Tuple) & factor(int) and return the result
    """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
