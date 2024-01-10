## Implement no match
## Check for corner cases for Binary

import sys
from sort import mergeSortWordList
from bsearch import binarySearchRec
from bsearch import linearSearchFirstMatch,linearSearchLastMatch

def get_Next_Matching_Word(firstFoundIndex,currentIndex, prefix, wordList,lastIndex):
    """
    Finds the next matching word from the text file for the prefix entered by the user

    :param firstFoundIndex: index of the word from the sorted word list after binary search
    :param currentIndex: the current index at which the word was printed corresponding to the prefix
    :param prefix: the user entered prefix
    :param wordList: sorted word List
    :param lastIndex: last index from the word list containing the prefix entered by the user
    :return: the next word that contains the prefix
    """
    prefixFound,posFound=linearSearchFirstMatch(currentIndex, prefix, wordList, lastIndex)

    # If prefix is found after subsequent matches
    if(prefixFound):
        return(wordList[posFound],posFound+1)

    # If words with prefix are exhausted , return to intial postion
    else:
        return(wordList[firstFoundIndex],firstFoundIndex+1)


def read_Word_List(file):
    """
    Reads the file line by line , stores the lines
    in a List and returns the List

    :param  file: File name containing the word list
    :return     : List of words in the file
    """
    s1 = []

    with open(file) as f:
        for word in f:
            word = word.strip()
            s1.append(word)

    return (s1)


def autoComplete(wordListSorted):
    """
    Asks user to input prefix for autocomplete and calls binary search to
    search the word for the prefix entered.

    :param wordListSorted: Stores the sorted word list of the text file
    :return:
    """
    firstFindPos = -1
    currentIndex=-1
    lastIndex=-1
    prefixFirstMatch=""
    while True:
        prefix = input("Enter a prefix to search for : ")

        if prefix == "<QUIT>":
            print("Exiting Auto-complete! Good bye.")
            break

        else:

            if prefix != "":
                firstFindPos = binarySearchRec(wordListSorted, prefix.lower(), 0, len(wordListSorted) - 1)
                currentIndex=firstFindPos+1
                lastIndex=linearSearchLastMatch(firstFindPos, prefix, wordListSorted)
                prefixFirstMatch=prefix

                # Binary serach returns -1 is prefix not found
                if firstFindPos < 0:
                    print("Match not found !")
                    continue

                # If prefix found , print the word
                else:
                    print(wordListSorted[firstFindPos])

            else:

                # If first input is blank
                if(prefixFirstMatch==''):
                    print("Not a valid Input , Please enter a prefix")
                    autoComplete(wordListSorted)

                # If blank string is input after a valid prefix
                else:
                    nextWord,currentIndex = get_Next_Matching_Word(firstFindPos,currentIndex, prefixFirstMatch, wordListSorted,lastIndex)
                    print(nextWord)

def main():
    """
    The main function of the program that starts the autocomplete.py and prints initial statements
    and takes word file input from the command line.

    """
    print("Welcome to Auto-complete!")
    print("Usage: Enter a prefix to auto-complete.")
    print("Entering nothing will print the first word in the sorted list.")
    print("Enter <QUIT> to exit.")

    wordfile = sys.argv[1]
    #wordfile = "words.txt"

    wordList = read_Word_List(wordfile)
    wordListSorted = mergeSortWordList(wordList)
    print("The sorted list: " + str(wordListSorted))

    autoComplete(wordListSorted)


if __name__ == '__main__':
    main()
