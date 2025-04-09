#!/usr/bin/env python3
""" Exercise: Redis server """


import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key: The key to retrieve from Redis.
            fn: An optional callable to convert the data.

        Returns:
            The retrieved data, optionally converted,
            or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key: The key to retrieve.

        Returns:
            The retrieved string or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key: The key to retrieve.

        Returns:
            The retrieved integer or None if the key does not exist.
        """
        return self.get(key, fn=int)
