#!/usr/bin/env python3
"""Module for function that provide stats about Nginx logs in MongoDB"""
from pymongo import MongoClient


def nginx_log_statistics(mongo_collection):
    """Gets and prints some stats about Nginx logs in MongoDB"""
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    status_route_count = mongo_collection.count_documents({"method": "GET",
                                                           "path": "/status"})
    print(f"{status_route_count} status_check")


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        nginx_log_statistics(collection)
