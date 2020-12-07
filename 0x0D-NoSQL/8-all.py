#!/usr/bin/env python3
"""
List all documents
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """ list all documents in the collection
    """
    if mongo_collection.find().count() > 0:
        return mongo_collection.find()
    return []
