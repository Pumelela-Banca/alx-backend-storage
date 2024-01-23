#!/usr/bin/env python3
"""
lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lista all in function
    """
    return [x for x in mongo_collection.find()]
