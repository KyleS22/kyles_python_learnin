"""
File Name: sorts.py

Authors: Kyle Seidenthal

Date: 11-09-2020

Description: Various Sorting Algorithms

"""
import threading
import time
import heapq
import math

from kyles_python.data_structures.burst_trie import TrieNode, ENGLISH


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


def burst_sort(input_list, alphabet=ENGLISH):
    """Burst sort.
    Works by adding input items to a burst trie and then returning the depth
    first traversal of the trie.

    Args:
        input_list (list): A list of strings to sort that adhere to the given
                           alphabet.

    KWargs:
        alphabet (list): A list of valid characters for the sorting alphabet.
                         Default is english.

    Returns: The sorted items as a list
    """
    t = TrieNode(None, is_root=True, alphabet=alphabet)

    for word in input_list:
        t.insert(word)

    return t.dft()


def spaghetti_sort(input_list):
    """A simulated spaghetti sort.  (This is next to useless.)
    O(max(input_list))
    Args:
        input_list (list): A list of numbers to sort.

    Returns: The sorted items as a list.

    """

    if len(input_list) == 0:
        return input_list

    m = max(input_list)

    queue = []

    for i in range(len(input_list)):
        x = input_list[i]
        t = threading.Thread(target=_spaghetti_thread,
                             args=(x, x/m * 2, queue))
        t.daemon = True
        t.setDaemon(True)
        t.start()

    time.sleep(m/m * 2 + 0.01)

    return queue


def pigeonhole_sort(input_list):
    """Pigeonhole sort is suitable for lists of (key, value) pairs, where the
    number of possible keys (m) is is roughly the same as the number of entries
    (n).  O(m + n)

    Args:
        input_list (list): The input list of (key, value) tuples.

    Returns: The sorted list.

    """

    start = min([x[0] for x in input_list])
    size = max([x[0] for x in input_list]) - start + 1

    pigeonholes = [[] for i in range(size)]

    for key, value in input_list:
        i = key - start
        pigeonholes[i].append((key, value))

    sorted_list = []

    for p in pigeonholes:
        for x in p:
            sorted_list.append(x)

    return sorted_list


def patience_sort(input_list):
    """Patience sort, based on the cardgame.

    Args:
        input_list (list): A list of integers.

    Returns: Sorted list.

    """

    piles = []

    for x in input_list:
        if len(piles) == 0:
            piles.append([x])
        else:
            # Find leftmost pile whose value is >= x using binary search
            # O(n log n)

            p_index = _patience_binary_search(piles, x)

            if p_index is None:
                piles.append([x])
            else:
                piles[p_index].append(x)

    # Merge piles using priority queue O(n log n)
    elements = [(p[0], p) for p in piles]
    heapq.heapify(elements)

    sorted_list = []
    while(len(elements) > 0):
        val, p = heapq.heappop(elements)
        sorted_list.append(val)
        p.pop()
        if len(p) > 0:
            heapq.heappush(elements, (p[0], p))

    return sorted_list


def stooge_sort(input_list):
    """Stooge sort the list.  This is a recursive sorting algorithm with awful
    time complexity, O(n^(log 3 / log 1.5)).  Still interesting though.

    Args:
        input_list (list): A list of items to be sorted.

    Returns: The sorted list.

    """
    if len(input_list) == 0:
        return input_list

    # If the first item is bigger than the last, swap them
    if input_list[0] > input_list[-1]:
        temp = input_list[-1]
        input_list[-1] = input_list[0]
        input_list[0] = temp

    if len(input_list) >= 3:
        split = math.ceil(len(input_list) * (2/3))

        # Sort the first 2/3 of the list
        first_sort = stooge_sort(input_list[:split])

        input_list[:split] = first_sort

        # Sort the last 2/3 of the list
        split = math.floor(len(input_list) / 3)

        second_sort = stooge_sort(input_list[split:])
        input_list[split:] = second_sort

        # Sorth the first 2/3 again
        split = math.ceil(len(input_list) * (2/3))

        third_sort = stooge_sort(input_list[:split])
        input_list[:split] = third_sort

    return input_list


def _patience_binary_search(piles, x):
    """Search for the correct pile for x.

    Args:
        piles (list): A list of piles.
        x (int): The number to add to the piles.

    Returns: The index of the correct pile, or none if no pile works.

    """
    left = 0
    right = len(piles) - 1

    while left < right:
        mid = (left + right) // 2

        if piles[mid][-1] < x:
            left = mid + 1
        elif piles[mid][-1] > x:
            right = mid - 1

        else:
            return mid

    return None


def _spaghetti_thread(x, units, queue):
    """Create a thread for spaghetti sort.

    Args:
        x (number): The number we are sorting.
        units (int): The number of spaghetti units.
    Returns: x

    """
    time.sleep(units)
    queue.append(x)

    return None


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
