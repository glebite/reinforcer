"""derakht.py

"""


class Node:
    """
    """
    def __init__(self, label):
        self.label = label
        self.children = dict()


class Derakht:
    def __init__(self):
        """__init__ - instantiator for a special node and its
                      children

        When created, there will be a self.node that has an empty
        dictionary and a label of "*".
        """
        self.root = Node("*")

    def add_word(self, word):
        
        self.recurso(self.root, word)
        
    def recurso(self, node, word):
        

if __name__ == "__main__":
    obj = Derakht()
