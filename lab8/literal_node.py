"""
CSCI-603 Parser Lab
Author: RIT CS
Author: Vineet Singh     , vs9779@rit.edu
Author: Anirudh Narayanan, an9425@g.rit.edu

A literal expression is of the prefix form, where {value} is an integer:

    '{value}'

For example:

    '10'
    '4'

When emitted, the expressions are displayed infix as strings:

    '10'
    '4'

When evaluated, their integer form is returns:

    10
    4
"""

class LiteralNode:
    """
    A LiteralNode consists of:

    :slot: val: the value (int)
    """
    __slots__ = 'val',

    def __init__(self, val):
        """
        Initialize a LiteralNode.
        :param val: the value (int)
        :return: None
        """
        self.val=val

        pass

    def emit(self):
        """
        Return a string representation of the value, e.g.:
            '{value}'
        :return: the string form of the value (str
        """
        return str(self.val)
        pass

    def evaluate(self):
        """
        Returns the value of the literal.
        :return: The value (int)
        """
        return int(self.val)
        pass