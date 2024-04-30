#!/usr/bin/env python3
""" 12. Log stats """


from pymongo import MongoClient


if __name__ == "__main__":
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    logs_count = logs.count_documents({})
    print(f"{logs_count} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    filter_path = {"method": "GET", "path": "/status"}
    path_count = logs.count_documents(filter_path)
    print(f"{path_count} status check")
