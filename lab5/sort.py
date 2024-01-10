def _split(data):
    """
    Split the data into halves and return the two halves
    :param data: The list to split in half
    :return: Two lists, cut in half
    """
    return data[:len(data) // 2], data[len(data) // 2:]


def _merge(left, right):
    """
    Merges two sorted list, left and right, into a combined sorted result
    :param left: A sorted list
    :param right: A sorted list
    :return: One combined sorted list
    """

    # the sorted left + right will be stored in result
    result = []
    leftIndex, rightIndex = 0, 0

    # loop through until either the left or right list is exhausted
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    # take the un-exhausted list and extend the remainder onto the result
    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    elif rightIndex < len(right):
        result.extend(right[rightIndex:])

    return result


def mergeSortWordList(data):
    """
    Performs a merge sort and returns a newly sorted list.
    :param data: A list of data
    :return: A sorted list
    """

    # an empty list, or list of 1 element is already sorted
    if len(data) < 2:
        return data
    else:
        # split the data into left and right halves
        left, right = _split(data)

        # return the merged recursive mergeSort of the halves
        return _merge(mergeSortWordList(left), mergeSortWordList(right))
