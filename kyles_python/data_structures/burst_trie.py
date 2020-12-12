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
    def children(self, children):
        self.__children = children

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
        string = string.lower()

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

    def dft(self):
        """Return items in depth first traversal order.

        Returns: A list of the strings in depth first traversal order

        """

        if self._is_root:
            value = ""
        else:
            value = self.value

        child_words = []
        words = []

        if self.completes_string:
            words.append(value)

        for child in self.children:
            if child is not None:
                child_words.append(child.dft())

        for cw in child_words:
            for w in cw:
                string = value + w
                words.append(string)

        for suffix in self._container.get_suffixes():
            words.append(value + suffix)

        return words

    def search(self, word):
        """Search for the given word in the trie.

        Args:
            word (string): The word to search for.

        Returns: True if the word exists, False otherwise.

        """

        if len(word) == 0 and self.completes_string:
            return True
        elif len(word) == 0:
            return False

        word = word.lower()

        found = self._container.search(word)

        first_char = word[0]
        string = word[1:]

        if found is False:
            for child in self.children:
                if child is not None and child.value == first_char:

                    found = child.search(string)

                    break

        return found

    def remove(self, word):
        """Remove a word from the trie.

        Args:
            word (string): The word to remove.

        Returns: True if the word was removed successfully.

        """

        if not self.search(word):
            return False

        else:
            self._remove_help(word)
            return True

    def _remove_help(self, word):
        """Remove a word from the trie.

        Args:
            word (string): The word to remove.

        Returns: True if the current node can be removed.

        """

        word = word.lower()

        num_children = 0

        for child in self.children:
            if child is not None:
                num_children += 1

        if len(word) == 0 and self.completes_string:
            self.completes_string = False

            if len(self._container.get_suffixes()) == 0 and num_children == 0:
                return True
            else:
                return False

        container_found = self._container.search(word)
        remove_container = self._container.remove(word)



        if container_found and remove_container:

            # We removed the word from the container, and we no longer need
            # this node for anything
            if num_children == 0 and not self.completes_string:
                return True

            # We removed the word from the container, but this node completes
            # another string
            elif num_children == 0 and self.completes_string:
                return False

            # We removed the word from the container, but this node has
            # children
            else:
                return False

        elif container_found and not remove_container:
            # we removed the word from the container, but we still need this
            # node
            return False

        # We did not find the word in the container
        else:
            for child in self.children:
                if child is not None and child.value == word[0]:
                    remove_child = child._remove_help(word[1:])

                    if remove_child:
                        self.children[self.children.index(child)] = None

                        if (len(self._container.get_suffixes()) == 0 and
                                num_children - 1 == 0):
                            return True
                        else:
                            return False


class Container():

    """Container for suffixes"""

    def __init__(self, capacity=5):
        """Create a new container. """

        self._suffixes = []
        self._capacity = capacity

    def insert(self, suffix):
        """Insert a new suffix.

        Args:
            suffix (string): The suffix to add to this container.

        Returns: None

        """

        if suffix not in self._suffixes:
            self._suffixes.append(suffix)
            self._suffixes = sorted(self._suffixes)

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

    def get_suffixes(self):
        return self._suffixes

    def search(self, word):
        """Search the containter for the given word.

        Args:
            word (string): The word to search for.

        Returns: True if word appears in sufixes, False otherwise.

        """

        if word in self._suffixes:
            return True
        else:
            return False

    def remove(self, word):
        """Remove the word from the container.

        Args:
            word (string): The word to remove.

        Returns: True if the container can be removed.

        """
        if word in self._suffixes:
            self._suffixes.remove(word)

        if len(self._suffixes) == 0:
            return True

        else:
            return False
