"""
file: tests.py
description: Verify the chained hash map class implementation
"""

from hashmap import HashMap as Hashmap


def print_map(a_map):
    for word, counter in a_map:
        print(str(word) + "." + str(counter), end="-->")
    print()

def min_bucket_check():
    print("Trying to create a Hasmap of 8 buckets")
    h1 = Hashmap(initial_num_buckets=8)
    print("Creation complete , lets check the size")
    print("Bucket size of created Hashmap :" +str(h1.number_of_buckets))
    print("Conclusion Minimum buckets cannot be less than 10 ")

def remove_from_empty():
    print("Create an empty Hashmap of 10 buckets")
    h2 = Hashmap(initial_num_buckets=10)
    print("Creation complete , lets check if we can remove any element")
    print(h2.remove(""))
    print("Conclusion cannot remove from empty list")

def check_for_resize_on_addition():
    print("Create an empty Hashmap of 10 buckets")
    print("If we keep load limit to be 0.3")
    print("Then re-sizing should take place when more than 2 elements are added to list")
    h3 = Hashmap(initial_num_buckets=10,load_limit=0.3)
    print("Creation complete , lets add elements")

    h3.add("I", "Iter")
    h3.add("In", "Inters")
    print("****** All elements in the Hashmap currently ******")
    for i in h3.table:
        print(i)
    print("Current table Size: " +str(h3.number_of_buckets))
    print("Filled entires: " + str(h3.size))
    print("Let's add one more element and check")
    h3.add("app", "apple")
    print()
    print("****** All elements in the Hashmap currently ******")
    for i in h3.table:
        print(i)
    print("Current table Size: " + str(h3.number_of_buckets))
    print("Filled entires: " + str(h3.size))

def check_for_resize_on_removal():
    print("Create an empty Hashmap of 10 buckets")
    print("Creation complete , lets add elements")
    print("If we also load limit to be 0.5")
    print("Then re-sizing should take place when less list is lest than 50% filled")
    h4 = Hashmap(initial_num_buckets=10, load_limit=0.5)
    print("Creation complete , lets add elements")
    h4.add("I", "Iter")
    h4.add("In", "Inters")
    h4.add("app", "apple")
    h4.add("bar", "bars")
    h4.add("bottle", "waterbottle")
    h4.add("cat", "ABrownCat")
    h4.add("word", "Alphabet")
    h4.add("saint", "Church")
    h4.add("Umbrella", "Raining")

    print("****** All elements in the Hashmap currently ******")
    for i in h4.table:
        print(i)
    print("Current table Size: " + str(h4.number_of_buckets))
    print("Filled entires: " + str(h4.size))
    print("Let's remove elements and check")
    h4.remove("app")
    h4.remove("I")
    h4.remove("In")
    h4.remove("word")
    h4.remove("cat")
    h4.remove("saint")
    h4.remove("Umbrella")
    h4.remove("bottle")
    print()
    print("****** All elements in the Hashmap currently ******")
    for i in h4.table:
        print(i)
    print("Current table Size: " + str(h4.number_of_buckets))
    print("Current table Size: " + str(h4.size))


if __name__ == '__main__':


    print("** Check if a Hashmap of less than 10 buckets can be created **")
    print()
    min_bucket_check()
    print()

    print("** Check if we can remove from empyth Hash map **")
    remove_from_empty()
    print()

    print("** Check if HashMap resizes on reachin the load limit on addition **")
    check_for_resize_on_addition()
    print()

    print("** Check if HashMap resizes on reachin the load limit on removal of elements**")
    check_for_resize_on_removal()
    print()

    #test0()