#!/usr/bin/env python3
""" Simple helper function to paginate a list of items """


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Return a tuple of size two containing
        a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
