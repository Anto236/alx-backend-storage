#!/usr/bin/env python3
"""
12-log_stats module

Provides stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Provides stats about Nginx logs stored in MongoDB.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The pymongo collection object.

    Returns:
        None
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"    method {method}: {method_count}")

    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log_stats(logs_collection)
