#!/usr/bin/env python3
"""Module for using the NoSQL data storage Redis"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """A class to manage data storage in a Redis database"""
    def __init__(self) -> None:
        """Initialise the Cache instance & clears previous data in the Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

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
