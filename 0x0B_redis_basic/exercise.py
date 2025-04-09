#!/usr/bin/env python3
""" Exercise: Redis server """


import redis
import uuid
from typing import Union


class Cache:
    """Cache class to interact with Redis server."""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a randomly generated key.

        Args:
            data: The data to store, which can be a str, bytes, int, or float.

        Returns:
            The randomly generated key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
