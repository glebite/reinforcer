"""derakht.py

"""
from collections import defaultdict


class Node:
    def __init__(self, value):
        """
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
        print(word)
        if len(word) == 0:
            return
        first = word[0]
        if first in self.base_children:
            print(f"{first=} is here")
            self.descend(None, word[1:])
        else:
            print(f"{first=} is not here - adding.")
            self.base_children[first] = Node(first)
            print("Descending...")
            self.descend(self.base_children[first], word[1:])

    def descend(self, node, sub_word):
        print(f'In descend: {node=} {sub_word=}')
        if len(sub_word) == 0:
            print('\tNull -> returning...')
            return
        first = sub_word[0]
        print(f'\t{first=} is there... {sub_word[1:]=}')
        print(node)
        if first in node.children:
            print(f'\t{first=} is here in {node.children=}')
            self.descend(node.children[first], sub_word[1:])
        else:
            print(f'\t{first=} is NOT here - creating a new node.')
            thingy = Node(first)
            print(f'Node is created: {thingy=}')
            node.children[first] = thingy
            self.descend(thingy, sub_word[1:])


if __name__ == "__main__":
    x = Derakht()
    x.add('h')
    x.add('hi')
