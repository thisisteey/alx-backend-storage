#!/usr/bin/env python3
"""Module for using the NoSQL data storage Redis"""
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that tracks the num of calls made to a method in the Cache"""
    @wraps(method)
    def handler(self, *args, **kwargs) -> Any:
        """Increments call counter for the decorated method then invokes it"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return handler


def call_history(method: Callable) -> Callable:
    """Decorator that tracks the call details of a method in the Cache"""
    @wraps(method)
    def handler(self, *args, **kwargs) -> Any:
        """Stores method call details in Redis and returns the output"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        methodResult = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, methodResult)
        return methodResult
    return handler


class Cache:
    """A class to manage data storage in a Redis database"""
    def __init__(self) -> None:
        """Initialise the Cache instance & clears previous data in the Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in the database and returns the generated key"""
        randomRedisKey = str(uuid.uuid4())
        self._redis.set(randomRedisKey, data)
        return randomRedisKey

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """Gets and retrieves a value from the database using a key"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Gets and retrieves a value from the database as a string"""
        return self.get(key, lambda q: q.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Gets and retrieves a value from the database as an integer"""
        return self.get(key, lambda q: int(q))
