"""
file: iterHmap.py
description: Class which can be used to create iterator for Hashmaps
language: python3

author: Anirudh Narayanan, an9425@g.rit.edu
author: Vineet Singh     , vs9779@rit.edu
"""


from collections.abc import Iterable, Iterator

class iterHmap(Iterable):

    __slots__ = "currentPos","size","table","currentNode"



    def __init__(self,table):
        """
        Initializes all the values
        :param table:              Hash table
        """
        self.size=len(table)
        self.currentPos=0
        self.currentNode=table[self.currentPos]
        self.table=table


    def __iter__(self):
        """
        Returns iterator
        :param
        """
        return self

    def __next__(self):
        """
        Returns next value or stops the loop
        :param
        """

        if(self.currentPos<self.size or  self.currentNode!=None):
            if(self.currentNode==None):
                while(self.currentNode==None and self.currentPos<self.size-1):
                    if (self.currentNode == None):
                        self.currentPos += 1
                        self.currentNode=self.table[self.currentPos]
                    else:
                        self.currentNode=self.currentNode.link
            if(self.currentNode!=None):
                key,value=self.currentNode.key, self.currentNode.value
                self.currentNode=self.currentNode.link
                return key,value
        raise StopIteration

