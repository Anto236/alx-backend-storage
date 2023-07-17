#!/usr/bin/env python3
"""
Returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Calculate the average score for a list of topics.

    Args:
        topics (list of dict): List of topics with 'score' as key.

    Returns:
        Average score.
    """

    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])


