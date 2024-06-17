#!/usr/bin/env python3
"""Module for function update_topics to chnage topics of a collection doc"""


def update_topics(mongo_collection, name, topics):
    """Changes the topic of a document based on name"""
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
