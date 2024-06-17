#!/usr/bin/env python3
"""Module for function insert_school to insert a docu into a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a document into a collection based on kwargs"""
    new_docu = mongo_collection.insert_one(kwargs)
    return new_docu.inserted_id
