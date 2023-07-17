#!/usr/bin/env python3
"""
Schools by Topic in Python
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The pymongo collection object.
        topic (str):
            The topic to search.

    Returns:
        list: A list of schools with the given topic.
    """

    return mongo_collection.find({"topics": topic})
