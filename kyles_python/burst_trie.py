"""
File Name: burst_trie.py

Authors: Kyle Seidenthal

Date: 16-09-2020

Description: Implementation of a Burst Trie data-structure.

"""
ENGLISH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class TrieNode():

    """Represents a Trie Node

    A Trie Node represents one letter, and points to a list of children Trie
    Nodes, or possibly containers for prefixes.
    """

    def __init__(self, value, children=None, completes_string=False,
                 alphabet=ENGLISH, is_root=False):
        """Create a new Trie Node

        Args:
            value: The value (alphabet character) that this node represents.

        Kwargs:
            children: A list of children for this node.
            completes_string: Whether this node completes a string.
            alphabet: A list of characters that are valid in the chosen
                      alphabet.
            is_root: Whether this node is the root of the trie.
        Returns: A Trie Node

        """
        self.alphabet = alphabet
        self._is_root = is_root

        if is_root:
            value = None

        self.value = value
        self.children = children
        self.completes_string = completes_string

        self._container = Container()

        if self.children is None:
            self.children = [None for i in self.alphabet]


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, x):

        if x is None and self._is_root:
            self.__value = None

        elif x.lower() not in self.alphabet:
            raise ValueError("Trie Node value must be part of the Node's"
                             "alphabet")

        else:
            self.__value = x.lower()

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, l):
        self.__children = l

    @property
    def completes_string(self):
        return self.__completes_string

    @completes_string.setter
    def completes_string(self, x):
        self.__completes_string = x

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, x):
        if not isinstance(x, list):
            raise ValueError("Alphabet must be a list of characters.")

        self.__alphabet = x

    def insert(self, string):
        """Insert the given string into the trie node.

        Args:
            string (string): The string to insert into this trie node.

        Returns: None
        """
        if len(string) == 0:
            self.completes_string = True
            return

        # Search children for trie node with first char and insert the
        # rest of string to that node. Use alphabet.indexof(letter)

        first_char = string[0]
        index = self.alphabet.index(first_char)


        if self._is_root:
            self._insert_idx(index, string, to_container=False)
        else:
            self._insert_idx(index, string, to_container=True)

        # If container over capacity, burst into trie node
        if self._container.is_full():
            suffixes = self._container.burst()

            for suffix in suffixes:
                first_char = suffix[0]
                index = self.alphabet.index(first_char)

                self._insert_idx(index, suffix, to_container=False)

    def _insert_idx(self, index, string, to_container=True):
        """Insert into the child at index.

        Args:
            index (int): The index of the child to insert to.
            string (string): The string to insert.

        Kwargs:
            to_container (bool): What to do if there is no child at index.
                                 If true, put the suffix in the container.
                                 If False, create a new TrieNode.

        Returns: None

        """
        node = self.children[index]

        if node is None:
            if to_container:
                self._container.insert(string)
            else:
                node = TrieNode(string[0])
                node.insert(string[1:])
                self.children[index] = node
        else:
            node.insert(string[1:])

    def __str__(self):

        if self.completes_string:
            out = "{}*\n".format(self.value)
        else:

            out = "{}\n".format(self.value)

        for child in self.children:
            if child is not None:
                out += str(child.value) + ", "

        out += "Container: {}".format(self._container)

        out += "\n"

        for child in self.children:
            if child is not None:
                out += str(child)

        return out

    # TODO: Depth First Traversal

    # TODO: Remove

    # TODO: Search

class Container():

    """Container for suffixes"""

    def __init__(self):
        """Create a new container. """

        self._suffixes = []
        self._capacity = 5

    def insert(self, suffix):
        """Insert a new suffix.

        Args:
            suffix (string): The suffix to add to this container.

        Returns: None

        """

        if suffix not in self._suffixes:
            self._suffixes.append(suffix)

    def is_full(self):

        if len(self._suffixes) >= self._capacity:
            return True

        else:
            return False

    def burst(self):
        """Clear the suffixes in the container.
        Returns: The list of suffixes before clearing.

        """
        sf = self._suffixes
        self._suffixes = []

        return sf

    def __str__(self):
        out = "{}".format(self._suffixes)

        return out

if __name__ == "__main__":

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
    print(t)
