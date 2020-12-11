"""
File Name: test_burst_trie.py

Authors: {% <AUTHOR> %}

Date: 10-12-2020

Description: {% <DESCRIPTION> %}

"""

import pytest

from kyles_python.data_structures.burst_trie import TrieNode, Container


class TestBurstTrie:

    def test_insert(self):

        t = TrieNode(None, is_root=True)

        t.insert("spaghetti")

        for child in t.children:
            if child is not None and child.value == "s":
                s_node = child

        assert "paghetti" in s_node._container.get_suffixes()

        t.insert("steve")

        for child in t.children:
            if child is not None and child.value == "s":
                s_node = child

        assert "paghetti" in s_node._container.get_suffixes()
        assert "teve" in s_node._container.get_suffixes()

        # Insert to burst container

        t.insert("salad")
        t.insert("sing")
        t.insert("sang")

        for child in t.children:
            if child is not None and child.value == "s":
                s_node = child

        assert len(s_node._container.get_suffixes()) == 0

        child_vals = []
        for child in s_node.children:

            if child is not None:
                child_vals.append(child.value)

        assert len(child_vals) == 4
        assert "a" in child_vals
        assert "p" in child_vals
        assert "t" in child_vals
        assert "i" in child_vals

        t.insert("a")

        for child in t.children:
            if child is not None and child.value == "a":
                a_node = child

        assert len(a_node._container.get_suffixes()) == 0

    def test_value(self):
        children = [TrieNode("a"), TrieNode("b")]
        node = TrieNode(None, children=children, is_root=True)

        with pytest.raises(ValueError):
            node.value = "'"
    def test_alphabet(self):
        node = TrieNode(None, is_root=True)

        with pytest.raises(ValueError):
            node.alphabet = "x"

    def test_str(self):

        node = TrieNode(None, is_root=True)

        node.insert("steve")

        expect_str ="None\ns, Container: []\ns\nContainer: ['teve']\n"

        assert node.__str__() == expect_str

        node.insert("spatula")
        node.insert("spaghetti")
        node.insert("sauce")
        node.insert("stove")
        node.insert("st")

        expect_str = ("None\ns, Container: []\ns\na, p, t, Container: "
                     "[]\na\nContainer: ['uce']\np\nContainer: ['aghetti', "
                      "'atula']\nt*\nContainer: ['eve', 'ove']\n")
        assert node.__str__() == expect_str

    def test_dft(self):

        t = TrieNode(None, is_root=True)

        t.insert("steve")
        t.insert("string")
        t.insert("sing")
        t.insert("sang")
        t.insert("strudel")
        t.insert("sact")
        t.insert("potato")
        t.insert("alfredo")
        t.insert("alpaca")
        t.insert("alarm")
        t.insert("alarming")
        t.insert("along")
        t.insert("studabaker")
        t.insert("studmuffin")
        t.insert("alf")
        t.insert("alfie")

        dft = t.dft()

        assert dft == ['alarm', 'alarming', 'alf', 'alfie', 'alfredo', 'along',
                      'alpaca', 'potato', 'sact', 'sang', 'sing', 'steve',
                      'string', 'strudel', 'studabaker', 'studmuffin']

    def test_search(self):
        t = TrieNode(None, is_root=True)

        test_words = ["steve", "string", "sing", "sang", "strudel",
                      "sact", "potato", "alfredo", "alpaca", "alarm",
                      "alarming", "along", "studabaker", "studmuffin", "alf",
                      "alfie"]

        for word in test_words:
            t.insert(word)

        # Search a nonexistant word
        assert t.search("Jim") is False

        # Search for all the words
        for word in test_words:
            print(word)
            assert t.search(word) is True

class TestContainer:

    def test_insert(self):
        container = Container()

        # Insert something
        container.insert("b")

        assert container._suffixes[0] == "b"

        # Insert something that already exists
        container.insert("b")

        assert len(container._suffixes) == 1
        assert container._suffixes[0] == "b"

        container.insert("a")

        assert len(container._suffixes) == 2
        assert container._suffixes[0] == "a"

    def test_is_full(self):

        container = Container()

        # Cap is 5
        assert container.is_full() is False

        container.insert("a")
        assert container.is_full() is False

        container.insert("b")
        assert container.is_full() is False

        container.insert("c")
        assert container.is_full() is False

        container.insert("d")
        assert container.is_full() is False

        container.insert("e")
        assert container.is_full() is True

    def test_burst(self):

        container = Container()

        container.insert("a")

        sf = container.burst()

        assert sf == ["a"]
        assert len(container.get_suffixes()) == 0

    def test_search(self):

        container = Container()

        assert container.search("x") is False

        container.insert("steve")
        assert container.search("steve") is True

    def test_remove(self):
        container = Container()

        assert container.remove("X") is True

        container.insert("a")

        assert container.remove("a") is True
        assert len(container.get_suffixes()) == 0

        container.insert("a")
        container.insert("b")

        assert container.remove("a") is False
        assert len(container.get_suffixes()) == 1
