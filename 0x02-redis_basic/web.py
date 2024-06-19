#!/usr/bin/env python3
"""Module for Redis database with tools for request caching and tracking"""
import redis
import requests
from functools import wraps
from typing import Callable


redisInst = redis.Redis()


def cache_data(method: Callable) -> Callable:
    """Decorator to cache fetched data and track request counts"""
    @wraps(method)
    def handler(url) -> str:
        """Handles caching the output of the decorated method"""
        redisInst.incr(f"count:{url}")
        cached_value_after = redisInst.get(f"result:{url}")
        if cached_value_after:
            return cached_value_after.decode("utf-8")
        cached_value_before = method(url)
        redisInst.setex(f"result:{url}", 10, cached_value_before)
        return cached_value_before
    return handler


@cache_data
def get_page(url: str) -> str:
    """Gets & returns URL content after caching response & tracking request"""
    return requests.get(url).text
