#!/usr/bin/env python3
"""Module for using the NoSQL data storage Redis"""
import redis
import uuid
from typing import Union

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
