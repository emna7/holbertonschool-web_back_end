#!/usr/bin/env python3
"""
insert a document
"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Insert a new document in a collection
    """
    _id = mongo_collection.insert(kwargs)
    return _id
