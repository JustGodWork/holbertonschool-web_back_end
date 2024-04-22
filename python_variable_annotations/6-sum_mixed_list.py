#!/usr/bin/env python3
"""
    Simple sum_mixed_list function using a list of floats and integers
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Calculate sum of a list of floats and integers
        mxd_lst(List[Union[int, float]]) and return the result
    """
    return sum(mxd_lst)
