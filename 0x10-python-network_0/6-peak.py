#!/usr/bin/python3
""" Find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Find and return a peak element in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: A peak element in the list.

    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
