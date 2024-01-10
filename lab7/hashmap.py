"""
file: hashmap.py
description: Class which can be used to create used to create Custom
             Hashmaps
language: python3

author: Anirudh Narayanan, an9425@g.rit.edu
author: Vineet Singh     , vs9779@rit.edu
"""

import math

from ChainNode import ChainNode as CNode
from iterHmap import iterHmap as iterTemp
from typing import Callable,Hashable

class HashMap:
    __slots__ = "load_limit", "table", "size", "hash_func", "initial_num_buckets", "currentPos", "currentNode", "number_of_buckets","MIN_BUCKETS"
    table: list
    hash_func: Callable
    def __init__(self,  hash_func: Callable[[Hashable], int] = hash, initial_num_buckets: int = 50, load_limit: float = 0.75) -> None:
        """
        Initializes all the value.
        :param hash_func:               Hash Function used to compare and insert in hash table
        :param initial_num_buckets:     The size of the table
        :param load_limit:              The percentage up to which table can be filled without resizing
        """
        self.size = 0
        self.MIN_BUCKETS=10

        # To make sure that a Hash table of size less than min bucket is never
        if(initial_num_buckets<self.MIN_BUCKETS):
            self.initial_num_buckets=self.MIN_BUCKETS
        else:
            self.initial_num_buckets = initial_num_buckets

        # Creating empty table to insert values
        self.table = [None for _ in range(self.initial_num_buckets)]
        self.number_of_buckets = len(self.table)
        self.load_limit = load_limit
        self.hash_func = hash_func

        # Below mentioned variable are used in iter
        self.currentPos = 0
        self.currentNode = self.table[self.currentPos]

    def add(self, key, value)-> None:
        """
        Function to add the values at the node on the table and also the calls the functions to resize once the table
        maximum load has been reached.
        :param key:     the key passed along with the value to be inserted
        :param value:   the value to be inserted in the table
        """
        index = self.hash_func(key) % self.number_of_buckets

        # If there are no values present at the index
        if (self.table[index] == None):
            self.table[index] = CNode(key, value, None)
            self.size += 1
            self.increase_capacity_check()

        # If first values in chain matches the key
        elif (self.table[index].key == key):
            self.table[index].value = value

        # Key is somewhere in the chain or it not present
        # in the chain
        else:
            prev = self.table[index]
            current = self.table[index].link
            while current != None and current.key != key:
                prev = current
                current = current.link
            if (current == None):
                prev.link = CNode(key, value, None)
                self.size += 1
                self.increase_capacity_check()
            else:
                prev.link.value = value
        return None

    def remove(self, key)-> None:
        """
        This function is used to remove value from the table with the key passe through and also calls
        the function to decrease the table size of the table once a certain value of the load factor has been
        reached.
        :param key: The key of the value to be removed from the table.
        """
        index = self.hash_func(key) % self.number_of_buckets

        if (self.table[index] == None):
            print("Entry not found *" + key + "* , Please check the Key ")
            return None
        elif (self.table[index].key == key):
            self.table[index] = self.table[index].link
            self.decrease_capacity_check()
        else:
            prev = self.table[index]
            current = self.table[index].link
            while current != None and current.key != key:
                prev = current
                current = current.link
            if (current == None):
                print("Entry not found *"+key+"* , Please check the Key ")
                return None
            if (current.link == None):
                prev.link = None
            else:
                prev.link = current.link
            self.decrease_capacity_check()
        return None

    def increase_capacity_check(self):
        """
        This function is used to increase the size of the table once the load capacity has been reached while adding
        values
        """
        load_factor = self.size / self.number_of_buckets
        if (load_factor >= self.load_limit):
            # Double the capacity
            self.number_of_buckets = self.number_of_buckets * 2
            # Create the backup of table so that the existing values
            # are not lost
            table_Bkp = self.table
            # Recreate the table
            self.table = [None for _ in range(self.number_of_buckets)]
            self.size = 0
            # Fill in previous values in the new table
            for key, value in iterTemp(table_Bkp):
                self.add(key, value)

    def decrease_capacity_check(self):
        """
        This function is used to decrease the size of the table once the load factor has (1-load_limit)
        and adds all the values to the new hash table.
        """
        self.size -= 1
        load_factor = self.size / self.number_of_buckets


        if load_factor < (1 - self.load_limit) and (self.number_of_buckets // 2)>=10:
            # Half the capacity
            self.number_of_buckets = self.number_of_buckets // 2
            # Create the backup of table so that the existing values
            # are not lost
            table_Bkp = self.table
            # Recreate the table
            self.table = [None for _ in range(self.number_of_buckets)]
            self.size = 0
            # Fill in previous values in the new table
            for key, value in iterTemp(table_Bkp):
                self.add(key, value)

    def contains(self, key) -> bool:
        """
        This function checks if the value is present in the hash table.
        :param key:     The key to be searched for in the hash table.
        :return:        True/ False depending on whether the value is present or not.
        """
        index = self.hash_func(key) % self.number_of_buckets

        try:
            location = self.table[index]

            while location != None:
                if (location.key == key):
                    return True
                else:
                    location = location.link
            return False

        except IndexError:
            return False

    def get(self, key):
        """
        This function is used to get the value from the hash table using the key passed through.
        :param key:     The key passed to get the corresponding value.
        :return:        value at the location of the key or 'None' if the key is not present.
        """
        index = self.hash_func(key) % self.number_of_buckets

        try:
            location = self.table[index]

            while location != None:
                if (location.key == key):
                    return location.value
                else:
                    location = location.link
            return None

        except IndexError:
            return None



    def __iter__(self):
        """
        Created an iterator to iterator over the table
        :return:
        """
        return self

    def __next__(self):
        """
        This function provides the next element in the iterator
        :return: key, value : Key valuey pairs from Hashmap
        """
        if (self.currentPos < self.number_of_buckets or self.currentNode != None):
            if (self.currentNode == None):
                while (self.currentNode == None and self.currentPos < self.number_of_buckets - 1):
                    if (self.currentNode == None):
                        self.currentPos += 1
                        self.currentNode = self.table[self.currentPos]
                    else:
                        self.currentNode = self.currentNode.link
            if (self.currentNode != None):
                key, value = self.currentNode.key, self.currentNode.value
                self.currentNode = self.currentNode.link
                return key, value
        raise StopIteration

    def __str__(self):
        """
        returns string value of the hash table
        :return:
        """
        return str(self.table)

    def imbalance(self):
        """
        The imbalance function that returns the imbalance value after performing the required calculation.
        :return:
        """
        non_empty_chain_count = 0
        for location in self.table:
            if location is not None:
                non_empty_chain_count += 1

        if non_empty_chain_count > 0:
            return (self.size / non_empty_chain_count) - 1
        elif non_empty_chain_count == 0:
            return (0)

def hashFunction_ord_sum(key):
    """
    Computes and returns hash value of a given key as sum
    of ordinal values of inidividual characters
    """
    sum = 0
    for i in range(len(str(key))):
        sum += ord(key[i])
    return (int(sum))


def main():
    """
    This is the main function of the program. Here we add all the values to the Hashmap and print the hashmap and the
    imbalance value.
    """

    hmapTest = HashMap(hashFunction_ord_sum, 10, 0.5)
    #hmapTest = HashMap(initial_num_buckets=10, load_limit=0.5)
    hmapTest.add("I", "Iter")
    hmapTest.add("In", "Inters")
    hmapTest.add("app", "apple")
    hmapTest.add("bar", "bars")
    hmapTest.add("app", "ball")
    hmapTest.add("123456789", "Helloworld")
    hmapTest.add("ball", "ballshop")
    hmapTest.add("bottle", "waterbottle")
    hmapTest.add("1234567", "Test_Length_7")
    hmapTest.add("12345678", "Test_Length_8")
    hmapTest.add("123456788", "EndtestCase")
    hmapTest.add("12345677", "Test_Length_77")
    hmapTest.add("123456677", "Test_Length_6677")
    hmapTest.add("cat", "ABrownCat")
    hmapTest.add("word", "Alphabet")
    hmapTest.add("saint", "Church")
    hmapTest.add("Umbrella", "Raining")
    print(hmapTest)
    print("Current table Size: " + str(hmapTest.number_of_buckets))
    hmapTest.remove("123456789")
    hmapTest.remove("123456788")
    hmapTest.remove("ball")
    hmapTest.remove("bottle")
    hmapTest.remove("1234567")
    hmapTest.remove("12345678")
    hmapTest.remove("word")
    hmapTest.remove("bottle")
    hmapTest.remove("Vineet")
    print(hmapTest)
    print("Current table Size: " + str(hmapTest.number_of_buckets))


if __name__ == '__main__':
    main()

