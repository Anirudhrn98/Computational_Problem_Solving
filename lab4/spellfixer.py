"""

file: spellfixer.py
description: Spell checks and corrects the input text
language: python3
author: Anirudh Narayanan, an9425@g.rit.edu
author: Vineet Singh     , vs9779@rit.edu

"""

import sys
import re


def wordListToSet(file) -> set:
    """
    Reads the file line by line , stores the lines
    in a set and returns the set

    :param  file: File name containing the word list
    :return     : set of words in the file
    """
    s1 = set()

    with open(file) as f:
        for word in f:
            word = word.strip().lower()
            s1.add(word)
    return (s1)


def keyboardToDict(file) -> dict:
    """
    Reads the file line by line , creates a dictionary.
    dictionary's key is the first character of every line
    dictionary's value is a list of values apart from first
    character for every line

    :param file: File name containing the word list
    :return    : Dictionary of charcters and surrounding
                 elements
    """

    keyChars = dict()

    with open(file) as f:
        for word in f:
            word = word.strip()
            splitWords = word.split()
            keyChars[splitWords[0]] = splitWords[1:]

    return (keyChars)


def existsInWordList(wordList, word) -> bool:
    """
    Checks if word exists in the word List
    :param wordList: set of words
    :param     word: word to be checked
    :return        : Boolean indicating if word exists
                     in the set
    """
    return (word in wordList)


def wordCorrection_Transpose(wordList, word):
    """
    Corrects word if adjacent characters have
    been interchanged
    :param wordList: set of words
    :param     word: word to be checked
    :return        : corrected word
    """
    wordCorrected = False
    wordClean = "".join(re.sub('[^0-9a-zA-Z]+', '', word)).replace(" ", "")
    for i in range(len(wordClean) - 1):
        x = list(wordClean)
        x[i], x[i + 1] = x[i + 1], x[i]
        tempWord = "".join(x)
        if tempWord in wordList:
            return tempWord
            wordCorrected = True
            break
        else:
            continue

    if wordCorrected == False:
        return word


def wordCorrection_Deletion(wordList, word):
    """
    Corrects word if word contains one extra
    character
    :param wordList: set of words
    :param     word: word to be checked
    :return        : corrected word
    """
    wordCorrected = False
    wordClean = "".join(re.sub('[^0-9a-zA-Z]+', '', word)).replace(" ", "")

    for i in range(len(wordClean)):
        tempWord = wordClean[0:i] + wordClean[i + 1:]
        if tempWord in wordList:
            return tempWord
            wordCorrected = True
            break
        else:
            continue

    if wordCorrected == False:
        return word


def wordCorrection_UsingKeyChars(wordList, keyChars, word):
    """
    Corrects word if one of the chars was
    was mistakingly replaced by one of the characters
    around the correct character
    :param wordList: set of words
    :param keycahrs: Dictionary of surrounding chars
    :param     word: word to be checked
    :return        : corrected word
    """
    wordCorrected = False
    wordClean = "".join(re.sub('[^0-9a-zA-Z]+', '', word)).replace(" ", "")
    for i in range(len(wordClean)):
        for keys in keyChars[wordClean[i].lower()]:
            tempWord = wordClean[0:i] + keys + wordClean[i + 1:]
            if tempWord in wordList:
                return tempWord
                wordCorrected = True
                break
            else:
                continue
    if wordCorrected == False:
        return word


if __name__ == "__main__":

    ## set of correct words
    wordList = set()
    ## Dictionary of surrounding characters
    keyChars = dict()

    ## Exception handling module
    try:
        #wordfile = input("Enter word list file: ").lower()
        wordfile = sys.argv[1]
        wordList = wordListToSet(wordfile)

        #keyCharsFile = input("Enter keyboard file: ").lower()
        keyCharsFile = sys.argv[2]
        keyChars = keyboardToDict(keyCharsFile)

        print("Welcome to Spell Fixer !!")
        print()

        while True:
            inputStr = input(">")

            if inputStr == "!*!":
                print("Bye")
                break

            else:
                ##Splitting the string
                words = re.findall(r"[\w']+|[.,!?;]", inputStr)
                ## Empty string to store corrected sentence
                cleanStr = ""
                for word in words:
                    ## Adding punctions to the final sentence
                    if word in [".",",","!","?",";"]:
                        cleanStr=cleanStr + word
                        continue

                    if existsInWordList(wordList, word):
                        cleanStr = cleanStr + " " + word
                        continue
                    else:
                        ## First Correction for character sliding type of errors
                        firstCorrection = wordCorrection_UsingKeyChars(wordList, keyChars, word)
                        ## Second Correction for transpose type of errors
                        secondCorrection = wordCorrection_Transpose(wordList, word)
                        ## Third Correction for extra character type of errors
                        thirdCorrection = wordCorrection_Deletion(wordList, word)

                        if existsInWordList(wordList, firstCorrection):
                            cleanStr = cleanStr +" "+ firstCorrection
                            continue
                        elif existsInWordList(wordList, secondCorrection):
                            cleanStr = cleanStr +" "+ secondCorrection
                            continue
                        elif existsInWordList(wordList, thirdCorrection):
                            cleanStr = cleanStr +" "+ thirdCorrection
                            continue

                        else:
                            cleanStr = cleanStr + " "+ word
                            continue
                ## Print corrected sentence
                print(cleanStr.strip() + "\n")

    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)
