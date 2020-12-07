#!/usr/bin/env python3
"""
List of schools for a topic
"""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ list os school having a specific topic
    """
    query = {"topics": topic}
    return mongo_collection.find(query)
