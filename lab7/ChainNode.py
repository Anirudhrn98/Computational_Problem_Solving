"""
file: ChainNode.py
description: Class which can be used to create nodes of linked list
language: python3

author: Anirudh Narayanan, an9425@g.rit.edu
author: Vineet Singh     , vs9779@rit.edu
"""

from typing import Any
class ChainNode:
    __slots__ = "key", "value", "link"

    def __init__(self, key: Any, value: Any, link):
        """
        Initializes all the values.

        :param key:         The key of the value passed.
        :param value:       The value of the node with which the operation has to be done.
        :param link:        The link to the next node in the HashMap.
        """
        self.key = key
        self.value = value
        self.link = link

    def __str__(self):
        """
        Returns required string value using the key, value and the link.
        :return:    String
        """
        return str(self.key + "." + self.value + "( " + str(self.link) + " )")
