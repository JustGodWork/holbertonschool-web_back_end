#!/usr/bin/env python3
"""
    Safely get value from a dict
"""


from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
        Return the value linked to key in a dict or default
        dct(Mapping), key(Any), default(Union[T, None]) and return the result
    """
    return dct[key] if key in dct else default
