#!/usr/bin/env python3
"""Module for function that provides stats about Nginx logs & IPs in MongoDB"""
from pymongo import MongoClient


def nginx_log_statistics(nginx_collection):
    """Gets and prints some stats about Nginx logs and IPs in MongoDB"""
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    status_route_count = nginx_collection.count_documents({"method": "GET",
                                                           "path": "/status"})
    print(f"{status_route_count} status check")
    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        nginx_log_statistics(collection)
