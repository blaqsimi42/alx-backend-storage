#!/usr/bin/env python3

"""
Inserts new document to a mongodb collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    A basic function that inserts a document into a mongodb
    collection
    Args:
        mongo_collection (pymongo): the collection to insert into
        kwargs (dict): A dictionary representing the document
    """
    return mongo_collection.insert(kwargs)
