"""
File Name: sorts.py

Authors: Kyle Seidenthal

Date: 11-09-2020

Description: Various Sorting Algorithms

"""


def bubble_sort(input_list):
    """Bubble sort the given list.
    Works by "bubbling" large items to the top, by comparing every element to
    every other element.  Time complexity is O(n^2), so don't ever use this.

    Args:
        input_list: A list of sortable items.

    Returns: A sorted list.

    """
    swapped = True
    n = len(input_list)

    while swapped:
        swapped = False

        for i in range(1, n):
            if input_list[i-1] > input_list[i]:
                tmp = input_list[i-1]
                input_list[i-1] = input_list[i]
                input_list[i] = tmp
                swapped = True
        n = n-1

    return input_list
