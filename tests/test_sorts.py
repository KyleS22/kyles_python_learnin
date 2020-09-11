"""
File Name: test_sorts.py

Authors: Kyle Seidenthal

Date: 11-09-2020

Description: Tests for sorting algorithms.

"""

import pytest

from kyles_python import sorts


class TestSort:

    def test_bubble_sort(self):

        list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        assert sorts.bubble_sort(list) == sorted

        list = []
        sorted = []

        assert sorts.bubble_sort(list) == sorted

        list = ['d', 'b', 'g', 'f', 'c', 'a', 'e']
        sorted = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        assert sorts.bubble_sort(list) == sorted

        list = ["cat", "cow", "car", "bat", "rat", "spaghetti"]
        sorted = ["bat", "car", "cat", "cow", "rat", "spaghetti"]

        assert sorts.bubble_sort(list) == sorted

        list = [1, 2, 4, 3, 1, 2, 3, 5]
        sorted = [1, 1, 2, 2, 3, 3, 4, 5]

        assert sorts.bubble_sort(list) == sorted
