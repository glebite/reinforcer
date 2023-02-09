"""derakht.py

Tree representations of words in a given language.
"""
from collections import defaultdict


class Node:
    """Node
    """
    def __init__(self, value):
        """__init__ - initializer for a Node class
        """
        self.value = value
        self.parent = None
        self.children = defaultdict()


class Derakht:
    """Derakht
    """
    def __init__(self):
        """__init__ - intializer
        """
        self.base_children = defaultdict()
        self.stack = []

    def add(self, word):
        """ add - a thing
        TODO: remove print - use logging
        """
        print(f'Adding: {word=}')
        if len(word) == 0:
            return
        first = word[0]
        if first in self.base_children:
            print(f"{first=} is already here in self.base_children")
            self.descend(self.base_children[first], word[1:])
        else:
            print(f"{first=} is not here - adding.")
            self.base_children[first] = Node(first)
            self.descend(self.base_children[first], word[1:])

    def descend(self, node, sub_word):
        if len(sub_word) == 0:
            print("At the end of the word.")
            node.children['NULL'] = Node('NULL')
            return
        first = sub_word[0]
        if first in node.children:
            print(f"{first=} is already here in children")
            self.descend(node.children[first], sub_word[1:])
        else:
            print(f"{first=} is not here - adding.")
            thingy = Node(first)
            thingy.parent = node
            node.children[first] = thingy
            self.descend(thingy, sub_word[1:])

    def walk(self):
        for letter in self.base_children:
            print(f'{letter=} {type(letter)=}', end='')
            self.stack.append(letter)
            self.step(self.base_children[letter])
            print(f'{self.stack=}')
            self.stack.pop()

    def step(self, node):
        print(f'Coming into: {node.value=}')
        if not node.children:
            print()
            # self.stack.pop()
            return
        else:
            print(f'\t{node.parent=}')
            for letter in node.children:
                self.stack.append(letter)
                if letter == "NULL":
                    print('-> NULL')
                    continue
                print(f'-> {letter} ', end='')
                self.step(node.children[letter])
                print(f'STACK: {self.stack=}')
        return


if __name__ == "__main__":
    x = Derakht()
    x.add('dog')
    x.add('do')
    x.add('bat')
    x.walk()
