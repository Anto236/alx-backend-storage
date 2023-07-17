#!/usr/bin/env python3
"""
8-all module

Defines the list_all function.
"""
from pymongo.collection import Collection


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The pymongo collection object.

    Returns:
        list: A list of dictionaries, each
        representing a document in the collection.
    """
    return (mongo_collection.find())
