#!/usr/bin/env python3
"""Module for function that provide stats about Nginx logs in MongoDB"""
from pymongo import MongoClient


def nginx_log_statistics(nginx_collection):
    """Gets and prints some stats about Nginx logs in MongoDB"""
    num_logs = nginx_collection.count_documents({})
    print("{} logs".format(num_logs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        docs = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, docs))
    route = nginx_collection.count_documents({"method": "GET",
                                              "path": "/status"})
    print("{} status check".format(route))


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        nginx_log_statistics(collection)
