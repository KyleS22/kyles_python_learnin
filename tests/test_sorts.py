"""
File Name: test_sorts.py

Authors: Kyle Seidenthal

Date: 11-09-2020

Description: Tests for sorting algorithms.

"""

import pytest
import sys

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

    @pytest.fixture
    def word_lists(self):
        cases = []

        scrambled = ["cat", "cow", "car", "bat", "rat", "spaghetti"]
        expected = ["bat", "car", "cat", "cow", "rat", "spaghetti"]

        cases.append((scrambled, expected))

        return cases

    @pytest.fixture
    def number_lists(self):
        cases = []

        scrambled = [3, 1, 2, 4, 5, 6, 8, 7, 9, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        cases.append((scrambled, expected))

        scrambled = [1, 2, 4, 3, 1, 2, 3, 5]
        expected = [1, 1, 2, 2, 3, 3, 4, 5]

        cases.append((scrambled, expected))

        scrambled = [1.1, 1.2, 1.4, 1.3, 1.1, 1.2, 1.3, 1.5]
        expected = [1.1, 1.1, 1.2, 1.2, 1.3, 1.3, 1.4, 1.5]

        cases.append((scrambled, expected))

        scrambled = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        cases.append((scrambled, expected))

        scrambled = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1]
        expected = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

        cases.append((scrambled, expected))

        scrambled = [52, 2, 19, 10, 32, 74, 32, 14, 13, 2, 1, 74, 11, 102]
        expected = [1, 2, 2,  10, 11,  13, 14, 19, 32, 32, 52, 74, 74, 102]

        cases.append((scrambled, expected))

        scrambled = []
        expected = []

        cases.append((scrambled, expected))

        return cases

    @pytest.fixture
    def key_value_lists(self):
        cases = []

        scrambled = [(3, 'a'), (2, 'b'), (3, 'x'), (1, 'y'), (5, 'c'),
                     (1, 'd')]

        expected = [(1, 'y'), (1, 'd'), (2, 'b'), (3, 'a'), (3, 'x'), (5, 'c')]

        cases.append((scrambled, expected))

        return cases

    def test_bubble_sort(self, simple_lists):

        for scrambled, expected in simple_lists:
            assert sorts.bubble_sort(scrambled) == expected

    def test_merge_sort(self, simple_lists):
        for scrambled, expected in simple_lists:
            assert sorts.merge_sort(scrambled) == expected

    def test_burst_sort(self, word_lists):
        for scrambled, expected in word_lists:
            assert sorts.burst_sort(scrambled) == expected

    def test_spaghetti_sort(self, number_lists):

        if sys.platform.startswith("mac"):
            pytest.skip("This does not work on macos for some reason.")

        for scrambled, expected in number_lists:
            assert sorts.spaghetti_sort(scrambled) == expected

    def test_pigeonhole_sort(self, key_value_lists):
        for scrambled, expected in key_value_lists:
            assert sorts.pigeonhole_sort(scrambled) == expected

    def test_patience_sort(self, number_lists):
        for scrambled, expected in number_lists:
            assert sorts.patience_sort(scrambled) == expected

    def test_stooge_sort(self, simple_lists):
        for scrambled, expected in simple_lists:
            assert sorts.stooge_sort(scrambled) == expected

    def test_shellsort(self, simple_lists, number_lists):
        for scrambled, expected in simple_lists:
            assert sorts.shellsort(scrambled) == expected

        for scrambled, expected in number_lists:
            assert sorts.shellsort(scrambled) == expected

    def test_bogosort(self, simple_lists, number_lists):

        for scrambled, expected in simple_lists:
            assert sorts.bogosort(scrambled) == expected


class TestHelpers:

    def test_sedgewick(self):

        assert sorts._sedgewick_gap(5) == [1]

        assert sorts._sedgewick_gap(16) == [1, 5]

        assert sorts._sedgewick_gap(58) == [1, 5, 19]

        assert sorts._sedgewick_gap(124) == [1, 5, 19, 41]

        assert sorts._sedgewick_gap(330) == [1, 5, 19, 41, 109]
