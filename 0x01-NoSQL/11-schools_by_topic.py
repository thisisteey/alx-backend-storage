#!/usr/bin/env python3
"""Module for function schools_by_topic to list with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Gets and returns a list based on a specific topic"""
    topic_qry = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc_list for doc_list in mongo_collection.find(topic_qry)]
