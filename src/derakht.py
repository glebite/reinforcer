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

    def add(self, word):
        """ add - a thing
        TODO: remove print - use logging
        """
        print(word)
        if len(word) == 0:
            return
        first = word[0]
        if first in self.base_children:
            print(f"{first=} is here")
            self.descend(self.base_children[first], word[1:])
        else:
            print(f"{first=} is not here - adding.")
            self.base_children[first] = Node(first)
            print("Descending...")
            self.descend(self.base_children[first], word[1:])

    def descend(self, node, sub_word):
        """ descend - a thing

        TODO: remove print - use logging
        """
        print(f'In descend: {node=} {sub_word=}')
        if len(sub_word) == 0:
            print('\tNull -> returning...')
            node.children['NULL'] = Node('NULL')
            return
        first = sub_word[0]
        print(type(node.children))
        print(f'\t{first=} is there... {sub_word[1:]=}')
        print(node)
        if first in node.children:
            print(f'\t{first=} is here in {node.children=}')
            self.descend(node.children[first], sub_word[1:])
        else:
            print(f'\t{first=} is NOT here - creating a new node.')
            thingy = Node(first)
            thingy.parent = node
            print(f'Node is created: {thingy=}')
            node.children[first] = thingy
            self.descend(thingy, sub_word[1:])

    def walk(self):
        for letter in self.base_children:
            print(f'{letter} ', end='')
            self.step(self.base_children[letter])

    # def step(self, node):
    #     if not node.children:
    #         print()
    #         return
    #     else:
    #         print(f'{node.parent}')
    #         for letter in node.children:
    #             print(f'-> {letter} ', end='')
    #             self.step(node.children[letter])
    #     return

    def step(self, node):
        print(f'Coming into: {node.value=}')
        if not node.children:
            print()
            return
        else:
            print(f'{node.parent=}')
            for letter in node.children:
                if letter == "NULL":
                    continue
                print(f'-> {letter} ', end='')
                self.step(node.children[letter])
                print(f'Backing out of: {node.value=}')
        return


if __name__ == "__main__":
    x = Derakht()
    x.add('dog')
    x.add('do')
    breakpoint()
    x.add('bat')
    # x.add('bad')
    x.walk()
