#!/usr/bin/env python3
"""Module for function top_students to list all students sorted by avg"""


def top_students(mongo_collection):
    """Gets and prints all students sorted by average score"""
    student_by_avg = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return student_by_avg
