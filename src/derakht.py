"""derakht.py

"""
from collections import defaultdict


class Node:
    """
    """
    def __init__(self, label):
        self.label = label
        self.children = defaultdict()


class Derakht:
    def __init__(self):
        """__init__ - instantiator for a special node and its
                      children

        When created, there will be a self.node that has an empty
        dictionary and a label of "*".
        """
        self.root = Node('*')


if __name__ == "__main__":
    obj = Derakht()
    obj.root.children['*'] = Node('d')
    obj.root.children['d']
