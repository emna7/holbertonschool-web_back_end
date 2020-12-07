#!/usr/bin/env python3
"""
Update topics
"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ change school topics based on name
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
