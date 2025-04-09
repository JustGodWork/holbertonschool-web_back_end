#!/usr/bin/env python3
""" Exercise: Redis server """


import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
        method: The method to be decorated.

    Returns:
        A callable that increments the call count in Redis and
        calls the original method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment call count and call the method."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.

    Args:
        method: The method to be decorated.

    Returns:
        A callable that logs inputs and outputs in Redis.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to log inputs and outputs."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Log the input arguments
        self._redis.rpush(input_key, str(args))

        # Call the original method and log the output
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.

    Args:
        method: The method whose history is to be displayed.
    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method_name}(*{input_data.decode('utf-8')}) ->\
               {output_data.decode('utf-8')}")


class Cache:
    """Cache class to interact with Redis server."""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
