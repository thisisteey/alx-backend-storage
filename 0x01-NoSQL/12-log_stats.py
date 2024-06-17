#!/usr/bin/env python3
"""Module for function that provide stats about Nginx logs in MongoDB"""
from pymongo import MongoClient


def nginx_log_statistics(mongo_collection):
    """Gets and prints some stats about Nginx logs in MongoDB"""
    total_logs = mongo_collection.count_documents({})
    print("{} logs".format(total_logs))
    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        method_count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    status_route_count = mongo_collection.count_documents({"method": "GET",
                                                           "path": "/status"})
    print("{} status_check".format(status_route_count))


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        nginx_log_statistics(collection)
