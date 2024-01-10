def binarySearchRec(data, val, left, right):
    """
    The function does the recursive binary search operation on the words.txt file to return the word with the 1st index
    containing the prefix entered by the user.

    :param data: The value to check at the specific index
    :param val: The prefix entered by the user
    :param left: left index during the binary search
    :param right: right index during the binary search
    :return: recursive call for the binary search
    """
    # if the left index is greater than the right index then word does not exist for the prefix
    if left > right:
        return -1
    midindex = (left + right) // 2  # find middle index by splitting the list into half
    if data[midindex].startswith(val):
        if not (data[midindex - 1].startswith(val)):
            return midindex
        if data[midindex - 1] == val:
            return binarySearchRec(data, val, left, midindex - 1)


    # if the data at middle index is greater than the value then decrement of right index and recursive call
    # or vice-versa.
    if data[midindex] > val:
        return binarySearchRec(data, val, left, midindex - 1)
    else:
        return binarySearchRec(data, val, midindex + 1, right)


def linearSearchFirstMatch(startIndex,prefix,wordList,lastIndex):
    """
    linear search to find the first index and word found from the the text file

    :param startIndex: start index of the word from which the prefix starts
    :param prefix: prefix entered by the user
    :param wordList: word file containing the words from which to search
    :param lastIndex: last index of the word containing the prefix
    :return:tuple containing boolean of whether word was found and its position
    """

    prefixFound=False
    posFound=-1

    for i in range(startIndex,lastIndex+1):

        if(wordList[i].startswith(prefix)):
            posFound=i
            prefixFound=True
            break

    return (prefixFound,posFound)


def linearSearchLastMatch(startIndex, prefix, wordList):
    """
    linear search to find the index of the last word which contains the prefix entered by the user

    :param startIndex: start index of the word from which the prefix starts
    :param prefix: prefix entered by the user
    :param wordList: word file containing the words from which to search
    :return: lastIndex: index of the last word which contains the prefix
    """
    lastIndex=-1

    for i in range(startIndex, len(wordList)):
        if (wordList[i].startswith(prefix)):
            lastIndex=i
        else:
            continue

    return(lastIndex)