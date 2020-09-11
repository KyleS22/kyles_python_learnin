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


def merge_sort(input_list):
    """Merge sort the given list.
    Works by recursively splitting the list into smaller sublists until they
    are trivial to sort.   Then merge them all back together.
    Time complexity: O(n log n).

    Args:
        input_list: A list of sortable items

    Returns: A sorted list

    """
    # Base case, list has zero or one element, which is sorted
    if len(input_list) <= 1:
        return input_list

    # Recursive case.
    left, right = _split(input_list)

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)


def _split(input_list):
    """Split a list into two equal(ish) halves.

    Args:
        input_list: The list to split.

    Returns: Two lists: (left, right)

    """
    n = len(input_list)//2

    return input_list[:n], input_list[n:]


def _merge(left, right):
    """Merge two lists into sorted order.

    Args:
        left: Left half of the list.
        right: Right half of the list.

    Returns: One list, containing both lists.

    """
    new_list = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            new_list.append(left[0])
            left.pop(0)
        else:
            new_list.append(right[0])
            right.pop(0)

    while len(left) > 0:
        new_list.append(left[0])
        left.pop(0)

    while len(right) > 0:
        new_list.append(right[0])
        right.pop(0)

    return new_list
