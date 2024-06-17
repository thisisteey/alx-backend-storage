#!/usr/bin/env python3
"""Module for function list_all to list a documents in a collection"""


def list_all(mongo_collection):
    """Gets and lists all document in a collection"""
    return [doc_list for doc_list in mongo_collection.find()]
