"""
File Name: test_sorts.py

Authors: Kyle Seidenthal

Date: 11-09-2020

Description: Tests for sorting algorithms.

"""

import pytest

from kyles_python import sorts


class TestSort:

    @pytest.fixture
    def simple_lists(self):
        cases = []

        scrambled = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        cases.append((scrambled, expected))

        scrambled = []
        expected = []

        cases.append((scrambled, expected))

        scrambled = ['d', 'b', 'g', 'f', 'c', 'a', 'e']
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        cases.append((scrambled, expected))

        scrambled = ["cat", "cow", "car", "bat", "rat", "spaghetti"]
        expected = ["bat", "car", "cat", "cow", "rat", "spaghetti"]

        cases.append((scrambled, expected))

        scrambled = [1, 2, 4, 3, 1, 2, 3, 5]
        expected = [1, 1, 2, 2, 3, 3, 4, 5]

        cases.append((scrambled, expected))

        return cases

    def test_bubble_sort(self, simple_lists):

        for scrambled, expected in simple_lists:
            assert sorts.bubble_sort(scrambled) == expected

    def test_merge_sort(self, simple_lists):
        for scrambled, expected in simple_lists:
            assert sorts.merge_sort(scrambled) == expected
